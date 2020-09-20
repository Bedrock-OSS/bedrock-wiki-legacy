---
layout: page
title: Cancelling Death Animations
parent: Tutorials
---

# Cancelling Death Animations

Intermediate
{: .label .label-yellow }

Death animation refers to the rotation of the entity as it dies. This is accompanied by a red coloring, and followed shortly after by the disappearance of the entity geometry, and the appearance of the death particles.

# Teleporting the Entity

A fairly common way to remove entities without causing death-effects, is to simply teleport them into the void. This can be done from animation controllers like:
`/teleport @s ~ ~-1000 ~`

Please note that this will remove all death-effects, including sound, particles, loot, and the visual death of the entity. 

# Cancelling the Animation