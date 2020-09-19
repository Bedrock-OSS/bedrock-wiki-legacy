---
layout: page
title: Adding Sounds
parent: Tutorials
---

# Adding Sounds

Intermediate
{: .label .label-yellow }

In bedrock, we have the ability to add custom sounds, without overwriting any vanilla sounds. This is done by adding files to the resource pack. 

`protip:` The best way to learn about sounds is downloading and playing around with the default resource pack.

## Folder Structure
There are two main files that we edit when we want to add sounds. Note how `sound_definition` is nested inside `sounds`.

```
└───example_RP
    │   sounds.json
    └───sounds
            sound_definitions.json
```

## Sound Formats

The following sound formats are accepted:
 - ogg (recommended)
 - wav
 - fsb

# sound_definitions.json

`sound_definitions.json` is where we define new sound short-names. This should be thought of as typing a `short-name` or `id` to a physical sound path. Here is an example `sound_definitions.json` that adds a new trumpet sound.

```json
{
    "dirt.roar": {
        "category": "neutral",
        "sounds": [
            "sounds/trumpet"
        ]
    }
}
```

Sounds added in this way can be triggered using `/playsound`. Please note that `playsound` does not auto-correct, so you will need to be careful in your typing. 

`note:` New files that are referenced by file path, such as sounds, DO need a full client restart in order to load. This means that if sounds don't work, you should restart your entire MC client, rather than just reloading the world.

## Top Level Keys

In the example above, I showed two `top-level` fields: `category`, and `sounds`. Sounds will be discussed in further detail bellow, but the other `top-level` keys will be discussed here:

### Categories

Categories are used internally by the engine to decide how each sound is played. We can utilize different channels to get different effects. 

| Category | Note |
|----------|------|
| weather  |      |
| block    |      |
| bucket   |      |
| bottle   |      |
| ui       |      |
| player   |      |
| hostile  |      |
| music    |      |
| record   |      |
| neutral  |      |

### min_distance

WIP

### max_distance

WIP

## Sound definitions

In the example above, I showed `sounds` as simply a list with a single path. This is good for simple sounds, but does not have much power. For starts, I can add multiple sounds into the list. These sounds will be randomized when played:
```json
"sounds": [
    "sounds/trumpet",
    "sounds/trumpet2",
    "sounds/trumpet3"

]
```

Second, we can define each sound as an object, instead of a string. This allows us finer control, and unlocks some new settings. The string/object style can be mixed and matched.

### name

The path to the file, such as: `"sounds/music/game/creative/creative1"`

### stream

WIP

### volume

How loud the sound should play, from `0.0` to `1.0`. Sounds cannot be made louder than originally encoded.

### load_on_low_memory

WIP

### pitch

The pitch of the sound (how low/high it sounds). Ranges from `0.0` to `1.0` (normal), but can be higher, such as `1.48`.

## Example

Here is a more realistic example containing these options:
```json
"block.beehive.drip": {
    "category": "block",
    "max_distance": 8,
    "sounds": [
        {
            "name": "sounds/block/beehive/drip1",
            "load_on_low_memory": true
        },
        "sounds/block/beehive/drip2",
        "sounds/block/beehive/drip3",
        "sounds/block/beehive/drip4"
    ]
}
```
# sounds.json

If we want our sounds to run automatically, we can add them into the `sounds.json` file. This will tie the sound definitions directly to the entity.

Note that when adding sounds this way, you don't need to trigger them using a `playsound` or anything. The step and ambient will play automatically, based on their configured triggers.

Sounds in Minecraft are added in one of multiple categories:
 - **individual_event_sounds:** Contains sounds like beacon activation, chest-close, or explode.
 - **block_sounds:** Contains hit, step, and break sounds for blocks.
 - **entity_sounds:** Contains death, ambient, hurt, etc sounds for entities (Including custom ones!)
 - **interactive_sounds:**
   - **block_sounds:** (Needs citation, I don't know what this is for)
   - **entity_soundsS:** (Needs citation, I don't know what this is for)

I assume that sounds can be added in other categories, but I personally have experience adding sounds into the entities category. Entity sounds are automatically played at various points in the entities life-cycle:
 - **ambient**: Played randomly, such as grunts, clucks, or ghast noises
 - **hurt**: Played when damaged
 - **death**: Played when it dies
 - **step**: Played when the entity moves along the ground

There are also many sound definitions, which *most likely* trigger automatically, but which I don't have details for, such as:
 - breathe
 - attack
 - splash
 - swim
 - ambient.in.water
 - death.in.water
 - jump
 - eat
 - hurt.in.water
 - mad
 - stare
 - sniff
 - attack
 - sleep
 - spit
 - ambient
 - shoot
 - warn
 - scream

```json
{
    "entity_sounds": {
        "entities": {
            "sirlich:elephant": {
                "volume": 1,
                "pitch": [
                    0.9,
                    1.0
                ],
                "events": {
                    "step": {
                        "sound": "elephant.step",
                        "volume": 0.18,
                        "pitch": 1.1
                    },
                    "ambient": {
                        "sound": "elephant.trumpet",
                        "volume": 0.11,
                        "pitch": 0.9
                    }
                }
            }
        }
    }
}
```
