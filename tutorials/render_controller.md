---
layout: page
title: Render Controllers
parent: Tutorials
---

# Render Controllers

Render controllers are an often-missunderstood part of the Resource Pack ecosystem. You should think of render-controllers as logic packs that take short-name definitions from the Resource Entity File (from now on, the entity file), and determine how they will be combined/layered/rendered in-game.

# Defining short-names

Render controllers work based on the short-name definitions of the entity file. For example, variables such as `geometry`, `materials`, and `textures` can be defined in the entity, and then accessed in the render controller. For example, like this:

```json
"materials": {
    "default": "spider",
    "invisible": "spider_invisible"
},
"textures": {
    "default": "textures/entity/spider/cave_spider"
},
"geometry": {
    "default": "geometry.spider.v1.8"
}
```

In this case, four short-name definitions have been created:
 - `default`, in the materials array
 - `invisible`, in the materials array
 - `default`, in the textures array
 - `default`, in the geometry array

You can define multiple short-names in each array, such as in the `materials` example above. 

You should think of short-name definitions as `importing` the assets you want. At this state, you are bringing in textures, geometry, etc. In the render-controller stage, you won't import anything. You will simply use the assets you already imported to create the rendered entity.

# Simple render-controller 

A simple render controller looks like this:

```json
 {
  "format_version": "1.8.0",
  "render_controllers": {
    "controller.render.cow": {
      "geometry": "Geometry.default",
      "materials": [ { "*": "Material.default" } ],
      "textures": [ "Texture.default" ]
    }
  }
}
```

This controller is taking the short-name definitions from the entity file, and `rendering` them. For example the line: `"textures": [ "Texture.default"]` says: "Take the default texture, and apply it to the entity". The render controller doesn't what the default texture is, it simply applies it.

# Re-using render controllers

Since render controllers work based on short-names, it is possible to re-use the same render controller for all of your entities. For simple entities with one material, one texture, and one geometry, custom render controllers are not necesarry. 

For example, the render controller above is used for the `minecraft:cow` entity. If you want to use this render controller in your own pack, simple define like: `"render_controllers": [ "controller.render.cow" ]` in your entity file.

`warning:` Remember! Render controllers work based on short-named. If you want to use the cow render controller, you need to provide the short-names it is using. In this case, you will need to provide:
 - `default` geometry
 - `default` texture
 - `default` material

 # Creating custom render controllers

 Often we want more power over the rendering of our entities, such as rendering layered textures, multiple geometries, or applying different materials to different bones. To create a custom render controller, simply copy and paste a vanilla render controller into the `render_controllers` folder, and edit to your liking!

 # Texture layering

 Layering textures is currently written as a wiki article here: [Texture Layering](https://wiki.bedrock.dev/tutorials/texture_layering.html).

