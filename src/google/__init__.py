import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="google", description="LeetCode flashcard data tools")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("ingest", help="build data/problems.json from the source lists")
    commands.add_parser("check", help="validate data/approaches.json against ASD-STE100 rules")
    args = parser.parse_args()

    if args.command == "ingest":
        from google.ingest import ingest

        ingest()
    else:
        from google.approaches import check

        raise SystemExit(check())
