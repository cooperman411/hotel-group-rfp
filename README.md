# Hotel Group RFP Skill

> **Status: In development.**

Group hotel RFPs ask for the same details every time: dates, rooms by night, meeting days, attendees, hours, setups, food and beverage, AV, Wi-Fi. This skill collects those details once, turns them into a short RFP the hotel can act on, and walks through submission on a hotel chain RFP portal.

It is built for room blocks and meeting space together. Tell it what the group needs, and it prepares the intake, drafts the hotel-facing text, checks the work against a review checklist, and submits in batches, recording the confirmation number for each one.

## How it works

1. Interview. The skill asks for what is missing: request type, destination, arrival and departure dates, the room block by night, meeting dates with attendees and hours, preferred setup and fallback, AV, Wi-Fi, and food and beverage. It also takes the agency name and IATA number when supplied.
2. Intake. The answers become a normalized requirements summary in `templates/task-intake.md`, so the same details carry through every batch.
3. Draft. The skill writes a short hotel-facing paragraph from the intake and checks its length against the portal limit in the adapter.
4. Select. Hotels go in batches, up to the limit the portal adapter sets. If the user sets a review-score gate, only hotels at or above it qualify.
5. Verify and submit. The review checklist runs against the live page. When it passes, the skill submits and records the confirmation number, the hotels, and the stated response timing in the submission log.

## One skill, one adapter per portal

Portals differ in labels, batch limits, and text limits. The skill itself does not change per portal. Each portal gets a short adapter file that records its labels and limits, filled in from the live portal page. Copy `adapters/portal-adapter-template.md` to start one.

## What is in this repo

- `skills/group-room-rfp/SKILL.md`, the core skill
- `skills/group-room-rfp/adapters/portal-adapter-template.md`, a blank adapter to copy per portal
- `skills/group-room-rfp/adapters/README.md`, what an adapter is and how to add one
- `skills/group-room-rfp/templates/`, blank intake, field map, review checklist, output schema, and submission log
- `skills/group-room-rfp/examples/fictional-example.md`, a fictional example: a 20-room block plus one suite, 40 attendees, one meeting day

## How to use it

1. Copy the skill folder into an agent that can read `SKILL.md` files, or use it as a standalone reference.
2. Start with `SKILL.md`, then load or fill in the adapter for the portal you are using.
3. Complete `templates/task-intake.md` in a job folder before opening any portal.
4. Draft the hotel-facing text, check it against the adapter limit, and complete `templates/review-checklist.md`.
5. Verify the final page, then submit.

## Scope

It covers research, form completion, and RFP submission. Booking, contracting, payment, and negotiation are out of scope.
