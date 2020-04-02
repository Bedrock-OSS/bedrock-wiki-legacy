---
layout: page
title: Useful Links
parent: Timers
---

# Timers

Timers are a useful tool for making custom entities. The minecraft bedrock engine provides the `minecraft:timer` component, which can be used to trigger an event after a set time (or a random range).

In the vannila Behavior Pack, it is used in all kinds of circumstances. For example: 
 - The dolphin can only spend 20 seconds on land before it dries out.
 - zombies underwater will convert to drowned in 30 seconds.
 - The wandering trader will only stay for either 2400 or 3600 seconds. 

In short, you can use this component to create time-based interactions.

## minecraft:timer

The syntax for this component can be found [here](https://bedrock.dev/1.14.0.0/1.14.0.6/Entities#timer).

An example usage would be:

```JSON
"minecraft:timer": {
    "time": 5,
    "time_down_event": {
        "event": "namespace:my_event"
    }
}
```

## Multiple timers

Sometimes, it is useful to define multiple timers. As we all know, duplicate components replace each other, meaning that defining multiple timers using the `minecraft:timer` component isn't possible.

We can get around this by using dummy-timers, such as `minecraft:ageable`. As long as you aren't planning on using the component for something else, you can use it as a second timer.

That might look something like this:

```JSON
"minecraft:is_baby": {},
"minecraft:ageable": {
    "duration": 4,
    "grow_up": {
        "event": "namespace:my_other_event",
        "target": "self"
    }
}
```
Just make sure to also include the `minecraft:is_baby` component, which is required for the ageable component to work.

### Other dummy-timers:
I've never needed more than two timers at once, but taking a peak at the docs suggest there are others that can be used.

Some promising examples:
- `minecraft:angry`
- `minecraft.behavior.hide`
- `minecraft:behavior.celebrate`

Essentially, you are looking for any component with a "time down event" or a "duration".

## Tickers

Another good way to handle time events is using a single, looping `minecraft:timer` component, and then handle the events on each tick. 

Simply use randomize with weight to determine how often events will be run. This is a good way to get extra mileage out of the single timer component. 

A solution might look like this:

```JSON
"sirlich:do_tick": {
    "randomize": [
        {
            "weight": 1,
            "add": {
                "component_groups": [
                    "sirlich:my_event"
                ]
            }
        },
        {
            "weight": 5,
            "add": {
                "component_groups": [
                    "sirlich:my_more_frequent_event"
                ]
            }
        },
        {
            "weight": 50 //do nothing!
        }
    ]
}
```

## Time sensing:

Another possibility is to use `minecraft:environment_sensor` with the `hourly_clock_time` or `clock_time` filters.

A solution of this form might look like this:
```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                { "test": "hourly_clock_time", "operator": "=", "value": 800 }
                ]
            },
            "event": "namespace:my_daily_event"
        }
    ]
}
```

Hopefully this spread some light on the subject of handling time in Minecraft Bedrock!