---
layout: page
title: Resource Folder Schema
parent: Documentation
---

# Resource Pack Folder Schema

This shows the top-level folder/file structure for a resource pack. Additional folder nesting can be used as needed.

```
\---example_RP
    |   biomes_client.json
    |   manifest.json
    |   pack_icon.png
    |   sounds.json
    |   
    +---animations
    |       example.animation.json
    |       
    +---animation_controllers
    |       example.animation_controller.json
    |       
    +---entity
    |       exampl.entity.json
    |       
    +---items
    |       example.item.txt
    |       
    +---models
    |   \---entity
    |           example.geo.json
    |           
    +---particles
    |       example.particle.json
    |       
    +---render_controllers
    |       example.render_controller.json
    |       
    +---sounds
    |       example.sound.ogg
    |       sound_definitions.json
    |       
    +---texts
    |       en_US.lang
    |       languages.json
    |       
    \---textures
        |   item_texture.json
        |   
        +---blocks
        |       example.block.png
        |       
        +---entity
        |       example.entity.png
        |       
        +---items
        |       example.item.png
        |       
        \---particle
                example.particle.png
```