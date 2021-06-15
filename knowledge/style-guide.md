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

This document will present the officially supported Bedrock-Wiki style-guide for addon-creation. The goal of this guide is to promote best-practices
while creating addons and create a consistent format for everyone to follow.

The style-guide is a living, breathing document, which will evolve as addon-creation evolves. Please get in touch if you think something needs to be
updated or changed.

## Folder Structure

- No spaces in your file paths. `use_underscores`.
- No `CAPITALS` in your identifiers, file names, or folder names.
- The total character-length of any path must not exceed 80 characters (console limitation).
- Content folders should use consistent pluralization: Don't mix and match.

## Identifiers

Identifiers are used almost everywhere, and this section applies to entities, component_groups, events, and anything else that takes a
`namespace:name` pair. Identifiers are to be specified using the following rules:

- Do not start the identifier with a number.
- Identifiers cannot be numbers only.
- All lowercase.
- No spaces.

## File and Folder names

If multiple options are available, the preference goes to the first found item. However, the second one is recognized as valid as well.

| Concept              | Example Identifier                                   |
| -------------------- | ---------------------------------------------------- |
| Behavior Pack        | dragons_bp                                           |
| Resource Pack        | dragons_rp                                           |
| Geometry             | dragon.geo.json                                      |
| Animation            | dragon.animation.json                                |
| Animation Controller | dragon.controller.json<br/>dragon.ac.json            |
| Dialogue             | intro.diag.json                                      |
| Behaviorpack Entity  | dragon.entity.json<br/>dragon.entity.bp.json         |
| Resourcepack Entity  | dragon.entity.json<br/>dragon.entity.rp.json         |
| Behaviorpack Item    | dragon_tooth.item.json<br/>dragon_tooth.item.bp.json |
| Resourcepack Item    | dragon_tooth.item.json<br/>dragon_tooth.item.rp.json |
| Render Controller    | dragon.render.json                                   |
| Loot Table           | dragon.loot.json                                     |
| Recipe               | dragon_saddle.recipe.json                            |
| Spawn Rules          | dragon.spawn.json                                    |
| Trade Table          | dragon.trade.json                                    |
| Particles            | dragon_magic.particle.json                           |
| Texture              | dragon.png                                           |

Note: prefered to use subfolders instead of underscores in filenames. for example: dragon/saddle.recipe.json instead of dragon_saddle.recipe.json

## Namespaces

A good namespace should be completely unique to you or your team. Something like `mob` or `cars` or `content` or `custom` would be a **bad**
namespace, since another developer might come up with the same namespace as you. For personal projects, use a convenient version of your player name,
and for team projects, use a convenient version of your team name.  
Note: `minecraft` and `minecon` namespaces are reserved. Don't use these unless you are overriding the default Minecraft specification.

**Examples**

- `sapphire:dragon`
- `sirlich:dragon`

**Where to use name-spaces:** ✔️

- blocks
- entities
- items
- particles
- spawn rules

**Where to use name-spaces optional:**

- component-groups
- events
- geometry
- sounds

**When not to use name-spaces:** ❌

- do not include your name-space in any folder path or file-name

## Groups and Events should complement each other

| Group        | Event                  |
| ------------ | ---------------------- |
| sirlich:wild | ✔️ sirlich:become_wild |
| sirlich:wild | ❌ sirlich:wild        |
| sirlich:tame | ✔️ sirlich:on_tame     |
| sirlich:tame | ❌ sirlich:tame        |

### Types defintions

A second accepted form is to use the namespace of component groups and events as type declarations. This can be used as an indication of
transformation, signals going in or out. or a specific event made for a certain system:

**Examples**

| Group        | Event                                   |
| ------------ | --------------------------------------- |
| self:wild    | to:wild                                 |
| self:tame    | to:tame                                 |
| self:varian1 | to:varian1                              |
| self:varian2 | to:varian2                              |
| self:baby    | to:adult                                |
| self:adult   | to:baby                                 |
| anger:attack | anger:attack</br>out:anger</br>in:anger |
| anger:follow | anger:follow                            |
| music:dance  | music:dance                             |
| music:stop   | music:stop                              |

## Sub-indexing

Sub indexing is the use of `.` to separate chained concepts. Sub-indexing should go in descending order from big to small:

✔️ `animation.controller.dragon.flying.taking_off`

❌ `animation.controller.dragon_take_off_flying`

When using sub-indexing, use `_` as a space, not another `.`.

✔️ `animation.controller.dragon.flying.taking_off`

❌ `animation.controller.dragon.flying.taking.off`

You can use sub-indexing in your entities: `sirlich:dragon.drake`

## Short-Names should be Generic

Short-names are file-specific identifiers, which are used to map between an identifier and a pretty name. They are instrumental, because they allow us
to re-use animation controllers, and render controllers. For this reason, your short-names should be generic.

✔️ `"sit": "animation.dragon.sit"`

❌ `"dragon_sitting": "animation.dragon.sit"`

When we make short-names of this form, we can use a generic "sit" animation controller for all of them, since we can use the `sit` short-name to play
the sit animation.

## Functions should be nested

✔️ `function teleport/zone/hell`

❌ `function teleport_hellzone`

## Group animations files when possible

Example:

```jsonc
{
	"format_version": "1.8.0",
	"animations": {
		"animation.dragon.sit": {...},
    "animation.dragon.fly": {...},
		"animation.dragon.roar": {...},
  }
}
```

## Split textures by path, not name

✔️ `textures/dragon/red`

❌ `textures/dragon_red_skin`

✔️ `textures/npc/dragon_hunter/archer`

❌ `textures npc/dragon_hunter_archer`

## .lang File Comments

Comments intended for the localizer should always be in-line, in the following format:

```ini
the.key=The string<\t>## Comment, intended for the one localizing
```

`<\t>` represents a tab-character.

Own-line comments can be used for organizational purposes, but should not store localization-critical information.

## Acronyms when discussing

| Acronym | Concept                            |
| ------- | ---------------------------------- |
| BP      | Behavior Pack                      |
| RP      | Resource pack                      |
| VRP     | Vanilla Resource Pack              |
| VBP     | Vanilla Behavior Pack              |
| AC      | Animation Controller               |
| RPAC    | Resource Pack Animation Controller |
| BPAC    | Behavior Pack Animation Controller |
| BB      | Blockbench                         |
| BDS     | Bedrock Dedicated Server           |
| FPV     | First Person View                  |
