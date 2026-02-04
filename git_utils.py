import subprocess

def get_changed_files(repo, commit):
    result = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "--name-status", "-r", commit],
        cwd=repo,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    changes = []
    for line in result.stdout.strip().split("\n"):
        if line:
            s, f = line.split("\t")
            changes.append((s, f))
    return changes
