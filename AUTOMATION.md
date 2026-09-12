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
- body = `out/report.txt`
- body_html = `out/report.html`

Never submit picks on CBS unless the latest user message is `approve`
listing the eight sides.

## After a successful run

Push these two files back to `main` (fetch blob SHA first):

- `data/season_ledger.json`
- `data/last_market.json`

Do not push `data/odds_api_live.json` or `out/*`.

## MNF job (Mon 16:00 PT)

Same pull + run. Email only if `out/mnf_alert.json` has `"alert": true`.
