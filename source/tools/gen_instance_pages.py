"""Create a page for every official instance that has none yet, and refresh the nav.

Run from wiki/:  python3 tools/gen_instance_pages.py
Existing pages are left alone, so text written above the macro survives.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import official  # noqa: E402

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(HERE, "docs", "official", "instances")

created = 0
nav = ["      - Instances:", "          - official/instances/index.md"]
for key, title, _ in sorted(official.instance_groups(), key=lambda g: g[1].lower()):
    path = os.path.join(DOCS, f"{key}.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f'# {title}\n\n{{{{ instance_page("{key}") }}}}\n')
        created += 1
    nav.append(f'          - "{title}": official/instances/{key}.md')

cfg = os.path.join(HERE, "mkdocs.yml")
text = open(cfg, encoding="utf-8").read()
text = re.sub(r"      - Instances: official/instances(?:/index)?\.md\n|      - Instances:\n(?:          - .*\n)+",
              "\n".join(nav) + "\n", text, count=1)
open(cfg, "w", encoding="utf-8").write(text)
print(f"{created} pages created, {len(nav) - 2} in the nav")
