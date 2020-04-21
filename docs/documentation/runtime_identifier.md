---
layout: page
title: Runtime Identifiers
parent: Documentation
---

# Runtime Identifiers

`runtime_identifier` is an optional parameter that sits inside the description of the entity's behavior file, and is used to imitate a vanilla entity's hardcoded elements.
It accepts Vanilla Minecraft identifiers, like `minecraft:shulker`.

```json
"description": {
    "identifier": "assassin:my_box",
    "is_spawnable": true,
    "is_summonable": true,
    "is_experimental": false,
    "runtime_identifier": "minecraft:shulker"
}```

It's important to remember that `runtime_identifier` will only parse the hardcoded properties of an entity. This means that using a 100% datadriven mob as the Runtime Identifier will not add any new properties to your entity.

# Uses

Down below are a few Runtime Identifiers that you can add to your entity with their pros and cons.

`minecraft:shulker`
---
**Pros:**
- A solid collision box of 1x1x1.
- The entity will stick to the center of the block it's spawned in.
- Perfect for imitating a block.

**Cons:**
- If the block it's attached to is removed, the entity will teleport to another location nearby.
- If the entity is spawned on a non-full block (e.g. bed, slab, etc...), it will teleport to another location nearby.
- The solid collision box's width and height cannot be changed.

`minecraft:end_crystal`
---
**Pros:**
- The entity will stick to the center of the block it's spawned in.
- Unless teleported, the entity will always maintain its positions.
- Can be placed on any surface

**Cons:**
- Will always be pushable through by other entites.
- Cannot be configured to recieve damage.
- Cannot change the direction it faces.

## Additional Identifiers to look out for:
 - minecraft:boat
 - minecraft:egg
 - ...
 - Probably others! If you know what different Identifiers do, please get in touch!