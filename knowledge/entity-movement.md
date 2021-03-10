---
layout: page
title: Entity Movement
parent: Knowledge
badge: NEW
badge_color: blue
---

# Entity Movement

Entity movement is a confusing subject, with many pieces that must be done correctly, or your entity will not move. The following is required:

 - movement speed
 - movement type
 - movement modifiers
 - navigation
 - navigation abilities
 - AI

# Movement Speed

The first thing your entity needs is a speed component. This sets how quickly your entity will move through the world.

| Component                     | Note                         |
|-------------------------------|------------------------------|
| minecraft:movement            | Set movement speed on land.  |
| minecraft:underwater_movement | Set movement speed in water. |
| minecraft:flying_speed        | Set the speed in the air.    |

You should always include `minecraft:movement`. Add the other two as needed.

All vanilla swimming" entities like Dolphin include `underwater_movement`. Only some flying entities include `flying_speed`. It is not known why this is the case.

# Movement Type

Your entity will also need a movement type. Movement types set hard-coded behavior for *how* your entity will move through the world. 

You may only include one movement type in your entity. Select the component that most closely matches your needs. 

| Component                     | Note                                                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------|
| minecraft:movement.amphibious | This move control allows the mob to swim in water and walk on land.                         |
| minecraft:movement.basic      | This component accents the movement of an entity.                                           |
| minecraft:movement.fly        | This move control causes the mob to fly.                                                    |
| minecraft:movement.generic    | This move control allows a mob to fly, swim, climb, etc.                                    |
| minecraft:movement.hover      | This move control causes the mob to hover.                                                  |
| minecraft:movement.jump       | Move control that causes the mob to jump as it moves with a specified delay between jumps.  |
| minecraft:movement.skip       | This move control causes the mob to hop as it moves.                                        |
| minecraft:movement.sway       | This move control causes the mob to sway side to side giving the impression it is swimming. |

# Movement Modifiers

Movement modifiers provide additional information about how your entity will move through the world.

| Component                   |                                                    |
|-----------------------------|----------------------------------------------------|
| minecraft:water_movement    | Sets the friction the entity experiences in water. |
| minecraft:rail_movement     | Sets that the entity can move on rails (only).     |
| minecraft:friction_modifier | Sets the friction the entity experiences on land.  |

# Navigation

The next thing your entity needs is a navigation component. Navigation components have quite a few fields, like whether the entity can open doors, or should avoid sunlight. How you set these fields is generally more important than the navigation component you pick. 

The reason there are so many navigation components, is that each one gives a slightly different hard-coded behavior. Pick the navigation component whose name/description best matches the kind of navigation your entity will be doing.

You can only have one navigation component at any given time.

| Component                                                                                               |
|---------------------------------------------------------------------------------------------------------|
| [minecraft:navigation.climb](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.climb)     |
| [minecraft:navigation.float](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.float)     |
| [minecraft:navigation.generic](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.generic) |
| [minecraft:navigation.float](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.float)     |
| [minecraft:navigation.fly](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.fly)         |
| [minecraft:navigation.swim](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.swim)       |
| [minecraft:navigation.walk](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.walk)       |

# Navigation Abilities

On top of the movement and the navigation component, there exists many additional components to augment the abilities of your entity, as they move through the world.


| Component                       | Note                                                                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| minecraft:annotation.break_door | Allows entity to break doors. Must also be turned on in navigation component.                                                     |
| minecraft:annotation.open_door  | Allows entity to open doors. Must also be turned on in navigation component.                                                      |
| minecraft:buoyant               | Specify which liquids the entity can float in.                                                                                    |
| minecraft:can_climb             | Allows this entity to climb up ladders.                                                                                           |
| minecraft:can_fly               | Marks the entity as being able to fly, the pathfinder won't be restricted to paths where a solid block is required underneath it. |
| minecraft:can_power_jump        | Allows the entity to power jump like the horse does in vanilla.                                                                   |
| minecraft:floats_in_liquid      | Sets that this entity can float in liquid blocks.                                                                                 |

There are also components like `minecraft:preferred_path`, which will further modify navigation, based on block-based path-cost.

# AI

The navigation component tells the entity *how* to generate paths, but it doesn't say *when* or *where* to generate paths. This is what the AI components are for. 

AI components are prefixed with `behavior`.

There are too many AI components that generate paths to list in this document. A few will be provided as examples:

| Component                        |
|----------------------------------|
| minecraft:behavior.random_stroll |
| minecraft:behavior.run_around_like_crazy	   |





