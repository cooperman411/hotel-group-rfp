# Portal adapter template

Copy this file and save it as the adapter for one portal, for example `adapters/my-portal.md`. Fill in every field from the live portal page. Do not guess a limit. If a limit cannot be verified on the page, record it as unverified and stop before relying on it.

## Portal

- Portal name:
- Portal URL, as shown on the page:
- Request-type labels, as shown on the page:
- Maximum hotels per submission:
- Hotel-facing text limit, in characters, or no stated limit:
- How review scores, if any, are displayed on the results page:
- Brand, filter, and setup labels, as shown on the page:

## Preferences for this portal, to confirm per job

Record only preferences the user confirmed for this portal. These are examples of the kind of thing to record here, not rules:

- Brand filters:
- Review-score quality gate, if the user set one:
- Setup preference and fallback:
- Hours, if the user gave a default:

## Entry sequence

Use the skill for entry, with these portal-specific notes:

1. Open the portal. If sign-in, CAPTCHA, or verification is required, the user handles it through the connected browser.
2. Select the request type from the intake.
3. Enter the destination and select the matching autocomplete result.
4. Enter arrival and departure dates, guest rooms by night, and meeting attendees. Start the search.
5. Apply the filters the user confirmed. Record the filter state in the job notes.
6. Check the displayed review score for each candidate, if the user set a gate. Record the score beside each candidate's name. Only verified scores at or above the gate qualify. If no or too few eligible hotels meet the requested scope, stop and ask for guidance.
7. Select hotels only up to the batch limit above. Confirm no hotel was used in an earlier batch.
8. Create the RFP, name the event, select the event type, and verify carried-over dates, rooms, and attendees.
9. Leave any attachment blank unless the user requested an attachment and it is available.
10. Enter the room block for every night. Each night's total must equal the sum of its room types.
11. Open each meeting-day panel. Do not add meeting space on a check-in-only day. Enter attendees and hours separately for each meeting day.
12. Select and visibly verify the requested setup separately in every meeting-day panel. If any control cannot be completed or verified, or the requested setup is unavailable, stop and ask for help.
13. Enter only requested AV, Wi-Fi, and F and B information. Leave unrequested categories blank.
14. Continue to the contact section, verify visible contact fields, enter the hotel-facing text, and confirm its character count against the limit above.
15. Complete the final verification in `templates/review-checklist.md` against the current page.
16. Submit after successful final verification without separate user approval. If any part of the RFP is blocked or uncertain, stop and ask for help before proceeding.
17. Verify the confirmation page and record the confirmation number, selected hotels, event summary, and stated response timing in `submission-log.csv`.
18. For another batch, start a fresh search or clear prior selections, repeat the normalized request, and repeat final verification.

## Final verification for this portal

Immediately before submission, verify and record:

- selected hotel names and verified review scores, each at or above the gate the user confirmed, if a gate was set
- event name and dates
- room pattern by night
- meeting days, attendees, hours, and setup
- AV, Wi-Fi, and F and B choices
- exact hotel-facing text and character count, at or below the limit above
- whether an attachment is included
- current batch size, no more than the limit above

Repeat verification if the final page changes. Each batch must match the resolved requirements.

## Recovery

- If the visible page or form state does not match expectations, stop and ask rather than guessing.
- If login or browser control is blocked, tell the user exactly where to take over.
- If page text is stale or incomplete, inspect the visible page again and use a screenshot when needed.
- If no or too few suitable hotels meet the quality gate and location and capacity requirements, stop and ask for guidance. Report the eligible count and failed condition. Do not lower the gate or silently reduce the sourcing scope.
