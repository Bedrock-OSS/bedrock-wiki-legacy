---
layout: page
title: Solid Entities
parent: Tutorials
---

# Solid Entities

Solid entities are entities that the player can bump into, step on, or otherwise physically interact with, without passing through. Entities like this have many uses, such as emulating blocks.

This document will discuss some of the ways that solid entities can be created. 

Not all techniques are ideal for all scenarios. Experiment, and figure out what works best for you.

## Boat runtime identifier

The boat runtime identifier will cause the entity to be solid, as well as provide some other boat-like effects, which might not be desirable.

## Shulker runtime identifier

The shulker runtime identifier wil cause the entity to be solid, as well as act like a shulker, including unwanted teleports.

## is_stackable 

Place `is_stackable` on both entities you want to collide. `Note:` This requires editing `player.json` if you want the entity to be solid for the player.

## Faking it with blocks

In some scenarios, its probably better to `./setblock` barriers, either statically, or dynamically.


