"""MkDocs hooks: writes the Database JSON (tools/gen_db.py) into the built site, and links each enchanter guide to
its Database entry."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))


def on_post_build(config, **kwargs):
    import gen_db
    gen_db.build(os.path.join(config["site_dir"], "db", "data"), config["use_directory_urls"])


def on_page_markdown(markdown, page, **kwargs):
    import gen_enchants
    rel = page.file.src_uri
    folder, _, name = rel.rpartition("/")
    if folder not in gen_enchants.GUIDE_DIRS or name == "index.md":
        return markdown
    up = "../" * rel.count("/")
    note = (f'!!! tip "In the Database"\n    Every item this enchanter works on, the enchants it adds and the NPC on the map: '
            f'[open its Database entry]({up}db/enchants.md#G{name[:-3]}). Item pages link back here too.\n')
    return re.sub(r"^(# .*\n)", lambda m: m.group(1) + "\n" + note + "\n", markdown, count=1, flags=re.M)
