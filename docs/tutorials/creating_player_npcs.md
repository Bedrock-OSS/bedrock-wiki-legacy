---
layout: page
title: Creating Player NPCs
parent: Tutorials
nav_order: 2
---

# Creating Player NPCs

This tutorial will show you how to create player NPCs and add them into your world. These player NPCs will take vanilla player skins, and come included with walk-animations, attack animations, etc.

This tutorial is a *graphical* tutorial. Mechanics are not covered.

`Note:` This will be a very json-heavy document. The json is intended for copy-pasting.

# Geometry File

This json contains geometry for both the Steve and Alex versions.

```json
{
    "format_version": "1.12.0",
    "minecraft:geometry": [
      {
        "description": {
          "identifier": "geometry.cape",
          "texture_width": 64,
          "texture_height": 32
        },
        "bones": [
          {
            "name": "body",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "parent": "waist"
          },
          {
            "name": "waist",
            "pivot": [ 0.0, 12.0, 0.0 ]
          },
          {
            "name": "cape",
            "parent": "body",
            "pivot": [ 0.0, 24.0, 3.0 ],
            "rotation": [0.0, 180.0, 0.0],
            "cubes": [
              {
                "origin": [ -5.0, 8.0, 3.0 ],
                "size": [ 10, 16, 1 ],
                "uv": [ 0, 0 ]
              }
            ]
          }
        ]
      },
  
      {
        "description": {
          "identifier": "geometry.npc.steve",
          "visible_bounds_width": 1,
          "visible_bounds_height": 2,
          "visible_bounds_offset": [ 0, 1, 0 ],
          "texture_width": 64,
          "texture_height": 64
        },
        "bones": [
          {
            "name": "root",
            "pivot": [ 0.0, 0.0, 0.0 ]
          },
          {
            "name": "body",
            "parent": "waist",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 12.0, -2.0 ],
                "size": [ 8, 12, 4 ],
                "uv": [ 16, 16 ]
              }
            ]
          },
  
          {
            "name": "waist",
            "parent": "root",
            "pivot": [ 0.0, 12.0, 0.0 ]
          },
  
          {
            "name": "head",
            "parent": "body",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 24.0, -4.0 ],
                "size": [ 8, 8, 8 ],
                "uv": [ 0, 0 ]
              }
            ]
          },
  
          {
            "name": "cape",
            "pivot": [ 0.0, 24, 3.0 ],
            "parent": "body"
          },
          {
            "name": "hat",
            "parent": "head",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 24.0, -4.0 ],
                "size": [ 8, 8, 8 ],
                "uv": [ 32, 0 ],
                "inflate": 0.5
              }
            ]
          },
          {
            "name": "leftArm",
            "parent": "body",
            "pivot": [ 5.0, 22.0, 0.0 ],
            "cubes": [
              {
                "origin": [ 4.0, 12.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 32, 48 ]
              }
            ]
          },
          {
            "name": "leftSleeve",
            "parent": "leftArm",
            "pivot": [ 5.0, 22.0, 0.0 ],
            "cubes": [
              {
                "origin": [ 4.0, 12.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 48, 48 ],
                "inflate": 0.25
              }
            ]
          },
          {
            "name": "leftItem",
            "pivot": [ 6.0, 15.0, 1.0 ],
            "parent": "leftArm"
          },
          {
            "name": "rightArm",
            "parent": "body",
            "pivot": [ -5.0, 22.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -8.0, 12.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 40, 16 ]
              }
            ]
          },
          {
            "name": "rightSleeve",
            "parent": "rightArm",
            "pivot": [ -5.0, 22.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -8.0, 12.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 40, 32 ],
                "inflate": 0.25
              }
            ]
          },
          {
            "name": "rightItem",
            "pivot": [ -6, 15, 1 ],
            "locators": {
              "lead_hold": [ -6, 15, 1 ]
            },
            "parent": "rightArm"
          },
  
          {
            "name": "leftLeg",
            "parent": "root",
            "pivot": [ 1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -0.1, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 16, 48 ]
              }
            ]
          },
          {
            "name": "leftPants",
            "parent": "leftLeg",
            "pivot": [ 1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -0.1, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 48 ],
                "inflate": 0.25
              }
            ]
          },
  
          {
            "name": "rightLeg",
            "parent": "root",
            "pivot": [ -1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -3.9, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 16 ]
              }
            ]
          },
          {
            "name": "rightPants",
            "parent": "rightLeg",
            "pivot": [ -1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -3.9, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 32 ],
                "inflate": 0.25
              }
            ]
          },
  
          {
            "name": "jacket",
            "parent": "body",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 12.0, -2.0 ],
                "size": [ 8, 12, 4 ],
                "uv": [ 16, 32 ],
                "inflate": 0.25
              }
            ]
          }
        ]
      },
  
      {
        "description": {
          "identifier": "geometry.npc.alex",
          "visible_bounds_width": 1,
          "visible_bounds_height": 2,
          "visible_bounds_offset": [ 0, 1, 0 ],
          "texture_width": 64,
          "texture_height": 64
        },
        "bones": [
          {
            "name": "root",
            "pivot": [ 0.0, 0.0, 0.0 ]
          },
          {
            "name": "waist",
            "parent": "root",
            "pivot": [ 0.0, 12.0, 0.0 ]
          },
          {
            "name": "body",
            "parent": "waist",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 12.0, -2.0 ],
                "size": [ 8, 12, 4 ],
                "uv": [ 16, 16 ]
              }
            ]
          },
          {
            "name": "head",
            "parent": "body",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 24.0, -4.0 ],
                "size": [ 8, 8, 8 ],
                "uv": [ 0, 0 ]
              }
            ]
          },
          {
            "name": "hat",
            "parent": "head",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 24.0, -4.0 ],
                "size": [ 8, 8, 8 ],
                "uv": [ 32, 0 ],
                "inflate": 0.5
              }
            ]
          },
          {
            "name": "rightLeg",
            "parent": "root",
            "pivot": [ -1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -3.9, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 16 ]
              }
            ]
          },
          {
            "name": "rightPants",
            "parent": "rightLeg",
            "pivot": [ -1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -3.9, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 32 ],
                "inflate": 0.25
              }
            ]
          },
  
          {
            "name": "leftLeg",
            "parent": "root",
            "pivot": [ 1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -0.1, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 16 ]
              }
            ],
            "mirror": true
          },
          {
            "name": "leftPants",
            "parent": "leftLeg",
            "pivot": [ 1.9, 12.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -0.1, 0.0, -2.0 ],
                "size": [ 4, 12, 4 ],
                "uv": [ 0, 48 ],
                "inflate": 0.25
              }
            ]
          },
  
          {
            "name": "leftArm",
            "parent": "body",
            "pivot": [ 5.0, 21.5, 0.0 ],
            "cubes": [
              {
                "origin": [ 4.0, 11.5, -2.0 ],
                "size": [ 3, 12, 4 ],
                "uv": [ 32, 48 ]
              }
            ]
          },
          {
            "name": "leftSleeve",
            "parent": "leftArm",
            "pivot": [ 5.0, 21.5, 0.0 ],
            "cubes": [
              {
                "origin": [ 4.0, 11.5, -2.0 ],
                "size": [ 3, 12, 4 ],
                "uv": [ 48, 48 ],
                "inflate": 0.25
              }
            ]
          },
          {
            "name": "leftItem",
            "pivot": [ 6, 14.5, 1 ],
            "parent": "leftArm"
          },
          {
            "name": "rightArm",
            "parent": "body",
            "pivot": [ -5.0, 21.5, 0.0 ],
            "cubes": [
              {
                "origin": [ -7.0, 11.5, -2.0 ],
                "size": [ 3, 12, 4 ],
                "uv": [ 40, 16 ]
              }
            ]
          },
          {
            "name": "rightSleeve",
            "parent": "rightArm",
            "pivot": [ -5.0, 21.5, 0.0 ],
            "cubes": [
              {
                "origin": [ -7.0, 11.5, -2.0 ],
                "size": [ 3, 12, 4 ],
                "uv": [ 40, 32 ],
                "inflate": 0.25
              }
            ]
          },
          {
            "name": "rightItem",
            "pivot": [ -6, 14.5, 1 ],
            "locators": {
              "lead_hold": [ -6, 14.5, 1 ]
            },
            "parent": "rightArm"
          },
  
          {
            "name": "jacket",
            "parent": "body",
            "pivot": [ 0.0, 24.0, 0.0 ],
            "cubes": [
              {
                "origin": [ -4.0, 12.0, -2.0 ],
                "size": [ 8, 12, 4 ],
                "uv": [ 16, 32 ],
                "inflate": 0.25
              }
            ]
          },
  
          {
            "name": "cape",
            "pivot": [ 0.0, 24, -3.0 ],
            "parent": "body"
          }
        ]
      }
    ]
  }
  ```

