"""MkDocs hooks: writes the Database JSON (tools/gen_db.py) into the built site."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools"))


def on_post_build(config, **kwargs):
    import gen_db
    gen_db.build(os.path.join(config["site_dir"], "db", "data"), config["use_directory_urls"])
