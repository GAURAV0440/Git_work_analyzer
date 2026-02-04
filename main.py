from cli import parse_args
from git_utils import get_changed_files
from test_parser import extract_tests_from_file
from dependency_tracker import find_tests_importing_helper
from output import print_and_save_outputs
import os

def is_test_file(path):
    return path.startswith("tests/") and path.endswith(".spec.ts")

def is_helper_file(path):
    return path.startswith("tests/") and path.endswith(".ts") and not path.endswith(".spec.ts")

def map_status(status):
    return {"A": "added", "M": "modified", "D": "removed"}.get(status, "modified")

def main():
    args = parse_args()
    print("\n🔍 Analyzing impacted tests...\n")

    changes = get_changed_files(args.repo, args.commit)
    impacted = {}

    for status, path in changes:
        if is_test_file(path):
            impacted[path] = {
                "impact": map_status(status),
                "tests": extract_tests_from_file(os.path.join(args.repo, path))
            }

    for _, path in changes:
        if is_helper_file(path):
            for test_file in find_tests_importing_helper(args.repo, os.path.join(args.repo, path)):
                if test_file not in impacted:
                    impacted[test_file] = {
                        "impact": "modified",
                        "tests": extract_tests_from_file(os.path.join(args.repo, test_file))
                    }

    if not impacted:
        print("No impacted tests found.")
        return

    print_and_save_outputs(impacted, args.commit)

if __name__ == "__main__":
    main()
