    (OUT / "report.html").write_text(html)
    payload = {
        "week": pool["week"],
        "run_at": now.isoformat(),
        "mnf_alert": mnf_alert,
        "expected_points": expected_points(ranked),
        "season": {
            "expected": ledger.get("season_expected"),
            "actual": ledger.get("season_actual"),
            "max": ledger.get("season_max"),
            "week_expected": next((w.get("expected") for w in ledger.get("weeks") or [] if w.get("week") == pool.get("week")), None),
            "week_actual": next((w.get("actual") for w in ledger.get("weeks") or [] if w.get("week") == pool.get("week")), None),
        },
        "recommended": [
            {
                "weight": r["weight"],
                "team": r["best_team"],
                "opp": fmt_opp(r["best_team"], r["home"], r["away"]),
                "loc": loc_letter(r["best_team"], r["home"]),
                "spread": r["best_spread"],
                "cbs_spread": r["best_spread"],
                "current_spread": signed_for_team(r["best_team"], r["home"], r.get("market_home")),
                "p": r["best_p"],
                "q_mkt": r.get("best_q_mkt"),
                "woo_delta": r.get("best_woo_delta"),
                "away": r["away"],
                "home": r["home"],
                "pool_home": r["pool_home"],
                "market_home": r.get("market_home"),
                "last_market_home": r.get("last_market_home"),
                "d_vs_pool": r.get("d_vs_pool"),
                "d_vs_last": r.get("d_vs_last"),
                "change": r.get("change") or "",
                "kickoff": r["kickoff"],
            }
            for r in ranked["recommended"]
        ],
        "all_sides": all_sides(ranked),
        "all": [
            {
                "away": r["away"],
                "home": r["home"],
                "status": r["status"],
                "weight": r.get("weight"),
                "best_team": r.get("best_team"),
                "best_spread": r.get("best_spread"),
                "best_p": r.get("best_p"),
                "q_mkt": r.get("best_q_mkt"),
                "woo_delta": r.get("best_woo_delta"),
                "pool_home": r.get("pool_home"),
                "market_home": r.get("market_home"),
                "last_market_home": r.get("last_market_home"),
                "d_vs_pool": r.get("d_vs_pool"),
                "d_vs_last": r.get("d_vs_last"),
            }
            for r in ranked["rows"]
        ],
    }
    (OUT / "picks.json").write_text(json.dumps(payload, indent=2))
    (ROOT / "data" / "last_market.json").write_text(
        json.dumps(
            {
                "saved_at": now.isoformat(),
                "games": [
                    {
                        "away": r["away"],
                        "home": r["home"],
                        "market_home": r.get("market_home"),
                    }
                    for r in ranked["rows"]
                    if r.get("market_home") is not None
                ],
            },
            indent=2,
        )
    )
    print(report)
    print(
        "MNF_ALERT="
        + ("1" if mnf_alert.get("alert") else "0")
        + "  "
        + mnf_alert.get("reason", "")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
