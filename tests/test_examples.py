import csv, datetime, json, unittest, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'skills/group-room-rfp'
class Examples(unittest.TestCase):
 def test_dates(self):
  self.assertEqual(datetime.date(2027,3,13).strftime('%A'),'Saturday')
  self.assertEqual(datetime.date(2027,3,14).strftime('%A'),'Sunday')
  self.assertEqual(datetime.date(2027,3,15).strftime('%A'),'Monday')
 def test_record_template(self):
  j=json.loads((P/'templates/job-record.json').read_text());self.assertEqual(j['schema_version'],'1.0');self.assertEqual(j['hotels'][0]['status'],'candidate')
 def test_costs_and_unknowns(self):
  with (P/'examples/proposal-comparison.csv').open() as f:r=list(csv.DictReader(f))
  self.assertEqual(len(r),2)
  for row in r:
   self.assertEqual(int(row['Room nights'])*int(row['Rate per room-night USD']),int(row['Room subtotal USD']))
   self.assertEqual(sum(int(row[k] or 0) for k in ['Room subtotal USD','Meeting rental USD','F&B minimum USD','AV USD','Mandatory fees USD','Taxes USD']),int(row['Known subtotal USD']))
   self.assertEqual(row['Complete total USD'],'');self.assertEqual(row['Taxes USD'],'');self.assertIn('Taxes',row['Missing / conflicts'])
  self.assertEqual([x['Known subtotal USD'] for x in r],['10200','10450'])
 def test_workbook(self):
  with zipfile.ZipFile(P/'examples/proposal-comparison.xlsx') as z:
   self.assertIsNone(z.testzip())
   for n in z.namelist(): ET.fromstring(z.read(n))
   sheet=z.read('xl/worksheets/sheet1.xml').decode();self.assertIn('G2*H2',sheet);self.assertIn('SUM(I3:N3)',sheet)
 def test_public_example_has_no_placeholder(self):
  text=(P/'examples/fictional-example.md').read_text().split('## Hotel-facing RFP')[1].split('## Fictional record')[0]
  self.assertNotIn('To confirm',text);self.assertNotIn('{',text)
if __name__=='__main__': unittest.main()
