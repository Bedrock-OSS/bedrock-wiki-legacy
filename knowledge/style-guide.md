---
layout: page
title: Style Guide
parent: Knowledge
---

# Style Guide

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

This document will present the officially supported Bedrock-Wiki style-guide for addon-creation. The goal of this guide is to promote best-practices while creating addons, and create a consistent format for everyone to follow.

## Structuring

No spaces in your file paths. `use_underscores`.

No `CAPITALS` in your identifiers, file names, or folder names, except at the top level.

## File and Folder names

| Concept              | Example Identifier         |
|----------------------|----------------------------|
| Behavior Pack        | dragons_BP                 |
| Resource Pack        | dragons_RP                 |
| Geometry             | dragon.geo.json            |
| Animation            | dragon.animation.json      |
| Animation Controller | dragon.ac.json             |
| RP Entity            | dragon.entity.rp.json      |
| BP Entity            | dragon.entity.bp.json      |
| BP Item              | dragon_tooth.item.bp.json  |
| RP Item              | dragon_tooth.item.rp.json  |
| Render Controller    | dragon.render.json         |
| Loot Table           | dragon.loot.json           |
| Dragon Saddle        | dragon_saddle.recipe.json  |
| Spawn Rules          | dragon.spawn.json          |
| Trade Table          | dragon.trade.json          |
| Particles            | dragon_magic.particle.json |
| Texture              | dragon.png                 |

## Namespaces

A good namespace is completely unique to you. Something like `mob` or `cars` or `content` or `custom` would be a **bad** namespace, since another developer might come up with the same namespace as you.

For personal projects, use a convenient version of your player name, and for team projects, use a convenient version of your team name.

When multiple developers work a project together, the namespace should always be shared. If credit is required, use sub-indexing: `sapphire.sirlich:dragon`

## Sub-indexing

Sub indexing is the use of `.` to separate chained concepts. Sub-indexing should go in descending order from big to small:

`animation.controller.dragon.flying.taking_off` **NOT** `animation.controller.dragon_take_off_flying`

`_` should be used as spaces when sub-indexing -don't use another dot. 

`animation.controller.dragon.flying.taking_off` **NOT** `animation.controller.dragon.flying.taking.off`

You can use sub-indexing in your entities:
`sirlich:dragon.drake`

## Groups and Events should complement each other

| Group        | Event               |
|--------------|---------------------|
| sirlich:wild | sirlich:become_wild |

## Functions should be nested

| Good               | Bad               |
|--------------------|-------------------|
| teleport/zone/hell | teleport_hellzone |

## Group into files when possible

All animations for a specific entity should be grouped together into one file for example.

## Split textures by path, not name

| Good        | Bad         |
|-------------|-------------|
| dragon/blue | dragon_blue |
| dragon/red  | dragon_red  |

## Acronyms when discussing

| Acronym | Concept                            |
|---------|------------------------------------|
| BP      | Behavior Pack                      |
| RP      | Resource pack                      |
| VRP     | Vanilla Resource Pack              |
| VBP     | Vanilla Behavior Pack              |
| AC      | Animation Controller               |
| RPAC    | Resource Pack Animation Controller |
| BPAC    | Behavior Pack Animation Controller |
| BB      | Blockbench                         |
| BDS     | Bedrock Dedicated Server           |










