# Group RFP, Field Map Template

Use this file to map the intake fields to the portal you are using. Fill in the portal labels from the visible page. If a value is not supplied or supported, leave it blank unless the portal requires a value. Never invent a hidden or redacted value.

Chain:
Adapter:
Portal, as shown on the page:

## Source hierarchy

1. The user's current request
2. The normalized requirements summary in `task-intake.md`
3. `SKILL.md` in this skill
4. The chain adapter in `adapters/`
5. This field map

## Field map

| Portal field, as labeled on the page | Source | Rule |
|---|---|---|
| Request type | `task-intake.md` | Use the request type from intake, using the portal labels in the adapter. |
| Destination / city | `task-intake.md` | Select the exact matching autocomplete or dropdown result. |
| Arrival date | `task-intake.md` | Use the exact date. |
| Departure date | `task-intake.md` | Use the exact date. |
| Event name | `task-intake.md` | Use company or client plus event unless the user specifies another name. |
| Event type | `task-intake.md` | Use the supplied type. Use `Business` for an unspecified corporate event, to confirm. |
| Guest rooms needed | Room table in `task-intake.md` | Enter each night and room type. Verify totals. |
| Bed type / suites | Room table in `task-intake.md` | Preserve the requested bed type and separate suites when applicable. |
| Meeting dates | Meeting table in `task-intake.md` | Enter only actual meeting days, not check-in-only days. |
| Attendees | Meeting table in `task-intake.md` | Enter the count separately for each meeting day. |
| Meeting hours | Meeting table in `task-intake.md` | Enter each day's start and end time. Ask if missing. |
| Meeting setup | Meeting table + workflow | Select and verify the requested layout separately for every meeting day. Stop and ask for help if a control cannot be operated or verified, or the setup is unavailable. |
| Breakout rooms | `task-intake.md` | Enter only requested breakout count, capacity, and setup. |
| Audio and Visual | `task-intake.md` | Enter only when requested. Do not invent final specifications. |
| Wi-Fi | `task-intake.md` | Enter only when requested. |
| Food and Beverage | `task-intake.md` | Enter only when requested. Otherwise leave blank. |
| Destination search preferences | `task-intake.md` | Use for hotel selection. Normally exclude from hotel-facing text. |
| Brand filters | Adapter + user | Apply only the filters the user confirmed. Record the filter state. |
| Guest-review score, if shown | Portal results | Apply the quality gate the user set, if any. Verify and record the displayed score. Skip below-gate hotels. Do not select unverified scores. Stop and ask for guidance if no or too few eligible hotels meet the requested scope. |
| Hotel selection | Sourcing review | Maximum per batch from the adapter. No repeats across submitted batches. |
| Attachment | `task-intake.md` | Leave blank unless the user requested an available document. |
| Hotel-facing text | Generated from intake | Keep at or below the adapter character limit. Include commission, agency and IATA when supplied, core quantities, meeting details, setup and fallback, and only requested AV, Wi-Fi, and F and B. |
| Contact fields | Connected browser or user | Verify visible values. Do not infer hidden or redacted values. |
| Chain representative or national sales contact | `task-intake.md` | Leave blank unless requested. |
| Confirmation number | Portal response | Record after submission with hotels, event summary, and response timing. |

## Hotel-facing text requirements

Include commissionable rates and agency and IATA when supplied, room counts by night and bed type, meeting dates, attendees by day, hours, setup and fallback, and only requested AV, Wi-Fi, and F and B. Do not include budget or rate targets, neighborhoods, hotel names, or irrelevant detail unless requested. Keep the final assembled text at or below the adapter limit and record the count in the review.

Suggested pattern:

`Please quote commissionable rates to {agency} (IATA {iata}) for {room_pattern}. Meeting space needed {meeting_dates} for {attendee_by_day}, {hours} daily. {setup} preferred; {fallback} acceptable. {av_text} {wifi_text} {fb_text}.`

Remove unused sentences, fix spacing and punctuation, and verify the final character count against the adapter limit.

## Submission rule

Follow the final verification for each batch, then submit without separate user approval. If any part of the RFP cannot be reliably completed or verified, stop and ask for help.
