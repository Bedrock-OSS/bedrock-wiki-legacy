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
        //You can add as many layers as you like. Layers are added top to bottom.
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
  //Add more texture short-name definitions here.
}
```

## Texture Layering with Variance

While I guess hard-coding layered textures is cool, the real fun comes when you make the textures dynamic:

### Entity

Set multiple top textures, which we will index into later.

```json
"textures": {
  "top_1": "textures/top_1",
  "top_2": "textures/top_2",
  "top_3": "textures/top_3",
  "bottom_layer": "textures/bottom"
}
```

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
        "Texture.bottom", //static bottom texture
        "Array.top[query.variant]" //pick top texture based on entity variant.
      ]
    }
  }
}
```

By using arrays, and then `query.variant`, we are able to select the top texture based on the `variant` of the entity.

### Setting variant

Now, to select which layer will show up, we can simply set the variant component in the entity:

Remember that components like variant are zero-indexed, which means `0` is our first texture, and then `1` and `2` point to the second and third.

```json
"minecraft:variant": {
  "value": 0
}
```

### Dynamically Changing Texture

If you want to dynamically change the texture of an entity during gameplay, you simply need to change the `variant`. This can be done using component groups and events.

### Dynamic Layered Textures

Dynamic layered textures can be achieved by adding more lists of textures, and other other dummy components as indexes. You can read about dummy components [here](https://wiki.bedrock.dev/tutorials/dummy_entities.html)
