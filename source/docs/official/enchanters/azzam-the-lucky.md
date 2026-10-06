# Azzam the Lucky (Nebula Armor and Signets of Star)

<!-- npcs: Azzam The Lucky; OSC0007 -->

Two NPCs called **Azzam the Lucky** stand side by side and enchant the Constellation Tower gear:

- **Azzam the Lucky #1** enchants the **Nebula armors**.
- **Azzam the Lucky #2** enchants the **Signet of Star** accessories.

Both always succeed when adding an enchant. The only step that can fail is the Slot 2 upgrade on Signets.
Refine, the card in the first slot and the enchant grade are always kept.

## Nebula Armor (Azzam the Lucky #1)

**Where:** `/navi grademk 42/185`

### Items it works on

You must be **wearing** the armor, and it must be refined to **+9 or higher**.

| Armor | Own materials |
|---|---|
| {{ item(450169) }} | {{ item(1000398) }}, {{ item(1000442) }} |
| {{ item(450170) }} | {{ item(1000399) }}, {{ item(1000443) }} |
| {{ item(450171) }} | {{ item(1000400) }}, {{ item(1000444) }} |
| {{ item(450172) }} | {{ item(1000401) }}, {{ item(1000445) }} |
| {{ item(450173) }} | {{ item(1000402) }}, {{ item(1000446) }} |
| {{ item(450174) }} | {{ item(1000403) }}, {{ item(1000447) }} |

"Own materials" means the powder and fragment that match **your** armor. The NPC asks for those by name.

Enchants go in this order: **Slot 4 → Slot 3 → Slot 2**. The menu only offers the next empty slot.

After each change the armor goes back to your inventory unequipped, so put it on again before you talk to
Azzam again.

### Costs

| Step | Cost | Success |
|---|---|---|
| Enchant Slot 4 | 5 {{ item(1000372) }} + 50,000z | 100% |
| Enchant Slot 3 | 5 of your armor's powder + 100,000z | 100% |
| Enchant Slot 2 | 5 of your armor's fragment + 1,000,000z | 100% |

### Slot 4: stats

| Enchant | Chance |
|---|---|
| {{ item(4702) }} | 15% |
| {{ item(4703) }} | 4.5% |
| {{ item(4704) }} | 0.5% |
| {{ item(4712) }} | 15% |
| {{ item(4713) }} | 4.5% |
| {{ item(4714) }} | 0.5% |
| {{ item(4721) }} | 15% |
| {{ item(4722) }} | 4.5% |
| {{ item(4723) }} | 0.5% |
| {{ item(4732) }} | 15% |
| {{ item(4733) }} | 4.5% |
| {{ item(4734) }} | 0.5% |
| {{ item(4742) }} | 15% |
| {{ item(4743) }} | 4.5% |
| {{ item(4744) }} | 0.5% |

### Slot 3: Nebula enchants

| Enchant | Lv1 | Lv2 | Lv3 |
|---|---|---|---|
| Fighting Spirit ({{ item(310727) }}, {{ item(310728) }}, {{ item(310729) }}) | 14% | 2.4% | 0.3% |
| Expert Archer ({{ item(310730) }}, {{ item(310731) }}, {{ item(310732) }}) | 14% | 2.4% | 0.3% |
| Sharp ({{ item(310733) }}, {{ item(310734) }}, {{ item(310735) }}) | 14% | 2.4% | 0.2% |
| Spell ({{ item(310736) }}, {{ item(310737) }}, {{ item(310738) }}) | 14% | 2.4% | 0.2% |
| Healing ({{ item(310739) }}, {{ item(310740) }}, {{ item(310741) }}) | 14% | 2.4% | 0.3% |
| Health ({{ item(310742) }}, {{ item(310743) }}, {{ item(310744) }}) | 14% | 2.4% | 0.3% |

### Slot 2: Star Clusters

The Star Cluster that matches your armor is much more likely. Power armor favours Power, Stamina armor favours
Stamina, Concentration suit favours Concentration, and so on.

| Type | Lv1 | Lv2 | Lv3 |
|---|---|---|---|
| Power | {{ item(310674) }} | {{ item(310675) }} | {{ item(310676) }} |
| Stamina | {{ item(310677) }} | {{ item(310678) }} | {{ item(310679) }} |
| Concentration | {{ item(310680) }} | {{ item(310681) }} | {{ item(310682) }} |
| Creative | {{ item(310683) }} | {{ item(310684) }} | {{ item(310685) }} |
| Spell | {{ item(310686) }} | {{ item(310687) }} | {{ item(310688) }} |
| Wisdom | {{ item(310689) }} | {{ item(310690) }} | {{ item(310691) }} |

