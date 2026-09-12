from __future__ import annotations

import json
import sys
from pathlib import Path

from .cost_anomaly import detect_anomalies


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print('Usage: python -m src.cli samples/sample.json', file=sys.stderr)
        return 2
    payload = json.loads(Path(args[0]).read_text(encoding='utf-8'))
    result = detect_anomalies(payload['records'])
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
