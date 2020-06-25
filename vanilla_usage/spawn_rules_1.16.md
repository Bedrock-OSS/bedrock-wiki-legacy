---
layout: page
title: Vanilla Spawn Rules 1.16
parent: Vanilla Usage
---

# Vanilla Components
This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`

# Table of contents
 - [minecraft:biome_filter](#minecraft:biome_filter)
 - [minecraft:brightness_filter](#minecraft:brightness_filter)
 - [minecraft:delay_filter](#minecraft:delay_filter)
 - [minecraft:density_limit](#minecraft:density_limit)
 - [minecraft:difficulty_filter](#minecraft:difficulty_filter)
 - [minecraft:distance_filter](#minecraft:distance_filter)
 - [minecraft:height_filter](#minecraft:height_filter)
 - [minecraft:herd](#minecraft:herd)
 - [minecraft:mob_event_filter](#minecraft:mob_event_filter)
 - [minecraft:permute_type](#minecraft:permute_type)
 - [minecraft:player_in_village_filter](#minecraft:player_in_village_filter)
 - [minecraft:spawn_event](#minecraft:spawn_event)
 - [minecraft:spawns_lava](#minecraft:spawns_lava)
 - [minecraft:spawns_on_block_filter](#minecraft:spawns_on_block_filter)
 - [minecraft:spawns_on_block_prevented_filter](#minecraft:spawns_on_block_prevented_filter)
 - [minecraft:spawns_on_surface](#minecraft:spawns_on_surface)
 - [minecraft:spawns_underground](#minecraft:spawns_underground)
 - [minecraft:spawns_underwater](#minecraft:spawns_underwater)
 - [minecraft:weight](#minecraft:weight)
 - [minecraft:world_age_filter](#minecraft:world_age_filter)
# minecraft:biome_filter
### bat.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### bee.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "sunflower_plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "flower_forest"
    }
]
```

### chicken.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### cod.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "warm"
    }
]
```

### cow.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### creeper.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### dolphin.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "frozen"
    }
]
```

### donkey.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "plains"
}
```

### drowned.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "ocean"
}
```

### drowned.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "river"
}
```

### enderman.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### enderman.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "nether"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "spawn_endermen"
        }
    ]
}
```

### enderman.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "warped_forest"
}
```

### enderman.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "the_end"
    }
]
```

### fox.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "taiga"
}
```

### ghast.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "nether"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "spawn_ghast"
        }
    ]
}
```

### hoglin.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "crimson_forest"
}
```

### horse.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "plains"
}
```

### horse.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "savanna"
}
```

### husk.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "desert"
}
```

### llama.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "extreme_hills"
}
```

### llama.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "savanna"
}
```

### magma_cube.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_magma_cubes"
}
```

### magma_cube.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_many_magma_cubes"
}
```

### mooshroom.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "mooshroom_island"
}
```

### ocelot.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "jungle"
}
```

### panda.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "jungle"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "bamboo"
    }
]
```

### panda.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "bamboo"
}
```

### parrot.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "jungle"
}
```

### phantom.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### pig.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### piglin.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_piglin"
}
```

### piglin.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_few_piglins"
}
```

### pillager_patrol.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mooshroom_island"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "nether"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "the_end"
        }
    ]
}
```

### pillager_patrol.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mooshroom_island"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "nether"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "the_end"
        }
    ]
}
```

### pillager_patrol.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mooshroom_island"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "nether"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "the_end"
        }
    ]
}
```

### polar_bear.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "frozen"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "ocean"
    }
]
```

### polar_bear.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "frozen"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    }
]
```

### pufferfish.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "warm"
    }
]
```

### rabbit.json
```JSON
minecraft:biome_filter: {
    "any_of": [
        {
            "all_of": [
                {
                    "test": "has_biome_tag",
                    "operator": "==",
                    "value": "taiga"
                },
                {
                    "test": "has_biome_tag",
                    "operator": "!=",
                    "value": "mega"
                }
            ]
        },
        {
            "test": "is_snow_covered",
            "operator": "==",
            "value": true
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "desert"
        }
    ]
}
```

### rabbit.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "flower_forest"
}
```

### salmon.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "warm"
    }
]
```

### salmon.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "river"
    }
]
```

### sheep.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### skeleton.json
```JSON
minecraft:biome_filter: {
    "any_of": [
        {
            "all_of": [
                {
                    "test": "has_biome_tag",
                    "operator": "==",
                    "value": "monster"
                },
                {
                    "test": "has_biome_tag",
                    "operator": "!=",
                    "value": "frozen"
                }
            ]
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "soulsand_valley"
        }
    ]
}
```

