---
layout: page
title: Components
parent: Vanilla Usage
---

# Components

<details id="toc" class="top-level" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Components

This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`

# minecraft:addrider
### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.wither"
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:addrider": {
    "entity_type": "minecraft:pillager"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:evocation_illager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:vindicator"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:vindicator",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.wither"
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:addrider": {
    "entity_type": "minecraft:zombie_pigman",
    "spawn_event": "minecraft:spawn_as_strider_jockey"
}
```

```json
"minecraft:addrider": {
    "entity_type": "minecraft:strider",
    "spawn_event": "spawn_baby"
}
```

# minecraft:admire_item
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:admire_item": {
    "duration": 8,
    "cooldown_after_being_attacked": 20
}
```

# minecraft:ageable
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "ageable_grow_up",
        "target": "self"
    }
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "sweet_berries",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "crimson_fungus"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.1
        },
        {
            "item": "hay_block",
            "growth": 0.9
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "bamboo",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "carrot",
        "beetroot",
        "potato"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ],
    "grow_up": {
        "event": "grow_up",
        "target": "self"
    }
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "warped_fungus"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "seagrass"
    ],
    "drop_items": [
        "turtle_shell_piece"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "muttonRaw",
        "muttonCooked",
        "porkchop",
        "cooked_porkchop",
        "rabbit",
        "cooked_rabbit",
        "rotten_flesh"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

# minecraft:ambient_sound_interval
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "event_name": "ambient.pollinate",
    "range": 3.0,
    "value": 2.0
}
```

```json
"minecraft:ambient_sound_interval": {
    "event_name": "ambient",
    "range": 0.0,
    "value": 0.0
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "event_name": "ambient"
}
```

```json
"minecraft:ambient_sound_interval": {
    "event_name": "sleep"
}
```

```json
"minecraft:ambient_sound_interval": {
    "event_name": "screech",
    "value": 80,
    "range": 160
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "value": 4.0,
    "range": 8.0,
    "event_name": "ambient.in.raid"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

# minecraft:angry
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:angry": {
    "duration": 25,
    "broadcastAnger": true,
    "broadcastRange": 20,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "!=",
        "value": "pacified"
    },
    "calm_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:angry": {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 16,
    "calm_event": {
        "event": "on_calm",
        "target": "self"
    }
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:angry": {
    "duration": 25,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:angry": {
    "duration": 10,
    "broadcast_anger": true,
    "broadcast_range": 16,
    "calm_event": {
        "event": "become_calm_event",
        "target": "self"
    },
    "angry_sound": "angry",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:angry": {
    "duration": 4,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry": {
    "duration": 10,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:angry": {
    "duration": 500,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "==",
        "value": "panda_aggressive"
    },
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry": {
    "duration": 1,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "==",
        "value": "panda_aggressive"
    },
    "calm_event": {
        "event": "minecraft:baby_on_calm",
        "target": "self"
    }
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:angry": {
    "duration": 30,
    "broadcast_anger": true,
    "broadcast_anger_on_attack": true,
    "broadcast_anger_on_being_attacked": true,
    "broadcast_range": 16,
    "broadcast_targets": [
        "piglin"
    ],
    "calm_event": {
        "event": "become_calm_event",
        "target": "self"
    },
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "other",
                "operator": "!=",
                "value": "piglin"
            },
            {
                "test": "has_component",
                "subject": "self",
                "operator": "!=",
                "value": "minecraft:attack_cooldown"
            }
        ]
    },
    "angry_sound": "angry",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:angry": {
    "duration": 30,
    "broadcast_anger": false,
    "broadcast_anger_on_attack": false,
    "broadcast_anger_on_being_attacked": true,
    "broadcast_range": 16,
    "broadcast_targets": [
        "piglin"
    ],
    "calm_event": {
        "event": "become_calm_event",
        "target": "self"
    },
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "other",
                "operator": "!=",
                "value": "piglin"
            }
        ]
    },
    "angry_sound": "angry",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:angry": {
    "duration": 1,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "calm_event": {
        "event": "minecraft:baby_on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry": {
    "duration": 500,
    "broadcast_anger": false,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:angry": {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:become_calm",
        "target": "self"
    }
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:stop_aggro",
        "target": "self"
    }
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:angry": {
    "duration": 5,
    "broadcastAnger": true,
    "broadcastRange": 10,
    "broadcast_targets": [
        "llama"
    ],
    "broadcast_filters": {
        "test": "is_leashed_to",
        "subject": "other",
        "value": true
    },
    "calm_event": {
        "event": "minecraft:become_calm",
        "target": "self"
    }
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

# minecraft:annotation.break_door
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:annotation.break_door": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:annotation.break_door": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:annotation.break_door": {
    "break_time": 30,
    "min_difficulty": "normal"
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:annotation.break_door": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:annotation.break_door": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:annotation.break_door": {}
```

# minecraft:annotation.open_door
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:annotation.open_door": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:annotation.open_door": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:annotation.open_door": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:annotation.open_door": {}
```

# minecraft:area_attack
### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:area_attack": {
    "damage_range": 0.2,
    "damage_per_tick": 2,
    "cause": "contact",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

# minecraft:attack
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:attack": {
    "damage": 2
}
```

```json
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 10
}
```

```json
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 18
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:attack": {
    "damage": 6
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 0
}
```

```json
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 7
}
```

```json
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 15
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:attack": {
    "damage": 5
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:attack": {
    "damage": 7
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:attack": {
    "damage": 2
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:attack": {
    "damage": 2
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:attack": {
    "damage": 5
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:attack": {
    "damage": 1.0
}
```

```json
"minecraft:attack": {
    "damage": [
        3,
        9
    ]
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:attack": {
    "damage": 3,
    "effect_name": "hunger",
    "effect_duration": 30
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:attack": {
    "damage": {
        "range_min": 7,
        "range_max": 21
    }
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:attack": {
    "damage": 6
}
```

```json
"minecraft:attack": {
    "damage": 4
}
```

```json
"minecraft:attack": {
    "damage": 2
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:attack": {
    "damage": 2.0
}
```

```json
"minecraft:attack": {
    "damage": 6.0
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:attack": {
    "damage": 6
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:attack": {
    "damage": 5
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:attack": {
    "damage": 7
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:attack": {
    "damage": 1
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:attack": {
    "damage": 6.0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:attack": {
    "damage": 12.0
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:attack": {
    "damage": 1
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:attack": {
    "damage": 4
}
```

```json
"minecraft:attack": {
    "damage": 2
}
```

```json
"minecraft:attack": {
    "damage": 0
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:attack": {
    "damage": 2
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:attack": {
    "damage": 3,
    "effect_name": "slowness",
    "effect_duration": 10
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:attack": {
    "damage": 8
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:attack": {
    "damage": 4,
    "effect_name": "wither",
    "effect_duration": 10
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

```json
"minecraft:attack": {
    "damage": 4
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:attack": {
    "damage": 1
}
```

```json
"minecraft:attack": {
    "damage": [
        3,
        8
    ]
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:attack": {
    "damage": 5
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:attack": {
    "damage": 3
}
```

# minecraft:attack_cooldown
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:attack_cooldown": {
    "attack_cooldown_time": [
        10.0,
        15.0
    ],
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:attack_cooldown": {
    "attack_cooldown_time": [
        30.0,
        120.0
    ],
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

# minecraft:attack_damage
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:attack_damage": {
    "value": 4
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:attack_damage": {
    "value": 4
}
```

# minecraft:balloonable
### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:balloonable": {
    "mass": 0.5
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:balloonable": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:balloonable": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:balloonable": {
    "mass": 0.6
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:balloonable": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:balloonable": {
    "mass": 2.0
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:balloonable": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:balloonable": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:balloonable": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:balloonable": {
    "mass": 1.5
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:balloonable": {
    "mass": 0.75
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:balloonable": {
    "mass": 0.4
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:balloonable": {
    "mass": 0.75
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:balloonable": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:balloonable": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:balloonable": {}
```

# minecraft:barter
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:barter": {
    "barter_table": "loot_tables/entities/piglin_barter.json",
    "cooldown_after_being_attacked": 20
}
```

# minecraft:behavior.admire_item
```json
"minecraft:behavior.admire_item": {
    "priority": 2,
    "admire_item_sound": "admire",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "on_admire_item_start": {
        "event": "admire_item_started_event",
        "target": "self"
    },
    "on_admire_item_stop": {
        "event": "admire_item_stopped_event",
        "target": "self"
    }
}
```

# minecraft:behavior.avoid_block
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.avoid_block": {
    "priority": 1,
    "tick_interval": 5,
    "search_range": 8,
    "search_height": 4,
    "walk_speed_modifier": 1,
    "sprint_speed_modifier": 1,
    "avoid_block_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "target_selection_method": "nearest",
    "target_blocks": [
        "minecraft:warped_fungus",
        "minecraft:portal",
        "minecraft:respawn_anchor"
    ],
    "on_escape": [
        {
            "event": "escaped_event",
            "target": "self"
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.avoid_block": {
    "priority": 9,
    "tick_interval": 5,
    "search_range": 8,
    "search_height": 4,
    "sprint_speed_modifier": 1.1,
    "target_selection_method": "nearest",
    "target_blocks": [
        "minecraft:soul_fire",
        "minecraft:soul_lantern",
        "minecraft:soul_torch",
        "minecraft:item.soul_campfire"
    ],
    "avoid_block_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

# minecraft:behavior.avoid_mob_type
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 6,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10,
            "walk_speed_multiplier": 0.8,
            "sprint_speed_multiplier": 1.33
        }
    ]
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "ocelot"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "cat"
                    }
                ]
            },
            "max_dist": 6,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian_elder"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.0
        }
    ],
    "probability_per_strength": 0.14
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 1.0
        }
    ]
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "trusts",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            },
                            {
                                "test": "is_sneaking",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            }
                        ]
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "polarbear"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wolf"
                    }
                ]
            },
            "max_dist": 10,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1,
            "sprint_speed_multiplier": 1
        }
    ]
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 0,
    "remove_target": true,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_target",
                        "subject": "other",
                        "value": true
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "piglin"
                    }
                ]
            },
            "check_if_outnumbered": true,
            "max_dist": 10,
            "sprint_speed_multiplier": 1.2
        }
    ],
    "avoid_mob_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10,
            "walk_speed_multiplier": 0.8,
            "sprint_speed_multiplier": 1.33
        }
    ]
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "max_dist": 16,
    "max_flee": 20,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "operator": "!=",
                "subject": "other",
                "value": "panda"
            },
            "max_dist": 16,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 0,
    "max_dist": 16.0,
    "ignore_visibility": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "ocelot"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "cat"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "remove_target": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    }
                ]
            },
            "max_dist": 6
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zoglin"
                    }
                ]
            },
            "max_dist": 6
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_target",
                        "subject": "other",
                        "value": true
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "hoglin"
                    }
                ]
            },
            "sprint_speed_multiplier": 1.2,
            "check_if_outnumbered": true
        }
    ],
    "on_escape_event": {
        "event": "become_calm_event",
        "target": "self"
    },
    "avoid_mob_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.8
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 4,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.8
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            },
            "max_dist": 4,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 3,
            "max_flee": 10,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.2,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.2,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ]
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ],
    "max_dist": 6
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "llama"
            },
            "max_dist": 24,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.5
        }
    ],
    "probability_per_strength": 0.14
}
```

# minecraft:behavior.barter
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.barter": {
    "priority": 3
}
```

# minecraft:behavior.beg
### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.beg": {
    "priority": 9,
    "look_distance": 8,
    "look_time": [
        2,
        4
    ],
    "items": [
        "bone",
        "porkchop",
        "cooked_porkchop",
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "rotten_flesh",
        "muttonraw",
        "muttoncooked",
        "rabbit",
        "cooked_rabbit"
    ]
}
```

# minecraft:behavior.breed
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 0.6
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 0.8
}
```

```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.celebrate
### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

# minecraft:behavior.charge_attack
### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.charge_attack": {
    "priority": 4
}
```

# minecraft:behavior.charge_held_item
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.charge_held_item": {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.charge_held_item": {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

# minecraft:behavior.circle_around_anchor
### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:behavior.circle_around_anchor": {
    "priority": 3,
    "radius_change": 1.0,
    "radius_adjustment_chance": 0.004,
    "height_adjustment_chance": 0.002857,
    "goal_radius": 1.0,
    "angle_change": 15.0,
    "radius_range": [
        5.0,
        15.0
    ],
    "height_offset_range": [
        -4.0,
        5.0
    ],
    "height_above_target_range": [
        20.0,
        40.0
    ]
}
```

# minecraft:behavior.controlled_by_player
### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.controlled_by_player": {
    "priority": 0
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.controlled_by_player": {
    "priority": 0,
    "mount_speed_multiplier": 1.45
}
```

# minecraft:behavior.defend_trusted_target
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.defend_trusted_target": {
    "priority": 0,
    "within_radius": 25,
    "must_see": false,
    "aggro_sound": "mad",
    "sound_chance": 0.05,
    "on_defend_start": {
        "event": "minecraft:fox_configure_defending",
        "target": "self"
    }
}
```

# minecraft:behavior.defend_village_target
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.defend_village_target": {
    "priority": 1,
    "must_reach": true,
    "attack_chance": 0.05,
    "entity_types": {
        "filters": {
            "any_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "mob"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "player"
                }
            ]
        }
    }
}
```

# minecraft:behavior.delayed_attack
### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.delayed_attack": {
    "priority": 4,
    "attack_once": false,
    "track_target": true,
    "require_complete_path": false,
    "random_stop_interval": 0,
    "reach_multiplier": 1.5,
    "speed_multiplier": 1.0,
    "attack_duration": 0.75,
    "hit_delay_pct": 0.5
}
```

# minecraft:behavior.dragonchargeplayer
### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:behavior.dragonchargeplayer": {
    "priority": 1
}
```

# minecraft:behavior.dragondeath
```json
"minecraft:behavior.dragondeath": {
    "priority": 0
}
```

# minecraft:behavior.dragonflaming
```json
"minecraft:behavior.dragonflaming": {
    "priority": 1
}
```

# minecraft:behavior.dragonholdingpattern
```json
"minecraft:behavior.dragonholdingpattern": {
    "priority": 3
}
```

# minecraft:behavior.dragonlanding
```json
"minecraft:behavior.dragonlanding": {
    "priority": 0
}
```

# minecraft:behavior.dragonscanning
```json
"minecraft:behavior.dragonscanning": {
    "priority": 2
}
```

# minecraft:behavior.dragonstrafeplayer
```json
"minecraft:behavior.dragonstrafeplayer": {
    "priority": 2
}
```

# minecraft:behavior.dragontakeoff
```json
"minecraft:behavior.dragontakeoff": {
    "priority": 0
}
```

# minecraft:behavior.drink_potion
### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.drink_potion": {
    "priority": 1,
    "speed_modifier": -0.2,
    "potions": [
        {
            "id": 7,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "hourly_clock_time",
                                "operator": ">=",
                                "value": 18000
                            },
                            {
                                "test": "hourly_clock_time",
                                "operator": "<",
                                "value": 12000
                            }
                        ]
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "all_of": [
                                    {
                                        "test": "has_component",
                                        "subject": "self",
                                        "value": "minecraft:angry"
                                    },
                                    {
                                        "test": "is_family",
                                        "subject": "target",
                                        "operator": "!=",
                                        "value": "player"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": 8,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 18000
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "test": "has_component",
                                "subject": "self",
                                "value": "minecraft:angry"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

# minecraft:behavior.drop_item_for
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.drop_item_for": {
    "priority": 1,
    "seconds_before_pickup": 0.0,
    "cooldown": 0.25,
    "drop_item_chance": 0.7,
    "offering_distance": 5.0,
    "minimum_teleport_distance": 2.0,
    "max_head_look_at_height": 10.0,
    "target_range": [
        5.0,
        5.0,
        5.0
    ],
    "teleport_offset": [
        0.0,
        1.0,
        0.0
    ],
    "time_of_day_range": [
        0.74999,
        0.8
    ],
    "speed_multiplier": 1.0,
    "search_range": 5,
    "search_height": 2,
    "search_count": 0,
    "goal_radius": 1.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6
        }
    ],
    "loot_table": "loot_tables/entities/cat_gift.json",
    "on_drop_attempt": {
        "event": "minecraft:cat_gifted_owner",
        "target": "self"
    }
}
```

# minecraft:behavior.eat_block
### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.eat_block": {
    "priority": 6,
    "success_chance": "query.is_baby ? 0.02 : 0.001",
    "time_until_eat": 1.8,
    "eat_and_replace_block_pairs": [
        {
            "eat_block": "grass",
            "replace_block": "dirt"
        },
        {
            "eat_block": "tallgrass",
            "replace_block": "air"
        }
    ],
    "on_eat": {
        "event": "minecraft:on_eat_block",
        "target": "self"
    }
}
```

# minecraft:behavior.eat_carried_item
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.eat_carried_item": {
    "priority": 12,
    "delay_before_eating": 28
}
```

# minecraft:behavior.enderman_leave_block
### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.enderman_leave_block": {
    "priority": 10
}
```

# minecraft:behavior.enderman_take_block
```json
"minecraft:behavior.enderman_take_block": {
    "priority": 11
}
```

# minecraft:behavior.equip_item
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 2
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 2
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 5
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 2
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

# minecraft:behavior.explore_outskirts
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.explore_outskirts": {}
```

```json
"minecraft:behavior.explore_outskirts": {
    "priority": 9,
    "next_xz": 5,
    "next_y": 3,
    "min_wait_time": 3.0,
    "max_wait_time": 10.0,
    "max_travel_time": 60.0,
    "speed_multiplier": 0.6,
    "explore_dist": 6.0,
    "min_perimeter": 1.0,
    "min_dist_from_target": 2.5,
    "timer_ratio": 2.0,
    "dist_from_boundary": [
        5.0,
        0.0,
        5.0
    ]
}
```

# minecraft:behavior.find_cover
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.find_cover": {
    "priority": 0,
    "speed_multiplier": 1,
    "cooldown_time": 0.0
}
```

```json
"minecraft:behavior.find_cover": {
    "priority": 9,
    "speed_multiplier": 1,
    "cooldown_time": 5.0
}
```

# minecraft:behavior.find_mount
### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 3,
    "within_radius": 16,
    "avoid_water": true,
    "start_delay": 100,
    "target_needed": false,
    "mount_distance": 2.0
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

