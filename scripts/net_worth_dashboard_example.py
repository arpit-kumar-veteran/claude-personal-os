#!/usr/bin/env python3
"""
net_worth_dashboard_example.py

Demonstrates the net-worth dashboard pattern used by the original operating
system. Computes asset allocation and a simple FIRE (Financial Independence)
projection from a fictional holdings list, then renders a self-contained
HTML dashboard with three tabs.

The original at the source operating system runs to roughly 1,000 lines
and handles real holdings (multiple accounts, currencies, asset classes,
taxable versus tax-advantaged splits, monthly contribution flow, loan
amortisation, projection scenarios). This file demonstrates the shape only
with six fictional holdings.

Run:
    python3 net_worth_dashboard_example.py

Output:
    example_dashboard.html in the current directory. Open in any browser.

Requires:
    Python standard library only.
"""

from pathlib import Path
from datetime import date


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_DIR / "example_dashboard.html"

HOLDINGS = [
    {"name": "Cash & Equivalents",   "category": "Cash",         "value": 500_000},
    {"name": "Domestic Equity ETF",  "category": "Equity",       "value": 2_200_000},
    {"name": "International Equity", "category": "Equity",       "value": 1_300_000},
    {"name": "Bond Fund",            "category": "Fixed Income", "value": 800_000},
    {"name": "Real Estate Fund",     "category": "Real Estate",  "value": 1_400_000},
    {"name": "Gold ETF",             "category": "Commodities",  "value": 300_000},
]

MONTHLY_CONTRIBUTION = 50_000
ANNUAL_GROWTH_RATE = 0.08
TARGET_CORPUS = 30_000_000
PROJECTION_YEARS = 25
CURRENCY_SYMBOL = "₹"


def compute_allocation(holdings):
    total = sum(h["value"] for h in holdings)
    by_category = {}
    for h in holdings:
        by_category[h["category"]] = by_category.get(h["category"], 0) + h["value"]
    allocation = [
        {"category": cat, "value": value, "percent": round(value / total * 100, 1)}
        for cat, value in sorted(by_category.items(), key=lambda x: -x[1])
    ]
    return total, allocation


def project_fire(current_corpus, monthly_add, annual_growth, target, years):
    rows = []
    corpus = current_corpus
    monthly_growth = (1 + annual_growth) ** (1 / 12) - 1
    fi_year = None
    for year in range(0, years + 1):
        rows.append({"year": year, "corpus": round(corpus)})
        if fi_year is None and corpus >= target:
            fi_year = year
        for _ in range(12):
            corpus = corpus * (1 + monthly_growth) + monthly_add
    return rows, fi_year


CSS = """
body { font-family: -apple-system, system-ui, sans-serif; margin: 0; background: #f7f7f8; color: #1a1a1a; }
header { padding: 24px 32px; background: white; border-bottom: 1px solid #e5e5e7; }
h1 { margin: 0; font-size: 22px; font-weight: 600; }
.subtitle { color: #666; font-size: 14px; margin-top: 4px; }
.tabs { display: flex; gap: 4px; padding: 0 32px; background: white; border-bottom: 1px solid #e5e5e7; }
.tab { padding: 12px 20px; cursor: pointer; border-bottom: 2px solid transparent; font-size: 14px; color: #555; }
.tab.active { color: #1a1a1a; border-bottom-color: #1a1a1a; font-weight: 500; }
.content { padding: 32px; max-width: 960px; }
.panel { display: none; }
.panel.active { display: block; }
.stat-row { display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap; }
.stat { background: white; padding: 16px 20px; border-radius: 8px; border: 1px solid #e5e5e7; flex: 1; min-width: 160px; }
.stat-label { font-size: 12px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }
.stat-value { font-size: 24px; font-weight: 600; margin-top: 4px; }
table { width: 100%; border-collapse: collapse; background: white; border: 1px solid #e5e5e7; border-radius: 8px; overflow: hidden; }
th, td { padding: 10px 16px; text-align: left; border-bottom: 1px solid #f0f0f0; font-size: 14px; }
th { background: #fafafa; font-weight: 500; color: #555; }
tr:last-child td { border-bottom: none; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
.bar { height: 8px; background: #1a1a1a; border-radius: 4px; }
"""

