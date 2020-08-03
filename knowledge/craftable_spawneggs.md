---
layout: page
title: craftable_spawners
parent: Knowledge
---
 
# Using MoLang to create craftable spawn-eggs
 
Minecraft Bedrock 1.16 introduced the ability to use MoLang expressions in the `data` field of recipe results. We can use the `query.get_actor_info_id` function to get the runtime integer ID of a given entity.


## Shapeless recipe example
 
This recipe will convert a piece of gunpowder to a creeper spawn egg.
```json
{
    "format_version": "1.13.0",
    "minecraft:recipe_shapeless": {
        "description": {
            "identifier": "foo:bar"
        },
        "tags": [
            "crafting_table"
        ],
        "ingredients": [
            {
                "item": "minecraft:gunpowder"
            }
        ],
        "result":
            {
                "item": "spawn_egg",
                "data": "query.get_actor_info_id('minecraft:creeper')"
            }
    }
}
```