# Entity File

This is an edited version of the player entity file. It contains geometry, a normal player skin texture, as well as animations, and pre-animation identifiers for error free animations.

```json
{
	"format_version": "1.10.0",
	"minecraft:client_entity": {
		"description": {
			"identifier": "sirlich:my_entity",
			"materials": {
				"default": "entity_alphatest"
			},
            "textures": {
				"default": "textures/entity/player_skin"
			},
			"geometry": {
				"default": "geometry.npc.alex"
			},
			"render_controllers": [
				"controller.render.single_texture"
			],
			"scripts": {
				"scale": "0.9375",
				"initialize": [
					"variable.is_paperdoll = 0.0;",
					"variable.map_face_icon = 0.0;",
					"variable.is_first_person = 0.0;",
					"variable.is_holding_right = 0.0;",
					"variable.is_blinking = 0.0;",
					"variable.last_blink_time = 0.0;",
					"variable.hand_bob = 0.0;",
					"variable.player_x_rotation = 0.0;"
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
					"variable.item_use_normalized = query.main_hand_item_use_duration / query.main_hand_item_max_duration;"
				],
				"animate": [
					"root",
					"base_controller"
				]
			},
			"animations": {
				"root": "controller.animation.player.root",
				"base_controller": "controller.animation.player.base",
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
				"blink": "controller.animation.persona.blink"
			}
		}
	}
}
```

# Render Controller File

You can also use a vanilla render controller if you prefer.

```json
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.single_texture": {
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