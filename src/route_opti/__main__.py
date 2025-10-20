"""Command-line entry point for the route_opti playground."""

from __future__ import annotations

import argparse

from .core import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Demo entry point for route_opti")
    parser.add_argument("name", nargs="?", default="traveler", help="Name to greet")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
