---
layout: page
title: Death Effects
parent: Knowledge
---

# Death Effects

I define `Death Effects` as "Doing something when an Entity dies". There are a few wrong ways to achieve this that should be avoided, including:
 - Detecting death in the entity file, adding a component, and *then* trying to detect that component in the animation controller. This is wrong because the entity will be removed from the world before the animation controller has a chance to run.  
 - Detecting the entity death from an outside source, such as a ticking command block. This method isn't *stritly* wrong, and in some circumstances, it may even be preffered. However it is costly and easy to break.

## Using query.is_alive

The best way to create death effects is using the `is_alive` query.

This query does not show up in the 1.14.0 documentation, however entities set to 1.14.0 will run the query without errors. To be safe however it may be wiser to use 1.13.0 version when using this query.

Simply create an animation controller with a transition based on this query. The final `on_entry` will run before the entity is removed from the world.

Your animation controller might look something like this:
```JSON
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

I've included the BP entity and an animation file for download. Feel free to use them as templates, or directly in your projects if thats useful to you.

[Entity](../../../_site/docs/knowledge/death_effects/death_effects_entity.json)

[Animation Controller](../../../_site/docs/knowledge/death_effects/death_effects_animation_controller.json)

