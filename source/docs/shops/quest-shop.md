# Quest Shop

**Location:** {{ npc_where("Quest Shop") }} · Quest Room

The Quest Shop trades coins and materials for equipment. Pick a tab, select one item, and the NPC shows what
you need. Items bought here are announced to the server.

{% for tab in quest_shop_tabs() %}
## {{ tab }}

{{ quest_shop(loop.index) }}
{% endfor %}