### slime.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### slime.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "swamp"
}
```

### spider.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### squid.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "ocean"
}
```

### squid.json
```JSON
minecraft:biome_filter: {
    "any_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "river"
        }
    ]
}
```

### stray.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "frozen"
    },
    {
        "test": "has_biome_tag",
        "operator": "!=",
        "value": "ocean"
    }
]
```

### stray.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "frozen"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    }
]
```

### strider.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "nether"
}
```

### tropicalfish.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "warm"
    }
]
```

### tropicalfish.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "ocean"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "warm"
    }
]
```

### turtle.json
```JSON
minecraft:biome_filter: [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "beach"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "warm"
    }
]
```

### witch.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### wolf.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "taiga"
}
```

### wolf.json
```JSON
minecraft:biome_filter: {
    "all_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "forest"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mutated"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "birch"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "roofed"
        },
        {
            "test": "has_biome_tag",
            "operator": "!=",
            "value": "mountain"
        }
    ]
}
```

### zombie.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### zombie_pigman.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_zombified_piglin"
}
```

### zombie_pigman.json
```JSON
minecraft:biome_filter: {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "spawn_few_zombified_piglins"
}
```

# minecraft:brightness_filter
### bat.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 4,
    "adjust_for_weather": true
}
```

### bee.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### chicken.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### cow.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### creeper.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### donkey.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### drowned.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### drowned.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### enderman.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### enderman.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### fox.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### horse.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### horse.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### husk.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### llama.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### llama.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### mooshroom.json
```JSON
minecraft:brightness_filter: {
    "min": 9,
    "max": 15,
    "adjust_for_weather": false
}
```

### ocelot.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### panda.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### panda.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### parrot.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### phantom.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### pig.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### pillager_patrol.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": false
}
```

### pillager_patrol.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": false
}
```

### pillager_patrol.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": false
}
```

### polar_bear.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### polar_bear.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### rabbit.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### rabbit.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### sheep.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### skeleton.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### spider.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### stray.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### stray.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### turtle.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### witch.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### wolf.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### wolf.json
```JSON
minecraft:brightness_filter: {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### zombie.json
```JSON
minecraft:brightness_filter: {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

# minecraft:delay_filter
### pillager_patrol.json
```JSON
minecraft:delay_filter: {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_easy",
    "spawn_chance": 20
}
```

### pillager_patrol.json
```JSON
minecraft:delay_filter: {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_normal",
    "spawn_chance": 20
}
```

### pillager_patrol.json
```JSON
minecraft:delay_filter: {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_hard",
    "spawn_chance": 20
}
```

# minecraft:density_limit
### bat.json
```JSON
minecraft:density_limit: {
    "surface": 5
}
```

### cod.json
```JSON
minecraft:density_limit: {
    "surface": 20
}
```

### creeper.json
```JSON
minecraft:density_limit: {
    "surface": 5
}
```

### dolphin.json
```JSON
minecraft:density_limit: {
    "surface": 5,
    "underground": 0
}
```

### drowned.json
```JSON
minecraft:density_limit: {
    "surface": 5
}
```

### drowned.json
```JSON
minecraft:density_limit: {
    "surface": 2
}
```

### ghast.json
```JSON
minecraft:density_limit: {
    "surface": 0,
    "underground": 2
}
```

### phantom.json
```JSON
minecraft:density_limit: {
    "surface": 5
}
```

### pufferfish.json
```JSON
minecraft:density_limit: {
    "surface": 3
}
```

### salmon.json
```JSON
minecraft:density_limit: {
    "surface": 10
}
```

### salmon.json
```JSON
minecraft:density_limit: {
    "surface": 4
}
```

### squid.json
```JSON
minecraft:density_limit: {
    "surface": 4
}
```

### squid.json
```JSON
minecraft:density_limit: {
    "surface": 2
}
```

### strider.json
```JSON
minecraft:density_limit: {
    "surface": 3
}
```

### tropicalfish.json
```JSON
minecraft:density_limit: {
    "surface": 20
}
```

### tropicalfish.json
```JSON
minecraft:density_limit: {
    "surface": 20
}
```

# minecraft:difficulty_filter
### creeper.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### drowned.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### drowned.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### enderman.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### enderman.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### enderman.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### ghast.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### hoglin.json
```JSON
minecraft:difficulty_filter: {
    "min": "peaceful",
    "max": "hard"
}
```

### husk.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### magma_cube.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### magma_cube.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### phantom.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### piglin.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### piglin.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### pillager_patrol.json
```JSON
minecraft:difficulty_filter: {
    "max": "easy"
}
```

### pillager_patrol.json
```JSON
minecraft:difficulty_filter: {
    "min": "normal",
    "max": "normal"
}
```

### pillager_patrol.json
```JSON
minecraft:difficulty_filter: {
    "min": "hard"
}
```

### skeleton.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### slime.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### slime.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### spider.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### stray.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### stray.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### strider.json
```JSON
minecraft:difficulty_filter: {
    "min": "peaceful",
    "max": "hard"
}
```

### witch.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### zombie.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### zombie_pigman.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

### zombie_pigman.json
```JSON
minecraft:difficulty_filter: {
    "min": "easy",
    "max": "hard"
}
```

# minecraft:distance_filter
### cod.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

### pillager_patrol.json
```JSON
minecraft:distance_filter: {
    "min": 24,
    "max": 48
}
```

### pillager_patrol.json
```JSON
minecraft:distance_filter: {
    "min": 24,
    "max": 48
}
```

### pillager_patrol.json
```JSON
minecraft:distance_filter: {
    "min": 24,
    "max": 48
}
```

### pufferfish.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

### salmon.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

### salmon.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

### tropicalfish.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

### tropicalfish.json
```JSON
minecraft:distance_filter: {
    "min": 12,
    "max": 32
}
```

# minecraft:height_filter
### bat.json
```JSON
minecraft:height_filter: {
    "min": 0,
    "max": 63
}
```

### stray.json
```JSON
minecraft:height_filter: {
    "min": 60,
    "max": 66
}
```

### turtle.json
```JSON
minecraft:height_filter: {
    "min": 60,
    "max": 67
}
```

# minecraft:herd
### bat.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 2
}
```

### bee.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 1
}
```

### chicken.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### cod.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 7
}
```

