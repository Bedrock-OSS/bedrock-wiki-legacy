---
layout: page
title: Custom Item Models
parent: Tutorials
---

**Warning:** this tutorial assumes you have a basic understanding of MoLang, render controllers and client entity definitions. Make sure to check out the [tutorial](/tutorials/render-controller) on render controllers before starting this tutorial.

## Concept & Idea

Since Bedrock doesn't support custom item models out of the box, we have to get creative with their implementation. The idea behind this concept is very simple: we overlay an entity model onto the player model with the help of a render controller and adjust the display settings with a few animations.

## The Item

First of all, we need to make sure our item is ready. You can add custom models to both custom and vanilla items. In this tutorial, we will be making an automatic drill. We won't be going in depth on how to create custom items in this tutorial, but you can use [this](https://gitwither.github.io/bedrock-item-generator/) online custom item generator. Make sure your item has got a texture and displays properly in the player's inventory.

![](/assets/images/tutorials/custom-item-models/drill-sprite-inventory.png)

## Geometry

Before implementing your custom item model into the game, make sure your item geometry is ready to be used. For your item to render correctly inside a player's hand, it must contain the player's bone skeleton. This means that your item model must contain all of the bones the player model has **without their respective elements (the player's bones must be empty!)**. Export it with a unique identifier. In our case it will be `geometry.drill`. A geometry file example is present at the end of the file.

![](/assets/images/tutorials/custom-item-models/drill-bone-structure.png)

## Client Player Definition

This is the most important part. For our model to render inside a player's hand, we must add it to the player entity client definition. This step consists of several parts:
1. Defining a variable that tells us whether the player is currently holding our item.
2. Defining the textures and the geometry of our model in the player client definition.
3. Creating a conditional render controller that adds the model geometry whenever the player holds our item.
4. Creating animations that position our item correctly in first person.

Let's start by defining the texture and the geometry of our item in the player client definition file. Copy the `player.entity.json` file from the [Vanilla Resource Pack](https://aka.ms/resourcepacktemplate) into the `entity` folder of your resource pack. Open the file, find the `geometries` JSON object, and add a new entry to the `geometries` object:
```json
"geometry": {
    ...,
    "<your_item_name>": "geometry.<your_geometry_id>"
}
```
In our case it will look like this:
```json
"geometry": {
    ...,
    "drill": "geometry.drill"
}
```

Next, add a new entry to your `textures` entry that references the texture of your model:
```json
"textures": {
    ...,
    "<your_item_name>": "path/to/texture"
}
```

In our case it will look like this:
```json
"textures": {
    ...,
    "drill": "textures/items/models/drill"
}
```

Now, let's define the variable that tells us whether the player is holding our item. In your player's `scripts.pre_animation` array, add a new entry: 
`variable.<your_item> = query.get_equipped_item_name('main_hand') == <your_item_identifier_without_namespace>`
In our case, this entry will look like the following:

```json
"pre_animation": [
    ...,
    "variable.drill = query.get_equipped_item_name('main_hand') == 'drill';"
]

```
Note: it is important to define this variable because checking for the item directly in the render controller can yield delays when switching between items.

## Render Controller
Next, let's create a render controller that will render our item. Create a new file in the `render_controllers` folder of your resource pack called `<your_item_name>.render_controllers.json`. In our case it will be `drill.render_controllers.json`
```json
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.<your_item_name>": {
			"textures": [
				"Texture.<item_texture>" //Tis is the texture you defined in the 'textures' object in player.entity.json
			],
			"geometry": "Geometry.<item_geometry>", //This is the geometry you defined in the 'geometries' object in player.entity.json
			"materials": [
				{
					"*": "Material.default"
				}
			]
		}
	}
}
```
In our case, the render controller will look like the following:
```json
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.drill": {
			"textures": [
				"Texture.drill"
			],
			"geometry": "Geometry.drill",
			"materials": [
				{
					"*": "Material.default"
				}
			]
		}
	}
}
```

Now, let's add this render controller to our player client definition file. Add a new object to the `render_controllers array like so:
```json
"render_controllers": [
    ...,
    {
        //This is the ID of the render controller that you created in the previous step
        "controller.render.<your_item>": "variable.<your_item>" //This is the variable you defined in the 'pre_animation' array
    }
]
```

In our case, it will look like this:
```json
"render_controllers": [
    ...,
    {
        "controller.render.drill": "variable.drill"
    }
]
```

## Animations
This part contains an unnecessary step - creating custom animations for the item, but we will go over it anyway. Let's start with the important part. If you load up the pack right now, you will see that your item is shifted in a weird way in first-person. This is because it still renders as a third-person item. To fix this, we will create an animation that just offsets the item into the correct location. Create a new file called `<your_item>.animation.json` in the `animations` folder of your resource pack.
```json
{
	"format_version": "1.8.0",
	"animations": {
		"animation.<your_item>.first_person.hold": {
			"loop": true,
			"bones": {
				"<root_bone_of_your_item>": {
					"rotation": [87.5, 52.5, -7.5],
					"position": [0, 7, 0]
				}
			}
		}
	}
}
```
Note: it is highly likely that these numbers will **not** work for you. You must play around with various numbers to get the right ones.
Note: your item geometry must be contained within a root bone that can be easily manipulated.
In our case, the animation will look like this:
```json
{
	"format_version": "1.8.0",
	"animations": {
		"animation.drill.first_person.hold": {
			"loop": true,
			"bones": {
				"drill": {
					"rotation": [87.5, 52.5, -7.5],
					"position": [0, 7, 0]
				}
			}
		}
	}
}
```
Now, let's add the decorative animation for our drill:
```json
{
	"format_version": "1.8.0",
	"animations": {
		"animation.drill.hold": {
			"loop": true,
			"bones": {
				"rotator": {
					"rotation": [0, 0, "query.anim_time * 850"]
				},
				"inner_rotor": {
					"rotation": [0, 0, "query.anim_time * -950"]
				}
			}
		},
		"animation.drill.first_person.hold": {
			"loop": true,
			"bones": {
				"drill": {
					"rotation": [87.5, 52.5, -7.5],
					"position": [0, 7, 0]
				}
			}
		}
	}
}
```
This animation will spin the drill really quickly to simulate an actual drill.
Now, let's add these animations to the player client definition file. Add a new entity to the `animations` object of your `player.entity.json` file like this:
```json
"animations": {
    ...,
    "<your_item>_first_person": "animation.<your_item>.first_person.hold" //This is the first-person animation you definde in the previous step
}
```
Next, let's make this animation loop: add a new entry to your `scripts.animate` array like so:
```json
"animate": [
    ...,
    {
        //This is the animation you defined in the previous step
        "<your_item>_first_person": "variable.<your_item> && variable.is_first_person" //This is the variable you defined in the 'pre_animation' array. This animation will only play if the player is in first person and holding the item (p ∧ q)
    }
]
```

In our case, it will look like this:
```json
"animate": [
    ...,
    {
        "drill_first_person": "variable.drill && variable.is_first_person"
    },
    {
        "drill": "variable.drill"
    }
]
```
Note: we have the decorative animation defined here as well.

## Final Touches
Great! Our item works but there is a small problem: you can see that our item sprite is rendered with the 3D model in the player's hand.

![](/assets/images/tutorials/custom-item-models/drill-item-visible.png)

To fix this, simply set the opacity of the item texture to 1 in a free image editor like GIMP.

![](/assets/images/tutorials/custom-item-models/drill-opacity.png)

## The Files

Here you can find the final `player.entity.json` file, render controllers, animations, as well as a download link to the pack.

`entity/player.entity.json`
```json
{
	"format_version": "1.10.0",
	"minecraft:client_entity": {
		"description": {
			"identifier": "minecraft:player",
			"materials": {
				"default": "entity_alphatest",
				"cape": "entity_alphatest",
				"animated": "player_animated"
			},
			"textures": {
				"default": "textures/entity/steve",
				"cape": "textures/entity/cape_invisible",
				"drill": "textures/items/models/drill"
			},
			"geometry": {
				"default": "geometry.humanoid.custom",
				"cape": "geometry.cape",
				"drill": "geometry.drill"
			},
			"scripts": {
				"scale": 0.9375,
				"initialize": [
					"variable.is_holding_right = 0.0;",
					"variable.is_blinking = 0.0;",
					"variable.last_blink_time = 0.0;",
					"variable.hand_bob = 0.0;"
				],
				"pre_animation": [
					"variable.helmet_layer_visible = 1.0;",
					"variable.leg_layer_visible = 1.0;",
					"variable.boot_layer_visible = 1.0;",
					"variable.chest_layer_visible = 1.0;",
					"variable.attack_body_rot_y = Math.sin(360*Math.sqrt(variable.attack_time)) * 5.0;",
					"variable.tcos0 = (math.cos(query.modified_distance_moved * 38.17) * query.modified_move_speed / variable.gliding_speed_value) * 57.3;",
					"variable.first_person_rotation_factor = math.sin((1 - variable.attack_time) * 180.0);",
					"variable.hand_bob = query.life_time < 0.01 ? 0.0 : variable.hand_bob + ((query.is_on_ground && query.is_alive ? math.clamp(math.sqrt(math.pow(query.position_delta(0), 2.0) + math.pow(query.position_delta(2), 2.0)), 0.0, 0.1) : 0.0) - variable.hand_bob) * 0.02;",
					"variable.map_angle = math.clamp(1 - variable.player_x_rotation / 45.1, 0.0, 1.0);",
					"variable.item_use_normalized = query.main_hand_item_use_duration / query.main_hand_item_max_duration;",
					"variable.drill = query.get_equipped_item_name('main_hand') == 'drill';"
				],
				"animate": [
					"root",
					{
						"drill": "variable.drill"
                    },
                    {
                        "drill_first_person": "variable.drill && variable.is_first_person"
                    }
				]
			},
			"animations": {
				"root": "controller.animation.player.root",
				"base_controller": "controller.animation.player.base",
				"hudplayer": "controller.animation.player.hudplayer",
				"humanoid_base_pose": "animation.humanoid.base_pose",
				"look_at_target": "controller.animation.humanoid.look_at_target",
				"look_at_target_ui": "animation.player.look_at_target.ui",
				"look_at_target_default": "animation.humanoid.look_at_target.default",
				"look_at_target_gliding": "animation.humanoid.look_at_target.gliding",
				"look_at_target_swimming": "animation.humanoid.look_at_target.swimming",
				"look_at_target_inverted": "animation.player.look_at_target.inverted",
				"cape": "animation.player.cape",
				"move.arms": "animation.player.move.arms",
				"move.legs": "animation.player.move.legs",
				"swimming": "animation.player.swim",
				"swimming.legs": "animation.player.swim.legs",
				"riding.arms": "animation.player.riding.arms",
				"riding.legs": "animation.player.riding.legs",
				"holding": "animation.player.holding",
				"brandish_spear": "animation.humanoid.brandish_spear",
				"charging": "animation.humanoid.charging",
				"attack.positions": "animation.player.attack.positions",
				"attack.rotations": "animation.player.attack.rotations",
				"sneaking": "animation.player.sneaking",
				"bob": "animation.player.bob",
				"damage_nearby_mobs": "animation.humanoid.damage_nearby_mobs",
				"bow_and_arrow": "animation.humanoid.bow_and_arrow",
				"fishing_rod": "animation.humanoid.fishing_rod",
				"use_item_progress": "animation.humanoid.use_item_progress",
				"skeleton_attack": "animation.skeleton.attack",
				"sleeping": "animation.player.sleeping",
				"first_person_base_pose": "animation.player.first_person.base_pose",
				"first_person_empty_hand": "animation.player.first_person.empty_hand",
				"first_person_swap_item": "animation.player.first_person.swap_item",
				"first_person_attack_controller": "controller.animation.player.first_person_attack",
				"first_person_attack_rotation": "animation.player.first_person.attack_rotation",
				"first_person_vr_attack_rotation": "animation.player.first_person.vr_attack_rotation",
				"first_person_walk": "animation.player.first_person.walk",
				"first_person_map_controller": "controller.animation.player.first_person_map",
				"first_person_map_hold": "animation.player.first_person.map_hold",
				"first_person_map_hold_attack": "animation.player.first_person.map_hold_attack",
				"first_person_map_hold_off_hand": "animation.player.first_person.map_hold_off_hand",
				"first_person_map_hold_main_hand": "animation.player.first_person.map_hold_main_hand",
				"first_person_crossbow_equipped": "animation.player.first_person.crossbow_equipped",
				"third_person_crossbow_equipped": "animation.player.crossbow_equipped",
				"third_person_bow_equipped": "animation.player.bow_equipped",
				"crossbow_hold": "animation.player.crossbow_hold",
				"crossbow_controller": "controller.animation.player.crossbow",
				"shield_block_main_hand": "animation.player.shield_block_main_hand",
				"shield_block_off_hand": "animation.player.shield_block_off_hand",
				"blink": "controller.animation.persona.blink",
                "drill": "animation.drill.hold",
                "drill_first_person": "animation.drill.first_person.hold"
			},
			"render_controllers": [
				{
					"controller.render.player.first_person": "variable.is_first_person"
				},
				{
					"controller.render.player.third_person": "!variable.is_first_person && !variable.map_face_icon"
				},
				{
					"controller.render.player.map": "variable.map_face_icon"
				},
				{
					"controller.render.drill": "variable.drill"
				}
			],
			"enable_attachables": true
		}
	}
}
```

`render_controllers/drill.render_controllers.json`
```json
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.drill": {
			"textures": [
				"Texture.drill"
			],
			"geometry": "Geometry.drill",
			"materials": [
				{
					"*": "Material.default"
				}
			]
		}
	}
}
```

`animations/drill.animation.json`
```json
{
	"format_version": "1.8.0",
	"render_controllers": {
		"controller.render.drill": {
			"textures": [
				"Texture.drill"
			],
			"geometry": "Geometry.drill",
			"materials": [
				{
					"*": "Material.default"
				}
			]
		}
	}
}
```

`models/entity/drill.geo.json`
```json
{
	"format_version": "1.12.0",
	"minecraft:geometry": [
		{
			"description": {
				"identifier": "geometry.drill",
				"texture_width": 32,
				"texture_height": 32,
				"visible_bounds_width": 3,
				"visible_bounds_height": 3,
				"visible_bounds_offset": [0, 0, 0]
			},
			"bones": [
				{
					"name": "root",
					"pivot": [0, 0, 0]
				},
				{
					"name": "waist",
					"parent": "root",
					"pivot": [0, 12, 0]
				},
				{
					"name": "body",
					"parent": "waist",
					"pivot": [0, 24, 0]
				},
				{
					"name": "head",
					"parent": "body",
					"pivot": [0, 24, 0]
				},
				{
					"name": "hat",
					"parent": "head",
					"pivot": [0, 24, 0]
				},
				{
					"name": "cape",
					"parent": "body",
					"pivot": [0, 24, 3]
				},
				{
					"name": "leftArm",
					"parent": "body",
					"pivot": [5, 22, 0]
				},
				{
					"name": "leftSleeve",
					"parent": "leftArm",
					"pivot": [5, 22, 0]
				},
				{
					"name": "leftItem",
					"parent": "leftArm",
					"pivot": [6, 15, 1]
				},
				{
					"name": "rightArm",
					"parent": "body",
					"pivot": [-5, 22, 0]
				},
				{
					"name": "rightSleeve",
					"parent": "rightArm",
					"pivot": [-5, 22, 0]
				},
				{
					"name": "rightItem",
					"parent": "rightArm",
					"pivot": [-6, 15, 1],
					"locators": {
						"lead_hold": [-6, 15, 1]
					}
				},
				{
					"name": "drill",
					"parent": "rightArm",
					"pivot": [-7.55, 8.95, 2.25],
					"cubes": [
						{"origin": [-8.55, 3.95, -2.75], "size": [6, 6, 6], "uv": [0, 0]}
					]
				},
				{
					"name": "rotator",
					"parent": "drill",
					"pivot": [-5.55, 6.95, -2.75],
					"cubes": [
						{"origin": [-7.55, 4.95, -7.75], "size": [4, 4, 5], "uv": [0, 12]}
					]
				},
				{
					"name": "inner_rotor",
					"parent": "drill",
					"pivot": [-5.55, 6.95, -7.75],
					"cubes": [
						{"origin": [-6.55, 5.95, -11.75], "size": [2, 2, 4], "uv": [18, 0]}
					]
				},
				{
					"name": "handle",
					"parent": "drill",
					"pivot": [-8.05, 14.95, 2.25],
					"cubes": [
						{"origin": [-6.05, 9.95, 2.25], "size": [1, 2, 1], "uv": [0, 0]},
						{"origin": [-6.05, 11.95, -2.75], "size": [1, 1, 6], "uv": [12, 15]},
						{"origin": [-6.05, 9.95, -2.75], "size": [1, 2, 1], "uv": [0, 3]}
					]
				},
				{
					"name": "jacket",
					"parent": "body",
					"pivot": [0, 24, 0]
				},
				{
					"name": "leftLeg",
					"parent": "root",
					"pivot": [1.9, 12, 0]
				},
				{
					"name": "leftPants",
					"parent": "leftLeg",
					"pivot": [1.9, 12, 0]
				},
				{
					"name": "rightLeg",
					"parent": "root",
					"pivot": [-1.9, 12, 0]
				},
				{
					"name": "rightPants",
					"parent": "rightLeg",
					"pivot": [-1.9, 12, 0]
				}
			]
		}
	]
}
```

Pack download link: [Link](/assets/packs/tutorials/custom-item-models/CustomItemModels.mcaddon)