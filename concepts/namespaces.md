---
layout: page
title: Namespaces
parent: Concepts
---

# Namespaces

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Namespaces are identifiers that marks content ownership. You can think of them as folders. Namespaces are useful, because they keep naming conflicts from happening.

Namespaces in addon creation can essentially be thought of as "the part to the left of the colon". For example, `minecraft` is the namespace of `minecraft:zombie`. The general form is `namespace:name`.

As a really specific example of why namespaces are useful, lets imagine you create a new Mob. You name it `minecraft:shark`, not aware that you should create your own namespace for custom content. Next year, Mojang decides to add sharks into the game! Now there is a naming conflict, since there are two definitions of `minecraft:shark`. Your addon will break. 

If you had instead used `your_namespace:shark`, the naming conflict wouldn't have happened.

## Picking a namespace

A good namespace is completely unique to you. Something like `mob` or `cars` or `content` or `custom` would be a **bad** namespace, since another developer might come up with the same namespace as you.

A good namespace is short. You will be writing your namespace a **LOT**, so the shorter the better. `george_carlin_the_comedian` would be a bad namespace for this reason.

For personal projects, I recommend a convenient version of your player name, and for commercial projects, I recommend a convenient version of the company name.

Some good examples:
 - `gcarlin`
 - `sirlich`
 - `cubeworld`
 - `bworks`
 
**DO NOT USE** `minecraft` or `minecon` as a namespace unless editing a vanilla file. Not only is it a terrible idea but Minecraft reserves these and it won't even work. 

# Where to use namespaces?

In short, you should use name-spaces as often as you can.

For starters, you should use a namespace when adding custom entities to the game. 

`sirlich:shark` is much better than `shark`.

You should also use namespaces for components, and events. Just like Mojang uses `minecraft:pig_saddled` you should use `namespace:my_mob_event`, and `namespace:my_component_group`.

You should also use namespaces in animation controllers, render controllers, and animations.

For example: `controller.animation.namespace.entity_name.action` is better than `controller.animation.my_action`. 

## Where **NOT** to use namespaces.

The actual file structure does not need namespaces. 

`animations/namespace/my_entity/animation` is more confusing than `animations/my_entity/animation`.



