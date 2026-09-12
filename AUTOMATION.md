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
- body_html = `out/report.html` exactly as written by `render_html_email` — do not slim, rewrite, or drop sections

LOCKED FORMAT for every morning run and every MNF alert (the 9:15 contract):

Required HTML sections, in order:
1. Change banner (yellow/green/red badges on the 8)
2. Recommended 8 — columns: w, Pick, Opp, P, q_mkt, q−50, Pwoo−50, P−50, CBS spread, Current spread, Last spread, Δ vs pool, Δ vs last, Change, Kick. Inline cell colors via bgcolor+style on every td: NEW green `#c6f6d5`, FLIP red `#fed7d7`, weight-change yellow `#fefcbf`.
3. Expected points + season tracker line
4. Not selected — games we did not pick, same stat columns as the 8 minus w/Change, ranked by P
5. Already played — when any game is final: Game, Score, CBS line, Covered (which side covered the locked hook), Kick. Green row on a cover, yellow on a push.
6. Every live side by P (same columns + #/w)
7. Line moves

Never drop Opp / CBS spread / Current spread / Last spread / component columns. Never send a summary-only HTML body. MNF alerts use this same full HTML plus a one-line reason at the top.

Never submit picks on CBS unless the latest user message is `approve`
listing the eight sides.

## After a successful run

Push these two files back to `main` (fetch blob SHA first):

- `data/season_ledger.json`
- `data/last_market.json`

Do not push `data/odds_api_live.json` or `out/*`.

## MNF job (Mon 16:00 PT)

Same pull + run. Email only if `out/mnf_alert.json` has `"alert": true`.
When emailing, use the locked full HTML above — not a summary.
