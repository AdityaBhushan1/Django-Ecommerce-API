from collections import Counter
from glob import glob
ctr = Counter()
for ctr["files"], f in enumerate(glob("./**/*.py", recursive=True)):
    with open(f, encoding="UTF-8") as fp:
        for ctr["lines"], line in enumerate(fp, ctr["lines"]):
            line = line.lstrip()
            ctr["imports"] += line.startswith("import") + line.startswith("from")
            ctr["classes"] += line.startswith("class")
            ctr["comments"] += "#" in line
            ctr["functions"] += line.startswith("def")
            ctr["coroutines"] += line.startswith("async def")
            ctr["docstrings"] += line.startswith('"""') + line.startswith("'''")


print("\n".join([f"{k.capitalize()}=> {v}" for k, v in ctr.items()]))