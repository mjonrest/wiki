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

The wiki rebuilds itself. The **Rebuild wiki** workflow (`.github/workflows/build.yml`) checks out
`mjonrest/Miracle-MMO`, adds pages for new instances, runs `build.sh` and commits the result to `main`. It runs:

- when the game repository pushes to `main` (its **Update wiki** workflow sends a `game-updated` event here),
- when anything in `source/` changes on `main` (a guide edit, a tool fix),
- every hour as a safety net (it skips the build when the game has not changed; `.game-commit` holds the game
  commit the site was last built from),
- by hand from the Actions tab.

When the rebuild changes the database it starts **Sync images** for new pictures.

Both repositories need the secret `WIKI_SYNC_TOKEN` (Settings > Secrets and variables > Actions): a fine-grained
GitHub token with access to `mjonrest/Miracle-MMO` and `mjonrest/wiki`, permission **Contents: Read and write**.

On the web server, pull the wiki on a timer so new builds go live without anyone logging in, for example with
cron (`crontab -e`):

```
*/5 * * * * cd /path/to/wiki && git pull -q --ff-only
```

To build by hand instead:

```sh
MIRACLE_SERVER=/path/to/Miracle-MMO source/build.sh
git add -A && git commit -m "Rebuild wiki" && git push
```

`build.sh` builds the site and replaces the built files at the repository root. If the address changes, update
`site_url` in `mkdocs.yml`.

New official instances get a page with `python3 tools/gen_instance_pages.py` (run in `source/`). It only adds
missing pages and rewrites the Instances menu, so text written by hand on a page stays.

## Item descriptions

Item pages show the effects translated from each item's scripts (`tools/describe.py`), and "Also search
descriptions" searches that same text. The client's `itemInfo.lua` is only used for the "Server" filter (jRO tags),
saved as `data/item_text.json`. When the client's itemInfo changes, refresh it and rebuild:

```sh
python3 tools/iteminfo.py /path/to/itemInfo.lua
```

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