Chances on every armor **except** {{ item(450172) }}:

| Cluster type | Lv1 | Lv2 | Lv3 |
|---|---|---|---|
| Your armor's own type | 42% | 7.2% | 0.9% |
| Creative (when it is not your type) | 7.6% | 2% | 0.3% |
| Every other type | 7.7% | 2% | 0.3% |

Chances on {{ item(450172) }}:

| Cluster type | Lv1 | Lv2 | Lv3 |
|---|---|---|---|
| Creative | 41.96% | 7.19% | 0.9% |
| Every other type | 7.69% | 2% | 0.3% |

### Upgrading an enchant

Every enchant above (except the top level) can be raised one level at a time. Upgrades always succeed.

| Slot | Lv1 → Lv2 | Lv2 → Lv3 |
|---|---|---|
| Slot 4 (stats, for example {{ item(4702) }} → {{ item(4703) }} → {{ item(4704) }}) | 25 {{ item(1000372) }} + 250,000z | 75 {{ item(1000372) }} + 750,000z |
| Slot 3 | 25 of your armor's powder + 500,000z | 75 of your armor's powder + 1,500,000z |
| Slot 2 | 25 of your armor's fragment + 5,000,000z | 75 of your armor's fragment + 15,000,000z |

!!! warning "Known issue: the upgrade list can pick the wrong slot"
    The list of slots under **Upgrade Enchant** is numbered wrongly. It only lines up when Slot 3 holds an
    enchant that can still be upgraded. Otherwise the entry you click can upgrade a **different** slot, and
    **Cancel** can open an upgrade instead of closing.

    Always read the **Upgrade path** line on the next screen before you confirm. It must show your current
    enchant → the next level. If the right side is blank or shows the wrong enchant, choose **Cancel**.
    Confirming a blank upgrade takes the materials and either does nothing or **deletes the enchant** in that
    slot.

### Reroll and reset

| Option | Cost | What it does |
|---|---|---|
| Reroll Slot 4 | 500 {{ item(1000372) }} | Rolls a new Slot 4 stat from the Slot 4 table. Slots 2 and 3 are kept. |
| Reset All Enchants | 10 {{ item(1000372) }} + 1,000,000z | Removes all three enchants. Refine, the first card and the grade are kept. |

Both always succeed. A reroll can land on the same enchant you already had.

!!! warning "Known issue: Reroll Slot 4 with a spare copy"
    **Reroll Slot 4** looks for the armor by item ID instead of taking the one you are wearing. If you carry a
    second copy of the same Nebula armor, the NPC can use up that copy instead. Keep only the armor you are
    rerolling in your inventory.

## Signets of Star (Azzam the Lucky #2)

**Where:** `/navi grademk 45/185`

### Items it works on

Wear the signet in either accessory slot. If you wear two, the NPC asks which one.

{{ item(490132) }}, {{ item(490133) }}, {{ item(490134) }}, {{ item(490135) }}, {{ item(490136) }},
{{ item(490137) }}

The signet goes back to your inventory unequipped after every change.

!!! warning "Known issue: identical signets"
    The NPC takes the signet out of your inventory by item ID. If you carry or wear **two copies of the same
    signet**, it may change the other copy. Keep only one copy of that signet on you while enchanting.

### Slot 3 and Slot 4 (random)

Pick the slot, then pay. Each slot can only be filled once. Reset first if it already has an enchant.

| Slot | Cost | Success |
|---|---|---|
| Slot 3 | 10 {{ item(1000373) }} + 500,000z | 100% |
| Slot 4 | 5 {{ item(1000373) }} + 300,000z | 100% |

Both slots use the same table:

| Enchant | Chance |
|---|---|
| {{ item(4809) }} | 20.12% |
| {{ item(4816) }} | 20.12% |
| {{ item(4834) }} | 20.12% |
| {{ item(4813) }} | 20.02% |
| {{ item(4808) }} | 3.5% |
| {{ item(4812) }} | 3.5% |
| {{ item(4835) }} | 3.5% |
| {{ item(4843) }} | 3.5% |
| {{ item(310692) }} | 0.8% |
| {{ item(310697) }} | 0.8% |
| {{ item(310702) }} | 0.8% |
| {{ item(310707) }} | 0.8% |
| {{ item(310712) }} | 0.8% |
| {{ item(310717) }} | 0.8% |
| {{ item(310722) }} | 0.8% |

### Upgrade Normal Enchant (Slot 3 or 4)

Turns a Lv3 enchant into Lv4. Always succeeds.

