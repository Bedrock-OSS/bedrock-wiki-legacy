---
layout: page
title: Fake Blocks
parent: Tutorials
---

# Fake Blocks

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Intermediate
{: .label .label-yellow }

## Creating the Hitbox

Here is a tutorial of how to make solid Hitbox in four different ways, with `runtime_identifiers`, blocks and components. [Solid Entities](https://wiki.bedrock.dev/tutorials/solid-entities)

## Basic Components

Those components below are required to make the entity act like a block, and also don't add the "minecraft:physics": {} component in here, this will make your entity fall of have collision with some blocks like water or lava.

```jsonc
{
    "minecraft:knockback_resistance": {//Knockback resistance is needed to make it not be Knocked off by an entity.
        "value": 1
    },
    "minecraft:pushable": {//Tells if the entity can be pushed or not.
        "is_pushable": false,
        "is_pushable_by_piston": true
    },
    "minecraft:push_through": {//Sets the distance through which the entity can push through.
        "value": 1
    },
    "minecraft:damage_sensor": {//Makes it invincible.
        "triggers": [
            {
                "deals_damage": false,
                "cause": "all"
            }
        ]
    }
}
```

## Aligning the Entity Rotation

To align your entity in rotation, you will need some Math.

```jsonc
"rotation" : [ 0, "-query.body_y_rotation + (Math.round(query.body_y_rotation / 90) * 90)", 0 ]
```

Apply that code on the core folder of your model in an animation, make sure the pivot point is 0 in the X and Z Axis, to avoid visul bugs. And also you don't need to add components like:

`minecraft:behavior.look_at_entity
minecraft:behavior.look_at_player
minecraft:behavior.look_at_target
...`

The reason why is because this will change the Target Y Rotation, acusing it to move the Body Y Rotation so the Model will move, don't add walk component too.

## Aligning the Entity Position

To align the position of the entity, this will be more tricky.

First, in the `minecraft:entity_spawned` event, make it places a custom block with a run_command, and make a new dummy-entity with a transformation event, to transform the dummy entity to the original entity so we avoid triggering the `minecraft:entity_spawned` again. 

{% include filepath.html path="BP/entities/your_entity.json" local_path="minecraft:entity/events"%}

```jsonc
"minecraft:entity_spawned": {//Event in the original entity.
   "add": {
      "components_groups": [
         "despawn"//We will also need to despawn the first entity.
      ]
   },
   "run_command": {
      "command": [
         "setblock ~~~ thing:align"
      ]
   }
}
```

{% include filepath.html path="BP/entities/your_entity.json" local_path="minecraft:entity/component_groups"%}

```jsonc
"component_groups": {//Component Group in the original entity.
   "despawn": {
      "minecraft:despawn": {}
   }
}
```

{% include filepath.html path="BP/blocks/your_dummy_block.json"%}

```jsonc
{
    "format_version": "1.16.100",
    "minecraft:block": {
        "description": {
            "identifier": "thing:align"//Block used to summon the dummy entity right on the block, and as the block is centered, the entity will center too.
        },
        "components": {
            "minecraft:destroy_time": 2,
            "minecraft:block_light_emission": 0,
            "minecraft:block_light_absorption": 0,
            "minecraft:flammable": {
                "burn_odds": 0,
                "flame_odds": 0
            },
            "minecraft:unit_cube": {},
            "minecraft:entity_collision": {
                "origin": [ 0, 0, 0 ],
                "size": [ 0, 0, 0 ]
            },
            "minecraft:pick_collision": {
                "origin": [ 0, 0, 0 ],
                "size": [ 0, 0, 0 ]
            },
            "minecraft:on_placed": {
                "event": "my:event"
            },
            "minecraft:loot": "loot_tables/empty.json"
        },
        "events": {
            "my:event": {
                "run_command": {
                    "command": [
                        "setblock ~~~ air 0",//This will despawn the block
                        "summon thing:dummy_align"//And this spawn the dummy entity.
                    ]
                }
            }
        }
    }
}
```

{% include filepath.html path="BP/entities/your_dummy_entity.json"%}

```jsonc
{
    "format_version": "1.13.0",
    "minecraft:entity": {
        "description": {
            "identifier": "thing:dummy_align",//The dummy entity used to avoid triggering the entity_spawned event in the original entity.
            "is_spawnable": false,
            "is_summonable": true,
            "is_experimental": false
        },
        "component_groups": {
            "transform": {
                "minecraft:transformation": {
                    "into": "thing:your_entity",
                    "delay": 0
                }
            }
        },
        "components": {
            "minecraft:physics": {
                "has_gravity": false
            },
            "minecraft:collision_box": {
                "width": 0.1,
                "height": 0.1
            },
            "minecraft:damage_sensor": {
                "triggers": {
                    "cause": "all",
                    "deals_damage": false
                }
            }
        },
        "events": {
            "minecraft:entity_spawned": {
                "add": {
                    "component_groups": [
                        "transform"
                    ]
                }
            }
        }
    }
}
```
