---
layout: page
title: Items [BETA]
parent: Concepts
---

# Items [Beta]

Better documentation on the new item format introduced in the 1.16.100.56 Minecraft beta
## Item Events

### Using Events

```json
{
  "format_version": "1.16.100",
  "minecraft:item": {
    "description": {
      "identifier": "example:food_item",
      "category" : "items"
    },
    "components": {
      "minecraft:use_duration": 1.6,
      "minecraft:food": {
        "nutrition": 4,
        "saturation_modifier": "low",
        "can_always_eat": true,
        "on_consume": {
          "event": "on_consume",
          "target": "self"
        }      
      }
    },
    "events": {
      "on_consume": {
        "remove_mob_effect": {
          "effect": "nausea",
          "target": "holder"
        }
      }
    }
  }
}
```

### Event Functions

#### `swing`
```json
{
    "example:swing_event": {
        "swing": {}
    }
}
```

#### `shoot`
Shoots a projectile when triggered
```json
{
    "example:shoot_event": {
        "shoot": {
            "projectile": "minecraft:snowball",
            "launch_power": 5,
            "angle_offset": 20
        },
    }
}
```

#### `damage`
```json
{
    "example:damage_event": {
        "damage": {
            "type": "magic",
            "amount": 4
        }
    }
}
```

#### `add_mob_effect`
Adds a mob effect when triggered
```json
{
    "example:effect_event": {
        "add_mob_effect": {
            "effect": "poison",
            "target": "holder",
            "duration": 8,
            "amplifier": 3
        }
    }
}
```

#### `remove_mob_effect`
Removes a mob effect when triggered
```json
{
    "example:remove_effect_event": {
        "remove_mob_effect": {
            "effect": "poison",
            "target": "holder"
        }
    }
}
```

#### `transform_item`
Transforms the item into the item specified
```json
{
    "example:transform_event": {
        "transform_item": {
            "transform": "minecraft:apple"
        }
    }
}
```

#### `teleport`
Teleports the target to a random location in the specified range
```json
{
    "example:teleport_event": {
        "teleport": {
            "target": "holder",
            "max_range": [8, 8, 8]
        }
    }
}
```

#### `sequence`
Used to sequence event functions
```json
{
	"example:sequence_event": {
		"sequence": [
			{
				"add_mob_effect": {
                    "effect": "poison",
                    "target": "holder",
                    "duration": 8,
                    "amplifier": 3
                }
			},
			{
				"transform_item": {
                    "transform": "minecraft:apple"
                }
			}
		]
	}
}
```

#### `randomize`
Used to randomize event functions
```json
{
   "example:randomize_events": {
        "randomize": [
            {
                "weight": 1,
				"transform_item": {
                    "transform": "minecraft:apple"
                }
            },
            {
                "weight": 2,
                "add_mob_effect": {
                    "effect": "weakness",
                    "target": "holder",
                    "duration": 8,
                    "amplifier": 3
                }
            },
        ]
    } 
}
```

#### `execute_command`
Used to execute commands
_This seems to be broken as of 1.16.100.56_
```json
{
    "example:execute_command_event": {
        "execute_command": {
            "command": ["say hi"]
        }
    }
}
```

## BP Item Components

List of all new block components, with usage examples

- minecraft:ignores_permission
```json
{
  "minecraft:ignores_permission": true
}
```

- minecraft:mining_speed
```json
{
  "minecraft:mining_speed": 1
}
```

- minecraft:damage
```json
{
  "minecraft:damage": true
}
```

- minecraft:can_destroy_in_creative
```json
{
  "minecraft:can_destroy_in_creative": true
}
```

- minecraft:dye_powder
```json
{
  "minecraft:dye_powder": {
      "color": 4
  }
}
```

- minecraft:mirrored_art
```json
{
  "minecraft:mirrord_art": true
}
```

- minecraft:explodable
```json
{
  "minecraft:explodable": true
}
```

- minecraft:should_despawn
```json
{
  "minecraft:should_despawn": true
}
```

- minecraft:liquid_clipped
```json
{
  "minecraft:liquid_clipped": true
}
```

- minecraft:allow_off_hand
```json
{
  "minecraft:allow_off_hand": true
}
```

- minecraft:projectile
```json
{
  "minecraft:projectile": {
      "projectile_entity": "minecraft:arrow",
      "minimum_critical_power": 0.5
  }
}
```

- minecraft:block_placer
```json
{
    "minecraft:block_placer": {
      "block": "minecraft:grass",
      "use_block_description": true
    }
}
```

