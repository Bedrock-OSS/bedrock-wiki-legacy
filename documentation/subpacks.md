---
layout: page
title: Subpacks
parent: Documentation
---

# Subpacks

## What are subpacks?

Subpacks are what cause the gear icon to appear on packs.
They were originally intended for texture resolutions to 
load on different memory capacities, but can also be use 
to create file variations in behavior and resource packs 
which can then be chosen by clicking the gear icon and 
adjusting the slider.

## Creating subpacks

- To start adding a subpack you need to create a `subpacks` folder inside 
the root of your BP or RP.
- Then inside the `subpacks` folder add a folder for each subpack 
you want to have
e.g.
```
\---subpacks
    +---subpack_1
    +---other_subpack
```
- Inside each of these folders you can add the content of each subpack.
This can be anything that normally goes in your behavior or resource pack.
e.g.
```
\---subpacks
    +---subpack_1
         +---textures
              +---blocks
              |      dirt_1.png
              |
          +---items
          |      item_example.json
          |
    +---other_subpack
         +---textures
              +---blocks
              |      dirt_2.png
              |
```

## Adding subpacks to manifests

To register the subpacks in the manifest 
you need to add `subpacks` and this contains 
an array of subpacks.
Example:
```jsonc
{
     "format_version": 2,
     "header": {
          "name": "Pack Name",
          "description": "Pack Description",
          "uuid": "2fc2dd6f-86cb-4370-af70-21490a1ae471",
          "version": [1, 0, 0],
          "min_engine_version": [1, 13, 0]
     },
     "modules": [
          {
               "type": "data",
               "uuid": "f6821b4a-1854-44fc-a8a4-0c2847ffda46",
               "version": [1, 0, 0]
          }
     ],
     "subpacks": [
          {
               "folder_name": "subpack_1",
               "name": "First Subpack",
               "memory_tier": 0
          },
          {
               "folder_name": "other_subpack",
               "name": "Other Subpack",
               "memory_tier": 1
          }
     ]
}
```
- name
Defines the name that will show when selecting the subpacks.

- memory_tier
A number specifying the order of the subpacks on the slider. (Starts at 0)

- folder_name
This corresponds to the name of the folder to be used in this subpack, for 
example in the examples above this would be "subpack_1" or "other_subpack"
