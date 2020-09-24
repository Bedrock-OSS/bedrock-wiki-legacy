---
layout: page
title: Molang
parent: Documentation
---

# Molang

<details id="toc" open markdown="block">
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