---
layout: page
title: Blocks
parent: Documentation
---

# Blocks

Better documentation on the new block format introduced in the 1.16.100.56 Minecraft beta
## Block Properties

Defining Properties:

```json
{
    "minecraft:block": {
        "description": {
            "identifier": "example:my_block",
            "properties": {
                "example:string_property_example": ["red", "green", "blue", "purple"],
                "example:boolean_property_example": [true, false],
                "example:integer_property_example": [1, 2, 3, 4, 5]
            }
        }
    }
}
```

Using Properties:

Properties can be queried with `query.block_property`, like this:
`query.block_property('example:string_property_example') == 'blue'`

## Block Events

Using Events:

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "example:my_block"
    },
    "components": {
      "minecraft:on_step_on": {
        "event": "example:drop_loot",
        "target": "self"
      }
    },
    "events": {
      "example:drop_loot": {
        "spawn_loot": "loot_tables/blocks/my_loot_table.json"
      }
    }
  }
}
```

This example spawns a loot table when an entity stands on the block.

### Event functions:

#### `spawn_loot`
Summons a loot table when the event is triggered.
```json
{
    "example:drop_loot": {
        "spawn_loot": "loot_tables/blocks/my_loot_table.json"
    }
}
```

#### `set_block`
Removes the current block and replaces it with the defined block in the same position.
```json
{
    "example:place_block": {
        "set_block": "minecraft:grass"
    }
}
```

#### `set_block_property`
Used to set the value of a block's property
```json
{
    "example:change_color": {
        "set_block_property": {
            "example:string_property_example": "red"
        }
    }
}
```

#### `set_block_at_pos`
Used to set a block releative to this blocks position

#### `trigger`
Used to trigger an event, this can be a block event or an entity event.
```json
{
    "example:trigger_event": {
        "trigger": {
            "condition": "query.block_property('example:can_trigger_event') == true",
            "event": "example:my_event",
            "target": "self"              // If set to "other" an entity event can be defined, it will be triggered on the entity that causes the block event
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
				"set_block_property": {
					"test:my_prop": true
				}
			},
			{
				"trigger": {
					"event": "example:my_entity_event",
					"target": "other",
					"conditions": "query.block_propertry('test:my_prop') == true"
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
                "set_block_property": {
                    "example:boolean_property_example": false
                }
            },
            {
                "weight": 2,
                "set_block_property": {
                    "example:boolean_property_example": true
                }
            },
            {
                "weight": 4,
                "set_block": "minecraft:stone"
            }
        ]
    } 
}
```
### Triggering Events

Block components to trigger block events:

- `minecraft:on_interact`
- `minecraft:on_step_on`
- `minecraft:on_step_off`
- `minecraft:on_fall_on`
- `minecraft:on_placed`
- `minecraft:on_player_placing`

- `minecraft:ticking` and `minecraft:random_ticking` can both be used to trigger events after a set amount of time or at random times depending on which component you use


## Block Permutations

Block permutations are a way of conditionally applying components to a block with molang expressions.

Example:

```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "example:my_block",
      "properties": {
        "example:custom_integer_property": [ 10, 20, 30, 40 ],
        "example:custom_boolean_property": [ false, true ],
        "example:custom_string_property": [ "red", "green", "blue" ]
      }
    },
    "components": {...},
    "permutations": [
      {
        "condition": "query.block_property('test:custom_int_property') == 20",
        "components": {
          "minecraft:friction": 0.1
        }
      },
      {
        "condition": "query.block_property('test:custom_bool_property') == true",
        "components": {
          "minecraft:destroy_time": 0.5
        }
      },
      {
        "condition": "query.block_property('test:custom_str_property') == 'red'",
        "components": {
          "minecraft:geometry": "geometry.pig"
        }
      }
    ]
  }
```

## Block Tags

_Needs more information_

Block tags can be given to blocks to be queried or referenced with `any_tag` which is used inside item and entity files.
A tag can be applied like this:
```json
{
  "format_version": "1.16.100",
  "minecraft:block": {
    "description": {
      "identifier": "example:my_block",
    },
    "components": {
      "tag:example:my_tag": {}
    }
  }
```

and this tag can be queried with:
- `query.all_tags`
- `query.any_tag`
- `query.equipped_item_all_tags`
- `query.equipped_item_any_tag`
- `query.block_has_all_tags`
- `query.block_has_any_tag`
- `query.relative_block_has_all_tags`
- `query.relative_block_has_any_tag`