---
layout: page
title: Spawn Rules
parent: Vanilla Usage
---

# Spawn Rules
This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`

# Table of contents
 - [minecraft:biome_filter](#minecraftbiome_filter)
 - [minecraft:brightness_filter](#minecraftbrightness_filter)
 - [minecraft:delay_filter](#minecraftdelay_filter)
 - [minecraft:density_limit](#minecraftdensity_limit)
 - [minecraft:difficulty_filter](#minecraftdifficulty_filter)
 - [minecraft:distance_filter](#minecraftdistance_filter)
 - [minecraft:height_filter](#minecraftheight_filter)
 - [minecraft:herd](#minecraftherd)
 - [minecraft:mob_event_filter](#minecraftmob_event_filter)
 - [minecraft:permute_type](#minecraftpermute_type)
 - [minecraft:player_in_village_filter](#minecraftplayer_in_village_filter)
 - [minecraft:spawn_event](#minecraftspawn_event)
 - [minecraft:spawns_on_block_filter](#minecraftspawns_on_block_filter)
 - [minecraft:spawns_on_surface](#minecraftspawns_on_surface)
 - [minecraft:spawns_underground](#minecraftspawns_underground)
 - [minecraft:spawns_underwater](#minecraftspawns_underwater)
 - [minecraft:weight](#minecraftweight)
 - [minecraft:world_age_filter](#minecraftworld_age_filter)

# minecraft:biome_filter
### bat.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### bee.json
```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### cod.json
```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### creeper.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### dolphin.json
```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "plains"
}
```

### drowned.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "ocean"
}
```

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "river"
}
```

### enderman.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "nether"
}
```

```json
"minecraft:biome_filter:" [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "the_end"
    }
]
```

### fox.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "taiga"
}
```

### ghast.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "nether"
}
```

### horse.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "plains"
}
```

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "savanna"
}
```

### husk.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "desert"
}
```

### llama.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "extreme_hills"
}
```

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "savanna"
}
```

### magma_cube.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "nether"
}
```

### mooshroom.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "mooshroom_island"
}
```

### ocelot.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "jungle"
}
```

### panda.json
```json
"minecraft:biome_filter:" [
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

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "bamboo"
}
```

