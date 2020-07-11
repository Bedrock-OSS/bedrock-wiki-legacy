---
layout: page
title: Items
parent: Vanilla Usage
---

# Items
This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`

# Table of contents
 - [minecraft:block](#minecraftblock)
 - [minecraft:camera](#minecraftcamera)
 - [minecraft:foil](#minecraftfoil)
 - [minecraft:food](#minecraftfood)
 - [minecraft:hand_equipped](#minecrafthand_equipped)
 - [minecraft:max_damage](#minecraftmax_damage)
 - [minecraft:max_stack_size](#minecraftmax_stack_size)
 - [minecraft:seed](#minecraftseed)
 - [minecraft:stacked_by_data](#minecraftstacked_by_data)
 - [minecraft:use_duration](#minecraftuse_duration)

# minecraft:block
### camera.json
```json
"minecraft:block:" "minecraft:camera"
```

# minecraft:camera
```json
"minecraft:camera:" {
    "black_bars_duration": 0.2,
    "black_bars_screen_ratio": 0.08,
    "shutter_duration": 0.2,
    "picture_duration": 1.0,
    "slide_away_duration": 0.2
}
```

# minecraft:foil
### appleEnchanted.json
```json
"minecraft:foil:" true
```

### golden_apple.json
```json
"minecraft:foil:" false
```

# minecraft:food
### apple.json
```json
"minecraft:food:" {
    "nutrition": 4,
    "saturation_modifier": "low"
}
```

### appleEnchanted.json
```json
"minecraft:food:" {
    "nutrition": 4,
    "saturation_modifier": "supernatural",
    "can_always_eat": true,
    "effects": [
        {
            "name": "regeneration",
            "chance": 1.0,
            "duration": 30,
            "amplifier": 4
        },
        {
            "name": "absorption",
            "chance": 1.0,
            "duration": 120,
            "amplifier": 3
        },
        {
            "name": "resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        },
        {
            "name": "fire_resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        }
    ]
}
```

### baked_potato.json
```json
"minecraft:food:" {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

### beef.json
```json
"minecraft:food:" {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

### beetroot.json
```json
"minecraft:food:" {
    "nutrition": 1,
    "saturation_modifier": "normal"
}
```

### beetroot_soup.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

### bread.json
```json
"minecraft:food:" {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

### carrot.json
```json
"minecraft:food:" {
    "nutrition": 3,
    "saturation_modifier": "normal"
}
```

### chicken.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "low",
    "effects": [
        {
            "name": "hunger",
            "chance": 0.3,
            "duration": 30,
            "amplifier": 0
        }
    ]
}
```

### chorus_fruit.json
```json
"minecraft:food:" {
    "nutrition": 4,
    "saturation_modifier": "low",
    "on_use_action": "chorus_teleport",
    "on_use_range": [
        8,
        8,
        8
    ],
    "cooldown_type": "chorusfruit",
    "cooldown_time": 20,
    "can_always_eat": true
}
```

### clownfish.json
```json
"minecraft:food:" {
    "nutrition": 1,
    "saturation_modifier": "poor"
}
```

### cooked_beef.json
```json
"minecraft:food:" {
    "nutrition": 8,
    "saturation_modifier": "good"
}
```

### cooked_chicken.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "normal"
}
```

### cooked_fish.json
```json
"minecraft:food:" {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

### cooked_porkchop.json
```json
"minecraft:food:" {
    "nutrition": 8,
    "saturation_modifier": "good"
}
```

### cooked_rabbit.json
```json
"minecraft:food:" {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

### cooked_salmon.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "good"
}
```

### cookie.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

### dried_kelp.json
```json
"minecraft:food:" {
    "nutrition": 1,
    "saturation_modifier": "poor"
}
```

### fish.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

### golden_apple.json
```json
"minecraft:food:" {
    "nutrition": 4,
    "saturation_modifier": "supernatural",
    "can_always_eat": true,
    "effects": [
        {
            "name": "regeneration",
            "chance": 1.0,
            "duration": 5,
            "amplifier": 1
        },
        {
            "name": "absorption",
            "chance": 1.0,
            "duration": 120,
            "amplifier": 0
        }
    ]
}
```

### golden_carrot.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "supernatural"
}
```

### honey_bottle.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "poor",
    "can_always_eat": true,
    "using_converts_to": "glass_bottle",
    "remove_effects": [
        "poison"
    ]
}
```

### melon.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "low"
}
```

### mushroom_stew.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

### muttonCooked.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "good"
}
```

### muttonRaw.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "low"
}
```

### poisonous_potato.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "low",
    "effects": [
        {
            "name": "poison",
            "chance": 0.6,
            "duration": 5,
            "amplifier": 0
        }
    ]
}
```

### porkchop.json
```json
"minecraft:food:" {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

### potato.json
```json
"minecraft:food:" {
    "nutrition": 1,
    "saturation_modifier": "low"
}
```

### pufferfish.json
```json
"minecraft:food:" {
    "nutrition": 1,
    "saturation_modifier": "poor",
    "effects": [
        {
            "name": "poison",
            "duration": 60,
            "amplifier": 3
        },
        {
            "name": "nausea",
            "duration": 15,
            "amplifier": 1
        },
        {
            "name": "hunger",
            "duration": 15,
            "amplifier": 2
        }
    ]
}
```

### pumpkin_pie.json
```json
"minecraft:food:" {
    "nutrition": 8,
    "saturation_modifier": "low"
}
```

### rabbit.json
```json
"minecraft:food:" {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

### rabbit_stew.json
```json
"minecraft:food:" {
    "nutrition": 10,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

### rotten_flesh.json
```json
"minecraft:food:" {
    "nutrition": 4,
    "saturation_modifier": "poor",
    "effects": [
        {
            "name": "hunger",
            "chance": 0.8,
            "duration": 30,
            "amplifier": 0
        }
    ]
}
```

### salmon.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

### spider_eye.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "good",
    "effects": [
        {
            "name": "poison",
            "chance": 1.0,
            "duration": 5,
            "amplifier": 0
        }
    ]
}
```

### suspicious_stew.json
```json
"minecraft:food:" {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl",
    "on_use_action": "suspicious_stew_effect"
}
```

### sweet_berries.json
```json
"minecraft:food:" {
    "nutrition": 2,
    "saturation_modifier": "low",
    "is_meat": false
}
```

# minecraft:hand_equipped
### appleEnchanted.json
```json
"minecraft:hand_equipped:" false
```

# minecraft:max_damage
### clownfish.json
```json
"minecraft:max_damage:" 0
```

### cooked_fish.json
```json
"minecraft:max_damage:" 0
```

### cooked_salmon.json
```json
"minecraft:max_damage:" 0
```

### fish.json
```json
"minecraft:max_damage:" 0
```

### pufferfish.json
```json
"minecraft:max_damage:" 0
```

### salmon.json
```json
"minecraft:max_damage:" 0
```

# minecraft:max_stack_size
### beetroot_soup.json
```json
"minecraft:max_stack_size:" 1
```

### honey_bottle.json
```json
"minecraft:max_stack_size:" 16
```

### mushroom_stew.json
```json
"minecraft:max_stack_size:" 1
```

### rabbit_stew.json
```json
"minecraft:max_stack_size:" 1
```

### suspicious_stew.json
```json
"minecraft:max_stack_size:" 1
```

# minecraft:seed
### beetroot_seeds.json
```json
"minecraft:seed:" {
    "crop_result": "beetroot"
}
```

### carrot.json
```json
"minecraft:seed:" {
    "crop_result": "carrots"
}
```

### melon_seeds.json
```json
"minecraft:seed:" {
    "crop_result": "melon_stem"
}
```

### nether_wart.json
```json
"minecraft:seed:" {
    "plant_at": "soul_sand",
    "crop_result": "nether_wart"
}
```

### potato.json
```json
"minecraft:seed:" {
    "crop_result": "potatoes"
}
```

### pumpkin_seeds.json
```json
"minecraft:seed:" {
    "crop_result": "pumpkin_stem"
}
```

### sweet_berries.json
```json
"minecraft:seed:" {
    "crop_result": "sweet_berry_bush",
    "plant_at": [
        "grass",
        "dirt",
        "podzol"
    ]
}
```

### wheat_seeds.json
```json
"minecraft:seed:" {
    "crop_result": "wheat"
}
```

# minecraft:stacked_by_data
### appleEnchanted.json
```json
"minecraft:stacked_by_data:" true
```

### clownfish.json
```json
"minecraft:stacked_by_data:" true
```

### cooked_fish.json
```json
"minecraft:stacked_by_data:" true
```

### cooked_salmon.json
```json
"minecraft:stacked_by_data:" true
```

### fish.json
```json
"minecraft:stacked_by_data:" true
```

### golden_apple.json
```json
"minecraft:stacked_by_data:" true
```

### pufferfish.json
```json
"minecraft:stacked_by_data:" true
```

### salmon.json
```json
"minecraft:stacked_by_data:" true
```

# minecraft:use_duration
### apple.json
```json
"minecraft:use_duration:" 32
```

### appleEnchanted.json
```json
"minecraft:use_duration:" 32
```

### baked_potato.json
```json
"minecraft:use_duration:" 32
```

### beef.json
```json
"minecraft:use_duration:" 32
```

### beetroot.json
```json
"minecraft:use_duration:" 32
```

### beetroot_soup.json
```json
"minecraft:use_duration:" 32
```

### bread.json
```json
"minecraft:use_duration:" 32
```

### camera.json
```json
"minecraft:use_duration:" 100000
```

### carrot.json
```json
"minecraft:use_duration:" 32
```

### chicken.json
```json
"minecraft:use_duration:" 32
```

### chorus_fruit.json
```json
"minecraft:use_duration:" 32
```

### clownfish.json
```json
"minecraft:use_duration:" 32
```

### cooked_beef.json
```json
"minecraft:use_duration:" 32
```

### cooked_chicken.json
```json
"minecraft:use_duration:" 32
```

### cooked_fish.json
```json
"minecraft:use_duration:" 32
```

### cooked_porkchop.json
```json
"minecraft:use_duration:" 32
```

### cooked_rabbit.json
```json
"minecraft:use_duration:" 32
```

### cooked_salmon.json
```json
"minecraft:use_duration:" 32
```

### cookie.json
```json
"minecraft:use_duration:" 32
```

### dried_kelp.json
```json
"minecraft:use_duration:" 16
```

### fish.json
```json
"minecraft:use_duration:" 32
```

### golden_apple.json
```json
"minecraft:use_duration:" 32
```

### golden_carrot.json
```json
"minecraft:use_duration:" 32
```

### honey_bottle.json
```json
"minecraft:use_duration:" 40
```

### melon.json
```json
"minecraft:use_duration:" 32
```

### mushroom_stew.json
```json
"minecraft:use_duration:" 32
```

### muttonCooked.json
```json
"minecraft:use_duration:" 32
```

### muttonRaw.json
```json
"minecraft:use_duration:" 32
```

### poisonous_potato.json
```json
"minecraft:use_duration:" 32
```

### porkchop.json
```json
"minecraft:use_duration:" 32
```

### potato.json
```json
"minecraft:use_duration:" 32
```

### pufferfish.json
```json
"minecraft:use_duration:" 32
```

### pumpkin_pie.json
```json
"minecraft:use_duration:" 32
```

### rabbit.json
```json
"minecraft:use_duration:" 32
```

### rabbit_stew.json
```json
"minecraft:use_duration:" 32
```

### rotten_flesh.json
```json
"minecraft:use_duration:" 32
```

### salmon.json
```json
"minecraft:use_duration:" 32
```

### spider_eye.json
```json
"minecraft:use_duration:" 32
```

### suspicious_stew.json
```json
"minecraft:use_duration:" 32
```

### sweet_berries.json
```json
"minecraft:use_duration:" 32
```

