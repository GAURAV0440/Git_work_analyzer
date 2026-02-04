import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze impacted Playwright tests from a Git commit"
    )

    parser.add_argument(
        "--commit",
        required=True,
        help="Git commit SHA to analyze"
    )

    parser.add_argument(
        "--repo",
        required=True,
        help="Path to local flash-tests repository"
    )

    parser.add_argument(
        "--format",
        choices=["cli", "json"],
        default="cli",
        help="Output format (default: cli)"
    )

    return parser.parse_args()
