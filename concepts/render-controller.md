---
layout: page
title: Render Controllers
parent: Concepts
---

# Render Controllers

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Beginner
{: .label .label-green }

Render controllers are an often-misunderstood part of the `Resource Pack`. But you don't need to be afraid! You should think of render-controllers as logic packs that take `short-name` definitions from the RP Entity File, and determine how they will be combined/layered/rendered in-game.

# Defining short-names

Render controllers work based on the short-name definitions of the RP entity file. Short-names are local identifiers, which we define in the RP entity file, and can then use in the render controller (and other places!). Variables such as `geometry`, `materials`, and `textures` can be defined in the entity,

Lets look at a simplified version of the spider RP entity file:

{% include filepath.html path="RP/entity/spider.json" %}
```json
{
    "format_version": "1.8.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "minecraft:cave_spider",
            "materials": {
                "default": "spider",
                "invisible": "spider_invisible"
            },
            "textures": {
                "default": "textures/entity/spider/cave_spider"
            },
            "geometry": {
                "default": "geometry.spider.v1.8"
            },
            "render_controllers": [
                "controller.render.spider"
            ]
        }
    }
}
```

In this case, four short-name definitions have been created:
 - `default`, in the materials array
 - `invisible`, in the materials array
 - `default`, in the textures array
 - `default`, in the geometry array

You can define multiple short-names in each array, such as in the `materials` example above.

You should think of short-name definitions as `importing` the assets you want. At this state, you are defining the textures, geometry, and materials that you want to use in your entity. In the render-controller stage, you won't import anything. You will simply use the assets you already imported to create the rendered entity.

# Simple render-controller

A simple render controller looks like this:

{% include filepath.html path="RP/render_controllers/cow.render.json" %}
```json
{
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.cow": {
            "geometry": "Geometry.default",
            "materials": [
                {
                    "*": "Material.default"
                }
            ],
            "textures": [
                "Texture.default"
            ]
        }
    }
}
```

This controller is taking the short-name definitions from the entity file, and `rendering` them. For example the line: `"textures": [ "Texture.default"]` says: "Take the default texture, and apply it to the entity". The render controller doesn't know what the default texture is, it simply applies it.

# Re-using render controllers

Since render controllers work based on short-names, it is possible to re-use the same render controller for all of your entities. For simple entities with one material, one texture, and one geometry, custom render controllers are not necessary.

For example, the render controller above is used for the `minecraft:cow` entity. If you want to use this render controller in your own pack, simple define like: `"render_controllers": [ "controller.render.cow" ]` in your entity file.

`warning:` Remember! Render controllers work based on short-names. If you want to use the cow render controller, you need to provide the short-names it is using. In this case, you will need to provide:
 - `default` geometry
 - `default` texture
 - `default` material

# Creating custom render controllers

 Often we want more power over the rendering of our entities, such as rendering layered textures, multiple geometries, or applying different materials to different bones. To create a custom render controller, simply copy and paste a vanilla render controller into the `render_controllers` folder, and edit to your liking!

# Texture layering

 Layering textures is currently written as a wiki article here: [Texture Layering](/tutorials/texture-layering).
