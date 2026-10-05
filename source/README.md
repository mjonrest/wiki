# Miracle RO Wiki

The player wiki for Miracle, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Pages are Markdown files in `docs/`. Prices, item lists, enchant pools, NPC locations and the event schedule
are **not typed by hand**: the macros in `main.py` read them from the server files when the site is built
(`npc/scripts_custom.conf`, the scripts in `npc/miracle/`, `npc/custom/barters.yml`, and the item, monster
and enchant databases in `db/`). Change an NPC script, rebuild, and the wiki follows.

## Layout

This repository holds two things:

- `source/`: the MkDocs project (this folder).
- Everything else at the root: the built site that is served at https://miracle-mmo.com/wiki/. Don't edit it by
  hand; it is overwritten on every build.

The macros read the server files from a checkout of `mjonrest/Miracle-MMO`. Set `MIRACLE_SERVER` to its path, or
keep it next to this repository as `../Miracle-MMO`.

## Preview locally

```sh
cd source
pip install -r requirements.txt
MIRACLE_SERVER=/path/to/Miracle-MMO mkdocs serve   # http://127.0.0.1:8000, reloads on save
```

## Publishing

```sh
MIRACLE_SERVER=/path/to/Miracle-MMO source/build.sh
git add -A && git commit -m "Rebuild wiki" && git push
```

`build.sh` builds the site and replaces the built files at the repository root. On the web server, run `git pull`
in the wiki folder. If the address changes, update `site_url` in `mkdocs.yml`.

New official instances get a page with `python3 tools/gen_instance_pages.py` (run in `source/`). It only adds
missing pages and rewrites the Instances menu, so text written by hand on a page stays.

## Writing pages

Useful macros (see `main.py` for all of them):

| Macro | Output |
|---|---|
| `{{ item(30002) }}` | Item name with its id |
| `{{ shop("CardR") }}` | Price table of a shop, pointshop, itemshop or barter, by its script name |
| `{{ quest_shop(1) }}` | One tab of the Quest Shop |
| `{{ npc_where("Card Trader") }}` | Map and coordinates of an NPC |
| `{{ arrays("npc/miracle/card.txt", "Card Trader") }}` | Every `setarray` of that NPC, for custom tables |
| `{{ item_enchant(15) }}` | An entry of `db/re/item_enchant.yml` with chances |

Server facts on the home page (rates, client) live under `extra.server` in `mkdocs.yml`. `conf/import/` is not in
the repository, so update them there if the live server overrides `conf/battle/`.
