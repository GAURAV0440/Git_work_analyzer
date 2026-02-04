import re

TEST = re.compile(r'test\s*\(\s*["\'](.+?)["\']')
DESC = re.compile(r'test\.describe\s*\(\s*["\'](.+?)["\']')

def extract_tests_from_file(path):
    tests = []
    current = None
    try:
        for line in open(path, encoding="utf-8"):
            d = DESC.search(line)
            if d:
                current = d.group(1)
            t = TEST.search(line)
            if t:
                tests.append({"describe": current, "test_name": t.group(1)})
    except:
        pass
    return tests
