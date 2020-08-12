---
layout: page
title: Runtime Identifiers
parent: Knowledge
---

# Runtime Identifiers

`runtime_identifier` is an optional parameter that sits inside the description of the entity's behavior file, and is used to imitate a vanilla entity's hard-coded elements.
It accepts Vanilla Minecraft identifiers, like `minecraft:shulker`.

```json
"description": {
    "identifier": "assassin:my_box",
    "is_spawnable": true,
    "is_summonable": true,
    "is_experimental": false,
    "runtime_identifier": "minecraft:shulker"
}
```

It's important to remember that `runtime_identifier` will only parse the hard-coded properties of an entity. This means that using a 100% datadriven mob as the Runtime Identifier will not add any new properties to your entity.

# Using Runtime Identifiers

Down below are a few Runtime Identifiers that you can add to your entity with their pros and cons.

## `minecraft:shulker`
---
### Pros
- A solid collision box of 1x1x1.
- The entity will stick to the center of the block it's spawned in.
- Perfect for imitating a block.

### Cons
- If the block it's attached to is removed, the entity will teleport to another location nearby.
- If the entity is spawned on a non-full block (e.g. bed, slab, etc...), it will teleport to another location nearby.
- The solid collision box's width and height cannot be changed.

## `minecraft:end_crystal`
---
### Pros
- The entity will stick to the center of the block it's spawned in.
- Unless teleported, the entity will always maintain its positions.
- Can be placed on any surface

### Cons
- Will always be pushable through by other entites.
- Cannot be configured to recieve damage.
- Cannot change the direction it faces.

## `minecraft:parrot`
### Notes:
 - makes the wing flap animation able to work
 - makes the mob fall slowly
 - makes it dance to music discs

## `minecraft:armor_stand`
### Notes:
 - Disables entity shadows
 - Equipment placeable on/removable from entity

## `minecraft:iron_golem`
### Notes:
- Allows launching attack
- Speeds up arm and leg animation (can be fixed manually, ~1/4 speed)
- May interact poorly with village/villager logic.

## `minecraft:arrow`
### Notes:
- Disables death animation, sound, and particles
- Disables entity shadow
- Not interactable

## `minecraft:thrown_trident`
### Notes:
- Disables death animation, sound, and particles
- Disables entity shadow
- Not interactable

## `minecraft:minecart`
### Notes:
- Disables entity shadow
- Makes the entity drop a minecart on death