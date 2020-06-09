---
layout: page
title: Timers
parent: Tutorials
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

```json
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

```json
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

```json
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
```json
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

## Using animation timelines

For certain timing needs, the use of animation timelines might be the most natural. Animations timelines will not be covered extensively in this document, but you should know they exist. 

By triggering animations from an animation controller, you can execute specific events, commands, or molang expressions in a timed-sequence, called a timeline.

You can set up timelines like this:

```json
"format_version": "1.8.0",
	"animations": {
		"animation.command.example_timeline": {
			"timeline": {
				"0.0": "/say this will trigger instantly",
				"3.0": "/say this will trigger after 3 seconds"
            },
            "animation_length": 3
		},
		"animation.command.example_timeline_2": {
			"timeline": {
				"0.0": [
                    "/say you can trigger multiple events at once",
                    "/say by using timelines."
                ],
                "55.55": "/say this will trigger after 55.55 seconds.",
                "100": "/say this will trigger after 100 seconds"
            },
            "animation_length": 55.55
		}
	}
}
```

For more information about animations and timelines, you should check out the official documentation, or the other pages on this wiki.