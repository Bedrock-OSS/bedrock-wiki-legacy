---
layout: page
title: Changing the speed of an animation
parent: Tutorial
---

# Changing the speed of an animation
It is faster for a developer to tweak an animation without the help of BlockBench, just by editing the raw .json file, but it can be daunting to manually fix every keyframe in an animation, even for the slightest of changes.

Luckly for us, we can just multiply the default value of `anim_time_update` to change the whole animation's speed however we please.

```json
{
    "format_version": "1.8.0",
    "animations": {
        "animation.myentity.myanimation": {
            "anim_time_update":"2 * query.delta_time + query.anim_time"
            //My animation goes here!
            //This will simply make the animation run 2 times faster.
            //We can tweak the value to any positive float, so we can even slow down animations
            //With 0.5 for example, the animation will run 2 times slower
        }
    }
}
```
