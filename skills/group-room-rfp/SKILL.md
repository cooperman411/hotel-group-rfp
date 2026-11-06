---
name: group-room-rfp
description: Interview a user for room block and meeting-space needs, prepare a concise solicitation, and use a hotel chain RFP portal to select hotels and submit RFPs in batches, with final verification and submission without separate approval; stop and ask for help if any part cannot be reliably completed.
---

# Hotel Group RFP

Use this workflow for hotel-solicitation RFPs on a chain RFP portal. It covers research, form completion, and RFP submission only; it does not authorize booking, contracting, payment, or negotiation.

## Supporting files

Use these files in this folder:

- `templates/task-intake.md` for intake
- `templates/field-map.md` for mapping intake fields to the portal you are using
- `templates/review-checklist.md` for the submission review
- `templates/output-schema.md` to verify completion
- `templates/submission-log.csv` as the blank submission log
- `adapters/` for portal-specific notes, limits, and field labels

Save run-specific files under `jobs/<job-name>/`. References to `task-intake.md` and `submission-log.csv` mean files in that job folder. Keep templates blank. Never publish job folders, client names, or submitted RFPs.

Load the adapter for the portal you are using before you open it. If no adapter exists for that portal, fill in `adapters/portal-adapter-template.md` from the visible portal and save it as the adapter for that portal. Do not guess a limit.

## Operating rules

- Treat the user's current request as authoritative. Defaults in a template or adapter are preferences to confirm, not hard rules, unless the user confirms them.
- Use the request type the user names: rooms only, meeting space only, or rooms plus meeting space.
- Ask for destination-specific search preferences, such as preferred neighborhoods, districts, airports, landmarks, or maximum travel distance. These guide hotel selection and normally do not belong in the hotel-facing text.
- Split larger hotel lists into batches. The maximum per submission comes from the portal adapter. Do not repeat a hotel already submitted in this run. Repeat the same event details for each batch unless the user changes them.
- A budget or target rate may be used internally to screen properties, but do not include it in the outbound RFP unless the user explicitly requests it.
- Keep the RFP simple and plain text. Do not add hotel names, unnecessary background, detailed catering or AV language, or an attachment unless the user requests them.
- Request commissionable rates and include the user's agency name and IATA number when supplied. Leave both blank if not supplied. Never invent an agency name or IATA number.
- If the user sets a review-score quality gate, apply it exactly as set. Check the score displayed on the portal for each candidate, record it, and skip every hotel below the gate or with a missing or unreadable score. If there are no eligible hotels, or too few to meet the requested sourcing scope, stop and ask the user for guidance before proceeding. Do not lower the gate, include a below-gate hotel, or silently reduce the sourcing scope. A batch maximum is not a required minimum.
- For eligible hotels, also consider the requested area, meeting-space capability, room count, and the user's internal price expectations. Never present an unverified price estimate as a fact.
- If the agent has trouble completing or verifying any part of the RFP, stop and ask the user for help before proceeding. Explain the affected field, meeting day, and problem. Do not guess, skip a required field, or submit a partially verified form.

## Intake interview

Ask only for information that is missing. Collect:

1. Request type: rooms only, meeting space only, or rooms plus meeting space.
2. Company or client name, event name, and event type. If no event type is supplied, Business is a reasonable selection for a corporate meeting.
3. Destination city or cities and preferred neighborhoods, districts, airports, landmarks, or travel-distance limits.
4. Arrival and departure dates, meeting dates, date flexibility, and alternate dates if any.
5. Guest rooms by night, including total rooms and bed type (for example, one bed or two beds). Capture suites separately if needed.
6. Meeting attendees for each meeting day and meeting start and end time. If time is unspecified, ask.
7. Preferred room setup, and an acceptable fallback if the preferred setup is unavailable. Do not silently substitute another setup when the preferred one is unavailable. Ask the user how to map the fallback.
8. Audio and visual needs, Wi-Fi needs, and food-and-beverage needs. Leave a category blank when not requested.
9. Commission recipient, agency name, and IATA number.
10. Whether to attach an RFP document, and any requested account representative or national sales contact.
11. Confirm whether rate or budget information should be omitted from the hotel-facing text. Default to omitting it.