# minecraft:behavior.find_underwater_treasure
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.find_underwater_treasure": {
    "priority": 2,
    "speed_multiplier": 2.0,
    "search_range": 30,
    "stop_distance": 50
}
```

# minecraft:behavior.flee_sun
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

# minecraft:behavior.float
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 19
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 1
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 2
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 1
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 1
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 1
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 1
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.float": {
    "priority": 0
}
```

# minecraft:behavior.float_wander
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:behavior.float_wander": {
    "xz_dist": 10,
    "y_dist": 7,
    "y_offset": -2.0,
    "random_reselect": true,
    "float_duration": [
        0.1,
        0.35
    ]
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:behavior.float_wander": {
    "priority": 2,
    "must_reach": true
}
```

# minecraft:behavior.follow_caravan
### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.follow_caravan": {
    "priority": 3,
    "speed_multiplier": 2.1,
    "entity_count": 10,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "llama"
        }
    }
}
```

# minecraft:behavior.follow_mob
### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.follow_mob": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "stop_distance": 3,
    "search_range": 20
}
```

# minecraft:behavior.follow_owner
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.follow_owner": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "start_distance": 5,
    "stop_distance": 1
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.follow_owner": {
    "priority": 6,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

# minecraft:behavior.follow_parent
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 11,
    "speed_multiplier": 1.1
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.1
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 9,
    "speed_multiplier": 1.1
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 13,
    "speed_multiplier": 1.1
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.25
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.follow_target_captain
### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

# minecraft:behavior.go_home
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.go_home": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 1,
    "goal_radius": 1.2,
    "on_home": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "find_hive_event",
            "target": "self"
        }
    ],
    "on_failed": {
        "event": "find_hive_event",
        "target": "self"
    }
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.go_home": {
    "priority": 6,
    "interval": 200,
    "speed_multiplier": 0.6,
    "goal_radius": 4.0,
    "on_failed": {
        "event": "go_back_to_spawn_failed",
        "target": "self"
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.go_home": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "interval": 700,
    "goal_radius": 4.0,
    "on_home": {
        "event": "minecraft:go_lay_egg",
        "target": "self"
    }
}
```

# minecraft:behavior.guardian_attack
### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

# minecraft:behavior.harvest_farm_block
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.harvest_farm_block": {
    "priority": 9,
    "speed_multiplier": 0.5
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.harvest_farm_block": {}
```

```json
"minecraft:behavior.harvest_farm_block": {
    "priority": 8,
    "max_seconds_before_search": 1.0,
    "search_cooldown_max_seconds": 8.0,
    "seconds_until_new_task": 0.5,
    "speed_multiplier": 0.5
}
```

# minecraft:behavior.hide
```json
"minecraft:behavior.hide": {
    "priority": 0,
    "speed_multiplier": 0.8,
    "poi_type": "bed",
    "duration": 30.0
}
```

# minecraft:behavior.hold_ground
### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.hold_ground": {
    "priority": 5,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:ranged_mode",
        "target": "self"
    }
}
```

```json
"minecraft:behavior.hold_ground": {
    "priority": 6,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:ranged_mode",
        "target": "self"
    }
}
```

# minecraft:behavior.hurt_by_target
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "creeper"
        }
    }
}
```

```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "all_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "player"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "creeper"
                }
            ]
        }
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "hurt_owner": true
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "alert_same_type": true
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

# minecraft:behavior.inspect_bookshelf
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.inspect_bookshelf": {}
```

```json
"minecraft:behavior.inspect_bookshelf": {
    "priority": 8,
    "speed_multiplier": 0.6,
    "search_range": 4,
    "search_height": 3,
    "goal_radius": 0.8,
    "search_count": 0
}
```

# minecraft:behavior.knockback_roar
### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.knockback_roar": {
    "priority": 1,
    "duration": 1,
    "attack_time": 0.5,
    "knockback_damage": 6,
    "knockback_strength": 3,
    "knockback_range": 4,
    "knockback_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "ravager"
    },
    "damage_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "illager"
    },
    "on_roar_end": {
        "event": "minecraft:end_roar"
    },
    "cooldown_time": 0.1
}
```

# minecraft:behavior.lay_down
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.lay_down": {
    "priority": 5,
    "interval": 400,
    "random_stop_interval": 2000
}
```

# minecraft:behavior.lay_egg
### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.lay_egg": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "search_range": 16,
    "search_height": 4,
    "goal_radius": 1.5,
    "on_lay": {
        "event": "minecraft:laid_egg",
        "target": "self"
    }
}
```

# minecraft:behavior.leap_at_target
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "target_dist": 0.4
}
```

# minecraft:behavior.look_at_entity
### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8.0,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8,
    "angle_of_view_horizontal": 45,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.look_at_entity": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

# minecraft:behavior.look_at_player
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6,
    "probability": 0.02
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8.0,
    "probability": 8.0
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 3.0,
    "probability": 1.0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 14,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6,
    "probability": 0.02
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 0,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 1,
    "look_distance": 8.0
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 11,
    "look_distance": 8
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 8
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 11
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6,
    "angle_of_view_horizontal": 45,
    "probability": 1
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 1,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 8
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 3,
    "look_distance": 6.0
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 8
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 12,
    "look_distance": 8,
    "probability": 0.02
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 10,
    "look_distance": 8,
    "probability": 0.02
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 8
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 10,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.look_at_player": {
    "priority": 10,
    "look_distance": 6,
    "probability": 0.02
}
```

# minecraft:behavior.look_at_target
### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.look_at_target": {
    "priority": 5
}
```

# minecraft:behavior.look_at_trading_player
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.look_at_trading_player": {
    "priority": 2
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.look_at_trading_player": {
    "priority": 7
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.look_at_trading_player": {
    "priority": 4
}
```

# minecraft:behavior.make_love
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.make_love": {
    "priority": 6
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.make_love": {
    "priority": 5
}
```

# minecraft:behavior.melee_attack
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "attack_once": true,
    "speed_multiplier": 1.4,
    "on_attack": {
        "event": "countdown_to_perish_event",
        "target": "self"
    }
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "track_target": true,
    "random_stop_interval": 100,
    "reach_multiplier": 0.8
}
```

```json
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "track_target": true,
    "reach_multiplier": 1.4
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "track_target": false,
    "reach_multiplier": 0.0
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "track_target": true
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false,
    "require_complete_path": true
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 2
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "track_target": true
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 10,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

```json
"minecraft:behavior.melee_attack": {
    "priority": 1,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1,
    "track_target": true,
    "reach_multiplier": 1.0,
    "cooldown_time": 0.75
}
```

```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1,
    "track_target": true,
    "reach_multiplier": 2.5,
    "cooldown_time": 2
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 1,
    "track_target": true
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "attack_once": true,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

```json
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 8,
    "speed_multiplier": 1.0,
    "track_target": true
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1,
    "track_target": true
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "track_target": true
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "track_target": true
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "track_target": true,
    "speed_multiplier": 1.25
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "track_target": true,
    "reach_multiplier": 0.8
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "track_target": true,
    "speed_multiplier": 1.25
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "track_target": true,
    "speed_multiplier": 1.25
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 5
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.4,
    "track_target": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 3
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.5
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 6
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.melee_attack": {
    "priority": 6
}
```

# minecraft:behavior.mingle
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.mingle": {}
```

```json
"minecraft:behavior.mingle": {
    "priority": 7,
    "speed_multiplier": 0.5,
    "duration": 30,
    "cooldown_time": 10,
    "mingle_partner_type": "minecraft:villager_v2",
    "mingle_distance": 2.0
}
```

# minecraft:behavior.mount_pathing
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 4.0,
    "track_target": true
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

# minecraft:behavior.move_indoors
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.move_indoors": {
    "priority": 4,
    "speed_multiplier": 0.8
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.move_indoors": {
    "priority": 6,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

# minecraft:behavior.move_through_village
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.move_through_village": {
    "priority": 3,
    "speed_multiplier": 0.6,
    "only_at_night": true
}
```

# minecraft:behavior.move_to_block
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.move_to_block": {
    "priority": 10,
    "tick_interval": 1,
    "start_chance": 0.5,
    "search_range": 6,
    "search_height": 4,
    "goal_radius": 1.0,
    "stay_duration": 20.0,
    "target_selection_method": "random",
    "target_offset": [
        0,
        0.25,
        0
    ],
    "target_blocks": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sweet_berry_bush",
        "minecraft:double_plant:8",
        "minecraft:double_plant:9",
        "minecraft:double_plant:12",
        "minecraft:double_plant:13"
    ],
    "on_stay_completed": [
        {
            "event": "collected_nectar",
            "target": "self"
        }
    ]
}
```

```json
"minecraft:behavior.move_to_block": {
    "priority": 10,
    "search_range": 16,
    "search_height": 10,
    "tick_interval": 1,
    "goal_radius": 0.633,
    "target_blocks": [
        "bee_nest",
        "beehive"
    ],
    "on_reach": [
        {
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        }
    ]
}
```

# minecraft:behavior.move_to_land
### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.move_to_land": {
    "priority": 6,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 0.5
}
```

# minecraft:behavior.move_to_liquid
### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.move_to_liquid": {
    "priority": 7,
    "search_range": 16,
    "search_height": 10,
    "goal_radius": 0.9,
    "material_type": "Lava",
    "search_count": 30
}
```

# minecraft:behavior.move_to_random_block
### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.move_to_random_block": {
    "priority": 6,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.move_to_random_block": {
    "priority": 5,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

# minecraft:behavior.move_to_village
### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.move_to_village": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.move_to_village": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.move_to_village": {
    "priority": 3,
    "speed_multiplier": 1.2,
    "goal_radius": 2.0
}
```

# minecraft:behavior.move_to_water
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.move_to_water": {
    "priority": 4,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 1.5
}
```

```json
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5,
    "goal_radius": 0.1
}
```

# minecraft:behavior.move_towards_dwelling_restriction
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 7
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 4,
    "speed_multiplier": 1
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

# minecraft:behavior.move_towards_home_restriction
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 9
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.move_towards_target
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.move_towards_target": {
    "priority": 2,
    "speed_multiplier": 0.9,
    "within_radius": 32
}
```

# minecraft:behavior.nap
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.nap": {
    "priority": 8,
    "cooldown_min": 2.0,
    "cooldown_max": 7.0,
    "mob_detect_dist": 12.0,
    "mob_detect_height": 6.0,
    "can_nap_filters": {
        "all_of": [
            {
                "test": "in_water",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            {
                "test": "on_ground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_underground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "weather_at_position",
                "subject": "self",
                "operator": "!=",
                "value": "thunderstorm"
            }
        ]
    },
    "wake_mob_exceptions": {
        "any_of": [
            {
                "test": "trusts",
                "subject": "other",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_family",
                "subject": "other",
                "operator": "==",
                "value": "fox"
            },
            {
                "test": "is_sneaking",
                "subject": "other",
                "operator": "==",
                "value": true
            }
        ]
    }
}
```

# minecraft:behavior.nearest_attackable_target
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10
        }
    ]
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 48.0
        }
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "reselect_targets": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "attack_interval": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "must_see": true,
    "must_see_forget_duration": 3.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ]
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "must_see": true,
    "within_radius": 12.0,
    "must_see_forget_duration": 17.0,
    "persist_time": 0.5,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "snowgolem"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "irongolem"
                            }
                        ]
                    },
                    {
                        "any_of": [
                            {
                                "test": "in_water",
                                "subject": "other",
                                "value": true
                            },
                            {
                                "test": "is_daytime",
                                "value": false
                            }
                        ]
                    }
                ]
            },
            "max_dist": 20
        },
        {
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "villager"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "wandering_trader"
                            }
                        ]
                    },
                    {
                        "any_of": [
                            {
                                "test": "in_water",
                                "subject": "other",
                                "value": true
                            },
                            {
                                "test": "is_daytime",
                                "value": false
                            }
                        ]
                    }
                ]
            },
            "max_dist": 20,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 20
        }
    ]
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "squid"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval_min": 1.0,
    "must_see": true
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "must_see": true,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "endermite"
            },
            "max_dist": 64
        }
    ]
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "must_see": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "enderman"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 20
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 20
        }
    ],
    "must_see": true
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 28
        }
    ],
    "must_see": true
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "squid"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval_min": 1.0,
    "must_see": true
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "operator": "!=",
                        "value": "minecraft:attack_cooldown"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "within_radius": 25.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ]
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "must_reach": true,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "monster"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            },
            "within_default": 10
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "hoglin"
                    },
                    {
                        "test": "is_difficulty",
                        "operator": "!=",
                        "value": "peaceful"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zoglin"
                    },
                    {
                        "test": "is_difficulty",
                        "operator": "!=",
                        "value": "peaceful"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "attack_interval": 16,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wolf"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_tamed"
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "must_see": false,
    "must_reach": true
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "reselect_targets": true,
    "scan_interval": 20,
    "within_radius": 64.0,
    "must_see_forget_duration": 0.5,
    "target_search_height": 80.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 64
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 7,
    "within_radius": 16.0,
    "persist_time": 2.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wither"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "self",
                        "value": "piglin_hunter"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "hoglin_huntable"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "operator": "!=",
                        "value": "minecraft:attack_cooldown"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "has_equipment",
                        "subject": "other",
                        "domain": "head",
                        "operator": "!=",
                        "value": "golden_helmet"
                    },
                    {
                        "test": "has_equipment",
                        "subject": "other",
                        "domain": "torso",
                        "operator": "!=",
                        "value": "golden_chestplate"
                    },
                    {
                        "test": "has_equipment",
                        "subject": "other",
                        "domain": "leg",
                        "operator": "!=",
                        "value": "golden_leggings"
                    },
                    {
                        "test": "has_equipment",
                        "subject": "other",
                        "domain": "feet",
                        "operator": "!=",
                        "value": "golden_boots"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "has_container_open",
                        "subject": "other",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 7,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ]
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ]
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ]
}
```

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "fox"
            },
            "max_dist": 16
        }
    ],
    "must_see": false
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "must_see": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "subject": "other",
                        "test": "is_family",
                        "value": "player"
                    },
                    {
                        "subject": "other",
                        "test": "is_family",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "player"
        },
        "max_dist": 16
    },
    "must_see": true
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            },
            "within_default": 6
        }
    ]
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "attack_interval": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 70
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 70
        }
    ],
    "must_see": true
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "within_radius": 12.0,
    "must_see_forget_duration": 40.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "illager"
                    }
                ]
            },
            "max_dist": 12
        }
    ]
}
```

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "within_radius": 12.0,
    "must_see_forget_duration": 40.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 12
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 12
        }
    ]
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "must_reach": true
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 70
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "undead"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "inanimate"
                    }
                ]
            },
            "max_dist": 70
        }
    ],
    "must_see": true
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "piglin"
                    },
                    {
                        "test": "is_difficulty",
                        "operator": "!=",
                        "value": "peaceful"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "reselect_targets": true,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "skeleton"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "rabbit"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "fox"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "skeleton"
                    },
                    {
                        "test": "is_underwater",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "skeleton"
            },
            "max_dist": 16
        }
    ]
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "zoglin"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "within_radius": 25.0,
    "must_see_forget_duration": 17.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ]
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ]
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ]
}
```

# minecraft:behavior.nearest_prioritized_attackable_target
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 0
        }
    ]
}
```

```json
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 1
        }
    ]
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 3,
    "within_radius": 12.0,
    "persist_time": 2.0,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wither"
            },
            "max_dist": 12,
            "priority": 1
        }
    ]
}
```

# minecraft:behavior.ocelot_sit_on_block
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.ocelotattack
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "cooldown_time": 1.0,
    "x_max_rotation": 30.0,
    "y_max_head_rotation": 30.0,
    "max_distance": 15.0,
    "max_sneak_range": 15.0,
    "max_sprint_range": 4.0,
    "reach_multiplier": 2.0,
    "sneak_speed_multiplier": 0.6,
    "sprint_speed_multiplier": 1.33,
    "walk_speed_multiplier": 0.8
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "cooldown_time": 1.0,
    "x_max_rotation": 30.0,
    "y_max_head_rotation": 30.0,
    "max_distance": 15.0,
    "max_sneak_range": 15.0,
    "max_sprint_range": 4.0,
    "reach_multiplier": 2.0,
    "sneak_speed_multiplier": 0.6,
    "sprint_speed_multiplier": 1.33,
    "walk_speed_multiplier": 0.8
}
```

# minecraft:behavior.offer_flower
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.offer_flower": {
    "priority": 5
}
```

# minecraft:behavior.open_door
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
}
```

# minecraft:behavior.owner_hurt_by_target
### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.owner_hurt_by_target": {
    "priority": 1
}
```

# minecraft:behavior.owner_hurt_target
```json
"minecraft:behavior.owner_hurt_target": {
    "priority": 2
}
```

# minecraft:behavior.panic
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "force": true
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.5
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```json
"minecraft:behavior.panic": {
    "priority": 2,
    "speed_multiplier": 1.25
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 1.2
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 4,
    "speed_multiplier": 1.2
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 2.5
}
```

```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "ignore_mob_damage": true
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 0,
    "speed_multiplier": 1.25
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 1.25
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.1
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 2,
    "speed_multiplier": 2.0
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 2.2
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 1.1,
    "panic_sound": "panic",
    "sound_interval": {
        "range_min": 1.0,
        "range_max": 3.0
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 0,
    "prefer_water": true,
    "speed_multiplier": 1.2
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 0.6
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.pet_sleep_with_owner
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.pet_sleep_with_owner": {
    "priority": 2,
    "speed_multiplier": 1.2,
    "search_radius": 10,
    "search_height": 10,
    "goal_radius": 1.0
}
```

# minecraft:behavior.pickup_items
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 11,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 10,
    "goal_radius": 2,
    "speed_multiplier": 0.8,
    "pickup_based_on_chance": false,
    "can_pickup_any_item": false,
    "cooldown_after_being_attacked": 20.0
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 7,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 5,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 5,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 9,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5,
    "can_pickup_to_hand_or_equipment": false
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 4,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5,
    "can_pickup_to_hand_or_equipment": false
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 5,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 8,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.pickup_items": {
    "priority": 8,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

# minecraft:behavior.play
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

# minecraft:behavior.player_ride_tamed
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.player_ride_tamed": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.player_ride_tamed": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.player_ride_tamed": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.player_ride_tamed": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.player_ride_tamed": {}
```

