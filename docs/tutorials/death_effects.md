---
layout: page
title: Death Effects
parent: Tutorials
---

# Death Effects

I define `Death Effects` as "Doing something when an Entity dies". There are a few wrong ways to achieve this that should be avoided, including:
 - Detecting death in the entity file, adding a component, and *then* trying to detect that component in the animation controller. This is wrong because the entity will be removed from the world before the animation controller has a chance to run.  
 - Detecting the entity death from an outside source, such as a ticking command block. This method isn't *strictly* wrong, and in some circumstances, it may even be preferred. However it is costly and easy to break.

## Using query.is_alive

The best way to create death effects is by using the `is_alive` query.

This query does not show up in the `1.14.0` documentation, however entities set to `1.14.0` will run the query without errors. To be safe however it may be wiser to use `1.13.0` version when creating death effects.

Simply create an animation controller with a transition based on `is_alive`. The final `on_entry` will run before the entity is removed from the world, allowing you to run your commands.

Your animation controller might look something like this:

```json
"states": {
    "default": {
        "transitions": [
            {
                "speak": "!query.is_alive"
            }
        ]
    },
    "speak": {
        "on_entry": [
            "/say I'm Dead!"
        ]
    }
}
```

## Example Files

I've included example files for download. Feel free to use them as templates, or directly in your projects if thats useful to you.

## Entity
```json
{
    "format_version": "1.13.0",
    "minecraft:entity": {
        "description": {
            "identifier": "sirlich:death_effects",
            "is_spawnable": true,
            "is_summonable": true,
            "is_experimental": false,
            "scripts": {
                "animate": [
                    "sirlich:death_effects_commands"
                ]
            },
            "animations": {
                "sirlich:death_effects_commands": "controller.animation.sirlich_death_effects"
            }
        },
        "components": {
            "minecraft:push_through": {
                "value": 1
            },
            "minecraft:health": {
                "value": 5,
                "max": 5
            },
            "minecraft:physics": {}
        }
    }
}
```

## Animation Controller
```json
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.sirlich_death_effects": {
            "states": {
                "default": {
                    "transitions": [
                        {
                            "speak": "!query.is_alive"
                        }
                    ]
                },
                "speak": {
                    "on_entry": [
                        "/say Good heavens! I can't believe I've been defeated!"
                    ]
                }
            }
        }
    }
}
```

