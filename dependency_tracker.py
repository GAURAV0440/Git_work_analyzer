import os

def normalize(path):
    path = path.replace("\\", "/")
    if path.endswith(".ts"):
        path = path[:-3]
    if path.startswith("tests/"):
        path = path[6:]
    return path

def find_tests_importing_helper(repo, helper):
    helper_key = normalize(os.path.relpath(helper, repo))
    tests_dir = os.path.join(repo, "tests")
    impacted = []

    for root, _, files in os.walk(tests_dir):
        for f in files:
            if not f.endswith(".spec.ts"):
                continue
            path = os.path.join(root, f)
            try:
                if helper_key in open(path, encoding="utf-8").read():
                    impacted.append(os.path.relpath(path, repo))
            except:
                pass

    return impacted
