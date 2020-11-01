---
layout: page
title: Changing Damage Colors
parent: Tutorials
---
# Command Tutorial
<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Intermediate
{: .label .label-yellow }


You may have thought to change the damage overlay color of the entity from that old boring red color.In this tutorial we will cover how to change damage color of any entity.
Before starting this tutorial you must have the basics of render controller so check the  [tutorial](/concepts/render-controller) of render controller.

# Let's Start


To change the damage overlay color  of any entity you want when it gets damage  we will use `is_hurt_color` and to change damage overlay color when an entity gets damage due to lava and fire we will use `on_fire _color`
For example if you want to make the damage overlay color to pink.
```json
{
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.lunae": {
            "geometry": "Geometry.default",
            "materials": [
                {
                    "*": "Material.default"
                }
            ],
            "textures": [
                "Texture.default"
            ],
               "is_hurt_color": {
                "r": "1.0",
                "g": "0.4",
                "b": "0.7",
                "a": "0.5"
            },
            "on_fire_color": {
                "r": "1.0",
                "g": "0.4",
                "b": "0.7",
                "a": "0.5"
            }

        }
    }
    }
```
You can change the damage color overlay just by putting different values in rgba.You can check out different websites to get the rgba values of all colors.
    



    
