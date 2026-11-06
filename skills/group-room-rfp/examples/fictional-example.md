# Fictional example, portal adapter

This is a fictional example only. No real client, company, event, or hotel is named. Dates are illustrative. Use it to see the shape of a completed intake, not as a real RFP.

## Intake, fictional

- Portal: a chain RFP portal, with an adapter filled in for this example
- Request type: rooms plus meeting space
- Company or client: Harbor View Association, fictional
- Event: Harbor View Annual Meeting, fictional
- Event type: Business
- Destination: Charlotte, fictional search area, downtown
- Arrival: Friday, March 13, 2027. Departure: Sunday, March 15, 2027.
- Meeting dates: Saturday, March 14, 2027
- Rooms: 20 rooms on March 13, 20 rooms on March 14, one bed, plus 1 suite on March 14
- Meeting: March 14, 40 attendees, 9:00 a.m. to 5:00 p.m.
- Setup: U-shape preferred, boardroom style acceptable
- AV: projector and screen requested. Wi-Fi: requested. F and B: none requested.
- Commission: commissionable rates requested. Agency and IATA: to be supplied by the user, left blank in this example.
- Review-score gate, example: 4.0 out of 5.0 or higher, verified on the portal.
- Batch limit, in this example: 3 hotels. Text limit, in this example: 500 characters.

## Hotel-facing text, fictional, 309 characters

`Please quote commissionable rates to {agency} (IATA {iata}) for 20 rooms Mar 13, 20 rooms plus 1 suite Mar 14, one bed. Meeting space needed Mar 14 for 40 attendees, 9:00 a.m. to 5:00 p.m. daily. U-shape preferred; boardroom style acceptable. Projector and screen requested. Wi-Fi requested. No F&B requested.`

Note: replace `{agency}` and `{iata}` with the supplied values before submission, recount the characters, and shorten if the count goes over 500. Do not submit this fictional text as a real RFP.

## What happens next in the example

1. The agent shows the normalized intake and the proposed batch of up to 3 hotels, with verified scores, to the user.
2. The agent completes the review checklist against the final page.
3. The agent submits after successful final verification.
4. The agent records the confirmation number, hotels, event summary, and response timing in `submission-log.csv`.
