---
layout: page
title: Molang
parent: Documentation
---

# Molang

<details id="toc" class="top-level" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


The bedrock documentation for Molang is notoriously bad. This page will attempt to remedy this by providing additional details for individual queries, *where possible*. This page is intended to be searched, not read in full. Use the side-bar, or use `ctrl-f` to navigate.

# query.armor_texture_slot

Formatted like: `query.armor_texture_slot(x) = y`. 

Where `x` and `y` are both integer arguments, from the following table:

### X

| Argument | Slot       |
|----------|------------|
| 0        | Helmet     |
| 1        | Chestplace |
| 2        | Leggings   |
| 3        | Boots      |

### Y

| Argument | Type                  |
|----------|-----------------------|
| -1       | none                  |
| 0        | chain armor piece     |
| 1        | iron armor piece      |
| 2        | diamond armor piece   |
| 3        | Boots of any type     |
| 4        | gold armor piece      |
| 5        | elytra                |
| 6        | turtle helmet         |
| 7        | netherite armor piece |

### Example

`query.armor_texture_slot(3) == 2`: queries for Iron Boots.

# query.armor_material_slot

Formatted like: `query.armor_material_slot(x) = y`. 

Where `x` and `y` are both integer arguments, from the following table:

### X

| Argument | Slot       |
|----------|------------|
| 0        | Helmet     |
| 1        | Chestplace |
| 2        | Leggings   |
| 3        | Boots      |

### Y
Unknown, possibly:

| Argument | Slot                       |
|----------|----------------------------|
| 0        | Default armor material     |
| 1        | Enchanted armor material   |
| 2        | Leather armor material     |
| 3        | Leather enchanted material |

# query.armor_color_slot

*Notice: As of version `1.16.100.51`, this query is crashing minecraft. It might be fixed in later versions.*

Formatted like: `color = query.armor_color_slot(slot, channel)`. 

Where `slot` and `channel` are both integer arguments, from the following tables:

### Slot

| Argument | Slot       |
|----------|------------|
| 0        | Helmet     |
| 1        | Chestplace |
| 2        | Leggings   |
| 3        | Boots      |

### Channel

| Argument | Slot                       |
|----------|----------------------------|
| 0        | Red channel                |
| 1        | Green channel              |
| 2        | Blue channel               |
| 3        | Alpha channel              |

### Color

Query returns color value in specified channel.

# query.is_ghost

Formatted like: `is_ghost = query.is_ghost`. 

Return 1.0 or 0.0 based on whether the entity is a ghost.

Currently, only returns 1.0 for a guardian ghost and is used by its renderer.

# query.is_jumping

Formatted like: `is_jumping = query.is_jumping`. 

Return 1.0 or 0.0 based on whether the entity is jumping.

For the player, conditions for its activation are:
 - the jump button is pressed (includes being in water and climbing a scaffolding)
 - OR auto-jump is triggered
 - OR swimming with auto-jump

# query.structural_integrity

Formatted like: `structural_integrity = query.structural_integrity`. 

Used by boats and minecrafts for destroying it. It will decrease when attacking the entity and will recover with time. 
Probably unusable by anything other than boats and minecrafts.