| From | To |
|---|---|
| {{ item(4809) }} | {{ item(4808) }} |
| {{ item(4813) }} | {{ item(4812) }} |
| {{ item(4816) }} | {{ item(4843) }} |
| {{ item(4834) }} | {{ item(4835) }} |

| Slot | Cost |
|---|---|
| Slot 3 | 25 {{ item(1000373) }} + 1,500,000z |
| Slot 4 | 50 {{ item(1000373) }} + 2,500,000z |

### Upgrade Star Enchant (Slot 3 or 4)

Always succeeds.

| From | To | Cost |
|---|---|---|
| {{ item(310702) }} | {{ item(310703) }} | 25 {{ item(1000373) }} + 1,500,000z |
| {{ item(310703) }} | {{ item(310704) }} | 75 {{ item(1000373) }} + 4,500,000z |
| {{ item(310704) }} | {{ item(310705) }} | 150 {{ item(1000373) }} + 9,000,000z |
| {{ item(310705) }} | {{ item(310706) }} | 250 {{ item(1000373) }} + 15,000,000z |

!!! warning "Known issue: only Star of Sharp can be upgraded"
    Only the **Star of Sharp** line is in the upgrade list. Star of Mettle, Master Archer, Spell, Speed, Vital
    and Spirit get "No upgrade available for this enchant!". The script also has a more expensive price list
    for Slot 3, but it is never used, so Slot 3 pays the prices above.

### Slot 2: Star Clusters (selectable)

Choose the Star Cluster you want. It always succeeds. Slot 2 must be empty.

| Enchant | Cost |
|---|---|
| {{ item(313024) }} | 15 {{ item(1000442) }}, 10 {{ item(1000444) }}, 15 {{ item(1000447) }}, 20 {{ item(1001599) }}, 5,000,000z |
| {{ item(313029) }} | 10 {{ item(1000442) }}, 15 {{ item(1000445) }}, 15 {{ item(1000446) }}, 20 {{ item(1001599) }}, 5,000,000z |
| {{ item(313034) }} | 15 {{ item(1000443) }}, 10 {{ item(1000444) }}, 15 {{ item(1000446) }}, 20 {{ item(1001599) }}, 5,000,000z |
| {{ item(313039) }} | 15 {{ item(1000443) }}, 15 {{ item(1000445) }}, 10 {{ item(1000447) }}, 20 {{ item(1001599) }}, 5,000,000z |

### Slot 2 Upgrade

Each try costs the materials below whether it works or not. On failure the enchant stays the same level
(no downgrade, nothing breaks).

| Step | Success | Zeny | {{ item(1001599) }} |
|---|---|---|---|
| Lv1 → Lv2 | 80% | 500,000z | 4 |
| Lv2 → Lv3 | 65% | 1,000,000z | 8 |
| Lv3 → Lv4 | 45% | 2,000,000z | 16 |
| Lv4 → Lv5 | 25% | 3,500,000z | 28 |

The other materials per step, for Lv1 → Lv2 / Lv2 → Lv3 / Lv3 → Lv4 / Lv4 → Lv5:

| Cluster | Materials |
|---|---|
| Strength ({{ item(313024) }} → {{ item(313028) }}) | {{ item(1000442) }} 5/10/20/35, {{ item(1000444) }} 4/8/16/28, {{ item(1000447) }} 5/10/20/35 |
| Luck ({{ item(313029) }} → {{ item(313033) }}) | {{ item(1000442) }} 4/8/16/28, {{ item(1000445) }} 5/10/20/35, {{ item(1000446) }} 5/10/20/35 |
| Intelligence ({{ item(313034) }} → {{ item(313038) }}) | {{ item(1000443) }} 5/10/20/35, {{ item(1000444) }} 4/8/16/28, {{ item(1000446) }} 5/10/20/35 |
| Resistance ({{ item(313039) }} → {{ item(313043) }}) | {{ item(1000443) }} 5/10/20/35, {{ item(1000445) }} 5/10/20/35, {{ item(1000447) }} 4/8/16/28 |

### Reset

30 {{ item(1000372) }} + 500,000z, always succeeds. Removes the enchants in slots 2, 3 and 4. Refine, the
first card and the grade are kept. You pay even if the signet has no enchants.

## Meteorite Powder

The machine **OSC0007** at `/navi e_tower 78/112` breaks down {{ item(1000373) }}: each fragment becomes
40 {{ item(1000372) }}. Type how many fragments to break down.

!!! tip
    The Reroll Slot 4 option needs 500 {{ item(1000372) }}, which is 13 fragments' worth. Resetting and
    enchanting Slot 4 again costs only 15 powder and 1,050,000z, but it also wipes Slots 2 and 3.
