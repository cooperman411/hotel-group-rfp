---
name: group-room-rfp
description: Manage hotel group sourcing from room and meeting requirements through RFP preparation, authorized submission, response tracking, proposal comparison, and decision-maker reporting. Use for rooms only, meeting space only, or both.
---
# Hotel group sourcing

Use one private job record throughout the job. Read `templates/first-use-setup.md` on first use, `templates/job-record.json` for the portable record, and `templates/comparison.md` when proposals arrive. Use `templates/review-checklist.md` before every submission. Examples are fictional. Never put client data, credentials, or user configuration in the public repository.

## Setup and intake

Discover actual tools and permissions; do not infer them from the assistant's name. Reuse existing approved preferences where available and ask only for missing, relevant information. Persist preferences only with user permission in supported private storage; otherwise tell the user how to retain them. Ask whether the request is rooms, meeting space, or both. Collect destination, dates, contact and response deadline when available, and the requirements that determine fit and a useful quote:

- Rooms: room counts by night, room types if material, and date flexibility. Calculate total room nights and peak rooms from the nightly counts.
- Meeting space: dates, times if known, attendees, function schedule and setup if known, essential space, food and beverage (F&B), audiovisual (AV), and other constraints. Do not require square footage when attendance and setup suffice.
- Both: collect both branches once. Record alternate dates, concessions, commission, rate limits, accessibility, and other details only when relevant or provided. Do not disclose an internal budget unless authorized.

Identify missing essential facts or conflicts; ask focused questions. Track material unresolved details internally. Do not invent values. Keep optional unanswered items and empty headings out of hotel-facing documents. Summarize the requirements and selected hotels before external action.

## Prepare and submit

Create a concise, easy-to-scan RFP from the record as plain text, Word or PDF according to user preference and available tools. Use short labeled fields such as “Arrival Date: March 13” and group related details under clear headings. Use a short list or room grid for nightly counts and meeting functions; avoid a dense paragraph. Present a human-readable job summary in the same style alongside the structured record. Include applicable dates, room grid, function schedule, hard requirements, contact and deadline; ask hotels to quote availability, rates, applicable meeting rental and F&B minimum, mandatory fees, taxes and service charges, concessions, commission terms when relevant, material conditions and offer validity. Omit unanswered optional fields; never insert placeholder text into the hotel-facing RFP. Render and check generated documents when tools permit.

Use the current hotel website or a user-supplied hotel/portal URL. If permitted browser control exists, inspect the visible form live; map known values to current labels and limits, verify every date, hotel and selection, and ask when a required field is uncertain. Do not build or rely on permanent chain adapters. Apply only user-approved hotel criteria; do not silently relax hard filters. Avoid duplicate submissions. Stop for human assistance when required. Never bypass authentication, CAPTCHA, rate limits, access restrictions or other controls. If restricted or unsupported, guide the user or prepare an RFP for manual submission or direct email.

Obtain authorization before any external submission or message. An explicit approval can cover subsequent batches within its stated hotels, content, channel and time scope, subject to host rules; seek renewed approval for changes outside that scope. Record scope and evidence. Verify the final page and run the checklist per batch. A click alone does not establish success. Record `submitted` only on reliable submission evidence (e.g., a sent message or explicit portal success); record `confirmed` only for actual receipt confirmation. If outcome is uncertain, retain `prepared` and flag possible submission to prevent duplication. Capture submission method, date, hotel, confirmation number/email, deadline, follow-up and evidence. A verified submission without receipt confirmation may be `submitted` or `awaiting_response`, not `confirmed`.

## Monitor and compare

Only access authorized mailboxes and permitted attachments. Search using event, dates, hotel, sender/domain and thread together; confirm ambiguous matches. Record message/attachment references and last check time. Extract quoted fields with source and date. Preserve versions and identify changes and conflicts. Never turn an absent fee into zero. Draft hotel-specific follow-ups for missing information and overdue responses; send only with authorization. Continuous monitoring requires an actual scheduler and user authorization. Otherwise offer on-demand mailbox checks or manual uploads, and explain that the assistant is not watching between sessions.

For each proposal, follow `templates/comparison.md`: preserve currency and charging basis, show itemized known costs and missing items, and distinguish commission from client cost. Generate XLSX when supported, CSV otherwise. Separate requirements, sourcing status and proposal versions in the job record; workbooks are outputs, not the only source of truth. Do not rank an incomplete quote as cheapest without qualification.

## Report and close

Produce a concise report with requirements, hotels and statuses, proposals received, comparable known costs and exclusions, concessions, restrictions, gaps, a reasoned shortlist, and decisions needed. Separate quoted facts, calculations and judgment; cite source references in the record. Refresh it when proposals change. Draft progress and final messages without sending unless authorized. Mark `completed` only when the user closes the sourcing task; a submitted request or receipt alone is not a completed sourcing job. Do not accept an offer, execute a contract, make payment, provide legal conclusions, or negotiate material terms autonomously.