### cow.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 3
}
```

### dolphin.json
```JSON
minecraft:herd: {
    "min_size": 3,
    "max_size": 5
}
```

### donkey.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 6
}
```

### drowned.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### drowned.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### enderman.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### enderman.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 1
}
```

### enderman.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 1
}
```

### enderman.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### fox.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4,
    "event": "minecraft:entity_born",
    "event_skip_count": 2
}
```

### hoglin.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### horse.json
```JSON
minecraft:herd: [
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_white"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_creamy"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_chestnut"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_brown"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_black"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_gray"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_darkbrown"
    }
]
```

### horse.json
```JSON
minecraft:herd: [
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_white"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_creamy"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_chestnut"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_brown"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_black"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_gray"
    },
    {
        "min_size": 2,
        "max_size": 6,
        "event": "minecraft:make_darkbrown"
    }
]
```

### husk.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### llama.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 6
}
```

### llama.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### magma_cube.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 4
}
```

### magma_cube.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 5
}
```

### mooshroom.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 8
}
```

### ocelot.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### panda.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### panda.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### parrot.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### pig.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 3
}
```

### piglin.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### piglin.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### pillager_patrol.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

### pillager_patrol.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

### pillager_patrol.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

### polar_bear.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2,
    "event": "minecraft:entity_born",
    "event_skip_count": 1
}
```

### polar_bear.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2,
    "event": "minecraft:entity_born",
    "event_skip_count": 1
}
```

### pufferfish.json
```JSON
minecraft:herd: {
    "min_size": 3,
    "max_size": 5
}
```

### rabbit.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 3
}
```

### rabbit.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### salmon.json
```JSON
minecraft:herd: {
    "min_size": 3,
    "max_size": 5
}
```

### salmon.json
```JSON
minecraft:herd: {
    "min_size": 3,
    "max_size": 5
}
```

### sheep.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 3
}
```

### skeleton.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### squid.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### squid.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### stray.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### stray.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 2
}
```

### strider.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### tropicalfish.json
```JSON
minecraft:herd: [
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_anenonme"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_black_tang"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_blue_dory"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_butterfly_fish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_cichlid"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_clownfish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_cc_betta"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_dog_fish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_e_red_snapper"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_goat_fish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_moorish_idol"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_ornate_butterfly"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_parrot_fish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_queen_angel_fish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_red_cichlid"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_red_lipped_benny"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_red_snapper"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_threadfin"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_tomato_clown"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_triggerfish"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_yellow_tang"
    },
    {
        "min_size": 3,
        "max_size": 5,
        "event": "minecraft:become_yellow_tail_parrot"
    }
]
```

### tropicalfish.json
```JSON
minecraft:herd: {
    "min_size": 1,
    "max_size": 3
}
```

### turtle.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 6
}
```

