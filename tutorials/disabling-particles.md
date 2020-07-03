---
layout: page
title: Disabling Particles 
parent: Tutorials
---

The basic idea of disabling a particle from emitting (as opposed to simply making the texture transparent) is as follows:

```json
{
    "format_version": "1.10.0",
    "particle_effect": {
        "description": {
            "identifier": "minecraft:some_vanilla_particle",
            "basic_render_parameters": {
                "material": "particles_alpha",
                "texture": "textures/particle/particles"
            }
        },
        "components": {
            "minecraft:emitter_lifetime_expression": {
                "activation_expression": 0,
                "expiration_expression": 1
            },
            "minecraft:emitter_rate_manual": {
                "max_particles": 0
            }
        }
    }
}
```

---
### **Original Author:** [ambientturtle](ambient#2309)