---
layout: page
title: Retexturing Spawn Eggs
parent: Tutorials
---

# Retexturing Spawn Eggs

Everysingle custom entity will automatically be given a spawn egg. This spawn egg can be found inside of the creative menu, with a name like `item.spawn_egg.entity.sirlich:my_entity.name`. If you want to rename your spawn egg as well as set a texture, you can do so in the lang files. 

A common task is retexturing the spawn egg so it looks more like your spawned item, and less like an egg. 

## Adding the texture:
The first step is to add the texture file under `textures/items/`. I personally suggest creating an `eggs` folder to contain all the spawn egg textures. For example, `textures/items/eggs/my_entity.png`. The file itself should be square.

## Giving the texture a name:
Now we need to give our texture a short-name. This can be done by adding a new file: `textures/item_texture.json`.

```json
{
	"resource_pack_name": "My Map Name", //I don't actually know if this field does anything.
	"texture_name": "atlas.items",
	"texture_data": {
		"my_entity": {
			"textures": "textures/items/egg/my_entity"
		}
        //Add more spawn egg textures here
    }
```

## Using the new texture:
Now we can use our new texture inside of the Resource Pack entity file:

```json
"spawn_egg": {
    "texture": "my_entity",
    "texture_index": 0
}
```

