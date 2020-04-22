---
layout: page
title: Texture Layering
parent: Tutorials
---

# Texture Layering

sometimes, it is useful to create layered textures for custom entities. Layered in this context simply means multiple textures overlayed on top of each other, where the top texture has alpha pixels, and allows the bottom texture to show through.

As a very simple example, imagine a **painting** entity. The frame of the painting is always the same, but the picture itself can change. While you *could* duplicate the frame 10 times, and paint in 10 paintings, you now created a problem: What if you want to change the frame? Now you need to edit 10 textures. 

This can be solved by layering textures. Simply place the frame texture on first, and then add the different paintings on top. You can now edit the frame in one, simple location. 

Or, you could even create multiple frames for each painting! This allows you to create more variety in your panting entity, since the player can independently change two textures. 

# Render Controllers

Texture layering is achieved through the use of render controllers. If you aren't comfortable with render controllers, you should do some looking through the vanilla usages. Entities such as the `horse`, which contain multiple textures, are especially good to look at.

## Texture Layering

### Render Controller
```json
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.texture_layering": {
			"geometry": "Geometry.default",
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": [
                "Texture.bottom_layer",
                "Texture.top_layer"
			]
		}
	}
}
```

### Entity

You need to define all textures in the entity, and also use `entity_alphatest` material.
```json
"materials": {
    "default": "entity_alphatest"
},
"textures": {
    "top_layer": "textures/top",
    "bottom_layer": "textures/bottom"
}
```

## Texture Layering with Variance

While I guess hard-coding layered textures is cool, the real fun comes when you make the textures dynamic:

### Render Controller

```json
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.wool_only": {
			"arrays": {
				"textures": {
					"Array.top": [
						"Texture.top_1",
						"Texture.top_2",
						"Texture.top_3"
					]
				}
			},
			"geometry": "Geometry.default",
			"materials": [
				{
					"*": "Material.default"
				}
			],
			"textures": [
                "Texture.bottom
				"Array.top[query.variant]"
			]
		}
	}
}
```

By using arrays, and then `query.variant`, we are able to select the top texture based on the `variant` of the entity.


