# Metrics

What this system measures, what it reports, and what to expect from a running deployment.

## Structural metrics

A typical deployment looks like this after the first month of use.

| Metric | Typical value |
|---|---|
| Workstations | 6 to 10 |
| Total Markdown files | 25 to 40 |
| Total lines of governance | 1,500 to 3,500 |
| Lines of Python (pipelines, dashboards) | 1,000 to 4,000 |
| Skills registered | 4 to 8 |
| Scheduled tasks | 3 to 6 |

Governance lines means lines in CLAUDE.md and MEMORY.md files combined. Python lines means the data-processing scripts the user has built for their own workstations.

## Operational metrics

The audit runs weekly. A representative pattern of findings from a stable deployment:

| Severity | Typical count per month |
|---|---|
| CRITICAL | 0 to 2 |
| WARNING | 2 to 5 |
| INFO | 5 to 15 |

CRITICAL is rare once the system is established. Most months it stays at zero. WARNING is mostly drift in routing maps or stale resource paths. INFO is mostly cadence and dedup observations.

## What it catches

Concrete categories of issues the audit catches in practice:

- A workstation MEMORY.md that grew over 200 lines and needs consolidation.
- A routing-map row pointing at a folder that has been renamed or moved.
- A resource path in a workstation that broke when an external file moved.
- A skill referenced in `skills-index.md` but missing from disk.
- Two workstations whose Identity sections have drifted into overlap.

Each finding takes 5 to 15 minutes to fix once surfaced. None would be noticed without the audit. Each would cause a visible failure within weeks if left alone.

## Time investment

| Activity | Time |
|---|---|
| Initial setup (root + first workstation) | 45 to 75 minutes |
| Adding a new workstation | 15 to 30 minutes |
| Weekly audit review | 5 to 10 minutes |
| Monthly close | 20 to 40 minutes |
| Periodic memory consolidation (quarterly) | 30 to 60 minutes |

Ongoing maintenance averages out to roughly 30 minutes per week once a deployment is mature. The system is designed so that the user's time goes to decisions, not to housekeeping.

## What it does not measure

The system does not track satisfaction, productivity, or output quality. Those are subjective and slippery. The metrics above are about the system itself: its structural integrity, its drift rate, its time cost. Whether the system makes the user more effective is a question the user answers for themselves.

## Measuring your own deployment

If you want concrete numbers for your own system:

1. Run `wc -l` over every CLAUDE.md and MEMORY.md once a month. Track the trend. Sudden growth in a single file usually means a missing rule.
2. Save each weekly audit report to a dated file. After three months you have a baseline; deviations become visible.
3. Note any time spent firefighting structural problems. If it stays under 30 minutes per week, the system is paying for itself.