# minecraft:behavior.raid_garden
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.raid_garden": {
    "priority": 12,
    "blocks": [
        "minecraft:sweet_berry_bush"
    ],
    "speed_multiplier": 1.2,
    "search_range": 12,
    "search_height": 2,
    "goal_radius": 0.8,
    "max_to_eat": 0,
    "initial_eat_delay": 2
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.raid_garden": {
    "priority": 5,
    "blocks": [
        "carrots"
    ],
    "search_range": 16,
    "goal_radius": 0.8
}
```

# minecraft:behavior.random_breach
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.random_breach": {
    "priority": 6,
    "interval": 50,
    "xz_dist": 6,
    "cooldown_time": 2.0
}
```

# minecraft:behavior.random_fly
### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.random_fly": {
    "priority": 2,
    "xz_dist": 15,
    "y_dist": 1,
    "y_offset": 0,
    "speed_multiplier": 1.0,
    "can_land_on_trees": true,
    "avoid_damage_blocks": true
}
```

# minecraft:behavior.random_hover
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.random_hover": {
    "priority": 12,
    "xz_dist": 8,
    "y_dist": 8,
    "y_offset": -1,
    "interval": 1,
    "hover_height": [
        1,
        4
    ]
}
```

# minecraft:behavior.random_look_around
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 5
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 15
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 12
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 10
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 4
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 10
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 11
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.random_look_around": {
    "priority": 11
}
```

# minecraft:behavior.random_look_around_and_sit
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.random_look_around_and_sit": {
    "priority": 12,
    "min_look_count": 2,
    "max_look_count": 5,
    "min_look_time": 80,
    "max_look_time": 100,
    "probability": 0.001
}
```

# minecraft:behavior.random_sitting
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.random_sitting": {
    "priority": 5,
    "start_chance": 0.01,
    "stop_chance": 0.3,
    "cooldown": 30,
    "min_sit_time": 10
}
```

```json
"minecraft:behavior.random_sitting": {
    "priority": 6,
    "start_chance": 0.02,
    "stop_chance": 0.2,
    "cooldown": 25,
    "min_sit_time": 15
}
```

# minecraft:behavior.random_stroll
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.6
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 13,
    "speed_multiplier": 0.8
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 0.4
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.6,
    "xz_dist": 16
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 14,
    "speed_multiplier": 0.8
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 0.6
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 1
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 5
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.6,
    "xz_dist": 2,
    "y_dist": 1
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.4
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 0.8
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "interval": 100
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 11,
    "speed_multiplier": 0.6
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "speed_multiplier": 1
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 1.0
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "speed_multiplier": 1
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "speed_multiplier": 1
}
```

# minecraft:behavior.random_swim
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 5,
    "interval": 0,
    "xz_dist": 20
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 7,
    "speed_multiplier": 0.5,
    "avoid_surface": false
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 7,
    "speed_multiplier": 1.0,
    "interval": 80,
    "avoid_surface": false
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:behavior.random_swim": {
    "speed_multiplier": 1.0,
    "priority": 3,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.random_swim": {
    "priority": 7,
    "interval": 0,
    "xz_dist": 30,
    "y_dist": 15
}
```

# minecraft:behavior.ranged_attack
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 3,
    "burst_shots": 3,
    "burst_interval": 0.3,
    "charge_charged_trigger": 0.0,
    "charge_shoot_trigger": 4.0,
    "attack_interval_min": 3.0,
    "attack_interval_max": 5.0,
    "attack_radius": 16.0
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 3,
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 10.0
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 1,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 8,
    "attack_interval_min": 1,
    "attack_interval_max": 1,
    "attack_radius": 8,
    "attack_radius_min": 4,
    "speed_multiplier": 1.0,
    "target_in_sight_time": 0.1
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 4,
    "attack_interval_min": 1.0,
    "attack_interval_max": 1.0,
    "attack_radius": 8.0
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 0,
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 15.0
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "attack_interval": 1,
    "attack_radius": 10
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 0,
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 15.0
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "attack_interval_min": 3,
    "attack_interval_max": 3,
    "attack_radius": 10.0
}
```

# minecraft:behavior.receive_love
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.receive_love": {
    "priority": 7
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.receive_love": {
    "priority": 6
}
```

# minecraft:behavior.restrict_open_door
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

# minecraft:behavior.rise_to_liquid_level
### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.rise_to_liquid_level": {
    "priority": 0,
    "liquid_y_offset": 0.25,
    "rise_delta": 0.01,
    "sink_delta": 0.01
}
```

# minecraft:behavior.roll
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.0016
}
```

```json
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.013
}
```

# minecraft:behavior.run_around_like_crazy
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.scared
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.scared": {
    "priority": 1,
    "sound_interval": 20
}
```

# minecraft:behavior.send_event
### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.send_event": {
    "priority": 3,
    "event_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 16.0,
            "cooldown_time": 5.0,
            "cast_duration": 3.0,
            "particle_color": "#FFB38033",
            "weight": 3,
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_color",
                        "subject": "other",
                        "value": "blue"
                    }
                ]
            },
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "base_delay": 2.0,
                    "event": "wololo",
                    "sound_event": "prepare.wololo"
                }
            ]
        }
    ]
}
```

# minecraft:behavior.share_items
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.share_items": {
    "priority": 8,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.share_items": {
    "priority": 9,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

# minecraft:behavior.silverfish_merge_with_stone
### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:behavior.silverfish_merge_with_stone": {
    "priority": 5
}
```

# minecraft:behavior.silverfish_wake_up_friends
```json
"minecraft:behavior.silverfish_wake_up_friends": {
    "priority": 1
}
```

# minecraft:behavior.skeleton_horse_trap
### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:behavior.skeleton_horse_trap": {
    "within_radius": 10.0,
    "duration": 900.0,
    "priority": 2
}
```

# minecraft:behavior.sleep
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.sleep": {}
```

```json
"minecraft:behavior.sleep": {
    "priority": 3,
    "goal_radius": 1.5,
    "speed_multiplier": 0.6,
    "sleep_collider_height": 0.3,
    "sleep_collider_width": 1.0,
    "sleep_y_offset": 0.6,
    "timeout_cooldown": 10.0
}
```

# minecraft:behavior.slime_attack
### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

# minecraft:behavior.slime_float
### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:behavior.slime_float": {
    "priority": 1,
    "jump_chance_percentage": 0.8,
    "speed_multiplier": 1.2
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:behavior.slime_float": {
    "priority": 1,
    "jump_chance_percentage": 0.8,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.slime_keep_on_jumping
### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.slime_random_direction
### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:behavior.slime_random_direction": {
    "priority": 4,
    "add_random_time_range": 3,
    "turn_range": 360,
    "min_change_direction_time": 2.0
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:behavior.slime_random_direction": {
    "priority": 4,
    "add_random_time_range": 3,
    "turn_range": 360,
    "min_change_direction_time": 2.0
}
```

# minecraft:behavior.snacking
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.snacking": {
    "priority": 2,
    "snacking_cooldown": 22.5,
    "snacking_cooldown_min": 20,
    "snacking_stop_chance": 0.001334,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

```json
"minecraft:behavior.snacking": {
    "priority": 3,
    "snacking_cooldown": 17.5,
    "snacking_cooldown_min": 10,
    "snacking_stop_chance": 0.0011,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

# minecraft:behavior.sneeze
```json
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.0001666,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

```json
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.002,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

# minecraft:behavior.squid_dive
### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:behavior.squid_dive": {
    "priority": 2
}
```

# minecraft:behavior.squid_flee
```json
"minecraft:behavior.squid_flee": {
    "priority": 2
}
```

# minecraft:behavior.squid_idle
```json
"minecraft:behavior.squid_idle": {
    "priority": 2
}
```

# minecraft:behavior.squid_move_away_from_ground
```json
"minecraft:behavior.squid_move_away_from_ground": {
    "priority": 1
}
```

# minecraft:behavior.squid_out_of_water
```json
"minecraft:behavior.squid_out_of_water": {
    "priority": 2
}
```

# minecraft:behavior.stalk_and_pounce_on_target
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.stalk_and_pounce_on_target": {
    "priority": 7,
    "stalk_speed": 1.2,
    "max_stalk_dist": 12.0,
    "leap_height": 0.9,
    "leap_dist": 0.8,
    "pounce_max_dist": 5.0,
    "interest_time": 2.0,
    "stuck_time": 2.0,
    "strike_dist": 2.0,
    "stuck_blocks": {
        "test": "is_block",
        "subject": "block",
        "operator": "==",
        "value": "snow_layer"
    }
}
```

# minecraft:behavior.stay_while_sitting
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:behavior.stay_while_sitting": {
    "priority": 1
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

# minecraft:behavior.stomp_attack
### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:behavior.stomp_attack": {
    "priority": 1,
    "track_target": true,
    "require_complete_path": true,
    "stomp_range_multiplier": 2.0,
    "no_damage_range_multiplier": 2.0
}
```

# minecraft:behavior.stomp_turtle_egg
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 5,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

# minecraft:behavior.stroll_towards_village
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.stroll_towards_village": {
    "priority": 11,
    "speed_multiplier": 1.0,
    "goal_radius": 3.0,
    "cooldown_time": 10.0,
    "search_range": 32,
    "start_chance": 0.005
}
```

# minecraft:behavior.summon_entity
### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:behavior.summon_entity": {
    "priority": 2,
    "summon_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 3.0,
            "cooldown_time": 5.0,
            "weight": 3,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 5,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 1.5,
                    "entity_lifespan": 1.1,
                    "sound_event": "prepare.attack"
                },
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 0.15,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 8,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 2.5,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "min_activation_range": 3.0,
            "weight": 3,
            "cooldown_time": 5.0,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "line",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.05,
                    "num_entities_spawned": 16,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 20,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "weight": 1,
            "cooldown_time": 17.0,
            "cast_duration": 5.0,
            "particle_color": "#FFB3B3CC",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 5.0,
                    "num_entities_spawned": 3,
                    "entity_type": "minecraft:vex",
                    "summon_cap": 8,
                    "summon_cap_radius": 16.0,
                    "size": 1.0,
                    "sound_event": "prepare.summon"
                }
            ]
        }
    ]
}
```

# minecraft:behavior.swell
### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:behavior.swell": {
    "start_distance": 2.5,
    "stop_distance": 6.0,
    "priority": 2
}
```

# minecraft:behavior.swim_idle
### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

# minecraft:behavior.swim_wander
### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.1,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:behavior.swim_wander": {
    "priority": 5,
    "interval": 1.0,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.0166,
    "look_ahead": 5.0,
    "speed_multiplier": 0.014,
    "wander_time": 5.0
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.1,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

# minecraft:behavior.swim_with_entity
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:behavior.swim_with_entity": {
    "priority": 4,
    "success_rate": 0.1,
    "chance_to_stop": 0.0333,
    "state_check_interval": 0.5,
    "catch_up_threshold": 12.0,
    "match_direction_threshold": 2.0,
    "catch_up_multiplier": 2.5,
    "speed_multiplier": 1.5,
    "search_range": 20.0,
    "stop_distance": 5.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            }
        }
    ]
}
```

# minecraft:behavior.swoop_attack
### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:behavior.swoop_attack": {
    "priority": 2,
    "damage_reach": 0.2,
    "speed_multiplier": 1.0,
    "delay_range": [
        10.0,
        20.0
    ]
}
```

# minecraft:behavior.take_flower
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.take_flower": {
    "priority": 7
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.take_flower": {
    "priority": 9
}
```

# minecraft:behavior.target_when_pushed
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:behavior.target_when_pushed": {
    "priority": 1,
    "percent_chance": 5.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "monster"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            }
        }
    ]
}
```

# minecraft:behavior.tempt
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "within_radius": 8,
    "can_tempt_vertically": true,
    "items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "fish",
        "salmon"
    ]
}
```

```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "items": [
        "fish",
        "salmon"
    ]
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ]
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "apple",
        "carrot",
        "golden_apple",
        "appleEnchanted",
        "golden_carrot",
        "carrotOnAStick",
        "hay_block",
        "sugar",
        "bread",
        "wheat"
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "sweet_berries"
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "golden_apple",
        "appleEnchanted",
        "golden_carrot"
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "apple",
        "carrot",
        "golden_apple",
        "appleEnchanted",
        "golden_carrot",
        "carrotOnAStick",
        "hay_block",
        "sugar",
        "bread",
        "wheat"
    ]
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "fish",
        "salmon"
    ]
}
```

```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "items": [
        "fish",
        "salmon"
    ]
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "bamboo"
    ]
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "potato",
        "carrot",
        "beetroot",
        "carrotOnAStick"
    ]
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 1,
    "items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ]
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "warped_fungus",
        "warped_fungus_on_a_stick"
    ],
    "can_tempt_while_ridden": true,
    "tempt_sound": "tempt",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 1.1,
    "items": [
        "seagrass"
    ]
}
```

# minecraft:behavior.trade_interest
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.trade_interest": {}
```

```json
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.trade_interest": {
    "priority": 3,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

# minecraft:behavior.trade_with_player
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:behavior.trade_with_player": {
    "priority": 1
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.trade_with_player": {
    "priority": 2
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:behavior.trade_with_player": {
    "priority": 1
}
```

# minecraft:behavior.wither_random_attack_pos_goal
### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:behavior.wither_random_attack_pos_goal": {
    "priority": 3
}
```

# minecraft:behavior.wither_target_highest_damage
```json
"minecraft:behavior.wither_target_highest_damage": {
    "priority": 1
}
```

# minecraft:behavior.work
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:behavior.work": {}
```

```json
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

# minecraft:block_sensor
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:block_sensor": {
    "sensor_radius": 16,
    "on_break": [
        {
            "block_list": [
                "minecraft:beehive",
                "minecraft:bee_nest"
            ],
            "on_block_broken": "hive_destroyed"
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:block_sensor": {
    "sensor_radius": 16,
    "on_break": [
        {
            "block_list": [
                "minecraft:gold_block",
                "minecraft:gilded_blackstone",
                "minecraft:nether_gold_ore",
                "minecraft:gold_ore",
                "minecraft:chest",
                "minecraft:trapped_chest",
                "minecraft:ender_chest",
                "minecraft:barrel",
                "minecraft:shulker_box",
                "minecraft:undyed_shulker_box"
            ],
            "on_block_broken": "important_block_destroyed_event"
        }
    ]
}
```

# minecraft:boostable
### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:boostable": {
    "speed_multiplier": 2.0,
    "duration": 3.0,
    "boost_items": [
        {
            "item": "carrotOnAStick",
            "damage": 2,
            "replace_item": "fishing_rod"
        }
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:boostable": {
    "speed_multiplier": 2.0,
    "duration": 16.0,
    "boost_items": [
        {
            "item": "warped_fungus_on_a_stick",
            "damage": 1,
            "replace_item": "fishing_rod"
        }
    ]
}
```

# minecraft:boss
### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:boss": {
    "should_darken_sky": false,
    "hud_range": 125
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:boss": {
    "should_darken_sky": true,
    "hud_range": 55
}
```

# minecraft:break_blocks
### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:break_blocks": {
    "breakable_blocks": [
        "bamboo",
        "bamboo_sapling",
        "beetroot",
        "brown_mushroom",
        "carrots",
        "carved_pumpkin",
        "chorus_flower",
        "chorus_plant",
        "deadbush",
        "double_plant",
        "leaves",
        "leaves2",
        "lit_pumpkin",
        "melon_block",
        "melon_stem",
        "potatoes",
        "pumpkin",
        "pumpkin_stem",
        "red_flower",
        "red_mushroom",
        "crimson_fungus",
        "warped_fungus",
        "reeds",
        "sapling",
        "snow_layer",
        "sweet_berry_bush",
        "tallgrass",
        "turtle_egg",
        "vine",
        "waterlily",
        "wheat",
        "yellow_flower"
    ]
}
```

# minecraft:breathable
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:breathable": {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 240,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false,
    "generates_bubbles": false
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:breathable": {
    "breathes_water": true
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:breathable": {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:breathable": {
    "breathes_water": true
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_lava": true
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": -1,
    "inhale_time": 3.75,
    "generates_bubbles": false
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:breathable": {
    "suffocate_time": 0,
    "total_supply": 15
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true,
    "breathes_air": true,
    "generates_bubbles": false
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

# minecraft:breedable
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:bee",
        "baby_type": "minecraft:bee",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:breedable": {
    "require_tame": true,
    "require_full_health": true,
    "allow_sitting": true,
    "breeds_with": {
        "mate_type": "minecraft:cat",
        "baby_type": "minecraft:cat",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:chicken",
        "baby_type": "minecraft:chicken",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ]
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:cow",
        "baby_type": "minecraft:cow",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:donkey",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "sweet_berries",
    "breeds_with": {
        "mate_type": "minecraft:fox",
        "baby_type": "minecraft:fox",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "love_filters": {
        "test": "has_component",
        "subject": "self",
        "operator": "!=",
        "value": "minecraft:attack_cooldown"
    },
    "breeds_with": {
        "mate_type": "minecraft:hoglin",
        "baby_type": "minecraft:hoglin",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "crimson_fungus"
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:horse",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "love_filters": {
        "test": "is_mark_variant",
        "subject": "self",
        "operator": "!=",
        "value": 1
    },
    "breeds_with": {
        "mate_type": "minecraft:llama",
        "baby_type": "minecraft:llama",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "hay_block"
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:mooshroom",
        "baby_type": "minecraft:mooshroom",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "deny_parents_variant": {
        "chance": 0.00098,
        "min_variant": 0,
        "max_variant": 1
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:ocelot",
        "baby_type": "minecraft:ocelot",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "blend_attributes": false,
    "environment_requirements": {
        "blocks": "bamboo",
        "count": 8,
        "radius": 5
    },
    "breed_items": "bamboo",
    "breeds_with": {
        "mate_type": "minecraft:panda",
        "baby_type": "minecraft:panda",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "mutation_factor": {
        "variant": 1.0
    }
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:pig",
        "baby_type": "minecraft:pig",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "carrot",
        "beetroot",
        "potato"
    ]
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:breedable": {
    "breed_items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ],
    "breeds_with": {
        "mate_type": "minecraft:rabbit",
        "baby_type": "minecraft:rabbit"
    },
    "require_tame": false,
    "mutation_factor": {
        "variant": 0.2
    }
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:sheep",
        "baby_type": "minecraft:sheep"
    },
    "breed_items": "wheat"
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:strider",
        "baby_type": "minecraft:strider",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "warped_fungus"
    ]
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:breedable": {
    "require_tame": false,
    "causes_pregnancy": true,
    "breeds_with": {
        "mate_type": "minecraft:turtle",
        "baby_type": "minecraft:turtle",
        "breed_event": {
            "event": "minecraft:become_pregnant",
            "target": "self"
        }
    },
    "breed_items": [
        "seagrass"
    ]
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:breedable": {
    "require_tame": true,
    "require_full_health": true,
    "breeds_with": {
        "mate_type": "minecraft:wolf",
        "baby_type": "minecraft:wolf",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "muttonRaw",
        "muttonCooked",
        "porkchop",
        "cooked_porkchop",
        "rabbit",
        "cooked_rabbit",
        "rotten_flesh"
    ]
}
```

