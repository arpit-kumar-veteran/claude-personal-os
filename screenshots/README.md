# Screenshots and diagrams

This folder holds the architecture diagram source and its rendered PNG, plus any redacted screenshots of a running deployment.

## What is here

- `architecture.mmd`: Mermaid source for the architecture diagram shown in ARCHITECTURE.md.
- `architecture.png`: PNG render of the diagram, suitable for inline use in README or in a LinkedIn post (if the render step in the release pipeline produced one).

If `architecture.png` is missing from this folder, render it yourself with the command below.

## How to render the diagram

Install the Mermaid CLI once:

```
npm install -g @mermaid-js/mermaid-cli
```

Then render:

```
mmdc -i architecture.mmd -o architecture.png -w 1600 -H 1200 -b transparent
```

## Adding your own screenshots

Drop redacted PNGs into this folder. Suggested naming:

- `audit-report-YYYYMMDD.png` for example audit outputs.
- `dashboard-YYYYMMDD.png` for net-worth dashboard exports.
- `routing-map-YYYYMMDD.png` for routing map screenshots.

Strip every personal identifier before saving. The audit will not catch personal data inside a PNG. That step is on you.