- minecraft:entity_placer
```json
{
    "minecraft:entity_placer": {
      "entity": "minecraft:zombie",
      "use_on": [
          "minecraft:grass",
          "minecraft:sand"
        ],
        "dispense_on": [
            "minecraft:stone",
            "minecraft:gold_ore"
        ]
    }
}
```

- minecraft:use_on
```json
{
    "minecraft:use_on": {
        "on_use": {
            "event": "example:block_event",
            "target": "block"
        }
    }
}
```

- minecraft:knockback_resistance
```json
{
    "minecraft:knockback_resistance": {
      "protection": 0.4
    }
}
```

- minecraft:enchantable
```json
{
    "minecraft:enchantable": {
      "slot": "bow",     // Can be any of the enchant slot listed below
      "value": 10
    }
}
```

### Enchant slots

| Slot Name     |
|---------------|
| bow           |
| armor_feet    |
| armor_torso   |
| armor_head    |
| armor_legs    |
| hoe           |
| axe           |
| pickaxe       |
| shovel        |
| sword         |
| elytra        |
| fishing_rod   |
| flintsteel    |
| shears        |
| cosmetic_head |

- minecraft:shooter
```json
{
    "minecraftshooter": {
        "max_draw_duration": 1,
        "charge_on_draw": false,
        "scale_power_by_draw_duration": true,
        "ammunition": [
            {
                "item": "minecraft:arrow",
                "use_offhand": true,
                "search_inventory": true,
                "use_in_creative": true
            }
        ]
    }
}
```

- minecraft:damageable
```json
{
    "minecraft:damageable": {
        "max_damage": 100,
        "damage_chance": {
            "min": 5,
            "max": 10
        }
    }
}
```

- minecraft:armor
```json
{
    "minecraft:armor": {
        "protection": 4
    }
}
```

- minecraft:wearable
```json
{
    "minecraft:wearable": {
        "slot": "slot.armor.feet"
    }
}
```

- minecraft:weapon
```json
{
    "minecraft:weapon": {
        "on_hurt": {
            "event": "example_event",
            "target": "holder"      // Can also be 'self' to trigger an item event"
        }
    }
}
```

- minecraft:record
```json
{
    "minecraft:record": {
        "sound_event": "cat",
        "duration": 120,
        "comparator_signal": 8
    }
}
```

- minecraft:repairable
```json
{
    "minecraft:repairable": {
        "repair_items": [
            {
                "items":[
                    "minecraft:iron_ingot",
                    "minecraft:gold_ingot"
                ],
                "repair_amount": 10,  // Can also be molang expression
                "on_repaired": {
                    "event": "example_event",
                    "target": "holder"    // Can also be 'self' to trigger an item event"
                }
            }
        ]
    }
}
```

- minecraft:cooldown
```json
{
    "minecraft:cooldown": {
        "category": "ender_pearl",
        "duration": 1
    }
}
```

- minecraft:digger
```json
{
    "minecraft:digger": {
        "use_efficiency": true,
        "destroy_speeds": [
            {
                "block": {
                    "tags": "query.any_tag('stone', 'metal')"
                },
                "speed": 6
            }
        ]
    }
}
```

- minecraft:fertilizer
```json
{
    "minecraft:fertilizer": {
        "type": "bonemeal" // Can also be "rapid"
    }
}
```

- minecraft:fuel
```json
{
    "minecraft:fuel": {
        "duration": 20
    }
}
```

- minecraft:throwable
```json
{
    "minecraft:throwable": {
        "do_swing_animation": true,
        "max_draw_duration": 2,
        "scale_power_by_draw_duration": true
    }
}
```

- minecraft:creative_category
```json
{
    "minecraft:creative_category": {
        "parent": "itemGroup.name.nature"
    }
}
```

- minecraft:food
_New Syntax_
```json
{
    "minecraft:food": {
        "on_consume": {
            "event": "example_event",
            "target": "holder"  // Can also be 'self' to trigger an item event"
        },
        "nurtition": 3,
        "can_always_eat": true,
        "saturation_modifier": "normal"
    }
}
```

## Breaking changes

If your item isn't showing up in the beta, these changes might have broken your item.

- Item behavior files now require a "category" to show up in the /give command and creative inventory.
Example:
```json
{
  "format_version": "1.16.100",
  "minecraft:item": {
    "description": {
      "identifier": "example:item",
      "category" : "items"     // This line is required
    },
    "components": {...},
    "events": {...}
  }
}
```