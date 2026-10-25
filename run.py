"""Execute a documented local scenario: python run.py ENGINE INPUT.json"""
import argparse
import json
from pathlib import Path
import sys
from calculations import ENGINES, calculate

def main():
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,"reconfigure"):
            stream.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("engine",choices=sorted(ENGINES))
    parser.add_argument("input",type=Path)
    args = parser.parse_args()
    try:
        if args.input.stat().st_size > 5000000:
            raise ValueError("Input file exceeds 5 MB")
        # Reject JSON NaN/Infinity, although Python's JSON decoder accepts them by default.
        def reject_constant(value):
            raise ValueError(f"Invalid JSON numeric constant: {value}")
        inputs = json.loads(args.input.read_text(encoding="utf-8-sig"),parse_constant=reject_constant)
        result = calculate(args.engine,inputs)
        print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False))
        return 0
    except (OSError,ValueError) as error:
        print(json.dumps({"error":str(error)},ensure_ascii=False),file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
