# Cloud Cost Anomaly Detector

A Python cost-monitoring utility that flags unusual service spend using rolling baselines. It is aimed at cloud platform, infrastructure, and FinOps teams that need fast explanations for cost spikes.

## Highlights

- Builds rolling spend baselines per service
- Flags spikes by absolute delta and percentage growth
- Returns ranked anomaly explanations for engineering review

## Run

```powershell
python -m unittest discover -s tests
```

