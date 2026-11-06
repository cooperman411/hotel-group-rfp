# Group RFP, Output Schema

References to `task-intake.md` and `submission-log.csv` mean files in the current `jobs/<job-name>/` folder. The blank submission log template is `templates/submission-log.csv`.

This file defines completion for the group-RFP workflow. It covers research, form preparation, and guided submission only. Booking, contracting, payment, negotiation, and post-selection client work are outside this workflow.

All job outputs are saved under:

`jobs/<job-name>/`

## Stage 1, Intake and normalization

- [ ] Current request captured in `task-intake.md`
- [ ] Chain and adapter identified, with batch limit and hotel-facing text limit recorded
- [ ] Request type identified: rooms only, meeting space only, or rooms plus meeting space
- [ ] Company or client, event name, and event type recorded when supplied, otherwise To confirm
- [ ] Destination and search preferences recorded
- [ ] Arrival, departure, and meeting dates recorded; flexibility and alternates recorded when offered, otherwise To confirm
- [ ] Room block recorded by night, including bed type and suites when applicable
- [ ] Attendees recorded for each meeting day; hours recorded when known, otherwise To confirm
- [ ] Setup and fallback recorded when known, otherwise To confirm; AV, Wi-Fi, and F and B recorded only when requested
- [ ] Commission recipient, agency, and IATA confirmed or left blank when not supplied
- [ ] Attachment preference and requested chain representative or national sales contact recorded
- [ ] Normalized requirements summary completed before website work begins

## Stage 2, Hotel research and batch selection

- [ ] Correct request type and exact destination selected on the portal
- [ ] Filters normalized as the user confirmed
- [ ] Displayed review score for each candidate checked and recorded in sourcing notes, if a gate was set. Only verified scores at or above the gate selected.
- [ ] No or too few eligible hotels for the requested sourcing scope triggered a stop and request for guidance. Any shortage was resolved before proceeding.
- [ ] Location, meeting capacity, room inventory, and visible facts reviewed
- [ ] Internal price expectations used only as screening heuristics and not stated as verified facts
- [ ] Proposed hotel names shown to the user when selection involved judgment
- [ ] Current batch contains no more than the adapter batch limit
- [ ] No hotel repeats a previously submitted batch

## Stage 3, RFP preparation

- [ ] Event profile matches the normalized intake
- [ ] Room block totals are correct for every night
- [ ] Meeting space appears only on actual meeting days
- [ ] Attendees are entered separately by meeting day; hours are entered when known, otherwise To confirm
- [ ] Requested layout is selected and visibly verified separately for every meeting day, when known. Any control problem or unavailable setup is resolved with the user.
- [ ] Only requested AV, Wi-Fi, and F and B fields are populated
- [ ] RFP document is created for every job unless the user declines, in the form the user picked (Word, PDF, or plain text), and is rendered and previewed before use
- [ ] Hotel-facing text is assembled and counted at or below the adapter limit

## Stage 4, Final verification and approval

- [ ] Final hotel batch and recorded review scores reviewed. Every selected hotel qualifies under the gate the user set, if any.
- [ ] Event name and dates reviewed
- [ ] Room pattern by night reviewed
- [ ] Meeting days, attendees, hours, and setup reviewed
- [ ] AV, Wi-Fi, and F and B choices reviewed
- [ ] Exact hotel-facing text and character count reviewed
- [ ] Attachment status reviewed
- [ ] Current final page matches the resolved request. No blocked fields or unverified selections remain.

## Stage 5, Submission and preservation

- [ ] Exact final `Submit` control clicked only after Stage 4 verification
- [ ] Confirmation page verified
- [ ] Confirmation number recorded in `submission-log.csv`
- [ ] Selected hotels, event summary, and response timing recorded
- [ ] Confirmation page preserved or left accessible when possible
- [ ] For another batch, prior selections cleared or a fresh search started

## Run completion

A run is complete when all applicable stages are checked, every submitted batch has a confirmation record, and unresolved follow-up is documented. Separate user approval is not required for RFP submission. If any part cannot be reliably completed or verified, stop and ask for help before submission.
