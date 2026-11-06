# Hotel Group Sourcing Skill

**Status: in development.** Prepare hotel requests, track submissions, compare proposals, and report to a decision-maker. Supports guest rooms, meeting space, or both.

**Use at your own risk.** This project has not been validated on live websites, mailboxes or hotel systems. You are responsible for verifying requirements, recipients, submissions, proposal calculations, fees, deadlines and contract terms before acting. Incorrect outputs or external actions can cause financial loss or disclose confidential information. The software and documentation are provided without warranty under the [MIT License](LICENSE), which includes a limitation of author liability.

## Why this exists

I built this based the hotel sourcing work I have been doing for over a decade. The RFP is only the start. Someone still has to track what was sent, confirm what arrived, sort through changing proposals, catch missing costs, follow up, and give a decision-maker a clear comparison. This skill helps an AI assistant carry that work through in a practical, reviewable way.

Like PT/OS, it keeps the system understandable and adaptable to the tools a person already has. The group record and outputs are portable. The workflow can use authorized browser, email, document, and spreadsheet tools when available, or plain files and manual steps when they are not.

## What makes this different

This is an assistant workflow for the meeting planner's end-to-end job, not a hotel marketplace or a vendor's sourcing platform. It can work across hotel websites and email, with no required service or connector. It keeps proposal versions and source evidence visible, distinguishes unknown costs from zero, records whether a submission was actually confirmed, and prepares information for a human decision. External actions remain subject to the user's authorization.

## Start

1. Give your assistant the `skills/group-room-rfp` folder, or paste `SKILL.md` and its referenced files into a capable chat. Installation differs by platform; no particular connector is required.
2. Say: “Help me source hotels for a group.” On first use, the assistant checks capabilities and asks for relevant preferences. Existing preferences are reused only when the environment can save them safely.
3. Give the destination, dates, request type, and the room pattern and/or meeting requirements. The assistant creates a short RFP and a job record. It can use a URL you supply.
4. Review the hotels and submission scope. External submissions and messages require your authorization. The assistant records only verified outcomes.
5. Provide proposals, or authorize mailbox checks if available. Request an updated comparison and decision report at any time.

See [the skill](skills/group-room-rfp/SKILL.md), [setup](skills/group-room-rfp/templates/first-use-setup.md), [job record](skills/group-room-rfp/templates/job-record.json), and [fictional example](skills/group-room-rfp/examples/fictional-example.md). Spreadsheet and report examples are in that folder. Copy job files to private storage outside this repository. Do not commit personal information, client records, or credentials.

Browser control, email, scheduling, persistent storage, and Word/PDF/XLSX generation depend on the host and permissions. Without them, use the plain-text RFP, manual submissions and uploads, and CSV comparison. The skill does not promise continuous monitoring.

## Use and review

AI output can be incomplete or wrong. Verify dates, calculations, prices, fees, deadlines, submission evidence, and contract terms before relying on them. Use only systems and data you are authorized to access; comply with applicable law and third-party website terms. Do not bypass authentication, CAPTCHAs, rate limits, or access controls. This project does not provide legal, tax, financial, or contracting advice, make payments, sign contracts, or accept proposals.

**License:** [MIT License](LICENSE). Copyright (c) 2026 Kerry Cooper.
