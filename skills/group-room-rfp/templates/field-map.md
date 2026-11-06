# Group RFP, Field Map Template

Use this file to check that you have everything the RFP needs before you open a portal, and to note where each piece goes on the portal you are using. Work through the job in the order below, not through any one portal's form. Fill in portal labels from the visible page, in the adapter. If a value is not supplied or supported, leave it blank unless the portal requires a value. Never invent a hidden or redacted value.

Portal, as shown on the page:
Adapter:

## Source hierarchy

When sources disagree, the earlier one wins:

1. The user's current request
2. The normalized requirements summary in `task-intake.md`
3. `SKILL.md` in this skill
4. The portal adapter in `adapters/`
5. This field map

## 1. The event

| Need | Source | Rule |
|---|---|---|
| Request type | `task-intake.md` | Rooms only, meeting space only, or rooms plus meeting space, as the user named it. Portal labels are in the adapter. |
| Event name | `task-intake.md` | Company or client plus event, unless the user specifies another name. |
| Event type | `task-intake.md` | Use the supplied type. Use `Business` for an unspecified corporate event, to confirm. |
| Destination city | `task-intake.md` | The city or cities. On the portal, select the exact matching autocomplete or dropdown result. |
| Arrival date | `task-intake.md` | Use the exact date. |
| Departure date | `task-intake.md` | Use the exact date. |
| Alternate dates, if any | `task-intake.md` | Keep in the job notes. Enter them only if the portal asks for them. |
| Search preferences | `task-intake.md` | Preferred neighborhoods, districts, airports, landmarks, or travel-distance limits. Use them to choose hotels. Normally keep them out of the hotel-facing text. |

## 2. The room block

| Need | Source | Rule |
|---|---|---|
| Rooms needed by night | Room table in `task-intake.md` | Enter each night and room type. Verify the totals. |
| Bed type | Room table in `task-intake.md` | Preserve the requested bed type. |
| Suites | Room table in `task-intake.md` | Capture separately when applicable. |

## 3. Meeting space

| Need | Source | Rule |
|---|---|---|
| Meeting dates | Meeting table in `task-intake.md` | Enter only actual meeting days, not check-in-only days. |
| Attendees by day | Meeting table in `task-intake.md` | Enter the count separately for each meeting day. |
| Hours by day | Meeting table in `task-intake.md` | Enter each day's start and end time. Ask if missing. |
| Room setup and fallback | Meeting table + workflow | Preferred setup, with an acceptable fallback. Verify the setup separately for every meeting day. Stop and ask for help if a control cannot be operated or verified, or the setup is unavailable. |
| Breakout rooms | `task-intake.md` | Enter only the requested count, capacity, and setup. |

## 4. Services

| Need | Source | Rule |
|---|---|---|
| Food and beverage | `task-intake.md` | Enter only when requested. Otherwise leave blank. |
| Audio and visual | `task-intake.md` | Enter only when requested. Do not invent final specifications. |
| Wi-Fi | `task-intake.md` | Enter only when requested. |

## 5. Commercial terms

| Need | Source | Rule |
|---|---|---|
| Commissionable rates | `task-intake.md` + workflow | Request commissionable rates. Include agency and IATA only when supplied. Never invent an agency name or IATA number. |
| Budget or rate targets | `task-intake.md` | For internal screening only. Keep out of the hotel-facing text unless the user explicitly asks. |
| Contact fields | Connected browser or user | Verify visible values. Do not infer hidden or redacted values. |
| Account or sales contact | `task-intake.md` | Leave blank unless requested. |
| Attachment | `task-intake.md` | Leave blank unless the user requested an available document. |

## 6. Choosing hotels and submitting

| Need | Source | Rule |
|---|---|---|
| Property filters | Adapter + user | Apply only the filters the user confirmed. Record the filter state. |
| Quality gate, if the portal shows scores | Portal results | Apply the gate the user set, if any. Verify and record the displayed score. Skip below-gate hotels. Do not select unverified scores. Stop and ask for guidance if no or too few eligible hotels meet the requested scope. |
| Hotels per batch | Sourcing review | Maximum per batch from the adapter. No repeats across submitted batches. |
| Hotel-facing text | Generated from intake | Keep at or below the adapter character limit. Include commission, agency and IATA when supplied, core quantities, meeting details, setup and fallback, and only requested AV, Wi-Fi, and F and B. |
| Confirmation number | Portal response | Record after submission with hotels, event summary, and response timing. |

## Hotel-facing text requirements

Include commissionable rates and agency and IATA when supplied, room counts by night and bed type, meeting dates, attendees by day, hours, setup and fallback, and only requested AV, Wi-Fi, and F and B. Do not include budget or rate targets, neighborhoods, hotel names, or irrelevant detail unless requested. Keep the final assembled text at or below the adapter limit and record the count in the review.

Suggested pattern:

`Please quote commissionable rates to {agency} (IATA {iata}) for {room_pattern}. Meeting space needed {meeting_dates} for {attendee_by_day}, {hours} daily. {setup} preferred; {fallback} acceptable. {av_text} {wifi_text} {fb_text}.`

Remove unused sentences, fix spacing and punctuation, and verify the final character count against the adapter limit.

## Submission rule

Follow the final verification for each batch, then submit without separate user approval. If any part of the RFP cannot be reliably completed or verified, stop and ask for help.
