# Adding Sounds

You can add unique sounds in Bedrock, without overwriting existing sound files. This is done by editing information in the Resource Pack.

`protip:` The best way to learn about sounds is downloading and playing around with the default resource pack.

There are two files you will need to edit:
 - `sounds.json`, which is found at the top-level of the resource pack.
 - `sounds/sound_definitions.json`, note the nesting inside of the `sounds` folder.

Additionally, you will need to include the actual sound files. This isn't an exhaustive list, but I believe that `.ogg` and `.wav` are supported. These files can be included inside the sounds folder, for example `sounds/elephant/trumpet.wav`.

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

Here is an example of adding step, and ambient sound-definitions for an imaginary elephant mob.

Note that when adding sounds this way, you don't need to trigger them using a `playsound` or anything. The step and ambient will play automatically, based on their configured triggers.
 
## sounds.json
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

## sounds/sound_definitions.json
```json
{
	"elephant.step": {
		"category": "neutral",
		"sounds": [
			"sounds/elephant/step"
		]
	},
	"elephant.trumpet": {
		"category": "neutral",
		"sounds": [
			"sounds/elephant/trumpet"
		]
	}
}
```