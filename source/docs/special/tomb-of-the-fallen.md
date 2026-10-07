# Tomb of the Fallen

{% set f = "npc/re/mobs/dungeons/lhz_dun_n.txt" %}
{% set reg = scalar(f, "regular_kills") %}
{% set mini = scalar(f, "mini_kills") %}

The Tomb of the Fallen (`lhz_dun_n`, the Nightmare Bio Laboratory) is full of the fallen heroes of the Bio Lab.
Killing them wakes their stronger third-job versions, and putting all of those to rest summons one of the MVPs.
It is a **map-wide group goal**: every player's kills count toward the same totals.

## How to get in

Use a {{ item(22687) }}. It warps you to a random spot in the Tomb. You can't use it while you're already inside.

- **Heimhunter** in the Eden Group market (`/navi paramk 71/15`) sells it for 200,000 Zeny. The shop
  restocks **1 per day** at midnight, for the whole server.
- The monsters inside drop it, so regulars can keep a supply going.

Inside the map you can't teleport or save a memo point, and you can't `@warp` straight to it.

## The three steps

### 1. Regular heroes

Kill **{{ reg }}** of one regular hero, and its third-job version rises as a **mini boss**.
Each of the 13 heroes counts separately.

The map announces it: *"[Tomb of the Fallen] Guillotine Cross Eremes has risen from the dead!"*

### 2. Mini bosses

Each of the 13 mini bosses must be killed **{{ mini }} times**. After each kill the count for its regular hero
starts again from 0, so another {{ reg }} regular kills bring it back. Once a mini boss has reached
{{ mini }} kills it stops coming back.

Each kill is announced with the progress: *"Rune Knight Seyren defeated (2/{{ mini }}). Fallen heroes laid to rest: 5/13."*

### 3. The MVP

When all 13 mini bosses have reached {{ mini }} kills, **one random MVP** appears at `/navi lhz_dun_n 140/230`.
The whole server sees *"[Tomb of the Fallen] … has appeared in the Tomb of the Fallen!"*

After the MVP dies, **kills don't count for 100 minutes**. When the wait ends, the map announces
*"The dead are restless again"* and the counting starts over from zero.

!!! info "In numbers"
    One full cycle takes about {{ fmt(reg * mini * 13) }} regular kills and {{ mini * 13 }} mini boss kills.
    That is a lot for a few players, so it pays to farm the map together.

!!! warning "A server restart resets everything"
    The counts are not saved. After a restart or a script reload, every hero starts again from 0.

## Monsters

| Regular hero ({{ reg }} kills) | Mini boss ({{ mini }} kills) | MVP version |
|---|---|---|
| {{ mob(3208) }} | {{ mob(3214) }} | {{ mob(3220) }} |
| {{ mob(3209) }} | {{ mob(3215) }} | {{ mob(3221) }} |
| {{ mob(3210) }} | {{ mob(3216) }} | {{ mob(3224) }} |
| {{ mob(3211) }} | {{ mob(3217) }} | {{ mob(3222) }} |
| {{ mob(3212) }} | {{ mob(3218) }} | {{ mob(3223) }} |
| {{ mob(3213) }} | {{ mob(3219) }} | {{ mob(3225) }} |
| {{ mob(3226) }} | {{ mob(3233) }} | {{ mob(3240) }} |
| {{ mob(3227) }} | {{ mob(3234) }} | {{ mob(3241) }} |
| {{ mob(3228) }} | {{ mob(3235) }} | {{ mob(3242) }} |
| {{ mob(3229) }} | {{ mob(3236) }} | {{ mob(3243) }} |
| {{ mob(3230) }} | {{ mob(3237) }} | {{ mob(3244) }} |
| {{ mob(3231) }} | {{ mob(3238) }} | {{ mob(3245) }} |
| {{ mob(3232) }} | {{ mob(3239) }} | {{ mob(3246) }} |

Only one MVP appears per cycle, picked at random from the 13.

## Cards

The **True** cards drop from the **regular** heroes, not from the mini bosses. Getting a True card doesn't mean a
mini boss spawned. The mini bosses drop no cards. The MVP versions drop the third-job cards.

| Regular hero | Card | MVP | Card |
|---|---|---|---|
| {{ mob(3208) }} | {{ item(4684) }} | {{ mob(3220) }} | {{ item(4674) }} |
| {{ mob(3209) }} | {{ item(4685) }} | {{ mob(3221) }} | {{ item(4675) }} |
| {{ mob(3210) }} | {{ item(4686) }} | {{ mob(3224) }} | {{ item(4678) }} |
| {{ mob(3211) }} | {{ item(4687) }} | {{ mob(3222) }} | {{ item(4676) }} |
| {{ mob(3212) }} | {{ item(4688) }} | {{ mob(3223) }} | {{ item(4677) }} |
| {{ mob(3213) }} | {{ item(4689) }} | {{ mob(3225) }} | {{ item(4679) }} |
| {{ mob(3226) }} | {{ item(4690) }} | {{ mob(3240) }} | {{ item(4680) }} |
| {{ mob(3227) }} | {{ item(4691) }} | {{ mob(3241) }} | {{ item(4681) }} |
| {{ mob(3228) }} | {{ item(4692) }} | {{ mob(3242) }} | {{ item(4671) }} |
| {{ mob(3229) }} | {{ item(4693) }} | {{ mob(3243) }} | {{ item(4672) }} |
| {{ mob(3230) }} | {{ item(4694) }} | {{ mob(3244) }} | {{ item(4682) }} |
| {{ mob(3231) }} | {{ item(4696) }} | {{ mob(3245) }} | {{ item(4673) }} |
| {{ mob(3232) }} | {{ item(4695) }} | {{ mob(3246) }} | {{ item(4683) }} |

Open a monster for its full drop list with the chances on Miracle.

## Related

- [Old Helmet Enchants (Nightmare Bio Lab)](../official/enchanters/old-helmet-enchants.md): the helmets made from the
  Tomb's drops.
- The Thanatos Tower trades for the Good and Evil Circlets also take True cards and Sentimental Fragments.
