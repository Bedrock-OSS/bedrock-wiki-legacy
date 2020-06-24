---
layout: page
title: Cancelling Death Animations
parent: Tutorials
---

# Cancelling Death Animations

Death animation refers to the rotation of the entity as it dies. This is accompanied by a red coloring, and followed shortly after by the disappearance of the entity geometry, and the appearance of the death particles.

# Teleporting the Entity

A fairly common way to remove entities without causing death-effects, is to simply teleport them into the void. This can be done from animation controllers like:
`/teleport @s ~ ~-1000 ~`

Please note that this will remove all death-effects, including sound, particles, loot, and the visual death of the entity. 

# Cancelling the Animation

We can also cancel the rotational value of the entity, allowing the entity to die more conventionally (particles, red-coloring, loot) without the 90 degree spin. This could be useful for things like furniture, where the tipping over effect of entity-death is not desirable.

If you need more information about triggering animations from entity death, see [this document](/tutorials/death-effects.html).

Rotation needs to be applied to a bone parent to all other bones, with a pivot at [0,0,0], and the animation should only start when `!query.is_alive`.

Animation:
```json
"rotation" : [ 0, 0, "Math.min(Math.sqrt(Math.max(0, query.anim_time * 20 - 0.5) / 20 * 1.6), 1) * -90" ]

```

---
### Credits
MrPengoiun & Energyxxer