### wolf.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### wolf.json
```JSON
minecraft:herd: {
    "min_size": 4,
    "max_size": 4
}
```

### zombie.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### zombie_pigman.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

### zombie_pigman.json
```JSON
minecraft:herd: {
    "min_size": 2,
    "max_size": 4
}
```

# minecraft:mob_event_filter
### pillager_patrol.json
```JSON
minecraft:mob_event_filter: {
    "event": "minecraft:pillager_patrols_event"
}
```

### pillager_patrol.json
```JSON
minecraft:mob_event_filter: {
    "event": "minecraft:pillager_patrols_event"
}
```

### pillager_patrol.json
```JSON
minecraft:mob_event_filter: {
    "event": "minecraft:pillager_patrols_event"
}
```

# minecraft:permute_type
### pillager_patrol.json
```JSON
minecraft:permute_type: [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

### pillager_patrol.json
```JSON
minecraft:permute_type: [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

### pillager_patrol.json
```JSON
minecraft:permute_type: [
    {
        "weight": 80,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    },
    {
        "weight": 20,
        "entity_type": "minecraft:vindicator"
    }
]
```

### zombie.json
```JSON
minecraft:permute_type: [
    {
        "weight": 95
    },
    {
        "weight": 5,
        "entity_type": "minecraft:zombie_villager_v2"
    }
]
```

# minecraft:player_in_village_filter
### pillager_patrol.json
```JSON
minecraft:player_in_village_filter: {
    "distance": 48,
    "village_border_tolerance": 32
}
```

### pillager_patrol.json
```JSON
minecraft:player_in_village_filter: {
    "distance": 48,
    "village_border_tolerance": 32
}
```

### pillager_patrol.json
```JSON
minecraft:player_in_village_filter: {
    "distance": 48,
    "village_border_tolerance": 32
}
```

# minecraft:spawn_event
### stray.json
```JSON
minecraft:spawn_event: {
    "event": "change_to_skeleton"
}
```

### stray.json
```JSON
minecraft:spawn_event: {
    "event": "change_to_skeleton"
}
```

# minecraft:spawns_lava
### strider.json
```JSON
minecraft:spawns_lava: {}
```

# minecraft:spawns_on_block_filter
### chicken.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### cow.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### donkey.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### horse.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### horse.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### llama.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### llama.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### ocelot.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### panda.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### panda.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### parrot.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### pig.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### polar_bear.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:ice"
```

### polar_bear.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:ice"
```

### rabbit.json
```JSON
minecraft:spawns_on_block_filter: [
    "minecraft:grass",
    "minecraft:snow",
    "minecraft:sand"
]
```

### rabbit.json
```JSON
minecraft:spawns_on_block_filter: [
    "minecraft:grass",
    "minecraft:snow",
    "minecraft:sand"
]
```

### sheep.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

### turtle.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:sand"
```

### wolf.json
```JSON
minecraft:spawns_on_block_filter: [
    "minecraft:grass",
    "minecraft:podzol",
    "minecraft:dirt"
]
```

### wolf.json
```JSON
minecraft:spawns_on_block_filter: "minecraft:grass"
```

# minecraft:spawns_on_block_prevented_filter
### hoglin.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### magma_cube.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### magma_cube.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### piglin.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### piglin.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight_block"
]
```

### skeleton.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### zombie_pigman.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

### zombie_pigman.json
```JSON
minecraft:spawns_on_block_prevented_filter: [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

# minecraft:spawns_on_surface
### bee.json
```JSON
minecraft:spawns_on_surface: {}
```

### chicken.json
```JSON
minecraft:spawns_on_surface: {}
```

### cod.json
```JSON
minecraft:spawns_on_surface: {}
```

### cow.json
```JSON
minecraft:spawns_on_surface: {}
```

### creeper.json
```JSON
minecraft:spawns_on_surface: {}
```

### dolphin.json
```JSON
minecraft:spawns_on_surface: {}
```

### donkey.json
```JSON
minecraft:spawns_on_surface: {}
```

### drowned.json
```JSON
minecraft:spawns_on_surface: {}
```

### drowned.json
```JSON
minecraft:spawns_on_surface: {}
```

### enderman.json
```JSON
minecraft:spawns_on_surface: {}
```

### enderman.json
```JSON
minecraft:spawns_on_surface: {}
```

### fox.json
```JSON
minecraft:spawns_on_surface: {}
```

### horse.json
```JSON
minecraft:spawns_on_surface: {}
```

### horse.json
```JSON
minecraft:spawns_on_surface: {}
```

### husk.json
```JSON
minecraft:spawns_on_surface: {}
```

### llama.json
```JSON
minecraft:spawns_on_surface: {}
```

### llama.json
```JSON
minecraft:spawns_on_surface: {}
```

### mooshroom.json
```JSON
minecraft:spawns_on_surface: {}
```

### ocelot.json
```JSON
minecraft:spawns_on_surface: {}
```

### panda.json
```JSON
minecraft:spawns_on_surface: {}
```

### panda.json
```JSON
minecraft:spawns_on_surface: {}
```

### parrot.json
```JSON
minecraft:spawns_on_surface: {}
```

### phantom.json
```JSON
minecraft:spawns_on_surface: {}
```

### pig.json
```JSON
minecraft:spawns_on_surface: {}
```

### pillager_patrol.json
```JSON
minecraft:spawns_on_surface: {}
```

### pillager_patrol.json
```JSON
minecraft:spawns_on_surface: {}
```

### pillager_patrol.json
```JSON
minecraft:spawns_on_surface: {}
```

### polar_bear.json
```JSON
minecraft:spawns_on_surface: {}
```

### polar_bear.json
```JSON
minecraft:spawns_on_surface: {}
```

### pufferfish.json
```JSON
minecraft:spawns_on_surface: {}
```

### rabbit.json
```JSON
minecraft:spawns_on_surface: {}
```

### rabbit.json
```JSON
minecraft:spawns_on_surface: {}
```

### salmon.json
```JSON
minecraft:spawns_on_surface: {}
```

### salmon.json
```JSON
minecraft:spawns_on_surface: {}
```

### sheep.json
```JSON
minecraft:spawns_on_surface: {}
```

### skeleton.json
```JSON
minecraft:spawns_on_surface: {}
```

### slime.json
```JSON
minecraft:spawns_on_surface: {}
```

### slime.json
```JSON
minecraft:spawns_on_surface: {}
```

### spider.json
```JSON
minecraft:spawns_on_surface: {}
```

### squid.json
```JSON
minecraft:spawns_on_surface: {}
```

### squid.json
```JSON
minecraft:spawns_on_surface: {}
```

### stray.json
```JSON
minecraft:spawns_on_surface: {}
```

### stray.json
```JSON
minecraft:spawns_on_surface: {}
```

### tropicalfish.json
```JSON
minecraft:spawns_on_surface: {}
```

### tropicalfish.json
```JSON
minecraft:spawns_on_surface: {}
```

### turtle.json
```JSON
minecraft:spawns_on_surface: {}
```

### witch.json
```JSON
minecraft:spawns_on_surface: {}
```

### wolf.json
```JSON
minecraft:spawns_on_surface: {}
```

### wolf.json
```JSON
minecraft:spawns_on_surface: {}
```

### zombie.json
```JSON
minecraft:spawns_on_surface: {}
```

# minecraft:spawns_underground
### bat.json
```JSON
minecraft:spawns_underground: {}
```

### creeper.json
```JSON
minecraft:spawns_underground: {}
```

### enderman.json
```JSON
minecraft:spawns_underground: {}
```

### enderman.json
```JSON
minecraft:spawns_underground: {}
```

### enderman.json
```JSON
minecraft:spawns_underground: {}
```

### ghast.json
```JSON
minecraft:spawns_underground: {}
```

### hoglin.json
```JSON
minecraft:spawns_underground: {}
```

### magma_cube.json
```JSON
minecraft:spawns_underground: {}
```

### magma_cube.json
```JSON
minecraft:spawns_underground: {}
```

### piglin.json
```JSON
minecraft:spawns_underground: {}
```

### piglin.json
```JSON
minecraft:spawns_underground: {}
```

### skeleton.json
```JSON
minecraft:spawns_underground: {}
```

### slime.json
```JSON
minecraft:spawns_underground: {}
```

### slime.json
```JSON
minecraft:spawns_underground: {}
```

### spider.json
```JSON
minecraft:spawns_underground: {}
```

### stray.json
```JSON
minecraft:spawns_underground: {}
```

### strider.json
```JSON
minecraft:spawns_underground: {}
```

### witch.json
```JSON
minecraft:spawns_underground: {}
```

### zombie_pigman.json
```JSON
minecraft:spawns_underground: {}
```

### zombie_pigman.json
```JSON
minecraft:spawns_underground: {}
```

# minecraft:spawns_underwater
### cod.json
```JSON
minecraft:spawns_underwater: {}
```

### dolphin.json
```JSON
minecraft:spawns_underwater: {}
```

### drowned.json
```JSON
minecraft:spawns_underwater: {}
```

### drowned.json
```JSON
minecraft:spawns_underwater: {}
```

### guardian.json
```JSON
minecraft:spawns_underwater: {}
```

### pufferfish.json
```JSON
minecraft:spawns_underwater: {}
```

### salmon.json
```JSON
minecraft:spawns_underwater: {}
```

### salmon.json
```JSON
minecraft:spawns_underwater: {}
```

### squid.json
```JSON
minecraft:spawns_underwater: {}
```

### squid.json
```JSON
minecraft:spawns_underwater: {}
```

### tropicalfish.json
```JSON
minecraft:spawns_underwater: {}
```

### tropicalfish.json
```JSON
minecraft:spawns_underwater: {}
```

# minecraft:weight
### bat.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### bee.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### chicken.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### cod.json
```JSON
minecraft:weight: {
    "default": 75
}
```

### cow.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### creeper.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### dolphin.json
```JSON
minecraft:weight: {
    "default": 7
}
```

### donkey.json
```JSON
minecraft:weight: {
    "default": 1
}
```

### drowned.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### drowned.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### enderman.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### enderman.json
```JSON
minecraft:weight: {
    "default": 6
}
```

### enderman.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### enderman.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### fox.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### ghast.json
```JSON
minecraft:weight: {
    "default": 40
}
```

### hoglin.json
```JSON
minecraft:weight: {
    "default": 20
}
```

### horse.json
```JSON
minecraft:weight: {
    "default": 4
}
```

### horse.json
```JSON
minecraft:weight: {
    "default": 1
}
```

### husk.json
```JSON
minecraft:weight: {
    "default": 240
}
```

### llama.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### llama.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### magma_cube.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### magma_cube.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### mooshroom.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### ocelot.json
```JSON
minecraft:weight: {
    "default": 30
}
```

### panda.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### panda.json
```JSON
minecraft:weight: {
    "default": 40
}
```

### parrot.json
```JSON
minecraft:weight: {
    "default": 40
}
```

### phantom.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### pig.json
```JSON
minecraft:weight: {
    "default": 10
}
```

### piglin.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### piglin.json
```JSON
minecraft:weight: {
    "default": 15
}
```

### polar_bear.json
```JSON
minecraft:weight: {
    "default": 1
}
```

### polar_bear.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### pufferfish.json
```JSON
minecraft:weight: {
    "default": 25
}
```

### rabbit.json
```JSON
minecraft:weight: {
    "default": 4
}
```

### rabbit.json
```JSON
minecraft:weight: {
    "default": 20
}
```

### salmon.json
```JSON
minecraft:weight: {
    "default": 26
}
```

### salmon.json
```JSON
minecraft:weight: {
    "default": 16
}
```

### sheep.json
```JSON
minecraft:weight: {
    "default": 12
}
```

### skeleton.json
```JSON
minecraft:weight: {
    "default": 80
}
```

### slime.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### slime.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### spider.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### squid.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### squid.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### stray.json
```JSON
minecraft:weight: {
    "default": 120
}
```

### stray.json
```JSON
minecraft:weight: {
    "default": 120
}
```

### strider.json
```JSON
minecraft:weight: {
    "default": 20
}
```

### tropicalfish.json
```JSON
minecraft:weight: {
    "default": 75
}
```

### tropicalfish.json
```JSON
minecraft:weight: {
    "default": 25
}
```

### turtle.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### witch.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### wolf.json
```JSON
minecraft:weight: {
    "default": 8
}
```

### wolf.json
```JSON
minecraft:weight: {
    "default": 5
}
```

### zombie.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### zombie_pigman.json
```JSON
minecraft:weight: {
    "default": 100
}
```

### zombie_pigman.json
```JSON
minecraft:weight: {
    "default": 1
}
```

# minecraft:world_age_filter
### pillager_patrol.json
```JSON
minecraft:world_age_filter: {
    "min": 6000
}
```

### pillager_patrol.json
```JSON
minecraft:world_age_filter: {
    "min": 6000
}
```

### pillager_patrol.json
```JSON
minecraft:world_age_filter: {
    "min": 6000
}
```

