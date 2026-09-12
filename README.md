# Hamster 26 pickem ranker

Private repo for Rob's CBS NFL ATS pool (8 picks, weights 8..1).

Source of truth for scheduled runs: https://github.com/rbralower/hamster26-pickem

## Run

```
python3 rank_picks.py
```

Writes `out/report.txt`, `out/report.html`, `out/picks.json`, `out/season_tracker.xlsx`.
Runs a 17-case walker self-test first.

## Inputs

- `config.json` — Odds API key, email, pool URL (private; see `config.example.json`)
- `pool_lines.json` — Tuesday CBS card. Refresh from `bookmarklet/` each week.
- `data/season_ledger.json` — expected vs actual, with kickoff locks
- `data/last_market.json` — prior-run consensus for line-move columns

## Method

`P = q_mkt + (P_woo − 0.50)`
Consensus = median US-book number + average de-vigged cover %. Walk to the pool hook with Wizard of Odds deltas. Zero-cross uses an 8% pick'em band.

Do not submit on CBS unless the latest user message is `approve` listing the 8 sides.
