import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.cost_anomaly import detect_anomalies


class CostAnomalyTests(unittest.TestCase):
    def test_detects_ranked_spend_spikes(self):
        records = [
            {"service": "compute", "date": f"2026-09-0{day}", "cost_usd": 100}
            for day in range(1, 8)
        ]
        records.append({"service": "compute", "date": "2026-09-08", "cost_usd": 280})

        anomalies = detect_anomalies(records)

        self.assertEqual(len(anomalies), 1)
        self.assertEqual(anomalies[0]["service"], "compute")
        self.assertEqual(anomalies[0]["delta_usd"], 180.0)

    def test_ignores_small_changes(self):
        records = [{"service": "storage", "date": f"2026-09-0{day}", "cost_usd": 50} for day in range(1, 8)]
        records.append({"service": "storage", "date": "2026-09-08", "cost_usd": 62})

        self.assertEqual(detect_anomalies(records), [])


if __name__ == "__main__":
    unittest.main()