### parrot.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "jungle"
}
```

### phantom.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### pig.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### pillager_patrol.json
```json
"minecraft:biome_filter:" {
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

```json
"minecraft:biome_filter:" {
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

```json
"minecraft:biome_filter:" {
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
```json
"minecraft:biome_filter:" [
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

```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" {
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

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "flower_forest"
}
```

### salmon.json
```json
"minecraft:biome_filter:" [
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

```json
"minecraft:biome_filter:" [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "river"
    }
]
```

### sheep.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

### skeleton.json
```json
"minecraft:biome_filter:" [
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
```

### slime.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "swamp"
}
```

### spider.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### squid.json
```json
"minecraft:biome_filter:" {
    "any_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "ocean"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "river"
        }
    ]
}
```

### stray.json
```json
"minecraft:biome_filter:" [
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

```json
"minecraft:biome_filter:" [
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

### tropicalfish.json
```json
"minecraft:biome_filter:" [
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

```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" [
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
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### wolf.json
```json
"minecraft:biome_filter:" {
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
}
```

### zombie.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "monster"
}
```

### zombie_pigman.json
```json
"minecraft:biome_filter:" {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "nether"
}
```

# minecraft:brightness_filter
### bat.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 4,
    "adjust_for_weather": true
}
```

### bee.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### chicken.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### cow.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### creeper.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### donkey.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### drowned.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### enderman.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### fox.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### horse.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### husk.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### llama.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### mooshroom.json
```json
"minecraft:brightness_filter:" {
    "min": 9,
    "max": 15,
    "adjust_for_weather": false
}
```

### ocelot.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### panda.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### parrot.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### phantom.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### pig.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### pillager_patrol.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": false
}
```

### polar_bear.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### rabbit.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### sheep.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### skeleton.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### spider.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### stray.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### turtle.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### witch.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

### wolf.json
```json
"minecraft:brightness_filter:" {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

### zombie.json
```json
"minecraft:brightness_filter:" {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

# minecraft:delay_filter
### pillager_patrol.json
```json
"minecraft:delay_filter:" {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_easy",
    "spawn_chance": 20
}
```

```json
"minecraft:delay_filter:" {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_normal",
    "spawn_chance": 20
}
```

```json
"minecraft:delay_filter:" {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_hard",
    "spawn_chance": 20
}
```

# minecraft:density_limit
### bat.json
```json
"minecraft:density_limit:" {
    "surface": 5
}
```

### cod.json
```json
"minecraft:density_limit:" {
    "surface": 20
}
```

### creeper.json
```json
"minecraft:density_limit:" {
    "surface": 5
}
```

### dolphin.json
```json
"minecraft:density_limit:" {
    "surface": 5,
    "underground": 0
}
```

### drowned.json
```json
"minecraft:density_limit:" {
    "surface": 5
}
```

```json
"minecraft:density_limit:" {
    "surface": 2
}
```

### ghast.json
```json
"minecraft:density_limit:" {
    "surface": 0,
    "underground": 2
}
```

### phantom.json
```json
"minecraft:density_limit:" {
    "surface": 5
}
```

### pufferfish.json
```json
"minecraft:density_limit:" {
    "surface": 3
}
```

### salmon.json
```json
"minecraft:density_limit:" {
    "surface": 10
}
```

```json
"minecraft:density_limit:" {
    "surface": 4
}
```

### squid.json
```json
"minecraft:density_limit:" {
    "surface": 4
}
```

### tropicalfish.json
```json
"minecraft:density_limit:" {
    "surface": 20
}
```

```json
"minecraft:density_limit:" {
    "surface": 20
}
```

# minecraft:difficulty_filter
### creeper.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### drowned.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### enderman.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### ghast.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### husk.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### magma_cube.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### phantom.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### pillager_patrol.json
```json
"minecraft:difficulty_filter:" {
    "max": "easy"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "normal",
    "max": "normal"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "hard"
}
```

### skeleton.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### slime.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### spider.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### stray.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### witch.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### zombie.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

### zombie_pigman.json
```json
"minecraft:difficulty_filter:" {
    "min": "easy",
    "max": "hard"
}
```

# minecraft:distance_filter
### cod.json
```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

### pillager_patrol.json
```json
"minecraft:distance_filter:" {
    "min": 24,
    "max": 48
}
```

```json
"minecraft:distance_filter:" {
    "min": 24,
    "max": 48
}
```

```json
"minecraft:distance_filter:" {
    "min": 24,
    "max": 48
}
```

### pufferfish.json
```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

### salmon.json
```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

### tropicalfish.json
```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

```json
"minecraft:distance_filter:" {
    "min": 12,
    "max": 32
}
```

# minecraft:height_filter
### bat.json
```json
"minecraft:height_filter:" {
    "min": 0,
    "max": 63
}
```

### stray.json
```json
"minecraft:height_filter:" {
    "min": 60,
    "max": 66
}
```

### turtle.json
```json
"minecraft:height_filter:" {
    "min": 60,
    "max": 67
}
```

# minecraft:herd
### bat.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 2
}
```

### bee.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 1
}
```

### chicken.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### cod.json
```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 7
}
```

### cow.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 3
}
```

### dolphin.json
```json
"minecraft:herd:" {
    "min_size": 3,
    "max_size": 5
}
```

### donkey.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 6
}
```

### drowned.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### enderman.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 1
}
```

```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 4
}
```

### fox.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4,
    "event": "minecraft:entity_born",
    "event_skip_count": 2
}
```

### horse.json
```json
"minecraft:herd:" [
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

```json
"minecraft:herd:" [
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
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### llama.json
```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 6
}
```

```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 4
}
```

### magma_cube.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 4
}
```

### mooshroom.json
```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 8
}
```

### ocelot.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

### panda.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

### parrot.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

### pig.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 3
}
```

### pillager_patrol.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 5,
    "initial_event": "minecraft:promote_to_patrol_captain",
    "initial_event_count": 1,
    "event": "minecraft:spawn_as_patrol_follower",
    "event_skip_count": 1
}
```

### polar_bear.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2,
    "event": "minecraft:entity_born",
    "event_skip_count": 1
}
```

```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2,
    "event": "minecraft:entity_born",
    "event_skip_count": 1
}
```

### pufferfish.json
```json
"minecraft:herd:" {
    "min_size": 3,
    "max_size": 5
}
```

### rabbit.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 3
}
```

```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### salmon.json
```json
"minecraft:herd:" {
    "min_size": 3,
    "max_size": 5
}
```

```json
"minecraft:herd:" {
    "min_size": 3,
    "max_size": 5
}
```