JS = """
function showTab(name) {
  document.querySelectorAll('.tab').forEach(function (t) {
    t.classList.toggle('active', t.dataset.tab === name);
  });
  document.querySelectorAll('.panel').forEach(function (p) {
    p.classList.toggle('active', p.dataset.panel === name);
  });
}
"""


def fmt_money(value):
    return f"{CURRENCY_SYMBOL}{value:,.0f}"


def render_overview(total, allocation):
    stats = (
        '<div class="stat-row">'
        f'<div class="stat"><div class="stat-label">Net Worth</div><div class="stat-value">{fmt_money(total)}</div></div>'
        f'<div class="stat"><div class="stat-label">Asset Classes</div><div class="stat-value">{len(allocation)}</div></div>'
        f'<div class="stat"><div class="stat-label">As of</div><div class="stat-value">{date.today():%d %b %Y}</div></div>'
        '</div>'
    )
    rows = "".join(
        f'<tr><td>{a["category"]}</td>'
        f'<td class="num">{fmt_money(a["value"])}</td>'
        f'<td class="num">{a["percent"]}%</td>'
        f'<td><div class="bar" style="width:{a["percent"] * 2}px;"></div></td></tr>'
        for a in allocation
    )
    table = (
        '<table><thead><tr><th>Asset Class</th><th class="num">Value</th>'
        f'<th class="num">Share</th><th></th></tr></thead><tbody>{rows}</tbody></table>'
    )
    return stats + table


def render_holdings(holdings):
    rows = "".join(
        f'<tr><td>{h["name"]}</td><td>{h["category"]}</td><td class="num">{fmt_money(h["value"])}</td></tr>'
        for h in sorted(holdings, key=lambda h: -h["value"])
    )
    return (
        '<table><thead><tr><th>Holding</th><th>Category</th>'
        f'<th class="num">Value</th></tr></thead><tbody>{rows}</tbody></table>'
    )


def render_fire(projection, fi_year):
    fi_text = f"Year {fi_year}" if fi_year is not None else "Beyond horizon"
    header = (
        '<div class="stat-row">'
        f'<div class="stat"><div class="stat-label">Projected FI</div><div class="stat-value">{fi_text}</div></div>'
        '</div>'
    )
    rows = "".join(
        f'<tr><td>{p["year"]}</td><td class="num">{fmt_money(p["corpus"])}</td></tr>'
        for p in projection
    )
    table = (
        '<table><thead><tr><th>Year</th>'
        f'<th class="num">Projected Corpus</th></tr></thead><tbody>{rows}</tbody></table>'
    )
    return header + table


def render_html(holdings, total, allocation, projection, fi_year):
    overview_html = render_overview(total, allocation)
    holdings_html = render_holdings(holdings)
    fire_html = render_fire(projection, fi_year)
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<title>Net Worth Dashboard (example)</title>
<style>{CSS}</style>
</head><body>
<header>
  <h1>Net Worth Dashboard</h1>
  <div class="subtitle">Fictional example data. Generated by net_worth_dashboard_example.py.</div>
</header>
<nav class="tabs">
  <div class="tab active" data-tab="overview" onclick="showTab('overview')">Overview</div>
  <div class="tab" data-tab="holdings" onclick="showTab('holdings')">Holdings</div>
  <div class="tab" data-tab="fire" onclick="showTab('fire')">FIRE Projection</div>
</nav>
<div class="content">
  <div class="panel active" data-panel="overview">{overview_html}</div>
  <div class="panel" data-panel="holdings">{holdings_html}</div>
  <div class="panel" data-panel="fire">{fire_html}</div>
</div>
<script>{JS}</script>
</body></html>"""


def main():
    total, allocation = compute_allocation(HOLDINGS)
    projection, fi_year = project_fire(
        total, MONTHLY_CONTRIBUTION, ANNUAL_GROWTH_RATE, TARGET_CORPUS, PROJECTION_YEARS,
    )
    html = render_html(HOLDINGS, total, allocation, projection, fi_year)
    OUTPUT_FILE.write_text(html, encoding="utf-8")

    print(f"Wrote {OUTPUT_FILE}")
    print(f"Net worth: {fmt_money(total)}")
    fi_text = f"Year {fi_year}" if fi_year is not None else "beyond horizon"
    print(f"Projected FI: {fi_text}")


if __name__ == "__main__":
    main()