# minecraft:bribeable
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:bribeable": {
    "bribe_items": [
        "fish",
        "salmon"
    ]
}
```

# minecraft:buoyant
### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ]
}
```

```json
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": false,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ],
    "drag_down_on_buoyancy_removed": 0.7
}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:buoyant": {
    "apply_gravity": false,
    "liquid_blocks": [
        "minecraft:flowing_water",
        "minecraft:water"
    ]
}
```

# minecraft:burns_in_daylight
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:burns_in_daylight": false
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:burns_in_daylight": {}
```

# minecraft:can_climb
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:can_climb": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:can_climb": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:can_climb": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:can_climb": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:can_climb": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:can_climb": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:can_climb": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:can_climb": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:can_climb": {}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:can_climb": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:can_climb": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:can_climb": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:can_climb": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:can_climb": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:can_climb": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:can_climb": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:can_climb": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:can_climb": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:can_climb": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:can_climb": {}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:can_climb": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:can_climb": {}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:can_climb": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:can_climb": {}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:can_climb": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:can_climb": {}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:can_climb": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:can_climb": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:can_climb": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:can_climb": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:can_climb": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:can_climb": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:can_climb": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:can_climb": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:can_climb": {}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:can_climb": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:can_climb": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:can_climb": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:can_climb": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:can_climb": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:can_climb": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:can_climb": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:can_climb": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:can_climb": {}
```

# minecraft:can_fly
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:can_fly": {}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:can_fly": {}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:can_fly": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:can_fly": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:can_fly": {}
```

# minecraft:can_power_jump
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:can_power_jump": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:can_power_jump": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:can_power_jump": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:can_power_jump": {}
```

# minecraft:celebrate_hunt
### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:celebrate_hunt": {
    "celebration_targets": {
        "all_of": [
            {
                "test": "is_family",
                "value": "hoglin"
            }
        ]
    },
    "broadcast": true,
    "duration": 10,
    "celebrate_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "radius": 16
}
```

# minecraft:collision_box
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.975
}
```

### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.5,
    "height": 0.9
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.55,
    "height": 0.5
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.8
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 0.455
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.7,
    "height": 0.5
}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.8
}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.8
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.6
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### dragon_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dragon_fireball.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### egg
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\egg.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.99,
    "height": 1.99
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 2.9
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.3
}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.98
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:collision_box": {
    "width": 13,
    "height": 4
}
```

### ender_pearl
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_pearl.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### eye_of_ender_signal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\eye_of_ender_signal.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### fireworks_rocket
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireworks_rocket.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.3
}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:collision_box": {
    "width": 4,
    "height": 4
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.85,
    "height": 0.85
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.85,
    "height": 0.85
}
```

```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.9
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 2.9
}
```

### lingering_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lingering_potion.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.87
}
```

### llama_spit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama_spit.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:collision_box": {
    "width": 2.08,
    "height": 2.08
}
```

```json
"minecraft:collision_box": {
    "width": 0.78,
    "height": 0.78
}
```

```json
"minecraft:collision_box": {
    "width": 0.52,
    "height": 0.52
}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 2.1
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.7,
    "height": 1.5
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.5
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.9
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.8
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.3,
    "height": 1.4
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.8,
    "height": 0.8
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.67,
    "height": 0.67
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:collision_box": {
    "height": 1.9,
    "width": 1.2
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.5,
    "height": 0.5
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### shulker_bullet
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker_bullet.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.625,
    "height": 0.625
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.3
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:collision_box": {
    "width": 2.08,
    "height": 2.08
}
```

```json
"minecraft:collision_box": {
    "width": 1.04,
    "height": 1.04
}
```

```json
"minecraft:collision_box": {
    "width": 0.52,
    "height": 0.52
}
```

### small_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\small_fireball.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### snowball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snowball.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.4,
    "height": 1.8
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 0.9
}
```

### splash_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\splash_potion.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.95,
    "height": 0.95
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.7
}
```

### thrown_trident
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\thrown_trident.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.35
}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.98
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.75,
    "height": 1.8
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.4
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.2
}
```

```json
"minecraft:collision_box": {
    "width": 1.2,
    "height": 0.4
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.8
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:collision_box": {
    "width": 1,
    "height": 3
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.72,
    "height": 2.01
}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.8
}
```

### xp_bottle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_bottle.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.85,
    "height": 0.85
}
```

```json
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.9
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

# minecraft:color
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:color": {
    "value": 14
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:color": {
    "value": 0
}
```

```json
"minecraft:color": {
    "value": 12
}
```

```json
"minecraft:color": {
    "value": 15
}
```

```json
"minecraft:color": {
    "value": 8
}
```

```json
"minecraft:color": {
    "value": 7
}
```

```json
"minecraft:color": {
    "value": 6
}
```

```json
"minecraft:color": {
    "value": 14
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:color": {
    "value": 0
}
```

```json
"minecraft:color": {
    "value": 1
}
```

```json
"minecraft:color": {
    "value": 2
}
```

```json
"minecraft:color": {
    "value": 3
}
```

```json
"minecraft:color": {
    "value": 4
}
```

```json
"minecraft:color": {
    "value": 5
}
```

```json
"minecraft:color": {
    "value": 6
}
```

```json
"minecraft:color": {
    "value": 7
}
```

```json
"minecraft:color": {
    "value": 8
}
```

```json
"minecraft:color": {
    "value": 9
}
```

```json
"minecraft:color": {
    "value": 10
}
```

```json
"minecraft:color": {
    "value": 11
}
```

```json
"minecraft:color": {
    "value": 12
}
```

```json
"minecraft:color": {
    "value": 13
}
```

```json
"minecraft:color": {
    "value": 14
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:color": {
    "value": 14
}
```

# minecraft:color2
### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:color2": {
    "value": 0
}
```

```json
"minecraft:color2": {
    "value": 1
}
```

```json
"minecraft:color2": {
    "value": 2
}
```

```json
"minecraft:color2": {
    "value": 3
}
```

```json
"minecraft:color2": {
    "value": 4
}
```

```json
"minecraft:color2": {
    "value": 5
}
```

```json
"minecraft:color2": {
    "value": 6
}
```

```json
"minecraft:color2": {
    "value": 7
}
```

```json
"minecraft:color2": {
    "value": 8
}
```

```json
"minecraft:color2": {
    "value": 9
}
```

```json
"minecraft:color2": {
    "value": 10
}
```

```json
"minecraft:color2": {
    "value": 11
}
```

```json
"minecraft:color2": {
    "value": 12
}
```

```json
"minecraft:color2": {
    "value": 13
}
```

```json
"minecraft:color2": {
    "value": 14
}
```

# minecraft:conditional_bandwidth_optimization
### area_effect_cloud
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\area_effect_cloud.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "use_motion_prediction_hints": true,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### egg
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\egg.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ender_pearl
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_pearl.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### eye_of_ender_signal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\eye_of_ender_signal.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### fireworks_rocket
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireworks_rocket.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### lightning_bolt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lightning_bolt.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### lingering_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lingering_potion.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### llama_spit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama_spit.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### shulker_bullet
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker_bullet.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### small_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\small_fireball.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### snowball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snowball.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 100.0,
        "max_dropped_ticks": 5,
        "use_motion_prediction_hints": true
    }
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### splash_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\splash_potion.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### thrown_trident
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\thrown_trident.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 60.0,
        "max_dropped_ticks": 20,
        "use_motion_prediction_hints": true
    },
    "conditional_values": [
        {
            "max_optimized_distance": 0.0,
            "max_dropped_ticks": 0,
            "conditional_values": [
                {
                    "test": "is_moving",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                }
            ]
        }
    ]
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### xp_bottle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_bottle.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 10,
        "use_motion_prediction_hints": true
    }
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:conditional_bandwidth_optimization": {}
```

# minecraft:custom_hit_test
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 1.0,
            "height": 0.85,
            "pivot": [
                0,
                0.5,
                0
            ]
        }
    ]
}
```

```json
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 2.0,
            "height": 1.75,
            "pivot": [
                0,
                1,
                0
            ]
        }
    ]
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 1.0,
            "height": 0.85,
            "pivot": [
                0,
                0.5,
                0
            ]
        }
    ]
}
```

```json
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 2.0,
            "height": 1.75,
            "pivot": [
                0,
                1,
                0
            ]
        }
    ]
}
```

# minecraft:damage_over_time
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:damage_over_time": {
    "damage_per_hurt": 1,
    "time_between_hurt": 0
}
```

# minecraft:damage_sensor
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            },
            "event": "minecraft:become_charged"
        },
        "deals_damage": false
    }
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_block",
                    "subject": "block",
                    "value": "minecraft:sweet_berry_bush"
                }
            },
            "deals_damage": false
        }
    ]
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": true,
        "on_damage": {
            "filters": {
                "test": "in_caravan",
                "value": false
            },
            "event": "minecraft:become_angry"
        }
    }
}
```

```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": true
    }
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 0
                        }
                    ]
                },
                "event": "minecraft:become_brown"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        },
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        }
                    ]
                },
                "event": "minecraft:become_red"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        }
    ]
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": false
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                {
                    "test": "is_difficulty",
                    "operator": "!=",
                    "value": "peaceful"
                }
            ],
            "event": "become_zombie"
        },
        "deals_damage": false
    }
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "other_with_families": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "lightning",
        "deals_damage": true,
        "damage_multiplier": 2000.0
    }
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "lightning"
                    },
                    {
                        "test": "is_difficulty",
                        "operator": "!=",
                        "value": "peaceful"
                    }
                ],
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": [
        {
            "cause": "entity_attack",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "projectile",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "magic",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        }
    ]
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "undead"
            }
        },
        "deals_damage": false
    }
}
```

# minecraft:despawn
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {
        "min_distance": 32,
        "max_distance": 40
    }
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:despawn": {
    "filters": {
        "any_of": [
            {
                "all_of": [
                    {
                        "test": "is_persistent",
                        "value": false
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 54
                    }
                ]
            },
            {
                "all_of": [
                    {
                        "test": "is_persistent",
                        "value": false
                    },
                    {
                        "test": "inactivity_timer",
                        "subject": "self",
                        "value": 30
                    },
                    {
                        "test": "random_chance",
                        "value": 800
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 32
                    }
                ]
            }
        ]
    }
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {
        "min_distance": 32,
        "max_distance": 40
    }
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {
        "min_distance": 32,
        "max_distance": 40
    }
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {
        "min_distance": 32,
        "max_distance": 40
    }
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:despawn": {
    "remove_child_entities": true,
    "filters": {
        "all_of": [
            {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "self",
                        "value": "wandering_trader_despawning"
                    },
                    {
                        "test": "has_trade_supply",
                        "subject": "self",
                        "value": false
                    }
                ]
            },
            {
                "test": "distance_to_nearest_player",
                "operator": ">",
                "value": 24
            }
        ]
    }
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:despawn": {
    "filters": {
        "any_of": [
            {
                "all_of": [
                    {
                        "test": "is_persistent",
                        "value": false
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 54
                    }
                ]
            },
            {
                "all_of": [
                    {
                        "test": "is_persistent",
                        "value": false
                    },
                    {
                        "test": "inactivity_timer",
                        "subject": "self",
                        "value": 30
                    },
                    {
                        "test": "random_chance",
                        "value": 800
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 32
                    }
                ]
            }
        ]
    }
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

# minecraft:dweller
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "passive",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "defender",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "farmer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "fisherman",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "shepherd",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "fletcher",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "librarian",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "cartographer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "cleric",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "armorer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "weaponsmith",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "toolsmith",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "butcher",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "leatherworker",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "mason",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

# minecraft:economy_trade_table
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:economy_trade_table": {}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/economy_trades/farmer_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/economy_trades/fisherman_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.shepherd",
    "table": "trading/economy_trades/shepherd_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.fletcher",
    "table": "trading/economy_trades/fletcher_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.librarian",
    "table": "trading/economy_trades/librarian_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.cartographer",
    "table": "trading/economy_trades/cartographer_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.cleric",
    "table": "trading/economy_trades/cleric_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.armor",
    "table": "trading/economy_trades/armorer_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.weapon",
    "table": "trading/economy_trades/weapon_smith_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.tool",
    "table": "trading/economy_trades/tool_smith_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.butcher",
    "table": "trading/economy_trades/butcher_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.leather",
    "table": "trading/economy_trades/leather_worker_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

```json
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.mason",
    "table": "trading/economy_trades/stone_mason_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -100,
        -100
    ],
    "max_cured_discount": [
        -500,
        -500
    ]
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:economy_trade_table": {
    "display_name": "entity.wandering_trader.name",
    "table": "trading/economy_trades/wandering_trader_trades.json",
    "new_screen": true
}
```

# minecraft:entity_sensor
### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:entity_sensor": {
    "sensor_range": 2.5,
    "relative_range": false,
    "minimum_count": 1,
    "event_filters": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "mob"
            },
            {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "none_of": {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    }
                ]
            }
        ]
    },
    "event": "minecraft:start_half_puff"
}
```

```json
"minecraft:entity_sensor": {
    "sensor_range": 2.5,
    "relative_range": false,
    "minimum_count": 1,
    "event_filters": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "mob"
            },
            {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "none_of": {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    }
                ]
            }
        ]
    },
    "event": "minecraft:start_full_puff"
}
```

```json
"minecraft:entity_sensor": {
    "sensor_range": 2.9,
    "relative_range": false,
    "require_all": true,
    "event_filters": {
        "none_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "mob"
            },
            {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "none_of": {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    }
                ]
            }
        ],
        "test": "distance_to_nearest_player",
        "operator": ">",
        "value": 2.9
    },
    "event": "minecraft:from_full_puff"
}
```

# minecraft:environment_sensor
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "event": "seek_shelter",
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": false
                            },
                            {
                                "test": "weather",
                                "operator": "==",
                                "value": "precipitation"
                            }
                        ]
                    },
                    {
                        "test": "has_component",
                        "value": "minecraft:is_charged",
                        "operator": "!="
                    },
                    {
                        "test": "has_biome_tag",
                        "value": "overworld"
                    }
                ]
            }
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "event": "abort_sheltering",
            "filters": {
                "all_of": [
                    {
                        "test": "weather",
                        "operator": "==",
                        "value": "clear"
                    },
                    {
                        "test": "is_daytime",
                        "value": true
                    }
                ]
            }
        }
    ]
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": "<",
            "value": 0.49
        },
        "event": "minecraft:become_hostile"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": ">",
            "value": 0.49
        },
        "event": "minecraft:become_neutral"
    }
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    },
                    {
                        "test": "in_water",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "event": "navigation_on_land"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "event": "stop_dryingout"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water",
                "operator": "==",
                "value": true
            },
            "event": "navigation_off_land"
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "!=",
                "value": true
            },
            "event": "start_dryingout"
        }
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_daytime",
                "value": false
            },
            "event": "minecraft:fox_configure_night"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": true
            },
            "event": "minecraft:fox_configure_day"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": true
                    },
                    {
                        "test": "has_target",
                        "operator": "==",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_docile_day"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": false
                    },
                    {
                        "test": "has_target",
                        "operator": "==",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_docile_night"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "weather_at_position",
                        "operator": "!=",
                        "value": "thunderstorm"
                    },
                    {
                        "test": "is_daytime",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:fox_configure_day"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "weather_at_position",
                        "operator": "!=",
                        "value": "thunderstorm"
                    },
                    {
                        "test": "is_daytime",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_night"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "weather_at_position",
                "value": "thunderstorm"
            },
            "event": "minecraft:fox_configure_thunderstorm"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": false
            },
            "event": "minecraft:fox_configure_night"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "weather_at_position",
                "value": "thunderstorm"
            },
            "event": "minecraft:fox_configure_thunderstorm"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": true
            },
            "event": "minecraft:fox_configure_day"
        }
    ]
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "start_zombification_event"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "stop_zombification_event"
    }
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:start_transforming"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:stop_transforming"
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "all_of": [
                {
                    "test": "is_leashed",
                    "subject": "self",
                    "value": false
                },
                {
                    "test": "has_component",
                    "subject": "self",
                    "operator": "!=",
                    "value": "minecraft:is_tamed"
                }
            ]
        },
        "event": "minecraft:on_tame"
    }
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "start_zombification_event"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "stop_zombification_event"
    }
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "start_zombification_event"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_nether",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "stop_zombification_event"
    }
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_water",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:ranged_mode"
    }
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "all_of": [
                {
                    "test": "has_mob_effect",
                    "subject": "self",
                    "value": "bad_omen"
                },
                {
                    "test": "is_in_village",
                    "subject": "self",
                    "value": true
                }
            ]
        },
        "event": "minecraft:trigger_raid"
    }
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:melee_mode"
        },
        {
            "filters": {
                "test": "has_ranged_weapon",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            "event": "minecraft:melee_mode"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "in_water",
                        "subject": "self",
                        "operator": "==",
                        "value": false
                    },
                    {
                        "test": "has_ranged_weapon",
                        "subject": "self",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:ranged_mode"
        }
    ]
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": "<",
            "value": 0.49
        },
        "event": "minecraft:become_hostile"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": ">",
            "value": 0.49
        },
        "event": "minecraft:become_neutral"
    }
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:melee_mode"
        },
        {
            "filters": {
                "test": "has_ranged_weapon",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            "event": "minecraft:melee_mode"
        }
    ]
}
```

```json
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "in_water",
                        "subject": "self",
                        "operator": "==",
                        "value": false
                    },
                    {
                        "test": "has_ranged_weapon",
                        "subject": "self",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:ranged_mode"
        }
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "any_of": [
                {
                    "test": "in_lava",
                    "subject": "self",
                    "operator": "==",
                    "value": true
                },
                {
                    "test": "in_lava",
                    "subject": "other",
                    "operator": "==",
                    "value": true
                }
            ]
        },
        "event": "stop_suffocating"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "all_of": [
                {
                    "test": "in_lava",
                    "subject": "self",
                    "operator": "==",
                    "value": false
                },
                {
                    "any_of": [
                        {
                            "test": "is_riding",
                            "subject": "self",
                            "operator": "==",
                            "value": false
                        },
                        {
                            "test": "in_lava",
                            "subject": "other",
                            "operator": "==",
                            "value": false
                        }
                    ]
                }
            ]
        },
        "event": "start_suffocating"
    }
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```json
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:stop_transforming"
    }
}
```

