# Hamster 26 pickem ranker

Private source of truth for Rob's CBS NFL ATS pool (pick 8, weights 8..1).

https://github.com/rbralower/hamster26-pickem

Scheduled Grok automations pull this repo each run so the workspace
isolation problem (missing `rank_picks.py`) cannot happen again.

## Run

```
python3 rank_picks.py
```

Writes `out/report.txt`, `out/report.html`, `out/picks.json`,
`out/mnf_alert.json`, `out/season_tracker.xlsx`.
Runs a walker self-test first.

## Inputs

- `config.json` — Odds API key, email, pool URL (private repo only; see `config.example.json`)
- `pool_lines.json` — Tuesday CBS card. Refresh from `bookmarklet/` each week.
- `data/season_ledger.json` — expected vs actual, with kickoff locks
- `data/last_market.json` — prior-run consensus for line-move columns
- `data/market_snapshot.json` — fallback board if Odds API is down

## Method

`P = q_mkt + (P_woo − 0.50)`

Consensus = median US-book number + average de-vigged cover %. Walk to the
pool hook with Wizard of Odds deltas. Zero-cross uses an 8% pick'em band.

Do not submit on CBS unless the latest user message is `approve` listing the 8 sides.

## Automations

- Morning ranker `acbfaebf-ef87-43b3-8644-4da6979454d8`: Wed–Sun 09:15 America/Los_Angeles, email only
- MNF check `d5d3060f-a68c-4c6a-bcd0-315535cc5dac`: Mon 16:00 PT, email only if MNF was on the 8 and the model now says drop or flip
