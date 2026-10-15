# Coin Exchanger

**Location:** {{ npc_where("Coin Exchanger") }} · Quest Room

Converts coin items into points and points back into coins, at the same rate both ways.

| Points | Coin | Value |
|---|---|---|
| Mission Points | {{ item(30002) }} | 1 |
| Mission Points | {{ item(30003) }} | 5 |
| Mission Points | {{ item(30004) }} | 10 |
| Mission Points | {{ item(30005) }} | 30 |
| Mission Points | {{ item(30006) }} | 50 |
| Instance Points | {{ item(30018) }} | 1 |
| Event Points | {{ item(30017) }} | 1 |

You can hold at most **100,000** of each point type.

## MVP Soul: bound to normal

The **MVP Soul - Bound → Normal** option turns account-bound {{ item_name(30007) }} into normal ones, 1 for 1,
so you can trade them.

## Bank Notes

The **Bank Notes <-> Zeny** option changes Zeny into Bank Notes and back, at face value with no fee.
Bank Notes weigh 1 and can be traded, so they are an easy way to carry or trade large amounts of Zeny.

| Bank Note | Worth |
|---|---|
| {{ item(30064) }} | 50,000,000 Zeny |
| {{ item(30065) }} | 100,000,000 Zeny |
| {{ item(30066) }} | 500,000,000 Zeny |
| {{ item(30067) }} | 1,000,000,000 Zeny |

!!! warning "Zeny limit"
    A character can hold at most **2,147,483,647 Zeny**. Cashing a note is refused if it would take you over that,
    so spend or store some Zeny first. Bank Notes cannot be sold to NPC shops.
