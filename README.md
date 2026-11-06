# Hotel Group RFP Skill

> **Status: In development.**
>
> This is a hotel group and meeting skill for preparing group hotel RFPs. It prepares the intake, the hotel-facing text, and the verification package, and it guides submission on a hotel chain RFP portal.

A chain-agnostic workflow with one adapter per portal. The adapter template is included. Fill it in from the live portal page for each portal you use.

## Included

- `skills/group-room-rfp/SKILL.md`, the core skill
- `skills/group-room-rfp/adapters/portal-adapter-template.md`, a blank adapter to copy per portal
- `skills/group-room-rfp/adapters/README.md`, what an adapter is and how to add one
- `skills/group-room-rfp/templates/`, blank intake, field map, review checklist, output schema, and submission log
- `skills/group-room-rfp/examples/fictional-example.md`, a fictional example, no real client or hotel

## How to use it

1. Copy the skill folder into an agent that can read `SKILL.md` files, or use it as a standalone reference.
2. Start with `SKILL.md`, then load or fill in the adapter for the portal you are using.
3. Complete `templates/task-intake.md` in a job folder before opening any portal.
4. Draft the hotel-facing text, check it against the adapter limit, and complete `templates/review-checklist.md`.
5. Verify the final page, then submit.

## Scope

It covers research, form completion, and RFP submission. Booking, contracting, payment, and negotiation are out of scope.