# minecraft:equip_item
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:equip_item": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:equip_item": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:equip_item": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:equip_item": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:equip_item": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:equip_item": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:equip_item": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:equip_item": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:equip_item": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:equip_item": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:equip_item": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:equip_item": {}
```

# minecraft:equipment
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_ranged_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

```json
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/fox_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.mainhand",
            "drop_chance": 1.0
        }
    ]
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_gear_ranged.json"
}
```

```json
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_gear_melee.json"
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_brute_gear.json"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/pillager_gear.json"
}
```

```json
"minecraft:equipment": {
    "table": "loot_tables/entities/pillager_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/vex_gear.json"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/vindicator_gear.json"
}
```

```json
"minecraft:equipment": {
    "table": "loot_tables/entities/vindicator_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/wither_skeleton_gear.json"
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_pigman_gear.json"
}
```

```json
"minecraft:equipment": {
    "table": "loot_tables/entities/zombified_piglin_rider_gear.json"
}
```

# minecraft:equippable
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:donkey_saddled"
            },
            "on_unequip": {
                "event": "minecraft:donkey_unsaddled"
            }
        }
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:horse_saddled"
            },
            "on_unequip": {
                "event": "minecraft:horse_unsaddled"
            }
        },
        {
            "slot": 1,
            "item": "horsearmoriron",
            "accepted_items": [
                "horsearmorleather",
                "horsearmoriron",
                "horsearmorgold",
                "horsearmordiamond"
            ]
        }
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:equippable": {
    "slots": [
        {
            "slot": 1,
            "item": "carpet",
            "accepted_items": [
                "carpet"
            ]
        }
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:mule_saddled"
            },
            "on_unequip": {
                "event": "minecraft:mule_unsaddled"
            }
        }
    ]
}
```

# minecraft:experience_reward
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 3 : 0"
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "10"
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 1 + (query.equipment_count * Math.Random(1,2)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 20 : 0"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "Math.Min(query.player_level * 7, 100)"
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 20 : 0"
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "!query.is_baby && query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "50"
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

# minecraft:explode
### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": true,
    "fire_affected_by_griefing": true,
    "destroy_affected_by_griefing": true
}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

```json
"minecraft:explode": {
    "fuse_length": {
        "range_min": 0.5,
        "range_max": 2.0
    },
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

```json
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": false,
    "max_resistance": 4.0,
    "destroy_affected_by_griefing": true
}
```

# minecraft:fire_immune
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:fire_immune": {}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:fire_immune": true
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:fire_immune": true
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:fire_immune": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:fire_immune": {}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:fire_immune": true
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:fire_immune": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:fire_immune": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:fire_immune": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:fire_immune": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:fire_immune": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:fire_immune": {}
```

# minecraft:flocking
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:flocking": {
    "in_water": false,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 6.0,
    "breach_influence": 0.0,
    "separation_weight": 1.75,
    "separation_threshold": 3.0,
    "cohesion_weight": 1.85,
    "cohesion_threshold": 6.5,
    "innner_cohesion_threshold": 3.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.0
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.25,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.75
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:flocking": {
    "in_water": true,
    "match_variants": true,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.75,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

# minecraft:flying_speed
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:flying_speed": {
    "value": 0.15
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:flying_speed": {
    "value": 0.6
}
```

# minecraft:follow_range
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:follow_range": {
    "value": 1024
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:follow_range": {
    "value": 16,
    "max": 16
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:follow_range": {
    "value": 32,
    "max": 32
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:follow_range": {
    "value": 64,
    "max": 64
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:follow_range": {
    "value": 16,
    "max": 16
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:follow_range": {
    "value": 40,
    "max": 40
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:follow_range": {
    "value": 64,
    "max": 64
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:follow_range": {
    "value": 48
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:follow_range": {
    "value": 1024
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:follow_range": {
    "value": 128
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:follow_range": {
    "value": 64
}
```

# minecraft:genetics
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:genetics": {
    "mutation_rate": 0.03125,
    "genes": [
        {
            "name": "panda_variant",
            "allele_range": {
                "range_min": 0,
                "range_max": 15
            },
            "genetic_variants": [
                {
                    "main_allele": 0,
                    "birth_event": {
                        "event": "minecraft:panda_lazy",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 1,
                    "birth_event": {
                        "event": "minecraft:panda_worried",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 2,
                    "birth_event": {
                        "event": "minecraft:panda_playful",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 3,
                    "birth_event": {
                        "event": "minecraft:panda_aggressive",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 4,
                        "range_max": 7
                    },
                    "birth_event": {
                        "event": "minecraft:panda_weak",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 8,
                        "range_max": 9
                    },
                    "birth_event": {
                        "event": "minecraft:panda_brown",
                        "target": "self"
                    }
                }
            ]
        }
    ]
}
```

# minecraft:giveable
```json
"minecraft:giveable": {
    "triggers": {
        "cooldown": 3.0,
        "items": [
            "bamboo",
            "cake"
        ],
        "on_give": {
            "event": "minecraft:on_calm",
            "target": "self"
        }
    }
}
```

# minecraft:group_size
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:group_size": {
    "radius": 32,
    "filters": {
        "all_of": [
            {
                "test": "has_component",
                "operator": "!=",
                "value": "minecraft:is_baby"
            },
            {
                "test": "is_family",
                "value": "hoglin"
            }
        ]
    }
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:group_size": {
    "radius": 32,
    "filters": {
        "all_of": [
            {
                "test": "has_component",
                "operator": "!=",
                "value": "minecraft:is_baby"
            },
            {
                "test": "is_family",
                "value": "piglin"
            }
        ]
    }
}
```

# minecraft:grows_crop
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:grows_crop": {
    "charges": 10,
    "chance": 0.03
}
```

# minecraft:healable
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "fish",
            "heal_amount": 2
        },
        {
            "item": "salmon",
            "heal_amount": 2
        }
    ]
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "hay_block",
            "heal_amount": 10
        }
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:healable": {
    "force_use": true,
    "filters": {
        "test": "is_riding",
        "operator": "!=",
        "value": true
    },
    "items": [
        {
            "item": "cookie",
            "heal_amount": 0,
            "effects": [
                {
                    "name": "fatal_poison",
                    "chance": 1.0,
                    "duration": 1000,
                    "amplifier": 0
                }
            ]
        }
    ]
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:healable": {
    "items": [
        {
            "item": "porkchop",
            "heal_amount": 3
        },
        {
            "item": "cooked_porkchop",
            "heal_amount": 8
        },
        {
            "item": "fish",
            "heal_amount": 2
        },
        {
            "item": "salmon",
            "heal_amount": 2
        },
        {
            "item": "clownfish",
            "heal_amount": 1
        },
        {
            "item": "pufferfish",
            "heal_amount": 1
        },
        {
            "item": "cooked_fish",
            "heal_amount": 5
        },
        {
            "item": "cooked_salmon",
            "heal_amount": 6
        },
        {
            "item": "beef",
            "heal_amount": 3
        },
        {
            "item": "cooked_beef",
            "heal_amount": 8
        },
        {
            "item": "chicken",
            "heal_amount": 2
        },
        {
            "item": "cooked_chicken",
            "heal_amount": 6
        },
        {
            "item": "muttonRaw",
            "heal_amount": 2
        },
        {
            "item": "muttonCooked",
            "heal_amount": 6
        },
        {
            "item": "rotten_flesh",
            "heal_amount": 4
        },
        {
            "item": "rabbit",
            "heal_amount": 3
        },
        {
            "item": "cooked_rabbit",
            "heal_amount": 5
        },
        {
            "item": "rabbit_stew",
            "heal_amount": 10
        }
    ]
}
```

# minecraft:health
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:health": {
    "value": 12,
    "max": 12
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:health": {
    "value": 80,
    "max": 80
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:health": {
    "value": 40,
    "max": 40
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:health": {
    "value": 200,
    "max": 200
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:health": {
    "value": 30,
    "max": 30
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:health": {
    "value": 40,
    "max": 40
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:health": {
    "value": 100,
    "max": 100
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

```json
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

```json
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:health": {
    "value": 50,
    "max": 50
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:health": {
    "value": 30
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:health": {
    "value": 3,
    "max": 3
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:health": {
    "max": 100,
    "value": 100
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:health": {
    "value": 30,
    "max": 30
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:health": {
    "value": 15,
    "max": 15
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

```json
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

```json
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:health": {
    "value": 30
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:health": {
    "value": 14,
    "max": 14
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:health": {
    "value": 26,
    "max": 26
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:health": {
    "value": 600,
    "max": 600
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:health": {
    "value": 5,
    "max": 5
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:health": {
    "value": 40,
    "max": 40
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:health": {
    "value": 15,
    "max": 15
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

# minecraft:hide
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:hide": {}
```

# minecraft:home
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:home": {
    "restriction_radius": 22,
    "home_block_list": [
        "minecraft:bee_nest",
        "minecraft:beehive"
    ]
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:home": {
    "restriction_radius": 16
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:home": {
    "restriction_radius": 16
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:home": {}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:home": {}
```

# minecraft:horse.jump_strength
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

# minecraft:hurt_on_condition
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "cause": "none",
            "damage_per_tick": 999
        }
    ]
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        },
        {
            "filters": {
                "test": "is_temperature_value",
                "operator": ">",
                "value": 1.0
            },
            "cause": "temperature",
            "damage_per_tick": 1
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

# minecraft:input_ground_controlled
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:input_ground_controlled": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:input_ground_controlled": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:input_ground_controlled": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:input_ground_controlled": {}
```

# minecraft:inside_block_notifier
### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:inside_block_notifier": {
    "block_list": [
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": true
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_down",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        },
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": false
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_up",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        }
    ]
}
```

# minecraft:insomnia
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:insomnia": {
    "days_until_insomnia": 3
}
```

# minecraft:interact
### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "bucket:0"
                        }
                    ]
                }
            },
            "use_item": true,
            "transform_to_item": "bucket:1",
            "play_sounds": "milk",
            "interact_text": "action.interact.milk"
        }
    ]
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "flint_and_steel"
                    },
                    {
                        "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:explode"
                    }
                ]
            },
            "event": "minecraft:start_exploding_forced",
            "target": "self"
        },
        "hurt_item": 1,
        "swing": true,
        "play_sounds": "ignite",
        "interact_text": "action.interact.creeper"
    }
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "chest"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "chest"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "bowl"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        }
                    ]
                },
                "event": "minecraft:flowerless",
                "target": "self"
            },
            "add_items": {
                "table": "loot_tables/gameplay/entities/mooshroom_milking.json"
            },
            "use_item": true,
            "play_sounds": "milk_suspiciously",
            "interact_text": "action.interact.moostew"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:2"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 7
                        }
                    ]
                },
                "event": "minecraft:ate_allium",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:3"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 3
                        }
                    ]
                },
                "event": "minecraft:ate_bluet",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:1"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 6
                        }
                    ]
                },
                "event": "minecraft:ate_orchid",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:9"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 1
                        }
                    ]
                },
                "event": "minecraft:ate_cornflower",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "yellow_flower"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 5
                        }
                    ]
                },
                "event": "minecraft:ate_dandelion",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:10"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 4
                        }
                    ]
                },
                "event": "minecraft:ate_lily",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:8"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 8
                        }
                    ]
                },
                "event": "minecraft:ate_daisy",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:0"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 0
                        }
                    ]
                },
                "event": "minecraft:ate_poppy",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:4"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:5"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:6"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:7"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 2
                        }
                    ]
                },
                "event": "minecraft:ate_tulip",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "wither_rose"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 9
                        }
                    ]
                },
                "event": "minecraft:ate_rose",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 0
                        }
                    ]
                },
                "event": "become_cow",
                "target": "self"
            },
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "spawn_items": {
                "table": "loot_tables/entities/mooshroom_shear.json"
            },
            "particle_on_start": {
                "particle_type": "largeexplode",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.mooshear"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        }
                    ]
                },
                "event": "become_cow",
                "target": "self"
            },
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "spawn_items": {
                "table": "loot_tables/entities/brown_mooshroom_shear.json"
            },
            "particle_on_start": {
                "particle_type": "largeexplode",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.mooshear"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "bucket:0"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                }
            },
            "use_item": true,
            "transform_to_item": "bucket:1",
            "play_sounds": "milk",
            "interact_text": "action.interact.milk"
        }
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "chest"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "test": "has_equipment",
                    "subject": "other",
                    "domain": "hand",
                    "value": "saddle"
                },
                "event": "minecraft:on_saddled"
            },
            "use_item": true,
            "play_sounds": "saddle",
            "interact_text": "action.interact.saddle"
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "gold_ingot"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "subject": "self",
                            "operator": "!=",
                            "value": "minecraft:is_baby"
                        }
                    ]
                }
            },
            "barter": true,
            "admire": true,
            "use_item": true,
            "cooldown_after_being_attacked": 20,
            "interact_text": "action.interact.barter"
        }
    ]
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "cooldown": 2.5,
            "use_item": false,
            "hurt_item": 1,
            "spawn_items": {
                "table": "loot_tables/entities/sheep_shear.json"
            },
            "play_sounds": "shear",
            "interact_text": "action.interact.shear",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:is_baby"
                        },
                        {
                            "test": "has_component",
                            "value": "minecraft:is_dyeable"
                        }
                    ]
                },
                "event": "minecraft:on_sheared",
                "target": "self"
            }
        }
    ]
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:0"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:16"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_black"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:8"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_gray"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:7"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_silver"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:15"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:19"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_white"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:12"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_light_blue"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:14"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_orange"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:1"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_red"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:4"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:18"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_blue"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:5"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_purple"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:13"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_magenta"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:9"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_pink"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:3"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:17"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_brown"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:11"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_yellow"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:10"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_lime"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:2"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_green"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:6"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_cyan"
            },
            "use_item": true
        }
    ]
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "cooldown": 2.5,
            "use_item": false,
            "hurt_item": 1,
            "spawn_items": {
                "table": "loot_tables/entities/snow_golem_shear.json"
            },
            "play_sounds": "shear",
            "interact_text": "action.interact.shear",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:is_sheared"
                        }
                    ]
                },
                "event": "minecraft:on_sheared",
                "target": "self"
            }
        }
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "test": "has_equipment",
                    "subject": "other",
                    "domain": "hand",
                    "value": "saddle"
                },
                "event": "minecraft:on_saddled"
            },
            "use_item": true,
            "play_sounds": "saddle",
            "interact_text": "action.interact.saddle"
        }
    ]
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "fireball:0"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "flint_and_steel"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_game_rule",
                            "domain": "tntexplodes",
                            "operator": "==",
                            "value": true
                        }
                    ]
                },
                "event": "minecraft:on_prime",
                "target": "self"
            },
            "swing": true,
            "play_sounds": "ignite",
            "interact_text": "action.interact.creeper"
        },
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_component",
                            "subject": "other",
                            "value": "fire_aspect"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_game_rule",
                            "domain": "tntexplodes",
                            "operator": "==",
                            "value": true
                        }
                    ]
                },
                "event": "minecraft:on_prime",
                "target": "self"
            },
            "swing": true,
            "interact_text": "action.interact.creeper"
        }
    ]
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "golden_apple"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "value": "minecraft:effect.weakness"
                    }
                ]
            },
            "event": "villager_converted",
            "target": "self"
        },
        "use_item": true,
        "interact_text": "action.interact.cure"
    }
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "golden_apple"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "value": "minecraft:effect.weakness"
                    }
                ]
            },
            "event": "villager_converted",
            "target": "self"
        },
        "use_item": true,
        "interact_text": "action.interact.cure"
    }
}
```

# minecraft:inventory
### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:inventory": {
    "container_type": "minecart_chest",
    "inventory_size": 27,
    "can_be_siphoned_from": true
}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:inventory": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:inventory": {
    "container_type": "minecart_hopper",
    "inventory_size": 5,
    "can_be_siphoned_from": true
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 2,
    "container_type": "horse"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse",
    "additional_slots_per_strength": 3
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 1,
    "private": true
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 8
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 8,
    "private": true
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:inventory": {
    "inventory_size": 8,
    "private": true
}
```

# minecraft:is_baby
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:is_baby": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:is_baby": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:is_baby": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:is_baby": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:is_baby": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:is_baby": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:is_baby": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:is_baby": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:is_baby": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:is_baby": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:is_baby": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:is_baby": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:is_baby": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:is_baby": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:is_baby": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:is_baby": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:is_baby": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:is_baby": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:is_baby": {}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:is_baby": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:is_baby": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:is_baby": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:is_baby": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:is_baby": {}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:is_baby": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:is_baby": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:is_baby": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:is_baby": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:is_baby": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:is_baby": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:is_baby": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:is_baby": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:is_baby": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:is_baby": {}
```

# minecraft:is_charged
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:is_charged": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:is_charged": {}
```

# minecraft:is_chested
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:is_chested": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:is_chested": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:is_chested": {}
```

# minecraft:is_dyeable
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

# minecraft:is_hidden_when_invisible
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:is_hidden_when_invisible": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:is_hidden_when_invisible": {}
```

# minecraft:is_ignited
### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:is_ignited": {}
```

# minecraft:is_illager_captain
### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:is_illager_captain": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:is_illager_captain": {}
```

# minecraft:is_saddled
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:is_saddled": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:is_saddled": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:is_saddled": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:is_saddled": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:is_saddled": {}
```

# minecraft:is_shaking
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:is_shaking": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:is_shaking": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:is_shaking": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:is_shaking": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:is_shaking": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:is_shaking": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:is_shaking": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:is_shaking": {}
```

# minecraft:is_sheared
### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:is_sheared": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:is_sheared": {}
```

# minecraft:is_stackable
### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:is_stackable": {}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:is_stackable": {
    "value": true
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:is_stackable": {}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:is_stackable": {}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:is_stackable": {}
```

# minecraft:is_stunned
### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:is_stunned": {}
```

# minecraft:is_tamed
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:is_tamed": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:is_tamed": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:is_tamed": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:is_tamed": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:is_tamed": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:is_tamed": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:is_tamed": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:is_tamed": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:is_tamed": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:is_tamed": {}
```

# minecraft:item_controllable
### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:item_controllable": {
    "control_items": "carrotOnAStick"
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:item_controllable": {
    "control_items": "warped_fungus_on_a_stick"
}
```

