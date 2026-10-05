# Card Trader

**Location:** {{ npc_where("Card Trader") }} · Quest Room

Trade unwanted cards for **Card Points**: every card is worth **1 point**, whatever card it is.
You can trade one card type at a time or **Trade ALL** cards in your inventory at once.

!!! warning "Trade ALL takes every card"
    Trade ALL removes every tradable card from your inventory. Put the cards you want to keep in storage first.

## Cards that cannot be traded

{{ items_table(arrays("npc/miracle/card.txt", "Card Trader")["banned_card_id"], "Card") }}

## Card Point Shop

{{ shop("CardR", collapsed=False) }}
