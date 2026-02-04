import json, os

def ensure_dir():
    os.makedirs("output", exist_ok=True)

def build_cli(data):
    lines = []
    for file, d in data.items():
        lines.append(f"[{d['impact'].upper()}] {file}")
        for t in d["tests"]:
            if t["describe"]:
                lines.append(f"  - {t['describe']} › {t['test_name']}")
            else:
                lines.append(f"  - {t['test_name']}")
    return "\n".join(lines)

def print_and_save_outputs(data, commit):
    ensure_dir()
    cli = build_cli(data)
    print(cli)

    with open(f"output/{commit}_cli.txt", "w", encoding="utf-8") as f:
        f.write(cli)

    out = {"commit": commit, "impacted_tests": []}
    for file, d in data.items():
        for t in d["tests"]:
            out["impacted_tests"].append({
                "file": file,
                "describe": t["describe"],
                "test_name": t["test_name"],
                "impact": d["impact"]
            })

    with open(f"output/{commit}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