# minecraft:item_hopper
### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:item_hopper": {}
```

# minecraft:jump.dynamic
### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:jump.dynamic": {}
```

# minecraft:jump.static
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:jump.static": {}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:jump.static": {}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:jump.static": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:jump.static": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:jump.static": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:jump.static": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:jump.static": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:jump.static": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:jump.static": {
    "jump_power": 0.6
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:jump.static": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:jump.static": {}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:jump.static": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:jump.static": {}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:jump.static": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:jump.static": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:jump.static": {}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:jump.static": {}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:jump.static": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:jump.static": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:jump.static": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:jump.static": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:jump.static": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:jump.static": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:jump.static": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:jump.static": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:jump.static": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:jump.static": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:jump.static": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:jump.static": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:jump.static": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:jump.static": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:jump.static": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:jump.static": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:jump.static": {}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:jump.static": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:jump.static": {}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:jump.static": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:jump.static": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:jump.static": {}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:jump.static": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:jump.static": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:jump.static": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:jump.static": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:jump.static": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:jump.static": {}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:jump.static": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:jump.static": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:jump.static": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:jump.static": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:jump.static": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:jump.static": {}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:jump.static": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:jump.static": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:jump.static": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:jump.static": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:jump.static": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:jump.static": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:jump.static": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:jump.static": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:jump.static": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:jump.static": {}
```

# minecraft:knockback_resistance
### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:knockback_resistance": {
    "value": 100,
    "max": 100
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:knockback_resistance": {
    "value": 0.5
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:knockback_resistance": {
    "value": 1.0
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:knockback_resistance": {
    "value": 0.5
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:knockback_resistance": {
    "value": 0.5
}
```

# minecraft:lava_movement
### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:lava_movement": {
    "value": 0.32
}
```

# minecraft:leashable
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "can_be_stolen": true
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
    },
    "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
    }
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
    },
    "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
    }
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

# minecraft:lookat
### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:lookat": {
    "search_radius": 64.0,
    "set_target": true,
    "look_cooldown": 5.0,
    "filters": {
        "all_of": [
            {
                "subject": "other",
                "test": "is_family",
                "value": "player"
            },
            {
                "test": "has_equipment",
                "domain": "head",
                "subject": "other",
                "operator": "not",
                "value": "carved_pumpkin"
            }
        ]
    }
}
```

# minecraft:loot
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/armor_stand.json"
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/blaze.json"
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/boat.json"
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/cat.json"
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/spider.json"
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/chicken.json"
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/cow.json"
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/creeper.json"
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/dolphin.json"
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/drowned.json"
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/elder_guardian.json"
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/enderman.json"
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/evocation_illager.json"
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/fish.json"
}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/gameplay/fishing.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/gameplay/jungle_fishing.json"
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/fox.json"
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/ghast.json"
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/guardian.json"
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/hoglin.json"
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/iron_golem.json"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/llama.json"
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/magma_cube.json"
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/mooshroom.json"
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/empty.json"
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/ocelot.json"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/panda.json"
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/parrot.json"
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/phantom.json"
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/pig.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/pig_saddled.json"
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/piglin.json"
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/piglin.json"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/pillager.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/pillager_raid.json"
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/empty.json"
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/polar_bear.json"
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/pufferfish.json"
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/rabbit.json"
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/ravager.json"
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/salmon_normal.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/salmon_large.json"
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/sheep_sheared.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/sheep.json"
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/shulker.json"
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/silverfish.json"
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/skeleton.json"
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/skeleton_horse.json"
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/slime.json"
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/snowman.json"
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/spider.json"
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/squid.json"
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/stray.json"
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/strider_saddled.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/strider.json"
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/empty.json"
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/tropicalfish.json"
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/sea_turtle.json"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/vindication_illager.json"
}
```

```json
"minecraft:loot": {
    "table": "loot_tables/entities/vindicator_raid.json"
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/witch.json"
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/wither_boss.json"
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/wither_skeleton.json"
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/wolf.json"
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zoglin.json"
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie_horse.json"
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie_pigman.json"
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

# minecraft:managed_wandering_trader
### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:managed_wandering_trader": {}
```

# minecraft:mark_variant
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:mark_variant": {
    "value": 1
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:mark_variant": {
    "value": 0
}
```

```json
"minecraft:mark_variant": {
    "value": 1
}
```

```json
"minecraft:mark_variant": {
    "value": 2
}
```

```json
"minecraft:mark_variant": {
    "value": 3
}
```

```json
"minecraft:mark_variant": {
    "value": 4
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:mark_variant": {
    "value": 0
}
```

```json
"minecraft:mark_variant": {
    "value": 1
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:mark_variant": {
    "value": -1
}
```

```json
"minecraft:mark_variant": {
    "value": 0
}
```

```json
"minecraft:mark_variant": {
    "value": 1
}
```

```json
"minecraft:mark_variant": {
    "value": 2
}
```

```json
"minecraft:mark_variant": {
    "value": 3
}
```

```json
"minecraft:mark_variant": {
    "value": 4
}
```

```json
"minecraft:mark_variant": {
    "value": 5
}
```

```json
"minecraft:mark_variant": {
    "value": 6
}
```

```json
"minecraft:mark_variant": {
    "value": 7
}
```

```json
"minecraft:mark_variant": {
    "value": 8
}
```

```json
"minecraft:mark_variant": {
    "value": 9
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:mark_variant": {
    "value": 0
}
```

```json
"minecraft:mark_variant": {
    "value": 1
}
```

```json
"minecraft:mark_variant": {
    "value": 2
}
```

```json
"minecraft:mark_variant": {
    "value": 3
}
```

```json
"minecraft:mark_variant": {
    "value": 4
}
```

```json
"minecraft:mark_variant": {
    "value": 5
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:mark_variant": {
    "value": 0
}
```

```json
"minecraft:mark_variant": {
    "value": 1
}
```

```json
"minecraft:mark_variant": {
    "value": 2
}
```

```json
"minecraft:mark_variant": {
    "value": 3
}
```

```json
"minecraft:mark_variant": {
    "value": 4
}
```

```json
"minecraft:mark_variant": {
    "value": 5
}
```

```json
"minecraft:mark_variant": {
    "value": 6
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:mark_variant": {
    "value": 1
}
```

```json
"minecraft:mark_variant": {
    "value": 2
}
```

```json
"minecraft:mark_variant": {
    "value": 3
}
```

```json
"minecraft:mark_variant": {
    "value": 4
}
```

```json
"minecraft:mark_variant": {
    "value": 5
}
```

```json
"minecraft:mark_variant": {
    "value": 6
}
```

# minecraft:mob_effect
### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:mob_effect": {
    "effect_range": 0.2,
    "mob_effect": "poison",
    "effect_time": 10,
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

# minecraft:movement
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:movement": {
    "value": 0.1
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:movement": {
    "value": 0.23
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:movement": {
    "value": 0.2
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:movement": {
    "value": 0.1
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:movement": {
    "value": 0.175
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:movement": {
    "value": 0.23
}
```

```json
"minecraft:movement": {
    "value": 0.25
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

```json
"minecraft:movement": {
    "value": 0.45
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:movement": {
    "value": 0.5
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:movement": {
    "value": 0.1
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:movement": {
    "value": 0.03
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:movement": {
    "value": 0.12
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:movement": {
    "value": 0.36
}
```

```json
"minecraft:movement": {
    "value": 0.3
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:movement": {
    "value": {
        "range_min": 0.1125,
        "range_max": 0.3375
    }
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

```json
"minecraft:movement": {
    "value": 0.23
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:movement": {
    "value": 0.75
}
```

```json
"minecraft:movement": {
    "value": 0.66
}
```

```json
"minecraft:movement": {
    "value": 0.6
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:movement": {
    "value": 0.175
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:movement": {
    "value": 0.5
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:movement": {
    "value": 0.15
}
```

```json
"minecraft:movement": {
    "value": 0.07
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:movement": {
    "value": 0.4
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:movement": {
    "value": 1.8
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:movement": {
    "value": 0.42
}
```

```json
"minecraft:movement": {
    "value": 0.35
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:movement": {
    "value": 0.1
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:movement": {
    "value": 0.13
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:movement": {
    "value": 0.0
}
```

```json
"minecraft:movement": {
    "value": 0.3
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:movement": {
    "value": 0.12
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:movement": {
    "value": 0.0,
    "max": 0.0
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:movement": {
    "value": 0.2
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:movement": {
    "value": 0.6
}
```

```json
"minecraft:movement": {
    "value": 0.4
}
```

```json
"minecraft:movement": {
    "value": 0.3
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:movement": {
    "value": 0.2
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:movement": {
    "value": 0.2
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:movement": {
    "value": 0.16
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:movement": {
    "value": 0.12
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:movement": {
    "value": 0.1
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:movement": {
    "value": 1.0
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:movement": {
    "value": 0.5
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:movement": {
    "value": 0.5
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:movement": {
    "value": 0.5
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:movement": {
    "value": 0.3
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:movement": {
    "value": 0.25
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

```json
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:movement": {
    "value": 0.2
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

```json
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:movement": {
    "value": 0.35
}
```

```json
"minecraft:movement": {
    "value": 0.23
}
```

# minecraft:movement.amphibious
### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:movement.amphibious": {
    "max_turn": 5.0
}
```

# minecraft:movement.basic
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:movement.basic": {}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:movement.basic": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:movement.basic": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:movement.basic": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:movement.basic": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:movement.basic": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:movement.basic": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:movement.basic": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:movement.basic": {}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:movement.basic": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:movement.basic": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:movement.basic": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:movement.basic": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:movement.basic": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:movement.basic": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:movement.basic": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:movement.basic": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:movement.basic": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:movement.basic": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:movement.basic": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:movement.basic": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:movement.basic": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:movement.basic": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:movement.basic": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:movement.basic": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:movement.basic": {}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:movement.basic": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:movement.basic": {}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:movement.basic": {}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:movement.basic": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:movement.basic": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:movement.basic": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:movement.basic": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:movement.basic": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:movement.basic": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:movement.basic": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:movement.basic": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:movement.basic": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:movement.basic": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:movement.basic": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:movement.basic": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:movement.basic": {}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:movement.basic": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:movement.basic": {
    "max_turn": 180.0
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:movement.basic": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:movement.basic": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:movement.basic": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:movement.basic": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:movement.basic": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:movement.basic": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:movement.basic": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:movement.basic": {}
```

# minecraft:movement.fly
### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:movement.fly": {}
```

# minecraft:movement.generic
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:movement.generic": {}
```

# minecraft:movement.glide
### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:movement.glide": {
    "start_speed": 0.1,
    "speed_when_turning": 0.2
}
```

# minecraft:movement.hover
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:movement.hover": {}
```

# minecraft:movement.jump
### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:movement.jump": {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```json
"minecraft:movement.jump": {
    "jump_delay": [
        0.667,
        2.0
    ]
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:movement.jump": {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```json
"minecraft:movement.jump": {
    "jump_delay": [
        0.16,
        0.5
    ]
}
```

# minecraft:movement.skip
### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:movement.skip": {}
```

# minecraft:movement.sway
### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:movement.sway": {}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:movement.sway": {}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

# minecraft:nameable
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:nameable": {}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:nameable": {}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:nameable": {}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:nameable": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:nameable": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:nameable": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:nameable": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:nameable": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:nameable": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:nameable": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:nameable": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:nameable": {}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:nameable": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:nameable": {}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:nameable": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:nameable": {}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:nameable": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:nameable": {}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:nameable": {}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:nameable": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:nameable": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:nameable": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:nameable": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:nameable": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:nameable": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:nameable": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:nameable": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:nameable": {}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:nameable": {
    "always_show": true,
    "allow_name_tag_renaming": false
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:nameable": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:nameable": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:nameable": {}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:nameable": {}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:nameable": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:nameable": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:nameable": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:nameable": {}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:nameable": {
    "always_show": true,
    "allow_name_tag_renaming": false
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:nameable": {}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:nameable": {}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:nameable": {}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:nameable": {}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:nameable": {}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:nameable": {}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:nameable": {}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:nameable": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:nameable": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:nameable": {}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:nameable": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:nameable": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:nameable": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:nameable": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:nameable": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:nameable": {}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:nameable": {}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:nameable": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:nameable": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:nameable": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:nameable": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:nameable": {
    "default_trigger": {
        "event": "minecraft:stop_johnny",
        "target": "self"
    },
    "name_actions": [
        {
            "name_filter": "Johnny",
            "on_named": {
                "event": "minecraft:start_johnny",
                "target": "self"
            }
        }
    ]
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:nameable": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:nameable": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:nameable": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:nameable": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:nameable": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:nameable": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:nameable": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:nameable": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:nameable": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:nameable": {}
```

# minecraft:navigation.climb
### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

# minecraft:navigation.float
### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

# minecraft:navigation.fly
### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:navigation.fly": {
    "can_path_over_water": true,
    "can_path_from_air": true
}
```

# minecraft:navigation.generic
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": true,
    "can_walk": true,
    "avoid_sun": true
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": true,
    "can_sink": false,
    "avoid_damage_blocks": true
}
```

# minecraft:navigation.hover
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:navigation.hover": {
    "can_path_over_water": true,
    "can_sink": false,
    "can_pass_doors": false,
    "can_path_from_air": true,
    "avoid_water": true,
    "avoid_damage_blocks": true,
    "avoid_sun": false
}
```

# minecraft:navigation.walk
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:navigation.walk": {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": false,
    "avoid_water": true
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_portals": false
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": false,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:navigation.walk": {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_open_doors": true
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_open_doors": true
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:navigation.walk": {
    "avoid_damage_blocks": true,
    "can_path_over_water": true,
    "can_sink": false
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:navigation.walk": {}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_water": true
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:navigation.walk": {
    "avoid_water": true
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_sink": false
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_lava": true,
    "avoid_water": true,
    "can_sink": false,
    "can_walk_in_lava": true
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "can_walk": true,
    "avoid_water": true
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_break_doors": true
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": false
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_walk": true,
    "can_break_doors": true
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_water": true
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_portals": true
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_sun": false
}
```

```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_sun": false
}
```

```json
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

# minecraft:npc
### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:npc": {
    "npc_data": {
        "portrait_offsets": {
            "translate": [
                -7,
                50,
                0
            ],
            "scale": [
                1.75,
                1.75,
                1.75
            ]
        },
        "picker_offsets": {
            "translate": [
                0,
                20,
                0
            ],
            "scale": [
                1.7,
                1.7,
                1.7
            ]
        },
        "skin_list": [
            {
                "variant": 0
            },
            {
                "variant": 1
            },
            {
                "variant": 2
            },
            {
                "variant": 3
            },
            {
                "variant": 4
            },
            {
                "variant": 5
            },
            {
                "variant": 6
            },
            {
                "variant": 7
            },
            {
                "variant": 8
            },
            {
                "variant": 9
            },
            {
                "variant": 10
            },
            {
                "variant": 11
            },
            {
                "variant": 12
            },
            {
                "variant": 13
            },
            {
                "variant": 14
            },
            {
                "variant": 15
            },
            {
                "variant": 16
            },
            {
                "variant": 17
            },
            {
                "variant": 18
            },
            {
                "variant": 19
            }
        ]
    }
}
```

# minecraft:on_death
### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:on_death": {
    "event": "minecraft:start_death",
    "target": "self"
}
```

# minecraft:on_friendly_anger
### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:on_friendly_anger": {
    "event": "minecraft:defend_wandering_trader",
    "target": "self"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

# minecraft:on_hurt
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:on_hurt": {
    "event": "minecraft:on_hurt_event",
    "target": "self"
}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:on_hurt": {
    "event": "minecraft:crystal_explode",
    "target": "self"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:on_hurt": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

# minecraft:on_hurt_by_player
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:on_hurt_by_player": {
    "event": "minecraft:on_hurt_event",
    "target": "self"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:on_hurt_by_player": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

# minecraft:on_start_landing
### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:on_start_landing": {
    "event": "minecraft:start_land",
    "target": "self"
}
```

# minecraft:on_start_takeoff
```json
"minecraft:on_start_takeoff": {
    "event": "minecraft:start_fly",
    "target": "self"
}
```

# minecraft:on_target_acquired
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "attacked",
    "target": "self"
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "become_angry",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:has_target",
    "target": "self"
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "become_angry_event",
    "target": "self"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:on_target_acquired": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:mad_at_wolf",
    "target": "self"
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "become_angry_event",
    "target": "self"
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "become_angry_event",
    "target": "self"
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggro",
    "target": "self"
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:on_target_acquired": {}
```

```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

# minecraft:on_target_escape
### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:stop_exploding",
    "target": "self"
}
```

```json
"minecraft:on_target_escape": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:on_target_escape": {
    "target": "self"
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:lost_target",
    "target": "self"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:on_target_escape": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:calm",
    "target": "self"
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:on_target_escape": {
    "event": "minecraft:stop_aggro",
    "target": "self"
}
```

# minecraft:on_wake_with_owner
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:on_wake_with_owner": {
    "event": "minecraft:pet_slept_with_owner",
    "target": "self"
}
```

# minecraft:out_of_control
### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:out_of_control": {}
```

# minecraft:peek
### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:peek": {
    "on_open": {
        "event": "minecraft:on_open"
    },
    "on_close": {
        "event": "minecraft:on_close"
    },
    "on_target_open": {
        "event": "minecraft:on_open"
    }
}
```

# minecraft:persistent
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:persistent": {}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:persistent": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:persistent": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:persistent": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:persistent": {}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:persistent": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:persistent": {}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:persistent": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:persistent": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:persistent": {}
```

# minecraft:physics
### area_effect_cloud
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\area_effect_cloud.json)</small>
```json
"minecraft:physics": {
    "has_collision": false
}
```

### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:physics": {}
```

### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:physics": {}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:physics": {}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:physics": {}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:physics": {}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:physics": {}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:physics": {}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:physics": {}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:physics": {}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:physics": {}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:physics": {}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:physics": {}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:physics": {}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:physics": {}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:physics": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:physics": {}
```

### egg
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\egg.json)</small>
```json
"minecraft:physics": {}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:physics": {}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:physics": {}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:physics": {}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:physics": {}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false,
    "has_collision": false
}
```

### ender_pearl
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_pearl.json)</small>
```json
"minecraft:physics": {}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:physics": {}
```

