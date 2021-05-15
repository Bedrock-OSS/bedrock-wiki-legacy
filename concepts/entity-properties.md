---
layout: page
title: Entity Properties
parent: Concepts
badge: BETA
badge_color: red
---

# Entity Properties [BETA]

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

* Documentation on the new Entity Properties, also known as Actor Properties introduced in the 1.16.230.50 Minecraft: Bedrock Edition beta version.
* Entity Properties were implemented to save data, or store values on entities efficiently without needing the use of components, or attributes (For example "minecraft:variant") in server-side of the entity (Behavior Pack), similar to Block Properties.
------------------
## Entity Properties Definitions

### Defining Properties on Entities

* Entity Properties Definition:
```jsonc
{
  "minecraft:entity": {
    "description": {
      "identifier": "entity:properties_test",
      "properties": {
        "property:number_range_example": {
          "values": {
            "min": 0,
            "max": 100
          }
        },
        "property:number_enum_example": {
          "values": [0, 1, 2, 3]
        },
        "property:string_enum_example": {
          "values": ["first", "second", "third"]
        },
        "property:boolean_enum_example": {
          "values": [true, false]
        }
      }
    }
  }
}
```
------------------
### Entity Properties Optional Fields
#### `default`
* You can set the default value of the entity property (By default, the first value of the enum array index), through the <code>default</code> field inside the defined property object:
```jsonc
"property:default_value_example": {
  "values": [true, false],
  "default": false
}
```
* As you can observe, the default property is set to `false` instead of `true` when the entity is spawned in the world.

#### `client_sync`
* To sync through the Resource Pack (client-side), <code>client_sync</code> field can be used to allow the Client Entity access the Entity Properties. By default, the value is set to `false`.
```jsonc
"property:client_sync_example": {
  "values": {
    "min": 0,
    "max": 20
  },
  "client_sync": true
}
```
------------------
### Manipulating and Accessing Entity Properties
* You can access entity properties though MoLang Entity Queries:
  * `query.actor_property`
  * `query.has_actor_property`

* Through entity events, you can set the entity property to a value with the `set_actor_property` event response:
```jsonc
"events": {
  "event:set_entity_property": {
    "set_actor_property": {
      "property:number_enum_example": 2,
      "property:string_enum_example": "'second'",
      "property:boolean_enum_example": "!query.actor_property('property:boolean_enum_example')"
    }
  }
}
```
------------------
## Entity Permutations
* Entity Permutations are implemented to apply a set of components every tick if the condition met.
* `permutations` array is inserted in the `minecraft:entity` object:
```jsonc

```

