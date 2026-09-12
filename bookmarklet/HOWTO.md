# Grab the CBS card without a screenshot

This does **not** log Grok into CBS. You stay logged in on your own browser. One click copies the Tuesday lines into `pool_lines.json`, which the ranker already reads.

## One-time setup (2 minutes, desktop Chrome or Safari)

1. Open the Hamster project folder. You should already see:
   - `pickem/pool_lines.json`
   - `pickem/bookmarklet/BOOKMARKLET.txt`
2. Open `pickem/bookmarklet/BOOKMARKLET.txt`. Select all, copy.
3. In Chrome: Bookmarks → Bookmark manager → ⋮ → Add new bookmark.
   - Name: `Hamster CBS card`
   - URL: paste the whole `javascript:(function () { ... })();` string
4. Save. Drag that bookmark onto your bookmarks bar.

You only do this once.

## Every Tuesday after lines lock (30 seconds)

1. Log into CBS in **your** browser.
2. Open the Hamster 26 pool and go to the **weekly pick board**.
   Pool URL: https://picks.cbssports.com/football/pickem/pools/kbxw63b2ge3dkmrxgeydk===?entryId=ivxhi4tzhizdiobxgazdembw
3. Click **Hamster CBS card** on the bookmarks bar.
4. Check week number and every `AWAY @ HOME` row.
5. Click **Download pool_lines.json** and overwrite `pickem/pool_lines.json`.
6. Message this project “card dropped” if you want a rank immediately.

Never send a CBS password.