### eye_of_ender_signal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\eye_of_ender_signal.json)</small>
```json
"minecraft:physics": {}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:physics": {}
```

### fireworks_rocket
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireworks_rocket.json)</small>
```json
"minecraft:physics": {}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false
}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:physics": {}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:physics": {}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:physics": {}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:physics": {}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:physics": {}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:physics": {}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:physics": {}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:physics": {}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:physics": {}
```

### lingering_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lingering_potion.json)</small>
```json
"minecraft:physics": {}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:physics": {}
```

### llama_spit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama_spit.json)</small>
```json
"minecraft:physics": {}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:physics": {}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:physics": {}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:physics": {}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:physics": {}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:physics": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:physics": {}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:physics": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:physics": {}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:physics": {}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:physics": {}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:physics": {}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:physics": {}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:physics": {}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:physics": {}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:physics": {}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:physics": {}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:physics": {}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:physics": {}
```

### shulker_bullet
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker_bullet.json)</small>
```json
"minecraft:physics": {
    "has_collision": false
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:physics": {}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:physics": {}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:physics": {}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:physics": {}
```

### small_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\small_fireball.json)</small>
```json
"minecraft:physics": {}
```

### snowball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snowball.json)</small>
```json
"minecraft:physics": {}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:physics": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:physics": {}
```

### splash_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\splash_potion.json)</small>
```json
"minecraft:physics": {}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:physics": {}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:physics": {}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:physics": {}
```

### thrown_trident
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\thrown_trident.json)</small>
```json
"minecraft:physics": {}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:physics": {}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:physics": {}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:physics": {}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:physics": {}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:physics": {
    "has_gravity": false,
    "has_collision": false
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:physics": {}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:physics": {}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:physics": {}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:physics": {}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:physics": {}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:physics": {}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:physics": {}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:physics": {}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:physics": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:physics": {}
```

### xp_bottle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_bottle.json)</small>
```json
"minecraft:physics": {}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:physics": {}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:physics": {}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:physics": {}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:physics": {}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:physics": {}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:physics": {}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:physics": {}
```

# minecraft:player.exhaustion
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:player.exhaustion": {
    "value": 0,
    "max": 4
}
```

# minecraft:player.experience
```json
"minecraft:player.experience": {
    "value": 0,
    "max": 1
}
```

# minecraft:player.level
```json
"minecraft:player.level": {
    "value": 0,
    "max": 24791
}
```

# minecraft:player.saturation
```json
"minecraft:player.saturation": {
    "value": 20
}
```

# minecraft:preferred_path
### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

```json
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 20,
    "default_block_cost": 3,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

# minecraft:projectile
### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                4
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                5
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": true,
            "semi_random_diff_damage": true,
            "destroy_on_hit": true,
            "max_critical_damage": 10,
            "min_critical_damage": 9,
            "power_multiplier": 0.97
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 5.0,
    "gravity": 0.05,
    "uncertainty_base": 1,
    "uncertainty_multiplier": 0,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                3,
                6
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

### dragon_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dragon_fireball.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "spawn_aoe_cloud": {
            "radius": 6.0,
            "radius_on_use": 0,
            "potion": 23,
            "particle": "dragonbreath",
            "duration": 120,
            "color": [
                220,
                0,
                239
            ],
            "affect_owner": false,
            "reapplication_delay": 20
        },
        "remove_on_hit": {}
    },
    "power": 1.3,
    "gravity": 0.0,
    "inertia": 1,
    "anchor": 2,
    "offset": [
        0,
        0.5,
        0
    ],
    "semi_random_diff_damage": true,
    "uncertainty_base": 10.0,
    "reflect_on_hurt": true,
    "hit_sound": "explode"
}
```

### egg
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\egg.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 0,
            "knockback": true,
            "destroy_on_hit": true
        },
        "spawn_chance": {
            "first_spawn_chance": 8,
            "second_spawn_chance": 32,
            "first_spawn_count": 1,
            "second_spawn_count": 4,
            "spawn_definition": "minecraft:chicken",
            "spawn_baby": true
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "iconcrack",
            "num_particles": 6,
            "on_entity_hit": true,
            "on_other_hit": true
        }
    },
    "power": 1.5,
    "gravity": 0.03,
    "angle_offset": 0.0
}
```

### ender_pearl
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_pearl.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "spawn_chance": {
            "first_spawn_percent_chance": 5.0,
            "first_spawn_count": 1,
            "spawn_definition": "minecraft:endermite"
        },
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

```json
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        }
    },
    "power": 1.6,
    "gravity": 0.0,
    "inertia": 1,
    "liquid_inertia": 1,
    "uncertainty_base": 0,
    "uncertainty_multiplier": 0,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "reflect_on_hurt": true,
    "catch_fire": true
}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "stick_in_ground": {}
    }
}
```

### lingering_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lingering_potion.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "douse_fire": {},
        "spawn_aoe_cloud": {
            "radius": 3.0,
            "radius_on_use": -0.5,
            "duration": 30,
            "reapplication_delay": 40
        },
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

### llama_spit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama_spit.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": false
        },
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.06,
    "inertia": 1,
    "uncertainty_base": 10,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "reflect_on_hurt": true
}
```

### shulker_bullet
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker_bullet.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 4,
            "knockback": true,
            "should_bounce": true
        },
        "mob_effect": {
            "effect": "levitation",
            "durationeasy": 200,
            "durationnormal": 200,
            "durationhard": 200,
            "amplifier": 1
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "largeexplode",
            "on_other_hit": true
        }
    },
    "hit_sound": "bullet.hit",
    "destroyOnHurt": true,
    "crit_particle_on_hurt": true,
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "homing": true
}
```

### small_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\small_fireball.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 5,
            "knockback": false,
            "catch_fire": true,
            "semi_random_diff_damage": false
        },
        "catch_fire": {
            "fire_affected_by_griefing": true
        },
        "remove_on_hit": {}
    },
    "power": 1.3,
    "gravity": 0.0,
    "inertia": 1,
    "liquid_inertia": 1,
    "anchor": 2,
    "offset": [
        0,
        0.5,
        0
    ],
    "semi_random_diff_damage": true,
    "uncertainty_base": 10.0,
    "reflect_on_hurt": true
}
```

### snowball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snowball.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "filter": "blaze",
            "damage": 3,
            "knockback": true
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "snowballpoof",
            "num_particles": 6,
            "on_entity_hit": true,
            "on_other_hit": true
        }
    },
    "anchor": 1,
    "power": 1.5,
    "gravity": 0.03,
    "angle_offset": 0.0,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

### splash_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\splash_potion.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "douse_fire": {},
        "thrown_potion_effect": {},
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

### thrown_trident
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\thrown_trident.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 8,
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": false
        },
        "stick_in_ground": {
            "shake_time": 0
        }
    },
    "liquid_inertia": 0.99,
    "hit_sound": "item.trident.hit",
    "hit_ground_sound": "item.trident.hit_ground",
    "power": 4,
    "gravity": 0.1,
    "uncertainty_base": 1,
    "uncertainty_multiplier": 0,
    "stop_on_hurt": true,
    "anchor": 1,
    "should_bounce": true,
    "multiple_targets": false,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        },
        "mob_effect": {
            "effect": "wither",
            "durationeasy": 0,
            "durationnormal": 200,
            "durationhard": 800,
            "amplifier": 1
        }
    },
    "power": 1.2,
    "gravity": 0.0,
    "uncertainty_base": 7.5,
    "uncertainty_multiplier": 1,
    "shoot_sound": "bow",
    "hit_sound": "bow.hit",
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "inertia": 1.0,
    "liquid_inertia": 1.0,
    "shoot_target": false
}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        },
        "mob_effect": {
            "effect": "wither",
            "durationeasy": 0,
            "durationnormal": 200,
            "durationhard": 800,
            "amplifier": 1
        }
    },
    "power": 0.6,
    "gravity": 0.0,
    "uncertainty_base": 7.5,
    "uncertainty_multiplier": 1,
    "shoot_sound": "bow",
    "hit_sound": "bow.hit",
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "is_dangerous": true,
    "inertia": 1.0,
    "liquid_inertia": 1.0,
    "shoot_target": false,
    "reflect_on_hurt": true
}
```

### xp_bottle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_bottle.json)</small>
```json
"minecraft:projectile": {
    "on_hit": {
        "grant_xp": {
            "minXP": 3,
            "maxXP": 11
        },
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

# minecraft:pushable
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### arrow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\arrow.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### egg
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\egg.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_crystal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_crystal.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_pearl
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_pearl.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### eye_of_ender_signal
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\eye_of_ender_signal.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireball.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireworks_rocket
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fireworks_rocket.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fishing_hook
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fishing_hook.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### lingering_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lingering_potion.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama_spit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama_spit.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### small_fireball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\small_fireball.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snowball
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snowball.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### splash_potion
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\splash_potion.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### thrown_trident
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\thrown_trident.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull_dangerous
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skull_dangerous.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### xp_bottle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_bottle.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### xp_orb
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\xp_orb.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

# minecraft:raid_trigger
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:raid_trigger": {
    "triggered_event": {
        "event": "minecraft:remove_raid_trigger",
        "target": "self"
    }
}
```

# minecraft:rail_movement
### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:rail_movement": {}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:rail_movement": {}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:rail_movement": {}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:rail_movement": {}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:rail_movement": {}
```

# minecraft:rail_sensor
### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:rail_sensor": {
    "check_block_types": true,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_deactivate": {
        "event": "minecraft:command_block_deactivate"
    }
}
```

```json
"minecraft:rail_sensor": {
    "check_block_types": false,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_activate": {
        "event": "minecraft:command_block_activate"
    }
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:rail_sensor": {
    "on_activate": {
        "event": "minecraft:hopper_deactivate"
    }
}
```

```json
"minecraft:rail_sensor": {
    "on_deactivate": {
        "event": "minecraft:hopper_activate"
    }
}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:rail_sensor": {
    "eject_on_activate": true
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:rail_sensor": {}
```

```json
"minecraft:rail_sensor": {
    "on_activate": {
        "filters": {
            "all_of": [
                {
                    "test": "is_game_rule",
                    "domain": "tntexplodes",
                    "operator": "==",
                    "value": true
                }
            ]
        },
        "event": "minecraft:on_prime"
    }
}
```

# minecraft:ravager_blocked
### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:ravager_blocked": {
    "knockback_strength": 3.0,
    "reaction_choices": [
        {
            "weight": 1,
            "value": {
                "event": "minecraft:become_stunned",
                "target": "self"
            }
        },
        {
            "weight": 1
        }
    ]
}
```

# minecraft:rideable
### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 2,
    "interact_text": "action.interact.ride.boat",
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.0,
                -0.2,
                0.0
            ],
            "min_rider_count": 0,
            "max_rider_count": 1,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                0.2,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        },
        {
            "position": [
                -0.6,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        }
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.35,
            0.0
        ]
    }
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            0.0
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            -0.1
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.25,
            -0.1
        ]
    }
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.4,
            0.0
        ]
    }
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            0.925,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            0.925,
            -0.2
        ]
    }
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 3,
    "family_types": [
        "piglin"
    ],
    "seats": [
        {
            "position": [
                0.0,
                0.9,
                -0.3
            ],
            "lock_rider_rotation": 0
        },
        {
            "position": [
                0.0,
                2.4,
                -0.3
            ],
            "lock_rider_rotation": 0
        },
        {
            "position": [
                0.0,
                3.9,
                -0.3
            ],
            "lock_rider_rotation": 0
        }
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            1.25,
            -0.3
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "interact_text": "action.interact.ride.minecart",
    "pull_in_entities": true,
    "seats": {
        "position": [
            0.0,
            -0.2,
            0.0
        ]
    }
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            0.975,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            0.975,
            -0.2
        ]
    }
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.35,
            0.0
        ]
    }
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.63,
            0.0
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "interact_text": "action.interact.mount",
    "family_types": [
        "player"
    ],
    "seats": {
        "position": [
            0.0,
            0.63,
            0.0
        ]
    }
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 2,
    "family_types": [
        "parrot_tame"
    ],
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.4,
                -0.2,
                -0.1
            ],
            "min_rider_count": 0,
            "max_rider_count": 0,
            "lock_rider_rotation": 0
        },
        {
            "position": [
                -0.4,
                -0.2,
                -0.1
            ],
            "min_rider_count": 1,
            "max_rider_count": 2,
            "lock_rider_rotation": 0
        }
    ]
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "pillager",
        "vindicator",
        "evocation_illager"
    ],
    "seats": {
        "position": [
            0.0,
            2.1,
            -0.3
        ]
    }
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.9,
            0.0
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.975,
            0.0
        ]
    }
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "skeleton",
        "zombie"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.2,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            -0.1
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            0.0
        ]
    }
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.strider",
    "seats": {
        "position": [
            0.0,
            1.6,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player",
        "zombie_pigman"
    ],
    "interact_text": "action.interact.ride.strider",
    "seats": {
        "position": [
            0.0,
            1.65,
            -0.2
        ]
    }
}
```

```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "strider"
    ],
    "seats": {
        "position": [
            0.0,
            1.6,
            0.0
        ]
    }
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.675,
            -0.1
        ]
    }
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.2,
            -0.2
        ]
    }
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ]
    }
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ]
    }
}
```

# minecraft:scaffolding_climber
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:scaffolding_climber": {}
```

# minecraft:scale
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:scale": {
    "value": 0.4
}
```

```json
"minecraft:scale": {
    "value": 0.8
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:scale": {
    "value": 0.65
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:scale": {
    "value": 1.0
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:scale": {
    "value": 0.53125
}
```

```json
"minecraft:scale": {
    "value": 1.0625
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

```json
"minecraft:scale": {
    "value": 1
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:scale": {
    "value": 1.0
}
```

```json
"minecraft:scale": {
    "value": 0.4
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:scale": {
    "value": 1.2
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:scale": {
    "value": 0.4
}
```

```json
"minecraft:scale": {
    "value": 0.6
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

```json
"minecraft:scale": {
    "value": 1
}
```

```json
"minecraft:scale": {
    "value": 1.5
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:scale": {
    "value": 1.3
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:scale": {
    "value": 0.16
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:scale": {
    "value": 1.2
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:scale": {
    "value": 0.5
}
```

# minecraft:scale_by_age
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

# minecraft:scheduler
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 0,
    "scheduled_events": [
        {
            "filters": [
                {
                    "test": "is_sleeping",
                    "value": true
                }
            ],
            "event": "minecraft:ambient_sleep"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": false
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 16
                    }
                ]
            },
            "event": "minecraft:ambient_night"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_sleeping",
                        "value": false
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": true
                            },
                            {
                                "test": "distance_to_nearest_player",
                                "operator": "<=",
                                "value": 16
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:ambient_normal"
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_play_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 2000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 13000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 13000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 14000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 14000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 2000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_fisher"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_fisher"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_librarian"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_librarian"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_farmer"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_farmer"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

# minecraft:shareables
### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:nautilus_shell",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:trident",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:shareables": {
    "all_items": true,
    "all_items_max_amount": 1,
    "items": [
        {
            "item": "minecraft:apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:appleEnchanted",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:baked_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot_soup",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:bread",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chorus_fruit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:clownfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cookie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:dried_kelp",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:melon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:mushroom_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonCooked",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonRaw",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:poisonous_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pufferfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pumpkin_pie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rotten_flesh",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:spider_eye",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:sweet_berries",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:suspicious_stew",
            "priority": 0,
            "max_amount": 1
        }
    ]
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:golden_sword",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_axe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_hoe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_pickaxe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_shovel",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_rail",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_helmet",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_chestplate",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_leggings",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_boots",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_apple",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:appleEnchanted",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_carrot",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_block",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_nugget",
            "priority": 2,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_ore",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:nether_gold_ore",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gilded_blackstone",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:horsearmorgold",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:crossbow",
            "priority": 2
        },
        {
            "item": "minecraft:porkchop",
            "consume_item": true,
            "priority": 3,
            "max_amount": 64
        },
        {
            "item": "minecraft:cooked_porkchop",
            "consume_item": true,
            "priority": 3,
            "max_amount": 64
        },
        {
            "item": "minecraft:netherite_helmet",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_helmet",
            "priority": 4
        },
        {
            "item": "minecraft:iron_helmet",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_helmet",
            "priority": 6
        },
        {
            "item": "minecraft:leather_helmet",
            "priority": 7
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:2",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:3",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:4",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:5",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:netherite_chestplate",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_chestplate",
            "priority": 4
        },
        {
            "item": "minecraft:iron_chestplate",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "priority": 6
        },
        {
            "item": "minecraft:leather_chestplate",
            "priority": 7
        },
        {
            "item": "minecraft:elytra",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_leggings",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_leggings",
            "priority": 4
        },
        {
            "item": "minecraft:iron_leggings",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_leggings",
            "priority": 6
        },
        {
            "item": "minecraft:leather_leggings",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_boots",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_boots",
            "priority": 4
        },
        {
            "item": "minecraft:iron_boots",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_boots",
            "priority": 6
        },
        {
            "item": "minecraft:bell",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:clock",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:speckled_melon",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:light_weighted_pressure_plate",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:leather_boots",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_sword",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_sword",
            "priority": 4
        },
        {
            "item": "minecraft:iron_sword",
            "priority": 5
        },
        {
            "item": "minecraft:stone_sword",
            "priority": 6
        },
        {
            "item": "minecraft:wooden_sword",
            "priority": 7
        },
        {
            "item": "minecraft:shield",
            "priority": 7
        },
        {
            "item": "minecraft:gold_ingot",
            "priority": 1,
            "pickup_limit": 1,
            "admire": true,
            "barter": true
        }
    ]
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:banner:15",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        }
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:bow",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:bow",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 60,
            "surplus_amount": 4,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:potato",
            "want_amount": 60,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 60,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:wheat_seeds",
            "want_amount": 64,
            "surplus_amount": 64,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot_seeds",
            "want_amount": 64,
            "surplus_amount": 64,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:wheat",
            "want_amount": 45,
            "surplus_amount": 18,
            "craft_into": "minecraft:bread",
            "stored_in_inventory": true
        }
    ]
}
```

```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:potato",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        }
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 60,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:potato",
            "want_amount": 60,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 60,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:wheat_seeds",
            "want_amount": 64,
            "surplus_amount": 64,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot_seeds",
            "want_amount": 64,
            "surplus_amount": 64,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:wheat",
            "want_amount": 45,
            "surplus_amount": 18,
            "craft_into": "minecraft:bread",
            "stored_in_inventory": true
        }
    ]
}
```

```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:potato",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 12,
            "surplus_amount": 24,
            "stored_in_inventory": true
        }
    ]
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:wooden_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:stone_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:golden_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:iron_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:diamond_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_shovel",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:wooden_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:stone_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:golden_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:iron_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:diamond_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_pickaxe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:wooden_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:stone_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:golden_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:iron_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:diamond_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_axe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:wooden_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:stone_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:golden_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:iron_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:diamond_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_hoe",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