Before opening any portal, summarize the normalized requirements and resolve contradictions or missing dates, room counts, attendees, or meeting days. Record the summary in `task-intake.md`.

## Hotel-facing text

Generate a short hotel-facing paragraph from the collected data. Check the platform character limit in the portal adapter first, count characters after the final text is assembled, and shorten it if necessary without dropping commissionability or core quantities.

Include:

- commissionable rates and agency and IATA, when supplied
- room counts by night and bed type
- meeting dates, attendees by day, and hours
- setup preference and acceptable fallback
- only the requested AV, Wi-Fi, or F and B requirements

Do not include budget or rate targets, destination neighborhoods, hotel names, or irrelevant event detail unless the user specifically asks. If F and B is not requested, say `No F&B requested` or omit it consistently.

Use this as a pattern, filling and polishing the placeholders rather than copying any one portal example:

`Please quote commissionable rates to {agency} (IATA {iata}) for {room_pattern}. Meeting space needed {meeting_dates} for {attendee_by_day}, {hours} daily. {setup} preferred; {fallback} acceptable. {av_text} {wifi_text} {fb_text}.`

Remove unused sentences, fix spacing and punctuation, and verify the final character count against the adapter limit.

## Optional RFP document

Create a Word document only when the user wants an attachment or a standalone RFP. Keep it plain and brief:

- company or client and event name
- destination and dates
- room block by night
- meeting dates, attendees, hours, and setup
- requested AV, Wi-Fi, or F and B
- commissionable-rate instruction and agency and IATA, when supplied

Do not add a budget, neighborhood, hotel names, or negotiation language unless the user requests it. When document-generation tools are available, create the `.docx`, render or preview it, and correct obvious layout problems before attaching it.

## Portal workflow

When browser control is available, inspect the visible page after each navigation or major action. If the page, selected tab, or form state does not match expectations, stop and ask the user rather than guessing.

1. Load the portal adapter and confirm its batch limit, character limit, request-type labels, and any filter notes.
2. If sign-in is required, let the user log in through their connected browser. Never request or handle credentials in chat. The user must handle CAPTCHA or other verification challenges.
3. Select the request type from the intake, enter the destination and select the matching autocomplete result, then enter dates, guest rooms, and meeting attendees. Start the search.
4. Apply the filters the user requested. Check and record each candidate's displayed review score on the portal, if the user set a score gate. Apply the gate before adding a hotel to an RFP.
5. Select hotels only up to the adapter batch limit. Confirm no hotel was used in an earlier batch. Show the proposed names to the user when selection involves judgment.
6. Create the RFP, name the event using company or client plus event, select the event type, and verify carried-over dates, rooms, and attendees.
7. Leave any attachment blank unless the user requested an attachment and it is available.
8. Enter the room block for every night. Each night's total must equal the sum of its room types.
9. Open each meeting-day panel. Do not add meeting space on a check-in-only day. Enter attendees and hours separately for each meeting day.
10. Select and visibly verify the requested setup separately in every meeting-day panel. If any control cannot be completed or verified, or the requested setup is unavailable, stop and ask for help.
11. Enter only requested AV, Wi-Fi, and F and B information. Leave unrequested categories blank.
12. Continue to the contact section, verify visible contact fields, enter the hotel-facing text, and confirm its character count against the adapter limit.
13. Complete the final verification in `templates/review-checklist.md` against the current page.
14. Submit after successful final verification without separate user approval. If any part of the RFP is blocked or uncertain, stop and ask for help before proceeding.
15. Verify the confirmation page and record the confirmation number, selected hotels, event summary, and stated response timing in `submission-log.csv`.
16. For another batch, start a fresh search or clear prior selections, repeat the normalized request, and repeat final verification.

## What this skill does not do

- It does not book, contract, pay for, or negotiate rooms or meeting space.