### sheep.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 3
}
```

### skeleton.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

### squid.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### stray.json
```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 2
}
```

### tropicalfish.json
```json
"minecraft:herd:" [
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

```json
"minecraft:herd:" {
    "min_size": 1,
    "max_size": 3
}
```

### turtle.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 6
}
```

### wolf.json
```json
"minecraft:herd:" {
    "min_size": 4,
    "max_size": 4
}
```

### zombie.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

### zombie_pigman.json
```json
"minecraft:herd:" {
    "min_size": 2,
    "max_size": 4
}
```

# minecraft:mob_event_filter
### pillager_patrol.json
```json
"minecraft:mob_event_filter:" {
    "event": "minecraft:pillager_patrols_event"
}
```

```json
"minecraft:mob_event_filter:" {
    "event": "minecraft:pillager_patrols_event"
}
```

```json
"minecraft:mob_event_filter:" {
    "event": "minecraft:pillager_patrols_event"
}
```

# minecraft:permute_type
```json
"minecraft:permute_type:" [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

```json
"minecraft:permute_type:" [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

```json
"minecraft:permute_type:" [
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
```json
"minecraft:permute_type:" [
    {
        "weight": 95
    },
    {
        "weight": 5,
        "entity_type": "minecraft:zombie_villager"
    }
]
```

# minecraft:player_in_village_filter
### pillager_patrol.json
```json
"minecraft:player_in_village_filter:" {
    "distance": 48,
    "village_border_tolerance": 10
}
```

```json
"minecraft:player_in_village_filter:" {
    "distance": 48,
    "village_border_tolerance": 10
}
```

```json
"minecraft:player_in_village_filter:" {
    "distance": 48,
    "village_border_tolerance": 10
}
```

# minecraft:spawn_event
### stray.json
```json
"minecraft:spawn_event:" {
    "event": "change_to_skeleton"
}
```

```json
"minecraft:spawn_event:" {
    "event": "change_to_skeleton"
}
```

# minecraft:spawns_on_block_filter
### chicken.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### cow.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### donkey.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### horse.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### llama.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### ocelot.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### panda.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### parrot.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### pig.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### sheep.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

### wolf.json
```json
"minecraft:spawns_on_block_filter:" "minecraft:grass"
```

# minecraft:spawns_on_surface
### bee.json
```json
"minecraft:spawns_on_surface:" {}
```

### chicken.json
```json
"minecraft:spawns_on_surface:" {}
```

### cod.json
```json
"minecraft:spawns_on_surface:" {}
```

### cow.json
```json
"minecraft:spawns_on_surface:" {}
```

### creeper.json
```json
"minecraft:spawns_on_surface:" {}
```

### dolphin.json
```json
"minecraft:spawns_on_surface:" {}
```

### donkey.json
```json
"minecraft:spawns_on_surface:" {}
```

### drowned.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### enderman.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### fox.json
```json
"minecraft:spawns_on_surface:" {}
```

### horse.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### husk.json
```json
"minecraft:spawns_on_surface:" {}
```

### llama.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### mooshroom.json
```json
"minecraft:spawns_on_surface:" {}
```

### ocelot.json
```json
"minecraft:spawns_on_surface:" {}
```

### panda.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### parrot.json
```json
"minecraft:spawns_on_surface:" {}
```

### phantom.json
```json
"minecraft:spawns_on_surface:" {}
```

### pig.json
```json
"minecraft:spawns_on_surface:" {}
```

### pillager_patrol.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### polar_bear.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### pufferfish.json
```json
"minecraft:spawns_on_surface:" {}
```

### rabbit.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### salmon.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### sheep.json
```json
"minecraft:spawns_on_surface:" {}
```

### skeleton.json
```json
"minecraft:spawns_on_surface:" {}
```

### slime.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### spider.json
```json
"minecraft:spawns_on_surface:" {}
```

### squid.json
```json
"minecraft:spawns_on_surface:" {}
```

### stray.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### tropicalfish.json
```json
"minecraft:spawns_on_surface:" {}
```

```json
"minecraft:spawns_on_surface:" {}
```

### turtle.json
```json
"minecraft:spawns_on_surface:" {}
```

### witch.json
```json
"minecraft:spawns_on_surface:" {}
```

### wolf.json
```json
"minecraft:spawns_on_surface:" {}
```

### zombie.json
```json
"minecraft:spawns_on_surface:" {}
```

# minecraft:spawns_underground
### bat.json
```json
"minecraft:spawns_underground:" {}
```

### creeper.json
```json
"minecraft:spawns_underground:" {}
```

### enderman.json
```json
"minecraft:spawns_underground:" {}
```

```json
"minecraft:spawns_underground:" {}
```

### ghast.json
```json
"minecraft:spawns_underground:" {}
```

### magma_cube.json
```json
"minecraft:spawns_underground:" {}
```

### skeleton.json
```json
"minecraft:spawns_underground:" {}
```

### slime.json
```json
"minecraft:spawns_underground:" {}
```

```json
"minecraft:spawns_underground:" {}
```

### spider.json
```json
"minecraft:spawns_underground:" {}
```

### stray.json
```json
"minecraft:spawns_underground:" {}
```

### witch.json
```json
"minecraft:spawns_underground:" {}
```

### zombie.json
```json
"minecraft:spawns_underground:" {}
```

### zombie_pigman.json
```json
"minecraft:spawns_underground:" {}
```

# minecraft:spawns_underwater
### cod.json
```json
"minecraft:spawns_underwater:" {}
```

### dolphin.json
```json
"minecraft:spawns_underwater:" {}
```

### drowned.json
```json
"minecraft:spawns_underwater:" {}
```

```json
"minecraft:spawns_underwater:" {}
```

### guardian.json
```json
"minecraft:spawns_underwater:" {}
```

### pufferfish.json
```json
"minecraft:spawns_underwater:" {}
```

### salmon.json
```json
"minecraft:spawns_underwater:" {}
```

```json
"minecraft:spawns_underwater:" {}
```

### squid.json
```json
"minecraft:spawns_underwater:" {}
```

### tropicalfish.json
```json
"minecraft:spawns_underwater:" {}
```

```json
"minecraft:spawns_underwater:" {}
```

# minecraft:weight
### bat.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### bee.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### chicken.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### cod.json
```json
"minecraft:weight:" {
    "default": 75
}
```

### cow.json
```json
"minecraft:weight:" {
    "default": 8
}
```

### creeper.json
```json
"minecraft:weight:" {
    "default": 100
}
```

### dolphin.json
```json
"minecraft:weight:" {
    "default": 7
}
```

### donkey.json
```json
"minecraft:weight:" {
    "default": 1
}
```

### drowned.json
```json
"minecraft:weight:" {
    "default": 100
}
```

```json
"minecraft:weight:" {
    "default": 5
}
```

### enderman.json
```json
"minecraft:weight:" {
    "default": 10
}
```

```json
"minecraft:weight:" {
    "default": 6
}
```

```json
"minecraft:weight:" {
    "default": 10
}
```

### fox.json
```json
"minecraft:weight:" {
    "default": 8
}
```

### ghast.json
```json
"minecraft:weight:" {
    "default": 40
}
```

### horse.json
```json
"minecraft:weight:" {
    "default": 4
}
```

```json
"minecraft:weight:" {
    "default": 1
}
```

### husk.json
```json
"minecraft:weight:" {
    "default": 240
}
```

### llama.json
```json
"minecraft:weight:" {
    "default": 5
}
```

```json
"minecraft:weight:" {
    "default": 8
}
```

### magma_cube.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### mooshroom.json
```json
"minecraft:weight:" {
    "default": 8
}
```

### ocelot.json
```json
"minecraft:weight:" {
    "default": 30
}
```

### panda.json
```json
"minecraft:weight:" {
    "default": 10
}
```

```json
"minecraft:weight:" {
    "default": 40
}
```

### parrot.json
```json
"minecraft:weight:" {
    "default": 40
}
```

### phantom.json
```json
"minecraft:weight:" {
    "default": 100
}
```

### pig.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### polar_bear.json
```json
"minecraft:weight:" {
    "default": 1
}
```

```json
"minecraft:weight:" {
    "default": 5
}
```

### pufferfish.json
```json
"minecraft:weight:" {
    "default": 25
}
```

### rabbit.json
```json
"minecraft:weight:" {
    "default": 4
}
```

```json
"minecraft:weight:" {
    "default": 20
}
```

### salmon.json
```json
"minecraft:weight:" {
    "default": 26
}
```

```json
"minecraft:weight:" {
    "default": 16
}
```

### sheep.json
```json
"minecraft:weight:" {
    "default": 12
}
```

### skeleton.json
```json
"minecraft:weight:" {
    "default": 80
}
```

### slime.json
```json
"minecraft:weight:" {
    "default": 100
}
```

```json
"minecraft:weight:" {
    "default": 100
}
```

### spider.json
```json
"minecraft:weight:" {
    "default": 100
}
```

### squid.json
```json
"minecraft:weight:" {
    "default": 10
}
```

### stray.json
```json
"minecraft:weight:" {
    "default": 120
}
```

```json
"minecraft:weight:" {
    "default": 120
}
```

### tropicalfish.json
```json
"minecraft:weight:" {
    "default": 75
}
```

```json
"minecraft:weight:" {
    "default": 25
}
```

### turtle.json
```json
"minecraft:weight:" {
    "default": 8
}
```

### witch.json
```json
"minecraft:weight:" {
    "default": 5
}
```

### wolf.json
```json
"minecraft:weight:" {
    "default": 8
}
```

### zombie.json
```json
"minecraft:weight:" {
    "default": 100
}
```

### zombie_pigman.json
```json
"minecraft:weight:" {
    "default": 100
}
```

# minecraft:world_age_filter
### pillager_patrol.json
```json
"minecraft:world_age_filter:" {
    "min": 6000
}
```

```json
"minecraft:world_age_filter:" {
    "min": 6000
}
```

```json
"minecraft:world_age_filter:" {
    "min": 6000
}
```