# minecraft:shooter
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:small_fireball"
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:thrown_trident"
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:shooter": {
    "type": "dragonfireball",
    "def": "minecraft:dragon_fireball"
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:fireball"
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:llama_spit"
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:arrow"
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:arrow"
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:shulker_bullet"
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:arrow"
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:snowball"
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:shooter": {
    "def": "minecraft:arrow",
    "aux_val": 19
}
```

# minecraft:sittable
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:sittable": {}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:sittable": {}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:sittable": {}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:sittable": {}
```

# minecraft:skin_id
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:skin_id": {
    "value": 0
}
```

```json
"minecraft:skin_id": {
    "value": 1
}
```

```json
"minecraft:skin_id": {
    "value": 2
}
```

```json
"minecraft:skin_id": {
    "value": 3
}
```

```json
"minecraft:skin_id": {
    "value": 4
}
```

```json
"minecraft:skin_id": {
    "value": 5
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:skin_id": {
    "value": 0
}
```

```json
"minecraft:skin_id": {
    "value": 1
}
```

```json
"minecraft:skin_id": {
    "value": 2
}
```

```json
"minecraft:skin_id": {
    "value": 3
}
```

```json
"minecraft:skin_id": {
    "value": 4
}
```

```json
"minecraft:skin_id": {
    "value": 5
}
```

# minecraft:spawn_entity
### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:spawn_entity": {
    "entities": {
        "min_wait_time": 300,
        "max_wait_time": 600,
        "spawn_sound": "plop",
        "spawn_item": "egg",
        "filters": {
            "test": "rider_count",
            "subject": "self",
            "operator": "==",
            "value": 0
        }
    }
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:spawn_entity": {
    "entities": [
        {
            "min_wait_time": 0,
            "max_wait_time": 0,
            "spawn_entity": "llama",
            "spawn_event": "minecraft:from_wandering_trader",
            "single_use": true,
            "num_to_spawn": 2,
            "should_leash": true
        }
    ]
}
```

# minecraft:spell_effects
### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "bad_omen",
            "duration": 6000,
            "display_on_screen_animation": true
        }
    ]
}
```

```json
"minecraft:spell_effects": {}
```

```json
"minecraft:spell_effects": {
    "remove_effects": "bad_omen"
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 100
        },
        {
            "effect": "heal",
            "duration": 100
        }
    ],
    "remove_effects": "weakness"
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 100
        },
        {
            "effect": "heal",
            "duration": 100
        }
    ],
    "remove_effects": "weakness"
}
```

# minecraft:strength
### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:strength": {
    "value": 1,
    "max": 5
}
```

```json
"minecraft:strength": {
    "value": 2,
    "max": 5
}
```

```json
"minecraft:strength": {
    "value": 3,
    "max": 5
}
```

```json
"minecraft:strength": {
    "value": 4,
    "max": 5
}
```

```json
"minecraft:strength": {
    "value": 5,
    "max": 5
}
```

# minecraft:tameable
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "fish",
        "salmon"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "wheat_seeds",
        "pumpkin_seeds",
        "melon_seeds",
        "beetroot_seeds"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": "bone",
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

# minecraft:tamemount
### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 30,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "hay_block",
            "temper_mod": 6
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

# minecraft:target_nearby_sensor
### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:target_nearby_sensor": {
    "inside_range": 2.0,
    "outside_range": 3.0,
    "must_see": true,
    "on_inside_range": {
        "event": "switch_to_melee",
        "target": "self"
    },
    "on_outside_range": {
        "event": "switch_to_ranged",
        "target": "self"
    }
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:target_nearby_sensor": {
    "inside_range": 2.5,
    "outside_range": 6.0,
    "must_see": true,
    "on_inside_range": {
        "event": "minecraft:start_exploding",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    },
    "on_vision_lost_inside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    }
}
```

```json
"minecraft:target_nearby_sensor": {}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 5.0,
    "on_inside_range": {
        "event": "minecraft:switch_to_melee",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:switch_to_ranged",
        "target": "self"
    }
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

# minecraft:teleport
### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:teleport": {
    "random_teleports": true,
    "max_random_teleport_time": 30,
    "random_teleport_cube": [
        32,
        32,
        32
    ],
    "target_distance": 16,
    "target_teleport_chance": 0.05,
    "light_teleport_chance": 0.05
}
```

# minecraft:timer
### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": [
        20,
        50
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "stop_panicking_after_fire",
        "target": "self"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": [
        10,
        60
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "perish_event",
        "target": "self"
    }
}
```

```json
"minecraft:timer": {
    "looping": true,
    "time": 5,
    "time_down_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

```json
"minecraft:timer": {
    "looping": true,
    "time": 180,
    "time_down_event": {
        "event": "find_flower_timeout"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": 180,
    "time_down_event": {
        "event": "find_hive_timeout",
        "target": "self"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": [
        5,
        20
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "find_hive_event",
        "target": "self"
    }
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 3,
    "time_down_event": {
        "event": "minecraft:sink",
        "target": "self"
    }
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 120,
    "time_down_event": {
        "event": "dried_out"
    }
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:timer": {
    "time": [
        1,
        3
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:target_far_enough",
        "target": "self"
    }
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 15,
    "time_down_event": {
        "event": "become_zombie_event"
    }
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_zombie"
    }
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 15,
    "time_down_event": {
        "event": "become_zombie_event"
    }
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 15,
    "time_down_event": {
        "event": "become_zombie_event"
    }
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:timer": {
    "time": [
        0.0,
        0.0
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:clear_add_bad_omen",
        "target": "self"
    }
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 2,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_half_puff"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": 2,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_normal_puff"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": 0.01,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_full_puff"
    }
}
```

```json
"minecraft:timer": {
    "looping": false,
    "time": 3,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_deflate"
    }
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 2,
    "time_down_event": {
        "event": "minecraft:start_roar"
    }
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "random_time_choices": [
        {
            "weight": 50,
            "value": 2400
        },
        {
            "weight": 50,
            "value": 3600
        }
    ],
    "time_down_event": {
        "event": "minecraft:start_despawn",
        "target": "self"
    }
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_drowned"
    }
}
```

# minecraft:trade_resupply
### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:trade_resupply": {}
```

# minecraft:trade_table
### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/farmer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/fisherman_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.shepherd",
    "table": "trading/shepherd_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.fletcher",
    "table": "trading/fletcher_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.librarian",
    "table": "trading/librarian_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.cartographer",
    "table": "trading/cartographer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.cleric",
    "table": "trading/cleric_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.armor",
    "table": "trading/armorer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.weapon",
    "table": "trading/weapon_smith_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.tool",
    "table": "trading/tool_smith_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.butcher",
    "table": "trading/butcher_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table": {
    "display_name": "entity.villager.leather",
    "table": "trading/leather_worker_trades.json",
    "convert_trades_economy": true
}
```

# minecraft:trail
### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:trail": {
    "block_type": "minecraft:snow_layer",
    "spawn_filter": {
        "test": "is_temperature_value",
        "operator": "<",
        "value": 0.81
    }
}
```

# minecraft:transformation
### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:zoglin",
    "transformation_sound": "converted_to_zombified",
    "keep_level": true
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:cow"
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:pig_zombie",
    "delay": 0.5
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:zombie_pigman",
    "transformation_sound": "converted_to_zombified",
    "keep_level": true,
    "drop_inventory": true,
    "preserve_equipment": true
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:zombie_pigman",
    "transformation_sound": "converted_to_zombified",
    "keep_level": true,
    "preserve_equipment": true
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:skeleton",
    "delay": 0.5
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "keep_level": true
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:zombie_villager"
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": true
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": false
}
```

```json
"minecraft:transformation": {
    "into": "minecraft:villager",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "keep_level": true,
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

# minecraft:trust
### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:trust": {}
```

# minecraft:trusting
### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:trusting": {
    "probability": 0.33,
    "trust_items": [
        "fish",
        "salmon"
    ],
    "trust_event": {
        "event": "minecraft:on_trust",
        "target": "self"
    }
}
```

# minecraft:type_family
### armor_stand
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\armor_stand.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "armor_stand",
        "inanimate",
        "mob"
    ]
}
```

### bat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bat.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "bat",
        "mob"
    ]
}
```

### bee
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\bee.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "bee",
        "mob",
        "arthropod"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "bee",
        "mob",
        "arthropod",
        "pacified"
    ]
}
```

### blaze
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\blaze.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "blaze",
        "monster",
        "mob"
    ]
}
```

### boat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\boat.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "boat",
        "inanimate"
    ]
}
```

### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "cat",
        "mob"
    ]
}
```

### cave_spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cave_spider.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "cavespider",
        "monster",
        "arthropod",
        "mob"
    ]
}
```

### chest_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chest_minecart.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### chicken
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\chicken.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "chicken",
        "mob"
    ]
}
```

### command_block_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\command_block_minecart.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### cow
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cow.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "cow",
        "mob"
    ]
}
```

### creeper
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\creeper.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "creeper",
        "monster",
        "mob"
    ]
}
```

### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "dolphin",
        "mob"
    ]
}
```

### donkey
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\donkey.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "donkey",
        "mob"
    ]
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "drowned",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "guardian_elder",
        "monster",
        "mob"
    ]
}
```

### enderman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\enderman.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "enderman",
        "monster",
        "mob"
    ]
}
```

### endermite
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\endermite.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "endermite",
        "arthropod",
        "monster",
        "mob"
    ]
}
```

### ender_dragon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ender_dragon.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "dragon",
        "mob"
    ]
}
```

### evocation_illager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\evocation_illager.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "evocation_illager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "cod",
        "fish"
    ]
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "fox",
        "mob"
    ]
}
```

### ghast
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ghast.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "ghast",
        "monster",
        "mob"
    ]
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "guardian",
        "monster",
        "mob"
    ]
}
```

### hoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hoglin.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "hoglin",
        "hoglin_baby",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "hoglin",
        "hoglin_adult",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "hoglin",
        "hoglin_adult",
        "hoglin_huntable",
        "mob"
    ]
}
```

### hopper_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\hopper_minecart.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "horse",
        "mob"
    ]
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "husk",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### iron_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\iron_golem.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "irongolem",
        "mob"
    ]
}
```

### lightning_bolt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\lightning_bolt.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "lightning"
    ]
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "llama",
        "mob"
    ]
}
```

### magma_cube
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\magma_cube.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "magmacube",
        "monster",
        "mob"
    ]
}
```

### minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\minecart.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "mushroomcow",
        "mob"
    ]
}
```

### mule
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mule.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "mule",
        "mob"
    ]
}
```

### npc
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\npc.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "npc",
        "mob"
    ]
}
```

### ocelot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ocelot.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "ocelot",
        "mob"
    ]
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "panda"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "panda",
        "panda_aggressive",
        "mob"
    ]
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "parrot_wild",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "parrot_tame",
        "mob"
    ]
}
```

### phantom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\phantom.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "phantom",
        "undead",
        "monster",
        "mob"
    ]
}
```

### pig
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pig.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "pig",
        "mob"
    ]
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "piglin",
        "piglin_hunter",
        "monster"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "piglin",
        "monster"
    ]
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "piglin",
        "adult_piglin",
        "piglin_brute",
        "monster"
    ]
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "pillager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### player
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\player.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "player"
    ]
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "polarbear",
        "mob"
    ]
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "pufferfish",
        "fish"
    ]
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "rabbit",
        "mob"
    ]
}
```

### ravager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\ravager.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "monster",
        "illager",
        "ravager",
        "mob"
    ]
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "salmon",
        "fish"
    ]
}
```

### sheep
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\sheep.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "sheep",
        "mob"
    ]
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "shulker",
        "monster",
        "mob"
    ]
}
```

### silverfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\silverfish.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "silverfish",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "skeleton",
        "undead",
        "monster",
        "mob"
    ]
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "skeletonhorse",
        "undead",
        "mob"
    ]
}
```

### slime
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\slime.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "slime",
        "monster",
        "mob"
    ]
}
```

### snow_golem
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\snow_golem.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "snowgolem",
        "mob"
    ]
}
```

### spider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\spider.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "spider",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### squid
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\squid.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "squid",
        "mob"
    ]
}
```

### stray
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\stray.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "stray",
        "skeleton",
        "monster",
        "mob",
        "undead"
    ]
}
```

### strider
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\strider.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "strider",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "strider",
        "strider_baby",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "strider",
        "strider_adult",
        "mob"
    ]
}
```

### tnt
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "tnt",
        "inanimate"
    ]
}
```

### tnt_minecart
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tnt_minecart.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### tripod_camera
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tripod_camera.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "tripodcamera",
        "inanimate",
        "mob"
    ]
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "tropicalfish",
        "fish"
    ]
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "turtle",
        "baby_turtle",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "turtle",
        "mob"
    ]
}
```

### vex
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vex.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "vex",
        "monster",
        "mob"
    ]
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "villager",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "villager",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "stone_mason",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "nitwit",
        "mob"
    ]
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "vindicator",
        "monster",
        "illager",
        "mob"
    ]
}
```

### wandering_trader
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wandering_trader.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "wandering_trader",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "wandering_trader",
        "wandering_trader_despawning",
        "mob"
    ]
}
```

### witch
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\witch.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "witch",
        "monster",
        "mob"
    ]
}
```

### wither
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "wither",
        "skeleton",
        "monster",
        "undead",
        "mob"
    ]
}
```

### wither_skeleton
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wither_skeleton.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "wither",
        "monster",
        "undead",
        "skeleton",
        "mob"
    ]
}
```

### wolf
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\wolf.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "wolf",
        "mob"
    ]
}
```

### zoglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zoglin.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "zoglin",
        "zoglin_baby",
        "undead",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "zoglin",
        "zoglin_adult",
        "undead",
        "mob"
    ]
}
```

### zombie
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_horse.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "zombiehorse",
        "undead",
        "mob"
    ]
}
```

### zombie_pigman
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_pigman.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "zombie_pigman",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "farmer",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "fisherman",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "shepherd",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "fletcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "librarian",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "cartographer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "cleric",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "armorer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "weaponsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "toolsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "butcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "leatherworker",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:type_family": {
    "family": [
        "unskilled",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "nitwit",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "farmer",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "fisherman",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "shepherd",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "fletcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "librarian",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "cartographer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "cleric",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "armorer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "weaponsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "toolsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "butcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "leatherworker",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```json
"minecraft:type_family": {
    "family": [
        "stone_mason",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

# minecraft:underwater_movement
### dolphin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\dolphin.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.15
}
```

### drowned
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\drowned.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.06
}
```

```json
"minecraft:underwater_movement": {
    "value": 0.08
}
```

### elder_guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\elder_guardian.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.3
}
```

### fish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fish.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.1
}
```

### guardian
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\guardian.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.13
}
```

### salmon
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\salmon.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### skeleton_horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\skeleton_horse.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.08
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:underwater_movement": {
    "value": 0.06
}
```

```json
"minecraft:underwater_movement": {
    "value": 0.12
}
```

# minecraft:variant
### cat
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\cat.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 5
}
```

```json
"minecraft:variant": {
    "value": 6
}
```

```json
"minecraft:variant": {
    "value": 7
}
```

```json
"minecraft:variant": {
    "value": 8
}
```

```json
"minecraft:variant": {
    "value": 9
}
```

```json
"minecraft:variant": {
    "value": 10
}
```

### fox
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\fox.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### horse
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\horse.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 5
}
```

```json
"minecraft:variant": {
    "value": 6
}
```

### husk
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\husk.json)</small>
```json
"minecraft:variant": {
    "value": 2
}
```

### llama
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\llama.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

### mooshroom
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\mooshroom.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 5
}
```

```json
"minecraft:variant": {
    "value": 6
}
```

### parrot
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\parrot.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

### piglin
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### piglin_brute
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\piglin_brute.json)</small>
```json
"minecraft:variant": {
    "value": 1
}
```

### pillager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pillager.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### pufferfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\pufferfish.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

### rabbit
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\rabbit.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 5
}
```

### shulker
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\shulker.json)</small>
```json
"minecraft:variant": {
    "value": 5
}
```

```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 6
}
```

```json
"minecraft:variant": {
    "value": 8
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 12
}
```

```json
"minecraft:variant": {
    "value": 10
}
```

```json
"minecraft:variant": {
    "value": 13
}
```

```json
"minecraft:variant": {
    "value": 14
}
```

```json
"minecraft:variant": {
    "value": 9
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 7
}
```

```json
"minecraft:variant": {
    "value": 16
}
```

```json
"minecraft:variant": {
    "value": 15
}
```

```json
"minecraft:variant": {
    "value": 11
}
```

### tropicalfish
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\tropicalfish.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

### villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\villager_v2.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

```json
"minecraft:variant": {
    "value": 5
}
```

```json
"minecraft:variant": {
    "value": 6
}
```

```json
"minecraft:variant": {
    "value": 7
}
```

```json
"minecraft:variant": {
    "value": 8
}
```

```json
"minecraft:variant": {
    "value": 9
}
```

```json
"minecraft:variant": {
    "value": 10
}
```

```json
"minecraft:variant": {
    "value": 11
}
```

```json
"minecraft:variant": {
    "value": 12
}
```

```json
"minecraft:variant": {
    "value": 13
}
```

```json
"minecraft:variant": {
    "value": 14
}
```

### vindicator
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\vindicator.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

### zombie_villager
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

```json
"minecraft:variant": {
    "value": 1
}
```

```json
"minecraft:variant": {
    "value": 2
}
```

```json
"minecraft:variant": {
    "value": 3
}
```

```json
"minecraft:variant": {
    "value": 4
}
```

### zombie_villager_v2
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\zombie_villager_v2.json)</small>
```json
"minecraft:variant": {
    "value": 0
}
```

# minecraft:water_movement
### panda
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\panda.json)</small>
```json
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

### polar_bear
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\polar_bear.json)</small>
```json
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

### turtle
<small>[View file](https://github.com/bedrock-dot-dev/packs/tree/master/stable/behavior/entities\turtle.json)</small>
```json
"minecraft:water_movement": {
    "drag_factor": 0.9
}
```