---
layout: page
title: Creating Boats
parent: Tutorials
---

# Boat Entities

Be they jet-skis, sailboats, or paddle-boards, water-based entities are a pretty common task. 

Sadly, Minecraft makes this difficult by making the `minecraft:boat` one of the most hard-coded entities in the game. This tutorial will teach you how to create boat mechanics for yourself.

## Using Runtime Identifiers
 
You can read more about runtime identifiers [here](https://wiki.bedrock.dev/docs/documentation/runtime_identifier.html). I don't honestly know what will happen if you add `minecraft:boat` to your entity, but if somebody bothers to try, you should update the wiki :)

In general though, runtime identifiers can be used to get hard-coded functionality into data-driven custom entities.

#  Using Components

I believe the best way to create boat entities is by using components, and by offsetting the geometry so that it doesn't sink too far into the water. This section will cover how to achieve boats in this way. 

## Base Entity

I don't actually remember what components are all necessary to get a good boat going, but this I've been reusing this boat code for a while. 

```json
{
    "minecraft:entity": {
        "format_version": "1.14.0",
        "description": {
            "identifier": "sirlich:boat",
            "is_summonable": true,
            "is_spawnable": true,
            "is_experimental": false
        },
        "components": {

            //Make sure the entity can float
            "minecraft:behavior.float": {
                "priority": 0
            },

            //Sets the boat speed
            "minecraft:underwater_movement": {
                "value": 5
            },
            "minecraft:navigation.walk": {
                "can_path_over_water": true,
                "can_sink": false,
                "avoid_damage_blocks": true,
                "can_walk_in_water": true
            },
            "minecraft:can_climb": {
            },
            "minecraft:balloonable": {
                "mass": 0.75
            },
            "minecraft:movement.amphibious": {

            },
            "minecraft:rideable": {
                "seat_count": 1,
                "family_types": [
                    "player",
                    "zombie"
                ],
                "interact_text": "action.interact.enter_boat",
                "seats": {
                    "position": [
                        0, 0, 0]
                }
            },
            "minecraft:input_ground_controlled": {},
            "minecraft:type_family": {},
            "minecraft:health": {
                "value": 10,
                "max": 10
            },
            "minecraft:movement": {
                "value": 3
            },
            "minecraft:movement.basic": {},
            "minecraft:collision_box": {
                "width": 1,
                "height": 1
            },
            "minecraft:physics": {}
        }
    }
}
```

## Geometry Offset

The boat will sink into the water. Open the model in [Blockbench](https://blockbench.net/), and move the entire model up a bit. This will allow it to "float" on top of the water more properly. 

# Skid-Boats

When the water level doesn't change, and the boat won't be interacted with in survival, its possible to create a skid-boat. A skid-boat is an entity that has no gravity, and therefor won't sink. This can be placed at the water level you like, and the boat will stay at that y level forever.
