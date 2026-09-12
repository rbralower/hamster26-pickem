# Automation contract

Source of truth: private repo `rbralower/hamster26-pickem` on branch `main`.

## Files to pull every run

Use GitHub `get_file_contents` (owner=`rbralower`, repo=`hamster26-pickem`)
and write the same relative paths under a work dir:

- `rank_picks.py`          (required)
- `woo_table.py`           (required)
- `config.json`            (required; Odds API key)
- `pool_lines.json`        (required; Tuesday CBS card)
- `data/season_ledger.json`
- `data/last_market.json`
- `data/market_snapshot.json`  (Odds API fallback)

Then:

```
cd $WORKDIR
python3 rank_picks.py
```

Email `rbralower@gmail.com`:

- subject: `Hamster 26 Week N pickem — YYYY-MM-DD`
- body = `out/report.txt` (full text report)
- body_html = `out/report.html` (the ranker HTML — do not slim it)

Required HTML sections, in order:
1. Change banner (yellow/green/red badges on the 8)
2. Recommended 8 — columns: w, Pick, Opp, P, q_mkt, q−50, Pwoo−50, P−50, CBS spread, Current spread, Last spread, Δ vs pool, Δ vs last, Change, Kick. Inline cell colors: NEW green, FLIP red, weight-change yellow.
3. Expected points + season tracker line
4. Not selected (same stat columns as the 8, minus w/Change)
5. Already played (Game, Score, CBS line, Covered, Kick) when any game is final
6. Every live side by P
7. Line moves

Never drop Opp / CBS spread / Current spread / component columns. Never send a summary-only HTML body.

Never submit picks on CBS unless the latest user message is `approve`
listing the eight sides.

## After a successful run

Push these two files back to `main` (fetch blob SHA first):

- `data/season_ledger.json`
- `data/last_market.json`

Do not push `data/odds_api_live.json` or `out/*`.

## MNF job (Mon 16:00 PT)

Same pull + run. Email only if `out/mnf_alert.json` has `"alert": true`.
