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
* Entity Properties were implemented to save data on entities efficiently without needing the use of components, or attributes (For example "minecraft:variant").

## Entity Properties Definitions

Defining Properties:

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
```


