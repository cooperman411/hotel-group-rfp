# Adapters

An adapter is a short file for one portal. It holds only what is specific to that portal: its labels, its batch limit, its hotel-facing text limit, and its filter and setup notes. The skill in `SKILL.md` does the intake, drafting, verification, and submission work, and it does not change per portal.

That split is why adapters exist. Without one, the core skill would have to carry every portal's limits and labels, and it would need rewriting for each new portal. With one, you copy the template, fill in the limits from the live page, and the core stays the same.

## Included

- `portal-adapter-template.md`, a blank adapter. Copy it for each portal you use.

## Adding a portal

Copy the template as a starting structure, then replace every blank from the live page for that portal. Do not copy one portal's limits to another. Record:

- portal name and URL, as shown on the page
- request-type labels
- maximum hotels per submission
- hotel-facing text limit, or that the portal has no stated limit
- how review scores, if any, are displayed
- brand, filter, and setup labels

If you cannot verify a limit on the live page, record it as unverified and stop before relying on it. Do not guess.
