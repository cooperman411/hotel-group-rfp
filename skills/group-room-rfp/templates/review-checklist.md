# Group RFP, Final Verification Checklist

References to `task-intake.md` and `submission-log.csv` mean files in the current `jobs/<job-name>/` folder. The blank submission log template is `templates/submission-log.csv`.

Complete this checklist immediately before submission. It applies separately to every hotel batch. Separate user approval is not required for submission. Stop and ask for help if any part cannot be reliably completed or verified.

Chain:
Adapter:
Portal batch limit, from the adapter:
Hotel-facing text limit, from the adapter:
Review-score quality gate, if the user set one:

## Request and hotel batch

- [ ] Current `task-intake.md` reflects the user's request
- [ ] Normalized requirements were resolved before website entry
- [ ] Request type is correct: rooms, meeting space, or rooms plus meeting space, using the portal labels
- [ ] Exact destination and dates are correct
- [ ] Current hotel batch contains no more than the adapter batch limit
- [ ] No hotel in the batch was submitted previously
- [ ] Brand filters and screening criteria were applied as specified
- [ ] Each selected hotel's displayed review score was verified and recorded, if a gate was set. Every score is at or above the gate.
- [ ] No below-gate or unverified-score hotel was selected
- [ ] Any shortage of eligible hotels for the requested sourcing scope was escalated and resolved with the user before proceeding
- [ ] Proposed hotels were shown to the user when selection involved judgment

## Event and room details

- [ ] Company or client, event name, and event type are correct
- [ ] Room pattern is correct for every night
- [ ] Bed types and suites are correct where applicable
- [ ] Meeting space is included only on actual meeting days
- [ ] Attendees and hours are correct for each meeting day
- [ ] Requested layout is selected and visibly verified separately in every meeting-day control
- [ ] Fallback setup was approved by the user if the preferred setup was unavailable
- [ ] Breakout rooms are correct, if any
- [ ] Only requested AV, Wi-Fi, and F and B options are selected

## Contact, attachment, and hotel-facing text

- [ ] Visible contact fields are verified
- [ ] Optional chain representative or national sales contact field is blank unless requested
- [ ] Attachment is blank unless the user requested an available document
- [ ] Hotel-facing text includes commissionable rates and agency and IATA, when supplied
- [ ] Hotel-facing text includes room quantities, bed type, meeting days, attendees, hours, and setup and fallback
- [ ] Hotel-facing text contains only requested AV, Wi-Fi, and F and B details
- [ ] Hotel-facing text excludes budget or rate targets, neighborhoods, and hotel names unless requested
- [ ] Hotel-facing text is at or below the adapter character limit
- [ ] Exact hotel-facing text is copied below

**Hotel-facing text:**

**Character count:**
**Adapter limit:**

## Final verification and approval

- [ ] Final page reviewed after all fields were entered
- [ ] All fields match the resolved request for this exact batch
- [ ] No blocked fields, uncertain selections, or unresolved questions remain

**Hotels in this batch and verified review scores, if a gate was set:**

**Date and time of final verification:**

## After submission

- [ ] Confirmation page verified
- [ ] Confirmation number recorded in `submission-log.csv`
- [ ] Selected hotels, event summary, and response timing recorded
- [ ] Confirmation page preserved or left accessible when possible

## Notes

Any mismatch, blocked field, stale page state, or unresolved question must be documented and escalated before submission.
