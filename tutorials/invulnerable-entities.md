---
layout: page
title: Invulnerable Entities
parent: Tutorials
---

# Multiple Textures

This is a stub. More information will be added later.

## Using Damage Sensor:
```json
"minecraft:damage_sensor": {
    "triggers": {
    "on_damage": {
        "filters": {}
    },
    "deals_damage": false
        }
}
```

## With High Health:
```json
"minecraft:health": {
    "value": 800,
    "max": 800
}
```

## Filtering Damage:
Using `minecraft:damage_sensor`, you can create some very nice damage-filtering. For example, only being invincible to lighting, or only taking damage from  players.

The best way to learn about this component is by using the [vanilla examples for damage sensor.](https://sirlich.github.io/technical-bedrock/vanilla-usage/components-1.14.html#minecraftdamage_sensor)

### Filtering Damage Example:

```json
"minecraft:lightning_immune": {
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
}
```
