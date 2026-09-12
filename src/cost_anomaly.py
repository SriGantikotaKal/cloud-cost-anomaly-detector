from __future__ import annotations

from collections import defaultdict
from statistics import mean
from typing import Iterable, Mapping


def detect_anomalies(
    records: Iterable[Mapping[str, object]],
    baseline_days: int = 7,
    min_delta_usd: float = 100.0,
    min_growth_ratio: float = 0.5,
) -> list[dict[str, object]]:
    by_service: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        by_service[str(record["service"])].append(
            {"date": str(record["date"]), "cost_usd": float(record["cost_usd"])}
        )

    anomalies: list[dict[str, object]] = []
    for service, service_records in by_service.items():
        ordered = sorted(service_records, key=lambda item: str(item["date"]))
        for index in range(baseline_days, len(ordered)):
            baseline = ordered[index - baseline_days:index]
            baseline_average = mean(float(item["cost_usd"]) for item in baseline)
            current_cost = float(ordered[index]["cost_usd"])
            delta = current_cost - baseline_average
            growth = delta / baseline_average if baseline_average else 0
            if delta >= min_delta_usd and growth >= min_growth_ratio:
                anomalies.append(
                    {
                        "service": service,
                        "date": ordered[index]["date"],
                        "cost_usd": round(current_cost, 2),
                        "baseline_average_usd": round(baseline_average, 2),
                        "delta_usd": round(delta, 2),
                        "growth_ratio": round(growth, 2),
                    }
                )

    return sorted(anomalies, key=lambda item: float(item["delta_usd"]), reverse=True)

