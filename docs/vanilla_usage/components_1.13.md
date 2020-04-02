---
layout: page
title: Vanilla Usage 1.13
parent: Vanilla Usage
nav_order: 1
---
# Vanilla Components 1.14
This documentation is auto-generated using a python script, written by SirLich. If there is an issue, please bring it to his attention by contacting him on discord: `SirLich#1658`

# Table of contents
 - [minecraft:addrider](#minecraftaddrider)
 - [minecraft:ageable](#minecraftageable)
 - [minecraft:ambient_sound_interval](#minecraftambient_sound_interval)
 - [minecraft:angry](#minecraftangry)
 - [minecraft:annotation.break_door](#minecraftannotationbreak_door)
 - [minecraft:annotation.open_door](#minecraftannotationopen_door)
 - [minecraft:area_attack](#minecraftarea_attack)
 - [minecraft:attack](#minecraftattack)
 - [minecraft:attack_damage](#minecraftattack_damage)
 - [minecraft:balloonable](#minecraftballoonable)
 - [minecraft:behavior.avoid_mob_type](#minecraftbehavioravoid_mob_type)
 - [minecraft:behavior.beg](#minecraftbehaviorbeg)
 - [minecraft:behavior.break_door](#minecraftbehaviorbreak_door)
 - [minecraft:behavior.breed](#minecraftbehaviorbreed)
 - [minecraft:behavior.celebrate](#minecraftbehaviorcelebrate)
 - [minecraft:behavior.charge_attack](#minecraftbehaviorcharge_attack)
 - [minecraft:behavior.charge_held_item](#minecraftbehaviorcharge_held_item)
 - [minecraft:behavior.circle_around_anchor](#minecraftbehaviorcircle_around_anchor)
 - [minecraft:behavior.controlled_by_player](#minecraftbehaviorcontrolled_by_player)
 - [minecraft:behavior.defend_trusted_target](#minecraftbehaviordefend_trusted_target)
 - [minecraft:behavior.defend_village_target](#minecraftbehaviordefend_village_target)
 - [minecraft:behavior.delayed_attack](#minecraftbehaviordelayed_attack)
 - [minecraft:behavior.dragonchargeplayer](#minecraftbehaviordragonchargeplayer)
 - [minecraft:behavior.dragondeath](#minecraftbehaviordragondeath)
 - [minecraft:behavior.dragonflaming](#minecraftbehaviordragonflaming)
 - [minecraft:behavior.dragonholdingpattern](#minecraftbehaviordragonholdingpattern)
 - [minecraft:behavior.dragonlanding](#minecraftbehaviordragonlanding)
 - [minecraft:behavior.dragonscanning](#minecraftbehaviordragonscanning)
 - [minecraft:behavior.dragonstrafeplayer](#minecraftbehaviordragonstrafeplayer)
 - [minecraft:behavior.dragontakeoff](#minecraftbehaviordragontakeoff)
 - [minecraft:behavior.drink_potion](#minecraftbehaviordrink_potion)
 - [minecraft:behavior.drop_item_for](#minecraftbehaviordrop_item_for)
 - [minecraft:behavior.eat_block](#minecraftbehavioreat_block)
 - [minecraft:behavior.eat_carried_item](#minecraftbehavioreat_carried_item)
 - [minecraft:behavior.enderman_leave_block](#minecraftbehaviorenderman_leave_block)
 - [minecraft:behavior.enderman_take_block](#minecraftbehaviorenderman_take_block)
 - [minecraft:behavior.explore_outskirts](#minecraftbehaviorexplore_outskirts)
 - [minecraft:behavior.find_cover](#minecraftbehaviorfind_cover)
 - [minecraft:behavior.find_mount](#minecraftbehaviorfind_mount)
 - [minecraft:behavior.find_underwater_treasure](#minecraftbehaviorfind_underwater_treasure)
 - [minecraft:behavior.flee_sun](#minecraftbehaviorflee_sun)
 - [minecraft:behavior.float](#minecraftbehaviorfloat)
 - [minecraft:behavior.float_wander](#minecraftbehaviorfloat_wander)
 - [minecraft:behavior.follow_caravan](#minecraftbehaviorfollow_caravan)
 - [minecraft:behavior.follow_mob](#minecraftbehaviorfollow_mob)
 - [minecraft:behavior.follow_owner](#minecraftbehaviorfollow_owner)
 - [minecraft:behavior.follow_parent](#minecraftbehaviorfollow_parent)
 - [minecraft:behavior.follow_target_captain](#minecraftbehaviorfollow_target_captain)
 - [minecraft:behavior.go_home](#minecraftbehaviorgo_home)
 - [minecraft:behavior.guardian_attack](#minecraftbehaviorguardian_attack)
 - [minecraft:behavior.harvest_farm_block](#minecraftbehaviorharvest_farm_block)
 - [minecraft:behavior.hide](#minecraftbehaviorhide)
 - [minecraft:behavior.hold_ground](#minecraftbehaviorhold_ground)
 - [minecraft:behavior.hurt_by_target](#minecraftbehaviorhurt_by_target)
 - [minecraft:behavior.inspect_bookshelf](#minecraftbehaviorinspect_bookshelf)
 - [minecraft:behavior.knockback_roar](#minecraftbehaviorknockback_roar)
 - [minecraft:behavior.lay_down](#minecraftbehaviorlay_down)
 - [minecraft:behavior.lay_egg](#minecraftbehaviorlay_egg)
 - [minecraft:behavior.leap_at_target](#minecraftbehaviorleap_at_target)
 - [minecraft:behavior.look_at_entity](#minecraftbehaviorlook_at_entity)
 - [minecraft:behavior.look_at_player](#minecraftbehaviorlook_at_player)
 - [minecraft:behavior.look_at_target](#minecraftbehaviorlook_at_target)
 - [minecraft:behavior.look_at_trading_player](#minecraftbehaviorlook_at_trading_player)
 - [minecraft:behavior.make_love](#minecraftbehaviormake_love)
 - [minecraft:behavior.melee_attack](#minecraftbehaviormelee_attack)
 - [minecraft:behavior.mingle](#minecraftbehaviormingle)
 - [minecraft:behavior.mount_pathing](#minecraftbehaviormount_pathing)
 - [minecraft:behavior.move_indoors](#minecraftbehaviormove_indoors)
 - [minecraft:behavior.move_through_village](#minecraftbehaviormove_through_village)
 - [minecraft:behavior.move_to_land](#minecraftbehaviormove_to_land)
 - [minecraft:behavior.move_to_random_block](#minecraftbehaviormove_to_random_block)
 - [minecraft:behavior.move_to_village](#minecraftbehaviormove_to_village)
 - [minecraft:behavior.move_to_water](#minecraftbehaviormove_to_water)
 - [minecraft:behavior.move_towards_restriction](#minecraftbehaviormove_towards_restriction)
 - [minecraft:behavior.move_towards_target](#minecraftbehaviormove_towards_target)
 - [minecraft:behavior.nap](#minecraftbehaviornap)
 - [minecraft:behavior.nearest_attackable_target](#minecraftbehaviornearest_attackable_target)
 - [minecraft:behavior.nearest_prioritized_attackable_target](#minecraftbehaviornearest_prioritized_attackable_target)
 - [minecraft:behavior.ocelot_sit_on_block](#minecraftbehaviorocelot_sit_on_block)
 - [minecraft:behavior.ocelotattack](#minecraftbehaviorocelotattack)
 - [minecraft:behavior.offer_flower](#minecraftbehavioroffer_flower)
 - [minecraft:behavior.open_door](#minecraftbehavioropen_door)
 - [minecraft:behavior.owner_hurt_by_target](#minecraftbehaviorowner_hurt_by_target)
 - [minecraft:behavior.owner_hurt_target](#minecraftbehaviorowner_hurt_target)
 - [minecraft:behavior.panic](#minecraftbehaviorpanic)
 - [minecraft:behavior.pet_sleep_with_owner](#minecraftbehaviorpet_sleep_with_owner)
 - [minecraft:behavior.pickup_items](#minecraftbehaviorpickup_items)
 - [minecraft:behavior.play](#minecraftbehaviorplay)
 - [minecraft:behavior.player_ride_tamed](#minecraftbehaviorplayer_ride_tamed)
 - [minecraft:behavior.raid_garden](#minecraftbehaviorraid_garden)
 - [minecraft:behavior.random_breach](#minecraftbehaviorrandom_breach)
 - [minecraft:behavior.random_fly](#minecraftbehaviorrandom_fly)
 - [minecraft:behavior.random_look_around](#minecraftbehaviorrandom_look_around)
 - [minecraft:behavior.random_look_around_and_sit](#minecraftbehaviorrandom_look_around_and_sit)
 - [minecraft:behavior.random_sitting](#minecraftbehaviorrandom_sitting)
 - [minecraft:behavior.random_stroll](#minecraftbehaviorrandom_stroll)
 - [minecraft:behavior.random_swim](#minecraftbehaviorrandom_swim)
 - [minecraft:behavior.ranged_attack](#minecraftbehaviorranged_attack)
 - [minecraft:behavior.receive_love](#minecraftbehaviorreceive_love)
 - [minecraft:behavior.restrict_open_door](#minecraftbehaviorrestrict_open_door)
 - [minecraft:behavior.roll](#minecraftbehaviorroll)
 - [minecraft:behavior.run_around_like_crazy](#minecraftbehaviorrun_around_like_crazy)
 - [minecraft:behavior.scared](#minecraftbehaviorscared)
 - [minecraft:behavior.send_event](#minecraftbehaviorsend_event)
 - [minecraft:behavior.share_items](#minecraftbehaviorshare_items)
 - [minecraft:behavior.silverfish_merge_with_stone](#minecraftbehaviorsilverfish_merge_with_stone)
 - [minecraft:behavior.silverfish_wake_up_friends](#minecraftbehaviorsilverfish_wake_up_friends)
 - [minecraft:behavior.skeleton_horse_trap](#minecraftbehaviorskeleton_horse_trap)
 - [minecraft:behavior.sleep](#minecraftbehaviorsleep)
 - [minecraft:behavior.slime_attack](#minecraftbehaviorslime_attack)
 - [minecraft:behavior.slime_float](#minecraftbehaviorslime_float)
 - [minecraft:behavior.slime_keep_on_jumping](#minecraftbehaviorslime_keep_on_jumping)
 - [minecraft:behavior.slime_random_direction](#minecraftbehaviorslime_random_direction)
 - [minecraft:behavior.snacking](#minecraftbehaviorsnacking)
 - [minecraft:behavior.sneeze](#minecraftbehaviorsneeze)
 - [minecraft:behavior.squid_dive](#minecraftbehaviorsquid_dive)
 - [minecraft:behavior.squid_flee](#minecraftbehaviorsquid_flee)
 - [minecraft:behavior.squid_idle](#minecraftbehaviorsquid_idle)
 - [minecraft:behavior.squid_move_away_from_ground](#minecraftbehaviorsquid_move_away_from_ground)
 - [minecraft:behavior.squid_out_of_water](#minecraftbehaviorsquid_out_of_water)
 - [minecraft:behavior.stalk_and_pounce_on_target](#minecraftbehaviorstalk_and_pounce_on_target)
 - [minecraft:behavior.stay_while_sitting](#minecraftbehaviorstay_while_sitting)
 - [minecraft:behavior.stomp_attack](#minecraftbehaviorstomp_attack)
 - [minecraft:behavior.stomp_turtle_egg](#minecraftbehaviorstomp_turtle_egg)
 - [minecraft:behavior.stroll_towards_village](#minecraftbehaviorstroll_towards_village)
 - [minecraft:behavior.summon_entity](#minecraftbehaviorsummon_entity)
 - [minecraft:behavior.swell](#minecraftbehaviorswell)
 - [minecraft:behavior.swim_idle](#minecraftbehaviorswim_idle)
 - [minecraft:behavior.swim_wander](#minecraftbehaviorswim_wander)
 - [minecraft:behavior.swoop_attack](#minecraftbehaviorswoop_attack)
 - [minecraft:behavior.take_flower](#minecraftbehaviortake_flower)
 - [minecraft:behavior.target_when_pushed](#minecraftbehaviortarget_when_pushed)
 - [minecraft:behavior.tempt](#minecraftbehaviortempt)
 - [minecraft:behavior.trade_interest](#minecraftbehaviortrade_interest)
 - [minecraft:behavior.trade_with_player](#minecraftbehaviortrade_with_player)
 - [minecraft:behavior.wither_random_attack_pos_goal](#minecraftbehaviorwither_random_attack_pos_goal)
 - [minecraft:behavior.wither_target_highest_damage](#minecraftbehaviorwither_target_highest_damage)
 - [minecraft:behavior.work](#minecraftbehaviorwork)
 - [minecraft:boostable](#minecraftboostable)
 - [minecraft:boss](#minecraftboss)
 - [minecraft:break_blocks](#minecraftbreak_blocks)
 - [minecraft:breathable](#minecraftbreathable)
 - [minecraft:breedable](#minecraftbreedable)
 - [minecraft:bribeable](#minecraftbribeable)
 - [minecraft:burns_in_daylight](#minecraftburns_in_daylight)
 - [minecraft:can_climb](#minecraftcan_climb)
 - [minecraft:can_fly](#minecraftcan_fly)
 - [minecraft:can_power_jump](#minecraftcan_power_jump)
 - [minecraft:collision_box](#minecraftcollision_box)
 - [minecraft:color](#minecraftcolor)
 - [minecraft:color2](#minecraftcolor2)
 - [minecraft:damage_over_time](#minecraftdamage_over_time)
 - [minecraft:damage_sensor](#minecraftdamage_sensor)
 - [minecraft:despawn](#minecraftdespawn)
 - [minecraft:dweller](#minecraftdweller)
 - [minecraft:economy_trade_table](#minecrafteconomy_trade_table)
 - [minecraft:entity_sensor](#minecraftentity_sensor)
 - [minecraft:environment_sensor](#minecraftenvironment_sensor)
 - [minecraft:equipment](#minecraftequipment)
 - [minecraft:equippable](#minecraftequippable)
 - [minecraft:experience_reward](#minecraftexperience_reward)
 - [minecraft:explode](#minecraftexplode)
 - [minecraft:fire_immune](#minecraftfire_immune)
 - [minecraft:flocking](#minecraftflocking)
 - [minecraft:flying_speed](#minecraftflying_speed)
 - [minecraft:follow_range](#minecraftfollow_range)
 - [minecraft:genetics](#minecraftgenetics)
 - [minecraft:giveable](#minecraftgiveable)
 - [minecraft:healable](#minecrafthealable)
 - [minecraft:health](#minecrafthealth)
 - [minecraft:hide](#minecrafthide)
 - [minecraft:home](#minecrafthome)
 - [minecraft:horse.jump_strength](#minecrafthorsejump_strength)
 - [minecraft:hurt_on_condition](#minecrafthurt_on_condition)
 - [minecraft:input_ground_controlled](#minecraftinput_ground_controlled)
 - [minecraft:insomnia](#minecraftinsomnia)
 - [minecraft:interact](#minecraftinteract)
 - [minecraft:inventory](#minecraftinventory)
 - [minecraft:is_baby](#minecraftis_baby)
 - [minecraft:is_charged](#minecraftis_charged)
 - [minecraft:is_chested](#minecraftis_chested)
 - [minecraft:is_dyeable](#minecraftis_dyeable)
 - [minecraft:is_hidden_when_invisible](#minecraftis_hidden_when_invisible)
 - [minecraft:is_ignited](#minecraftis_ignited)
 - [minecraft:is_illager_captain](#minecraftis_illager_captain)
 - [minecraft:is_saddled](#minecraftis_saddled)
 - [minecraft:is_shaking](#minecraftis_shaking)
 - [minecraft:is_sheared](#minecraftis_sheared)
 - [minecraft:is_stackable](#minecraftis_stackable)
 - [minecraft:is_stunned](#minecraftis_stunned)
 - [minecraft:is_tamed](#minecraftis_tamed)
 - [minecraft:item_controllable](#minecraftitem_controllable)
 - [minecraft:item_hopper](#minecraftitem_hopper)
 - [minecraft:jump.dynamic](#minecraftjumpdynamic)
 - [minecraft:jump.static](#minecraftjumpstatic)
 - [minecraft:knockback_resistance](#minecraftknockback_resistance)
 - [minecraft:leashable](#minecraftleashable)
 - [minecraft:lookat](#minecraftlookat)
 - [minecraft:loot](#minecraftloot)
 - [minecraft:managed_wandering_trader](#minecraftmanaged_wandering_trader)
 - [minecraft:mark_variant](#minecraftmark_variant)
 - [minecraft:mob_effect](#minecraftmob_effect)
 - [minecraft:movement](#minecraftmovement)
 - [minecraft:movement.amphibious](#minecraftmovementamphibious)
 - [minecraft:movement.basic](#minecraftmovementbasic)
 - [minecraft:movement.fly](#minecraftmovementfly)
 - [minecraft:movement.generic](#minecraftmovementgeneric)
 - [minecraft:movement.glide](#minecraftmovementglide)
 - [minecraft:movement.jump](#minecraftmovementjump)
 - [minecraft:movement.skip](#minecraftmovementskip)
 - [minecraft:movement.sway](#minecraftmovementsway)
 - [minecraft:nameable](#minecraftnameable)
 - [minecraft:navigation.climb](#minecraftnavigationclimb)
 - [minecraft:navigation.float](#minecraftnavigationfloat)
 - [minecraft:navigation.fly](#minecraftnavigationfly)
 - [minecraft:navigation.generic](#minecraftnavigationgeneric)
 - [minecraft:navigation.walk](#minecraftnavigationwalk)
 - [minecraft:on_death](#minecrafton_death)
 - [minecraft:on_friendly_anger](#minecrafton_friendly_anger)
 - [minecraft:on_hurt](#minecrafton_hurt)
 - [minecraft:on_hurt_by_player](#minecrafton_hurt_by_player)
 - [minecraft:on_start_landing](#minecrafton_start_landing)
 - [minecraft:on_start_takeoff](#minecrafton_start_takeoff)
 - [minecraft:on_target_acquired](#minecrafton_target_acquired)
 - [minecraft:on_target_escape](#minecrafton_target_escape)
 - [minecraft:on_wake_with_owner](#minecrafton_wake_with_owner)
 - [minecraft:peek](#minecraftpeek)
 - [minecraft:persistent](#minecraftpersistent)
 - [minecraft:physics](#minecraftphysics)
 - [minecraft:player.exhaustion](#minecraftplayerexhaustion)
 - [minecraft:player.experience](#minecraftplayerexperience)
 - [minecraft:player.level](#minecraftplayerlevel)
 - [minecraft:player.saturation](#minecraftplayersaturation)
 - [minecraft:preferred_path](#minecraftpreferred_path)
 - [minecraft:projectile](#minecraftprojectile)
 - [minecraft:pushable](#minecraftpushable)
 - [minecraft:raid_trigger](#minecraftraid_trigger)
 - [minecraft:rail_movement](#minecraftrail_movement)
 - [minecraft:rail_sensor](#minecraftrail_sensor)
 - [minecraft:ravager_blocked](#minecraftravager_blocked)
 - [minecraft:rideable](#minecraftrideable)
 - [minecraft:scaffolding_climber](#minecraftscaffolding_climber)
 - [minecraft:scale](#minecraftscale)
 - [minecraft:scale_by_age](#minecraftscale_by_age)
 - [minecraft:scheduler](#minecraftscheduler)
 - [minecraft:shareables](#minecraftshareables)
 - [minecraft:shooter](#minecraftshooter)
 - [minecraft:sittable](#minecraftsittable)
 - [minecraft:skin_id](#minecraftskin_id)
 - [minecraft:spawn_entity](#minecraftspawn_entity)
 - [minecraft:spell_effects](#minecraftspell_effects)
 - [minecraft:strength](#minecraftstrength)
 - [minecraft:tameable](#minecrafttameable)
 - [minecraft:tamemount](#minecrafttamemount)
 - [minecraft:target_nearby_sensor](#minecrafttarget_nearby_sensor)
 - [minecraft:teleport](#minecraftteleport)
 - [minecraft:timer](#minecrafttimer)
 - [minecraft:trade_resupply](#minecrafttrade_resupply)
 - [minecraft:trade_table](#minecrafttrade_table)
 - [minecraft:trail](#minecrafttrail)
 - [minecraft:transformation](#minecrafttransformation)
 - [minecraft:trust](#minecrafttrust)
 - [minecraft:trusting](#minecrafttrusting)
 - [minecraft:type_family](#minecrafttype_family)
 - [minecraft:underwater_movement](#minecraftunderwater_movement)
 - [minecraft:variant](#minecraftvariant)
 - [minecraft:water_movement](#minecraftwater_movement)
# minecraft:addrider
### cave_spider.json
```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.wither"
}
```

### ravager.json
```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:pillager"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:evocation_illager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:vindicator"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:vindicator",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

### spider.json
```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

```JSON
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.wither"
}
```

# minecraft:ageable
### cat.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### chicken.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### cow.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### dolphin.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### donkey.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### fox.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "sweet_berries",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### horse.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### llama.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.1
        },
        {
            "item": "hay_block",
            "growth": 0.9
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### mooshroom.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### mule.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        {
            "item": "wheat",
            "growth": 0.016667
        },
        {
            "item": "sugar",
            "growth": 0.025
        },
        {
            "item": "hay_block",
            "growth": 0.15
        },
        {
            "item": "apple",
            "growth": 0.05
        },
        {
            "item": "golden_carrot",
            "growth": 0.05
        },
        {
            "item": "golden_apple",
            "growth": 0.2
        },
        {
            "item": "appleEnchanted",
            "growth": 0.2
        }
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### ocelot.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### panda.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "bamboo",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### pig.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "carrot",
        "beetroot",
        "potato"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### polar_bear.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### rabbit.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ],
    "grow_up": {
        "event": "grow_up",
        "target": "self"
    }
}
```

### sheep.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### skeleton_horse.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### turtle.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "seagrass"
    ],
    "drop_items": [
        "turtle_shell_piece"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### villager.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### villager_v2.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### wolf.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "muttonRaw",
        "muttonCooked",
        "porkchop",
        "cooked_porkchop",
        "rabbit",
        "cooked_rabbit",
        "rotten_flesh"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### zombie_horse.json
```JSON
"minecraft:ageable": {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

# minecraft:ambient_sound_interval
### evocation_illager.json
```JSON
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### fox.json
```JSON
"minecraft:ambient_sound_interval": {
    "event_name": "ambient"
}
```

```JSON
"minecraft:ambient_sound_interval": {
    "event_name": "sleep"
}
```

```JSON
"minecraft:ambient_sound_interval": {
    "event_name": "screech",
    "value": 80,
    "range": 160
}
```

### pillager.json
```JSON
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### ravager.json
```JSON
"minecraft:ambient_sound_interval": {
    "value": 4.0,
    "range": 8.0,
    "event_name": "ambient.in.raid"
}
```

### vindicator.json
```JSON
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### witch.json
```JSON
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

# minecraft:angry
### cave_spider.json
```JSON
"minecraft:angry": {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### dolphin.json
```JSON
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 16,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### enderman.json
```JSON
"minecraft:angry": {
    "duration": 25,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### llama.json
```JSON
"minecraft:angry": {
    "duration": 4,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```JSON
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```JSON
"minecraft:angry": {
    "duration": 10,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### panda.json
```JSON
"minecraft:angry": {
    "duration": 500,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "==",
        "value": "panda_aggressive"
    },
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```JSON
"minecraft:angry": {
    "duration": 1,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "==",
        "value": "panda_aggressive"
    },
    "calm_event": {
        "event": "minecraft:baby_on_calm",
        "target": "self"
    }
}
```

### pillager.json
```JSON
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": true,
    "broadcast_range": 8
}
```

### polar_bear.json
```JSON
"minecraft:angry": {
    "duration": 1,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "calm_event": {
        "event": "minecraft:baby_on_calm",
        "target": "self"
    }
}
```

```JSON
"minecraft:angry": {
    "duration": 500,
    "broadcast_anger": false,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### silverfish.json
```JSON
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### spider.json
```JSON
"minecraft:angry": {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:become_calm",
        "target": "self"
    }
}
```

### vindicator.json
```JSON
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:stop_aggro",
        "target": "self"
    }
}
```

### wandering_trader.json
```JSON
"minecraft:angry": {
    "duration": 5,
    "broadcastAnger": true,
    "broadcastRange": 10,
    "broadcast_targets": [
        "llama"
    ],
    "broadcast_filters": {
        "test": "is_leashed_to",
        "subject": "other",
        "value": true
    },
    "calm_event": {
        "event": "minecraft:become_calm",
        "target": "self"
    }
}
```

### wolf.json
```JSON
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### zombie_pigman.json
```JSON
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 20,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

# minecraft:annotation.break_door
### drowned.json
```JSON
"minecraft:annotation.break_door": {}
```

### husk.json
```JSON
"minecraft:annotation.break_door": {}
```

### vindicator.json
```JSON
"minecraft:annotation.break_door": {
    "break_time": 30,
    "min_difficulty": "normal"
}
```

### zombie.json
```JSON
"minecraft:annotation.break_door": {}
```

### zombie_villager.json
```JSON
"minecraft:annotation.break_door": {}
```

# minecraft:annotation.open_door
### villager.json
```JSON
"minecraft:annotation.open_door": {}
```

### villager_v2.json
```JSON
"minecraft:annotation.open_door": {}
```

# minecraft:area_attack
### pufferfish.json
```JSON
"minecraft:area_attack": {
    "damage_range": 0.2,
    "damage_per_tick": 2,
    "cause": "contact",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

# minecraft:attack
### blaze.json
```JSON
"minecraft:attack": {
    "damage": 6
}
```

### cave_spider.json
```JSON
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 0
}
```

```JSON
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 7
}
```

```JSON
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 15
}
```

### creeper.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### dolphin.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### drowned.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### elder_guardian.json
```JSON
"minecraft:attack": {
    "damage": 5
}
```

### enderman.json
```JSON
"minecraft:attack": {
    "damage": 7
}
```

### endermite.json
```JSON
"minecraft:attack": {
    "damage": 2
}
```

### ender_dragon.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### fox.json
```JSON
"minecraft:attack": {
    "damage": 2
}
```

### guardian.json
```JSON
"minecraft:attack": {
    "damage": 5
}
```

### husk.json
```JSON
"minecraft:attack": {
    "damage": 3,
    "effect_name": "hunger",
    "effect_duration": 30
}
```

### iron_golem.json
```JSON
"minecraft:attack": {
    "damage": {
        "range_min": 7,
        "range_max": 21
    }
}
```

### magma_cube.json
```JSON
"minecraft:attack": {
    "damage": 6
}
```

```JSON
"minecraft:attack": {
    "damage": 4
}
```

```JSON
"minecraft:attack": {
    "damage": 2
}
```

### panda.json
```JSON
"minecraft:attack": {
    "damage": 2.0
}
```

```JSON
"minecraft:attack": {
    "damage": 6.0
}
```

### phantom.json
```JSON
"minecraft:attack": {
    "damage": 6
}
```

### pillager.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### player.json
```JSON
"minecraft:attack": {
    "damage": 1
}
```

### polar_bear.json
```JSON
"minecraft:attack": {
    "damage": 6.0
}
```

### ravager.json
```JSON
"minecraft:attack": {
    "damage": 12.0
}
```

### silverfish.json
```JSON
"minecraft:attack": {
    "damage": 1
}
```

### skeleton.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### slime.json
```JSON
"minecraft:attack": {
    "damage": 4
}
```

```JSON
"minecraft:attack": {
    "damage": 2
}
```

```JSON
"minecraft:attack": {
    "damage": 0
}
```

### snow_golem.json
```JSON
"minecraft:attack": {
    "damage": 2
}
```

### spider.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### stray.json
```JSON
"minecraft:attack": {
    "damage": 3,
    "effect_name": "slowness",
    "effect_duration": 10
}
```

### vex.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### vindicator.json
```JSON
"minecraft:attack": {
    "damage": 8
}
```

### wither_skeleton.json
```JSON
"minecraft:attack": {
    "damage": 4,
    "effect_name": "wither",
    "effect_duration": 10
}
```

### wolf.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

```JSON
"minecraft:attack": {
    "damage": 4
}
```

### zombie.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### zombie_pigman.json
```JSON
"minecraft:attack": {
    "damage": 5
}
```

### zombie_villager.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

### zombie_villager_v2.json
```JSON
"minecraft:attack": {
    "damage": 3
}
```

# minecraft:attack_damage
### cat.json
```JSON
"minecraft:attack_damage": {
    "value": 4
}
```

### ocelot.json
```JSON
"minecraft:attack_damage": {
    "value": 4
}
```

# minecraft:balloonable
### chicken.json
```JSON
"minecraft:balloonable": {
    "mass": 0.6
}
```

### cow.json
```JSON
"minecraft:balloonable": {}
```

### donkey.json
```JSON
"minecraft:balloonable": {}
```

### fox.json
```JSON
"minecraft:balloonable": {}
```

### horse.json
```JSON
"minecraft:balloonable": {}
```

### iron_golem.json
```JSON
"minecraft:balloonable": {}
```

### llama.json
```JSON
"minecraft:balloonable": {}
```

### mooshroom.json
```JSON
"minecraft:balloonable": {}
```

### mule.json
```JSON
"minecraft:balloonable": {}
```

### panda.json
```JSON
"minecraft:balloonable": {}
```

### pig.json
```JSON
"minecraft:balloonable": {
    "mass": 0.75
}
```

### rabbit.json
```JSON
"minecraft:balloonable": {
    "mass": 0.75
}
```

### sheep.json
```JSON
"minecraft:balloonable": {
    "mass": 0.75
}
```

### skeleton_horse.json
```JSON
"minecraft:balloonable": {}
```

### snow_golem.json
```JSON
"minecraft:balloonable": {}
```

### squid.json
```JSON
"minecraft:balloonable": {}
```

### zombie_horse.json
```JSON
"minecraft:balloonable": {}
```

# minecraft:behavior.avoid_mob_type
### cat.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 6,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10,
            "walk_speed_multiplier": 0.8,
            "sprint_speed_multiplier": 1.33
        }
    ]
}
```

### creeper.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "ocelot"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "cat"
                    }
                ]
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### dolphin.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian_elder"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.0
        }
    ],
    "probability_per_strength": 0.14
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 1.0
        }
    ]
}
```

### fish.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### fox.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "trusts",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            },
                            {
                                "test": "is_sneaking",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            }
                        ]
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "polarbear"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wolf"
                    }
                ]
            },
            "max_dist": 10,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### guardian.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1,
            "sprint_speed_multiplier": 1
        }
    ]
}
```

### ocelot.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10,
            "walk_speed_multiplier": 0.8,
            "sprint_speed_multiplier": 1.33
        }
    ]
}
```

### panda.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "max_dist": 16,
    "max_flee": 20,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "operator": "!=",
                "subject": "other",
                "value": "panda"
            },
            "max_dist": 16,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### phantom.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 0,
    "max_dist": 16.0,
    "ignore_visibility": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "ocelot"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "cat"
                    }
                ]
            },
            "max_dist": 16,
            "walk_speed_multiplier": 1,
            "sprint_speed_multiplier": 1
        }
    ]
}
```

### rabbit.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.8
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 4,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.8
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            },
            "max_dist": 4,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

### salmon.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 3,
            "max_flee": 10,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### skeleton.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.2,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### stray.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.2,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

### tropicalfish.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

### villager.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ]
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "zombie_pigman"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "illager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "vex"
                    }
                ]
            },
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 0.6
        }
    ],
    "max_dist": 6
}
```

### wolf.json
```JSON
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "llama"
            },
            "max_dist": 24,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 1.5
        }
    ],
    "probability_per_strength": 0.14
}
```

# minecraft:behavior.beg
```JSON
"minecraft:behavior.beg": {
    "priority": 9,
    "look_distance": 8,
    "look_time": [
        2,
        4
    ],
    "items": [
        "bone",
        "porkchop",
        "cooked_porkchop",
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "rotten_flesh",
        "muttonraw",
        "muttoncooked",
        "rabbit",
        "cooked_rabbit"
    ]
}
```

# minecraft:behavior.break_door
### zombie_villager_v2.json
```JSON
"minecraft:behavior.break_door": {
    "priority": 1
}
```

# minecraft:behavior.breed
### cat.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### chicken.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### cow.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### donkey.json
```JSON
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### fox.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### horse.json
```JSON
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### llama.json
```JSON
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### mooshroom.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### ocelot.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### panda.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### pig.json
```JSON
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### rabbit.json
```JSON
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 0.8
}
```

```JSON
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### sheep.json
```JSON
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### turtle.json
```JSON
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### wolf.json
```JSON
"minecraft:behavior.breed": {
    "priority": 7
}
```

# minecraft:behavior.celebrate
### evocation_illager.json
```JSON
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### pillager.json
```JSON
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### ravager.json
```JSON
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### vindicator.json
```JSON
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

### witch.json
```JSON
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

# minecraft:behavior.charge_attack
### vex.json
```JSON
"minecraft:behavior.charge_attack": {
    "priority": 4
}
```

# minecraft:behavior.charge_held_item
### pillager.json
```JSON
"minecraft:behavior.charge_held_item": {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

# minecraft:behavior.circle_around_anchor
### phantom.json
```JSON
"minecraft:behavior.circle_around_anchor": {
    "priority": 3,
    "radius_range": [
        5.0,
        15.0
    ],
    "radius_change_chance": 250,
    "height_above_target_range": [
        20.0,
        40.0
    ],
    "height_offset_range": [
        -4.0,
        5.0
    ],
    "height_change_chance": 350,
    "goal_radius": 1.0
}
```

# minecraft:behavior.controlled_by_player
### pig.json
```JSON
"minecraft:behavior.controlled_by_player": {
    "priority": 0
}
```

# minecraft:behavior.defend_trusted_target
### fox.json
```JSON
"minecraft:behavior.defend_trusted_target": {
    "priority": 0,
    "within_radius": 25,
    "must_see": false,
    "aggro_sound": "mad",
    "sound_chance": 0.05,
    "on_defend_start": {
        "event": "minecraft:fox_configure_defending",
        "target": "self"
    }
}
```

# minecraft:behavior.defend_village_target
### iron_golem.json
```JSON
"minecraft:behavior.defend_village_target": {
    "priority": 1
}
```

# minecraft:behavior.delayed_attack
### ravager.json
```JSON
"minecraft:behavior.delayed_attack": {
    "priority": 4,
    "reach_multiplier": 1.5,
    "attack_duration": 0.75,
    "hit_delay_pct": 0.5,
    "track_target": true,
    "sound_event": "attack.strong"
}
```

# minecraft:behavior.dragonchargeplayer
### ender_dragon.json
```JSON
"minecraft:behavior.dragonchargeplayer": {
    "priority": 1
}
```

# minecraft:behavior.dragondeath
```JSON
"minecraft:behavior.dragondeath": {
    "priority": 0
}
```

# minecraft:behavior.dragonflaming
```JSON
"minecraft:behavior.dragonflaming": {
    "priority": 1
}
```

# minecraft:behavior.dragonholdingpattern
```JSON
"minecraft:behavior.dragonholdingpattern": {
    "priority": 3
}
```

# minecraft:behavior.dragonlanding
```JSON
"minecraft:behavior.dragonlanding": {
    "priority": 0
}
```

# minecraft:behavior.dragonscanning
```JSON
"minecraft:behavior.dragonscanning": {
    "priority": 2
}
```

# minecraft:behavior.dragonstrafeplayer
```JSON
"minecraft:behavior.dragonstrafeplayer": {
    "priority": 2
}
```

# minecraft:behavior.dragontakeoff
```JSON
"minecraft:behavior.dragontakeoff": {
    "priority": 0
}
```

# minecraft:behavior.drink_potion
### wandering_trader.json
```JSON
"minecraft:behavior.drink_potion": {
    "priority": 1,
    "speed_modifier": -0.2,
    "potions": [
        {
            "id": 7,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "hourly_clock_time",
                                "operator": ">=",
                                "value": 18000
                            },
                            {
                                "test": "hourly_clock_time",
                                "operator": "<",
                                "value": 12000
                            }
                        ]
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "all_of": [
                                    {
                                        "test": "has_component",
                                        "subject": "self",
                                        "value": "minecraft:angry"
                                    },
                                    {
                                        "test": "is_family",
                                        "subject": "target",
                                        "operator": "!=",
                                        "value": "player"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": 8,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 18000
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "test": "has_component",
                                "subject": "self",
                                "value": "minecraft:angry"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

# minecraft:behavior.drop_item_for
### cat.json
```JSON
"minecraft:behavior.drop_item_for": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "search_range": 5,
    "search_height": 2,
    "search_count": 0,
    "goal_radius": 1.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6
        }
    ],
    "max_dist": 5,
    "drop_item_chance": 0.7,
    "offering_distance": 5,
    "loot_table": "loot_tables/entities/cat_gift.json",
    "time_of_day_range": [
        0.74999,
        0.8
    ],
    "on_drop_attempt": {
        "event": "minecraft:cat_gifted_owner",
        "target": "self"
    }
}
```

# minecraft:behavior.eat_block
### sheep.json
```JSON
"minecraft:behavior.eat_block": {
    "priority": 6,
    "on_eat": {
        "event": "minecraft:on_eat_block",
        "target": "self"
    }
}
```

# minecraft:behavior.eat_carried_item
### fox.json
```JSON
"minecraft:behavior.eat_carried_item": {
    "priority": 12,
    "delay_before_eating": 28
}
```

# minecraft:behavior.enderman_leave_block
### enderman.json
```JSON
"minecraft:behavior.enderman_leave_block": {
    "priority": 10
}
```

# minecraft:behavior.enderman_take_block
```JSON
"minecraft:behavior.enderman_take_block": {
    "priority": 11
}
```

# minecraft:behavior.explore_outskirts
### villager_v2.json
```JSON
"minecraft:behavior.explore_outskirts": {}
```

```JSON
"minecraft:behavior.explore_outskirts": {
    "priority": 9,
    "explore_dist": 6.0,
    "wait_time": 200,
    "speed_multiplier": 0.6
}
```

# minecraft:behavior.find_cover
### fox.json
```JSON
"minecraft:behavior.find_cover": {
    "priority": 0,
    "speed_multiplier": 1,
    "cooldown_time": 0.0
}
```

```JSON
"minecraft:behavior.find_cover": {
    "priority": 9,
    "speed_multiplier": 1,
    "cooldown_time": 5.0
}
```

# minecraft:behavior.find_mount
### husk.json
```JSON
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

### parrot.json
```JSON
"minecraft:behavior.find_mount": {
    "priority": 3,
    "within_radius": 16,
    "avoid_water": true,
    "start_delay": 100,
    "target_needed": false,
    "mount_distance": 2.0
}
```

### zombie.json
```JSON
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

# minecraft:behavior.find_underwater_treasure
### dolphin.json
```JSON
"minecraft:behavior.find_underwater_treasure": {
    "priority": 2,
    "speed_multiplier": 2.0,
    "search_range": 30,
    "stop_distance": 50
}
```

# minecraft:behavior.flee_sun
### drowned.json
```JSON
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### skeleton.json
```JSON
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### stray.json
```JSON
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

# minecraft:behavior.float
### bat.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### blaze.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### cat.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### cave_spider.json
```JSON
"minecraft:behavior.float": {
    "priority": 1
}
```

### chicken.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### cow.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### creeper.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### donkey.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### enderman.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### endermite.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### fox.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### ghast.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### horse.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### llama.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### mooshroom.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### mule.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### ocelot.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### panda.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### parrot.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### pig.json
```JSON
"minecraft:behavior.float": {
    "priority": 2
}
```

### pillager.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### polar_bear.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### rabbit.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### ravager.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### sheep.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### silverfish.json
```JSON
"minecraft:behavior.float": {
    "priority": 1
}
```

### spider.json
```JSON
"minecraft:behavior.float": {
    "priority": 1
}
```

### vex.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### villager.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### villager_v2.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### vindicator.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

### witch.json
```JSON
"minecraft:behavior.float": {
    "priority": 1
}
```

### wither.json
```JSON
"minecraft:behavior.float": {
    "priority": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.float": {
    "priority": 0
}
```

# minecraft:behavior.float_wander
### bat.json
```JSON
"minecraft:behavior.float_wander": {
    "xz_dist": 10,
    "y_dist": 7,
    "y_offset": -2.0,
    "random_reselect": true,
    "float_duration": [
        0.1,
        0.35
    ]
}
```

### ghast.json
```JSON
"minecraft:behavior.float_wander": {
    "priority": 2,
    "must_reach": true
}
```

# minecraft:behavior.follow_caravan
### llama.json
```JSON
"minecraft:behavior.follow_caravan": {
    "priority": 3,
    "speed_multiplier": 2.1,
    "entity_count": 10,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "llama"
        }
    }
}
```

# minecraft:behavior.follow_mob
### parrot.json
```JSON
"minecraft:behavior.follow_mob": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "stop_distance": 3,
    "search_range": 20
}
```

# minecraft:behavior.follow_owner
### cat.json
```JSON
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### ocelot.json
```JSON
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### parrot.json
```JSON
"minecraft:behavior.follow_owner": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "start_distance": 5,
    "stop_distance": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.follow_owner": {
    "priority": 6,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

# minecraft:behavior.follow_parent
### chicken.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

### cow.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```JSON
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### dolphin.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.1
}
```

### donkey.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### fox.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 9,
    "speed_multiplier": 1.1
}
```

### horse.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### llama.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### mooshroom.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```JSON
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### mule.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### panda.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 13,
    "speed_multiplier": 1.1
}
```

### pig.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### polar_bear.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.25
}
```

### rabbit.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### sheep.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```JSON
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.follow_target_captain
### pillager.json
```JSON
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

### vindicator.json
```JSON
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

# minecraft:behavior.go_home
### turtle.json
```JSON
"minecraft:behavior.go_home": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "interval": 700,
    "goal_radius": 4.0,
    "on_home": {
        "event": "minecraft:go_lay_egg",
        "target": "self"
    }
}
```

# minecraft:behavior.guardian_attack
### elder_guardian.json
```JSON
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

### guardian.json
```JSON
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

```JSON
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

# minecraft:behavior.harvest_farm_block
### villager.json
```JSON
"minecraft:behavior.harvest_farm_block": {
    "priority": 9,
    "speed_multiplier": 0.5
}
```

### villager_v2.json
```JSON
"minecraft:behavior.harvest_farm_block": {}
```

```JSON
"minecraft:behavior.harvest_farm_block": {
    "priority": 8,
    "speed_multiplier": 0.5
}
```

# minecraft:behavior.hide
```JSON
"minecraft:behavior.hide": {
    "priority": 0,
    "speed_multiplier": 0.8,
    "poi_type": "bed",
    "duration": 30.0
}
```

# minecraft:behavior.hold_ground
### pillager.json
```JSON
"minecraft:behavior.hold_ground": {
    "priority": 5,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:synchronized_ranged_mode",
        "target": "self"
    },
    "hurt_by_target_event": {
        "event": "minecraft:synchronized_ranged_mode",
        "target": "self"
    }
}
```

```JSON
"minecraft:behavior.hold_ground": {
    "priority": 6,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:synchronized_ranged_mode",
        "target": "self"
    },
    "hurt_by_target_event": {
        "event": "minecraft:synchronized_ranged_mode",
        "target": "self"
    }
}
```

# minecraft:behavior.hurt_by_target
### blaze.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### cave_spider.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### creeper.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### dolphin.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### drowned.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### enderman.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ghast.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### husk.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### iron_golem.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "creeper"
        }
    }
}
```

```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "all_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "player"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "operator": "!=",
                    "value": "creeper"
                }
            ]
        }
    }
}
```

### llama.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "hurt_owner": true
}
```

### panda.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### pillager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### polar_bear.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### ravager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "operator": "!=",
            "value": "illager"
        },
        "max_dist": 64
    }
}
```

### shulker.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### silverfish.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "alert_same_type": true
}
```

### skeleton.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### spider.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### stray.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### turtle.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vex.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### vindicator.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### witch.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wither.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 3
}
```

### zombie.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

# minecraft:behavior.inspect_bookshelf
### villager_v2.json
```JSON
"minecraft:behavior.inspect_bookshelf": {}
```

```JSON
"minecraft:behavior.inspect_bookshelf": {
    "priority": 8,
    "speed_multiplier": 0.6,
    "search_range": 4,
    "search_height": 3,
    "goal_radius": 0.8,
    "search_count": 0
}
```

# minecraft:behavior.knockback_roar
### ravager.json
```JSON
"minecraft:behavior.knockback_roar": {
    "priority": 1,
    "duration": 1,
    "attack_time": 0.5,
    "knockback_damage": 6,
    "knockback_strength": 3,
    "knockback_range": 4,
    "knockback_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "ravager"
    },
    "damage_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "illager"
    },
    "on_roar_end": {
        "event": "minecraft:end_roar"
    },
    "cooldown_time": 0.1
}
```

# minecraft:behavior.lay_down
### panda.json
```JSON
"minecraft:behavior.lay_down": {
    "priority": 5,
    "interval": 400,
    "random_stop_interval": 2000
}
```

# minecraft:behavior.lay_egg
### turtle.json
```JSON
"minecraft:behavior.lay_egg": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "search_range": 16,
    "search_height": 4,
    "goal_radius": 1.0,
    "on_lay": {
        "event": "minecraft:laid_egg",
        "target": "self"
    }
}
```

# minecraft:behavior.leap_at_target
### cat.json
```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

### cave_spider.json
```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### ocelot.json
```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

### spider.json
```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### wolf.json
```JSON
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "target_dist": 0.4
}
```

# minecraft:behavior.look_at_entity
### evocation_illager.json
```JSON
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8.0,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

### ravager.json
```JSON
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8,
    "angle_of_view_horizontal": 45,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

### vex.json
```JSON
"minecraft:behavior.look_at_entity": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

# minecraft:behavior.look_at_player
### cat.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9
}
```

### cave_spider.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### chicken.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### cow.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### creeper.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### dolphin.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6
}
```

### donkey.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### drowned.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### elder_guardian.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### enderman.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8.0,
    "probability": 8.0
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 3.0,
    "probability": 1.0
}
```

### fox.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 14,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### guardian.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### horse.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### husk.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### iron_golem.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### llama.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mooshroom.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mule.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### ocelot.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9
}
```

### panda.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### parrot.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 1,
    "look_distance": 8.0
}
```

### pig.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### pillager.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8
}
```

### polar_bear.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### rabbit.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 11
}
```

### ravager.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6,
    "angle_of_view_horizontal": 45,
    "probability": 1
}
```

### sheep.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### shulker.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 1,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### skeleton.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### snow_golem.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 3,
    "look_distance": 6.0
}
```

### spider.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### stray.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### turtle.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### vex.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### villager.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 12,
    "look_distance": 8,
    "probability": 0.02
}
```

### villager_v2.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### vindicator.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 10,
    "look_distance": 8,
    "probability": 0.02
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### witch.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "look_distance": 8
}
```

### wolf.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### zombie.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.look_at_player": {
    "priority": 9,
    "look_distance": 6,
    "probability": 0.02
}
```

# minecraft:behavior.look_at_target
### wither.json
```JSON
"minecraft:behavior.look_at_target": {
    "priority": 5
}
```

# minecraft:behavior.look_at_trading_player
### villager.json
```JSON
"minecraft:behavior.look_at_trading_player": {
    "priority": 2
}
```

### villager_v2.json
```JSON
"minecraft:behavior.look_at_trading_player": {
    "priority": 7
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.look_at_trading_player": {
    "priority": 4
}
```

# minecraft:behavior.make_love
### villager.json
```JSON
"minecraft:behavior.make_love": {
    "priority": 6
}
```

### villager_v2.json
```JSON
"minecraft:behavior.make_love": {
    "priority": 5
}
```

# minecraft:behavior.melee_attack
### blaze.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "max_dist": 3,
    "speed_multiplier": 1,
    "random_stop_interval": 2.0,
    "track_target": true
}
```

### cave_spider.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "random_stop_interval": 100,
    "reach_multiplier": 0.8
}
```

```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 1.4
}
```

### creeper.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "track_target": false,
    "reach_multiplier": 0.0
}
```

### dolphin.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "track_target": true
}
```

### drowned.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### enderman.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "track_target": false
}
```

### endermite.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": true
}
```

### fox.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 10,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

```JSON
"minecraft:behavior.melee_attack": {
    "priority": 1,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

### husk.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### iron_golem.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 1,
    "target_dist": 1.0,
    "track_target": true
}
```

### panda.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "attack_once": true,
    "reach_multiplier": 1.0
}
```

```JSON
"minecraft:behavior.melee_attack": {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### pillager.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1,
    "track_target": true
}
```

### silverfish.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "track_target": true
}
```

### skeleton.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### spider.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 0.8
}
```

### stray.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### vindicator.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### wolf.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 5,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### zombie.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 3,
    "speed_multiplier": 1.5,
    "track_target": false
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.melee_attack": {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

# minecraft:behavior.mingle
### villager_v2.json
```JSON
"minecraft:behavior.mingle": {}
```

```JSON
"minecraft:behavior.mingle": {
    "priority": 7,
    "speed_multiplier": 0.5,
    "duration": 30,
    "cooldown_time": 10,
    "mingle_partner_type": "minecraft:villager_v2",
    "mingle_distance": 2.0
}
```

# minecraft:behavior.mount_pathing
### cat.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### cave_spider.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### chicken.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### cow.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### donkey.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### horse.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### husk.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### llama.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### mooshroom.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### mule.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### ocelot.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### panda.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### pig.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### ravager.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### sheep.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 4.0,
    "track_target": true
}
```

### spider.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### wolf.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

# minecraft:behavior.move_indoors
### villager.json
```JSON
"minecraft:behavior.move_indoors": {
    "priority": 4,
    "speed_multiplier": 0.8
}
```

### villager_v2.json
```JSON
"minecraft:behavior.move_indoors": {
    "priority": 6,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

# minecraft:behavior.move_through_village
### iron_golem.json
```JSON
"minecraft:behavior.move_through_village": {
    "priority": 3,
    "speed_multiplier": 0.6,
    "only_at_night": true
}
```

# minecraft:behavior.move_to_land
### turtle.json
```JSON
"minecraft:behavior.move_to_land": {
    "priority": 6,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 0.5
}
```

# minecraft:behavior.move_to_random_block
### pillager.json
```JSON
"minecraft:behavior.move_to_random_block": {
    "priority": 6,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

### vindicator.json
```JSON
"minecraft:behavior.move_to_random_block": {
    "priority": 5,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

# minecraft:behavior.move_to_village
### evocation_illager.json
```JSON
"minecraft:behavior.move_to_village": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### pillager.json
```JSON
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### ravager.json
```JSON
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### vindicator.json
```JSON
"minecraft:behavior.move_to_village": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### witch.json
```JSON
"minecraft:behavior.move_to_village": {
    "priority": 3,
    "speed_multiplier": 1.2,
    "goal_radius": 2.0
}
```

# minecraft:behavior.move_to_water
### dolphin.json
```JSON
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5
}
```

### turtle.json
```JSON
"minecraft:behavior.move_to_water": {
    "priority": 4,
    "search_range": 16,
    "search_height": 5,
    "search_count": 1,
    "goal_radius": 0.1
}
```

```JSON
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5,
    "goal_radius": 0.1
}
```

# minecraft:behavior.move_towards_restriction
### cat.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 7
}
```

### drowned.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### elder_guardian.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "control_flags": [
        "move",
        "look"
    ]
}
```

### guardian.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "control_flags": [
        "move",
        "look"
    ]
}
```

### husk.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### iron_golem.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 4,
    "speed_multiplier": 1
}
```

### villager.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 7,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 7,
    "speed_multiplier": 0.6
}
```

### zombie.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 5
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 7,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.move_towards_restriction": {
    "priority": 7,
    "speed_multiplier": 1
}
```

# minecraft:behavior.move_towards_target
### iron_golem.json
```JSON
"minecraft:behavior.move_towards_target": {
    "priority": 2,
    "speed_multiplier": 0.9,
    "within_radius": 32
}
```

# minecraft:behavior.nap
### fox.json
```JSON
"minecraft:behavior.nap": {
    "priority": 8,
    "cooldown_min": 2.0,
    "cooldown_max": 7.0,
    "mob_detect_dist": 12.0,
    "mob_detect_height": 6.0,
    "can_nap_filters": {
        "all_of": [
            {
                "test": "in_water",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            {
                "test": "on_ground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_underground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_weather",
                "subject": "self",
                "operator": "!=",
                "value": "thunderstorm"
            }
        ]
    },
    "wake_mob_exceptions": {
        "any_of": [
            {
                "test": "trusts",
                "subject": "other",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_family",
                "subject": "other",
                "operator": "==",
                "value": "fox"
            },
            {
                "test": "is_sneaking",
                "subject": "other",
                "operator": "==",
                "value": true
            }
        ]
    }
}
```

# minecraft:behavior.nearest_attackable_target
### blaze.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 48
        }
    ],
    "must_see": true
}
```

### cat.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "attack_interval": 10,
    "reselect_targets": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

### cave_spider.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true,
    "attack_interval": 5
}
```

```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval": 10,
    "must_see": true
}
```

### creeper.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ],
    "must_see": true,
    "must_see_forget_duration": 0.0
}
```

### drowned.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 12,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "snowgolem"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "irongolem"
                            }
                        ]
                    },
                    {
                        "any_of": [
                            {
                                "test": "in_water",
                                "subject": "other",
                                "value": true
                            },
                            {
                                "test": "is_daytime",
                                "value": false
                            }
                        ]
                    }
                ]
            },
            "max_dist": 20
        },
        {
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "villager"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "wandering_trader"
                            }
                        ]
                    },
                    {
                        "any_of": [
                            {
                                "test": "in_water",
                                "subject": "other",
                                "value": true
                            },
                            {
                                "test": "is_daytime",
                                "value": false
                            }
                        ]
                    }
                ]
            },
            "max_dist": 20,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 20
        }
    ],
    "must_see": true,
    "must_see_forget_duration": 17.0,
    "persist_time": 0.5
}
```

### elder_guardian.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "squid"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval_min": 1.0,
    "must_see": true
}
```

### enderman.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "endermite"
            },
            "max_dist": 64
        }
    ],
    "must_see": true
}
```

### endermite.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "within_radius": 16,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "enderman"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 20
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 20
        }
    ],
    "must_see": true
}
```

### ghast.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 28
        }
    ],
    "must_see": true
}
```

### guardian.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "squid"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval_min": 1.0,
    "must_see": true
}
```

```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "squid"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval_min": 1.0,
    "must_see": true
}
```

### husk.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 25,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ],
    "must_see": true
}
```

### iron_golem.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "monster"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            },
            "within_default": 10
        }
    ],
    "must_see": true,
    "must_reach": true
}
```

### llama.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "attack_interval": 16,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wolf"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_tamed"
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "must_see": false,
    "must_reach": true
}
```

### magma_cube.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### ocelot.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "attack_interval": 10,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

### phantom.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "within_radius": 64,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 64
        }
    ],
    "must_see": false,
    "must_see_forget_duration": 0.5,
    "scan_interval": 20,
    "target_search_height": 80.0
}
```

### pillager.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 16.0,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### polar_bear.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        }
    ],
    "must_see": false
}
```

```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "fox"
            },
            "max_dist": 16
        }
    ],
    "must_see": false
}
```

### ravager.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "subject": "other",
                        "test": "is_family",
                        "value": "player"
                    },
                    {
                        "subject": "other",
                        "test": "is_family",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true,
    "priority": 3,
    "within_radius": 16
}
```

### shulker.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "player"
        },
        "max_dist": 16
    },
    "must_see": true
}
```

### silverfish.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 8,
            "attack_interval": 10
        }
    ]
}
```

### skeleton.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### slime.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### snow_golem.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            },
            "within_default": 6
        }
    ],
    "must_reach": true
}
```

### spider.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "attack_interval": 5,
    "must_see": true
}
```

### stray.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### vex.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 70
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 70
        }
    ],
    "must_see": true
}
```

### vindicator.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 12,
    "must_see": true,
    "must_see_forget_duration": 40.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "illager"
                    }
                ]
            },
            "max_dist": 12
        }
    ]
}
```

```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 12,
    "must_see": true,
    "must_see_forget_duration": 40.0,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 12
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    }
                ]
            },
            "max_dist": 12
        }
    ]
}
```

### witch.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "must_reach": true
}
```

### wither.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 70
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "undead"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "inanimate"
                    }
                ]
            },
            "max_dist": 70
        }
    ],
    "must_see": true
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### wolf.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 4,
    "attack_interval": 10,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "skeleton"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "rabbit"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "fox"
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "skeleton"
                    },
                    {
                        "test": "is_underwater",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 5,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "skeleton"
            },
            "max_dist": 16
        }
    ],
    "must_see": true
}
```

### zombie.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "within_radius": 25,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ],
    "must_see": true,
    "must_see_forget_duration": 17.0
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35,
            "must_see": false
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ],
    "must_see": true
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wandering_trader"
                    }
                ]
            },
            "max_dist": 35
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 35
        }
    ],
    "must_see": true
}
```

# minecraft:behavior.nearest_prioritized_attackable_target
### fox.json
```JSON
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 0
        }
    ]
}
```

```JSON
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 1
        }
    ]
}
```

# minecraft:behavior.ocelot_sit_on_block
### cat.json
```JSON
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### ocelot.json
```JSON
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.ocelotattack
### cat.json
```JSON
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "walk_speed_multiplier": 0.8,
    "sprint_speed_multiplier": 1.33,
    "sneak_speed_multiplier": 0.6
}
```

### ocelot.json
```JSON
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "walk_speed_multiplier": 0.8,
    "sprint_speed_multiplier": 1.33,
    "sneak_speed_multiplier": 0.6
}
```

# minecraft:behavior.offer_flower
### iron_golem.json
```JSON
"minecraft:behavior.offer_flower": {
    "priority": 5
}
```

# minecraft:behavior.open_door
### villager.json
```JSON
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
}
```

# minecraft:behavior.owner_hurt_by_target
### wolf.json
```JSON
"minecraft:behavior.owner_hurt_by_target": {
    "priority": 1
}
```

# minecraft:behavior.owner_hurt_target
```JSON
"minecraft:behavior.owner_hurt_target": {
    "priority": 2
}
```

# minecraft:behavior.panic
### cat.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### chicken.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.5
}
```

### cow.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### dolphin.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### donkey.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### fox.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```JSON
"minecraft:behavior.panic": {
    "priority": 2,
    "speed_multiplier": 1.25
}
```

### horse.json
```JSON
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 1.2
}
```

### llama.json
```JSON
"minecraft:behavior.panic": {
    "priority": 4,
    "speed_multiplier": 1.2
}
```

### mooshroom.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### mule.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### ocelot.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### panda.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 2.5
}
```

```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "ignore_mob_damage": true
}
```

### parrot.json
```JSON
"minecraft:behavior.panic": {
    "priority": 0,
    "speed_multiplier": 1.25
}
```

### pig.json
```JSON
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 1.25
}
```

### polar_bear.json
```JSON
"minecraft:behavior.panic": {
    "priority": 2,
    "speed_multiplier": 2.0
}
```

### rabbit.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 2.2
}
```

### sheep.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### turtle.json
```JSON
"minecraft:behavior.panic": {
    "priority": 0,
    "prefer_water": true,
    "speed_multiplier": 1.2
}
```

### villager.json
```JSON
"minecraft:behavior.panic": {
    "priority": 3,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.pet_sleep_with_owner
### cat.json
```JSON
"minecraft:behavior.pet_sleep_with_owner": {
    "priority": 2,
    "speed_multiplier": 1.2,
    "search_radius": 10,
    "search_height": 10,
    "goal_radius": 1.0
}
```

# minecraft:behavior.pickup_items
### fox.json
```JSON
"minecraft:behavior.pickup_items": {
    "priority": 11,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

### villager.json
```JSON
"minecraft:behavior.pickup_items": {
    "priority": 9,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

### villager_v2.json
```JSON
"minecraft:behavior.pickup_items": {
    "priority": 4,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

# minecraft:behavior.play
### villager.json
```JSON
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

### villager_v2.json
```JSON
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

# minecraft:behavior.player_ride_tamed
### donkey.json
```JSON
"minecraft:behavior.player_ride_tamed": {}
```

### horse.json
```JSON
"minecraft:behavior.player_ride_tamed": {}
```

### mule.json
```JSON
"minecraft:behavior.player_ride_tamed": {}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.player_ride_tamed": {}
```

### zombie_horse.json
```JSON
"minecraft:behavior.player_ride_tamed": {}
```

# minecraft:behavior.raid_garden
### fox.json
```JSON
"minecraft:behavior.raid_garden": {
    "priority": 12,
    "blocks": [
        "minecraft:sweet_berry_bush"
    ],
    "speed_multiplier": 1.2,
    "search_range": 12,
    "search_height": 2,
    "goal_radius": 0.8,
    "max_to_eat": 0,
    "initial_eat_delay": 2
}
```

### rabbit.json
```JSON
"minecraft:behavior.raid_garden": {
    "priority": 5,
    "blocks": [
        "carrots"
    ],
    "search_range": 16,
    "goal_radius": 0.8
}
```

# minecraft:behavior.random_breach
### dolphin.json
```JSON
"minecraft:behavior.random_breach": {
    "priority": 6,
    "interval": 50,
    "xz_dist": 6,
    "cooldown_time": 2.0
}
```

# minecraft:behavior.random_fly
### parrot.json
```JSON
"minecraft:behavior.random_fly": {
    "priority": 2,
    "xz_dist": 15,
    "y_dist": 1,
    "y_offset": 0,
    "speed_multiplier": 1.0,
    "can_land_on_trees": true,
    "avoid_damage_blocks": true
}
```

# minecraft:behavior.random_look_around
### blaze.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### cave_spider.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### chicken.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### cow.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### creeper.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### dolphin.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### donkey.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### drowned.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### elder_guardian.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### enderman.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### fox.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 15
}
```

### guardian.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### horse.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### husk.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### iron_golem.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### llama.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### mooshroom.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### mule.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### panda.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### pig.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### pillager.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### polar_bear.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### sheep.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### shulker.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### skeleton.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### snow_golem.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 4
}
```

### spider.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### stray.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### witch.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 6
}
```

### zombie.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.random_look_around": {
    "priority": 9
}
```

# minecraft:behavior.random_look_around_and_sit
### fox.json
```JSON
"minecraft:behavior.random_look_around_and_sit": {
    "priority": 12,
    "min_look_count": 2,
    "max_look_count": 5,
    "min_look_time": 80,
    "max_look_time": 100,
    "probability": 0.001
}
```

# minecraft:behavior.random_sitting
### panda.json
```JSON
"minecraft:behavior.random_sitting": {
    "priority": 5,
    "start_chance": 0.01,
    "stop_chance": 0.3,
    "cooldown": 30,
    "min_sit_time": 10
}
```

```JSON
"minecraft:behavior.random_sitting": {
    "priority": 6,
    "start_chance": 0.02,
    "stop_chance": 0.2,
    "cooldown": 25,
    "min_sit_time": 15
}
```

# minecraft:behavior.random_stroll
### blaze.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### cat.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### cave_spider.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### chicken.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

### cow.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### creeper.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### donkey.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### drowned.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### elder_guardian.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 0.5
}
```

### enderman.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### endermite.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### evocation_illager.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.6
}
```

### fox.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 13,
    "speed_multiplier": 0.8
}
```

### guardian.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0,
    "interval": 80
}
```

### horse.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### husk.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### iron_golem.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1,
    "xz_dist": 16
}
```

### llama.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### mooshroom.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### mule.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### ocelot.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### panda.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 14,
    "speed_multiplier": 0.8
}
```

### pig.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### pillager.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1
}
```

### polar_bear.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5
}
```

### rabbit.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.6,
    "xz_dist": 2,
    "y_dist": 1
}
```

### ravager.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.4
}
```

### sheep.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 0.8
}
```

### skeleton.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### skeleton_horse.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### snow_golem.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 2,
    "speed_multiplier": 1
}
```

### spider.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### stray.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### turtle.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "interval": 100
}
```

### villager.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 11,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### vindicator.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "speed_multiplier": 1
}
```

### witch.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### wither.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### wither_skeleton.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 5,
    "speed_multiplier": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 1.0
}
```

### zombie.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

### zombie_horse.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 1
}
```

# minecraft:behavior.random_swim
### dolphin.json
```JSON
"minecraft:behavior.random_swim": {
    "priority": 5,
    "interval": 0,
    "xz_dist": 20
}
```

### fish.json
```JSON
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### pufferfish.json
```JSON
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### salmon.json
```JSON
"minecraft:behavior.random_swim": {
    "speed_multiplier": 1.0,
    "priority": 3,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### tropicalfish.json
```JSON
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### turtle.json
```JSON
"minecraft:behavior.random_swim": {
    "priority": 7,
    "interval": 0,
    "xz_dist": 30,
    "y_dist": 15
}
```

# minecraft:behavior.ranged_attack
### blaze.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 4,
    "attack_interval_min": 3,
    "attack_interval_max": 5,
    "charge_charged_trigger": 0.0,
    "charge_shoot_trigger": 4.0,
    "attack_radius": 16,
    "burst_shots": 3,
    "burst_interval": 0.3
}
```

### drowned.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 3,
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 10
}
```

### ghast.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 1,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### llama.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### pillager.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 4,
    "attack_interval_min": 1,
    "attack_interval_max": 1,
    "attack_radius": 8
}
```

### shulker.json
```JSON
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### skeleton.json
```JSON
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

```JSON
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### snow_golem.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "attack_interval": 1,
    "attack_radius": 10
}
```

### stray.json
```JSON
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

```JSON
"minecraft:behavior.ranged_attack": {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### witch.json
```JSON
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "attack_interval_min": 3,
    "attack_interval_max": 3,
    "attack_radius": 10.0
}
```

# minecraft:behavior.receive_love
### villager.json
```JSON
"minecraft:behavior.receive_love": {
    "priority": 7
}
```

### villager_v2.json
```JSON
"minecraft:behavior.receive_love": {
    "priority": 6
}
```

# minecraft:behavior.restrict_open_door
### villager.json
```JSON
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

# minecraft:behavior.roll
### panda.json
```JSON
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.0016
}
```

```JSON
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.013
}
```

# minecraft:behavior.run_around_like_crazy
### donkey.json
```JSON
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### horse.json
```JSON
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### llama.json
```JSON
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### mule.json
```JSON
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.scared
### panda.json
```JSON
"minecraft:behavior.scared": {
    "priority": 1,
    "sound_interval": 20
}
```

# minecraft:behavior.send_event
### evocation_illager.json
```JSON
"minecraft:behavior.send_event": {
    "priority": 3,
    "event_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 16.0,
            "cooldown_time": 5.0,
            "cast_duration": 3.0,
            "particle_color": "#FFB38033",
            "weight": 3,
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_color",
                        "subject": "other",
                        "value": "blue"
                    }
                ]
            },
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "base_delay": 2.0,
                    "event": "wololo",
                    "sound_event": "prepare.wololo"
                }
            ]
        }
    ]
}
```

# minecraft:behavior.share_items
### villager.json
```JSON
"minecraft:behavior.share_items": {
    "priority": 8,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:behavior.share_items": {
    "priority": 9,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

# minecraft:behavior.silverfish_merge_with_stone
### silverfish.json
```JSON
"minecraft:behavior.silverfish_merge_with_stone": {
    "priority": 5
}
```

# minecraft:behavior.silverfish_wake_up_friends
```JSON
"minecraft:behavior.silverfish_wake_up_friends": {
    "priority": 1
}
```

# minecraft:behavior.skeleton_horse_trap
### skeleton_horse.json
```JSON
"minecraft:behavior.skeleton_horse_trap": {
    "within_radius": 10.0,
    "duration": 900.0,
    "priority": 2
}
```

# minecraft:behavior.sleep
### villager_v2.json
```JSON
"minecraft:behavior.sleep": {}
```

```JSON
"minecraft:behavior.sleep": {
    "priority": 3,
    "goal_radius": 1.5,
    "speed_multiplier": 0.6,
    "sleep_collider_height": 0.3,
    "sleep_collider_width": 1.0,
    "sleep_y_offset": 0.6,
    "timeout_cooldown": 10.0
}
```

# minecraft:behavior.slime_attack
### magma_cube.json
```JSON
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

### slime.json
```JSON
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

# minecraft:behavior.slime_float
### magma_cube.json
```JSON
"minecraft:behavior.slime_float": {
    "priority": 1
}
```

### slime.json
```JSON
"minecraft:behavior.slime_float": {
    "priority": 1
}
```

# minecraft:behavior.slime_keep_on_jumping
### magma_cube.json
```JSON
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5
}
```

### slime.json
```JSON
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5
}
```

# minecraft:behavior.slime_random_direction
### magma_cube.json
```JSON
"minecraft:behavior.slime_random_direction": {
    "priority": 4
}
```

### slime.json
```JSON
"minecraft:behavior.slime_random_direction": {
    "priority": 4
}
```

# minecraft:behavior.snacking
### panda.json
```JSON
"minecraft:behavior.snacking": {
    "priority": 2,
    "snacking_cooldown": 22.5,
    "snacking_cooldown_min": 20,
    "snacking_stop_chance": 0.001334,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

```JSON
"minecraft:behavior.snacking": {
    "priority": 3,
    "snacking_cooldown": 17.5,
    "snacking_cooldown_min": 10,
    "snacking_stop_chance": 0.0011,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

# minecraft:behavior.sneeze
```JSON
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.0001666,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

```JSON
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.002,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

# minecraft:behavior.squid_dive
### squid.json
```JSON
"minecraft:behavior.squid_dive": {
    "priority": 2
}
```

# minecraft:behavior.squid_flee
```JSON
"minecraft:behavior.squid_flee": {
    "priority": 2
}
```

# minecraft:behavior.squid_idle
```JSON
"minecraft:behavior.squid_idle": {
    "priority": 2
}
```

# minecraft:behavior.squid_move_away_from_ground
```JSON
"minecraft:behavior.squid_move_away_from_ground": {
    "priority": 1
}
```

# minecraft:behavior.squid_out_of_water
```JSON
"minecraft:behavior.squid_out_of_water": {
    "priority": 2
}
```

# minecraft:behavior.stalk_and_pounce_on_target
### fox.json
```JSON
"minecraft:behavior.stalk_and_pounce_on_target": {
    "priority": 7,
    "stalk_speed": 1.2,
    "max_stalk_dist": 12.0,
    "leap_height": 0.9,
    "leap_dist": 0.8,
    "pounce_max_dist": 5.0,
    "interest_time": 2.0,
    "stuck_time": 2.0,
    "strike_dist": 2.0,
    "stuck_blocks": {
        "test": "is_block",
        "subject": "block",
        "operator": "==",
        "value": "snow_layer"
    }
}
```

# minecraft:behavior.stay_while_sitting
### cat.json
```JSON
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

### ocelot.json
```JSON
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

### parrot.json
```JSON
"minecraft:behavior.stay_while_sitting": {
    "priority": 1
}
```

### wolf.json
```JSON
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

# minecraft:behavior.stomp_attack
### polar_bear.json
```JSON
"minecraft:behavior.stomp_attack": {
    "priority": 1,
    "track_target": true,
    "require_complete_path": true
}
```

# minecraft:behavior.stomp_turtle_egg
### drowned.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

### husk.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

### zombie.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

### zombie_pigman.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

### zombie_villager.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 24,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

### zombie_villager_v2.json
```JSON
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 24,
    "search_height": 3,
    "goal_radius": 1.14,
    "search_count": 4,
    "interval": 20
}
```

# minecraft:behavior.stroll_towards_village
### fox.json
```JSON
"minecraft:behavior.stroll_towards_village": {
    "priority": 11,
    "speed_multiplier": 1.0,
    "goal_radius": 3.0,
    "cooldown_time": 10.0,
    "search_range": 32,
    "start_chance": 0.005
}
```

# minecraft:behavior.summon_entity
### evocation_illager.json
```JSON
"minecraft:behavior.summon_entity": {
    "priority": 2,
    "summon_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 3.0,
            "cooldown_time": 5.0,
            "weight": 3,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 5,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 1.5,
                    "entity_lifespan": 1.1,
                    "sound_event": "prepare.attack"
                },
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 0.15,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 8,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 2.5,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "min_activation_range": 3.0,
            "weight": 3,
            "cooldown_time": 5.0,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "line",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.05,
                    "num_entities_spawned": 16,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 20,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "weight": 1,
            "cooldown_time": 17.0,
            "cast_duration": 5.0,
            "particle_color": "#FFB3B3CC",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 5.0,
                    "num_entities_spawned": 3,
                    "entity_type": "minecraft:vex",
                    "summon_cap": 8,
                    "summon_cap_radius": 16.0,
                    "size": 1.0,
                    "sound_event": "prepare.summon"
                }
            ]
        }
    ]
}
```

# minecraft:behavior.swell
### creeper.json
```JSON
"minecraft:behavior.swell": {
    "start_distance": 2.5,
    "stop_distance": 6.0,
    "priority": 2
}
```

# minecraft:behavior.swim_idle
### fish.json
```JSON
"minecraft:behavior.swim_idle": {
    "priority": 5
}
```

### salmon.json
```JSON
"minecraft:behavior.swim_idle": {
    "priority": 5
}
```

### tropicalfish.json
```JSON
"minecraft:behavior.swim_idle": {
    "priority": 5
}
```

# minecraft:behavior.swim_wander
### fish.json
```JSON
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 10,
    "look_ahead": 2.0
}
```

### pufferfish.json
```JSON
"minecraft:behavior.swim_wander": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "interval": 0,
    "look_ahead": 2.0
}
```

### salmon.json
```JSON
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "speed_multiplier": 0.014,
    "interval": 60
}
```

### tropicalfish.json
```JSON
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 10,
    "look_ahead": 2.0
}
```

# minecraft:behavior.swoop_attack
### phantom.json
```JSON
"minecraft:behavior.swoop_attack": {
    "priority": 2,
    "delay_range": [
        10.0,
        20.0
    ]
}
```

# minecraft:behavior.take_flower
### villager.json
```JSON
"minecraft:behavior.take_flower": {
    "priority": 7
}
```

### villager_v2.json
```JSON
"minecraft:behavior.take_flower": {
    "priority": 9
}
```

# minecraft:behavior.target_when_pushed
### iron_golem.json
```JSON
"minecraft:behavior.target_when_pushed": {
    "priority": 1,
    "percent_chance": 5.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "monster"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            }
        }
    ]
}
```

# minecraft:behavior.tempt
### cat.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "fish",
        "salmon"
    ]
}
```

```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "items": [
        "fish",
        "salmon"
    ]
}
```

### chicken.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ]
}
```

### cow.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### donkey.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "apple",
        "carrot",
        "golden_apple",
        "appleEnchanted",
        "golden_carrot",
        "carrotOnAStick",
        "hay_block",
        "sugar",
        "bread",
        "wheat"
    ]
}
```

### fox.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "sweet_berries"
    ]
}
```

### horse.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "apple",
        "carrot",
        "golden_apple",
        "appleEnchanted",
        "golden_carrot",
        "hay_block",
        "sugar",
        "bread",
        "wheat"
    ]
}
```

### mooshroom.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### mule.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "apple",
        "carrot",
        "golden_apple",
        "appleEnchanted",
        "golden_carrot",
        "carrotOnAStick",
        "hay_block",
        "sugar",
        "bread",
        "wheat"
    ]
}
```

### ocelot.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "items": [
        "fish",
        "salmon"
    ]
}
```

```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "items": [
        "fish",
        "salmon"
    ]
}
```

### panda.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "bamboo"
    ]
}
```

### pig.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.2,
    "items": [
        "potato",
        "carrot",
        "beetroot",
        "carrotOnAStick"
    ]
}
```

### rabbit.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 1,
    "items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ]
}
```

### sheep.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### turtle.json
```JSON
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 1.1,
    "items": [
        "seagrass"
    ]
}
```

# minecraft:behavior.trade_interest
### villager_v2.json
```JSON
"minecraft:behavior.trade_interest": {}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```JSON
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.trade_interest": {
    "priority": 3,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

# minecraft:behavior.trade_with_player
### villager.json
```JSON
"minecraft:behavior.trade_with_player": {
    "priority": 1
}
```

### villager_v2.json
```JSON
"minecraft:behavior.trade_with_player": {
    "priority": 2
}
```

### wandering_trader.json
```JSON
"minecraft:behavior.trade_with_player": {
    "priority": 1
}
```

# minecraft:behavior.wither_random_attack_pos_goal
### wither.json
```JSON
"minecraft:behavior.wither_random_attack_pos_goal": {
    "priority": 3
}
```

# minecraft:behavior.wither_target_highest_damage
```JSON
"minecraft:behavior.wither_target_highest_damage": {
    "priority": 1
}
```

# minecraft:behavior.work
### villager_v2.json
```JSON
"minecraft:behavior.work": {}
```

```JSON
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

```JSON
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

```JSON
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

```JSON
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

# minecraft:boostable
### pig.json
```JSON
"minecraft:boostable": {
    "speed_multiplier": 2.0,
    "duration": 3.0,
    "boost_items": [
        {
            "item": "carrotOnAStick",
            "damage": 2,
            "replace_item": "fishing_rod"
        }
    ]
}
```

# minecraft:boss
### ender_dragon.json
```JSON
"minecraft:boss": {
    "should_darken_sky": false,
    "hud_range": 125
}
```

### wither.json
```JSON
"minecraft:boss": {
    "should_darken_sky": true,
    "hud_range": 55
}
```

# minecraft:break_blocks
### ravager.json
```JSON
"minecraft:break_blocks": {
    "breakable_blocks": [
        "bamboo",
        "bamboo_sapling",
        "beetroot",
        "brown_mushroom",
        "carrots",
        "carved_pumpkin",
        "chorus_flower",
        "chorus_plant",
        "deadbush",
        "double_plant",
        "leaves",
        "leaves2",
        "lit_pumpkin",
        "melon_block",
        "melon_stem",
        "potatoes",
        "pumpkin",
        "pumpkin_stem",
        "red_flower",
        "red_mushroom",
        "reeds",
        "sapling",
        "snow_layer",
        "sweet_berry_bush",
        "tallgrass",
        "turtle_egg",
        "vine",
        "waterlily",
        "wheat",
        "yellow_flower"
    ]
}
```

# minecraft:breathable
### bat.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cat.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cave_spider.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### chicken.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cow.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### creeper.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### dolphin.json
```JSON
"minecraft:breathable": {
    "total_supply": 240,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false,
    "generates_bubbles": false
}
```

### donkey.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### drowned.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### elder_guardian.json
```JSON
"minecraft:breathable": {
    "breathes_water": true
}
```

### enderman.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### endermite.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### evocation_illager.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### fish.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### fox.json
```JSON
"minecraft:breathable": {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

### ghast.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### guardian.json
```JSON
"minecraft:breathable": {
    "breathes_water": true
}
```

### horse.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### husk.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### llama.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### magma_cube.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_lava": true
}
```

### mooshroom.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### mule.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ocelot.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### panda.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### parrot.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### phantom.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false
}
```

### pig.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pillager.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### player.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": -1,
    "inhale_time": 3.75,
    "generates_bubbles": false
}
```

### polar_bear.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pufferfish.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### rabbit.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ravager.json
```JSON
"minecraft:breathable": {
    "suffocate_time": 0,
    "total_supply": 15
}
```

### salmon.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### sheep.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### shulker.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### silverfish.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### skeleton.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### skeleton_horse.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### slime.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### snow_golem.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### spider.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### squid.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### stray.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### tropicalfish.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### turtle.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true,
    "breathes_air": true,
    "generates_bubbles": false
}
```

### villager.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### villager_v2.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### vindicator.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wandering_trader.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### witch.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither_skeleton.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### wolf.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### zombie.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### zombie_horse.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_pigman.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager_v2.json
```JSON
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

# minecraft:breedable
### cat.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "allow_sitting": true,
    "breeds_with": {
        "mate_type": "minecraft:cat",
        "baby_type": "minecraft:cat",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### chicken.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:chicken",
        "baby_type": "minecraft:chicken",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds"
    ]
}
```

### cow.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:cow",
        "baby_type": "minecraft:cow",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### donkey.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:donkey",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### fox.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "sweet_berries",
    "breeds_with": {
        "mate_type": "minecraft:fox",
        "baby_type": "minecraft:fox",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

### horse.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:horse",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

### llama.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "inherit_tamed": false,
    "love_filters": {
        "test": "is_mark_variant",
        "subject": "self",
        "operator": "!=",
        "value": 1
    },
    "breeds_with": {
        "mate_type": "minecraft:llama",
        "baby_type": "minecraft:llama",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "hay_block"
    ]
}
```

### mooshroom.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:mooshroom",
        "baby_type": "minecraft:mooshroom",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "deny_parents_variant": {
        "chance": 0.00098,
        "min_variant": 0,
        "max_variant": 1
    }
}
```

### ocelot.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:ocelot",
        "baby_type": "minecraft:ocelot",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

### panda.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "blend_attributes": false,
    "environment_requirements": {
        "blocks": "bamboo",
        "count": 8,
        "radius": 5
    },
    "breed_items": "bamboo",
    "breeds_with": {
        "mate_type": "minecraft:panda",
        "baby_type": "minecraft:panda",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "mutation_factor": {
        "variant": 1.0
    }
}
```

### pig.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:pig",
        "baby_type": "minecraft:pig",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "carrot",
        "beetroot",
        "potato"
    ]
}
```

### rabbit.json
```JSON
"minecraft:breedable": {
    "breed_items": [
        "golden_carrot",
        "carrot",
        "yellow_flower"
    ],
    "breeds_with": {
        "mate_type": "minecraft:rabbit",
        "baby_type": "minecraft:rabbit"
    },
    "require_tame": false,
    "mutation_factor": {
        "variant": 0.2
    }
}
```

### sheep.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:sheep",
        "baby_type": "minecraft:sheep"
    },
    "breed_items": "wheat"
}
```

### turtle.json
```JSON
"minecraft:breedable": {
    "require_tame": false,
    "causes_pregnancy": true,
    "breeds_with": {
        "mate_type": "minecraft:turtle",
        "baby_type": "minecraft:turtle",
        "breed_event": {
            "event": "minecraft:become_pregnant",
            "target": "self"
        }
    },
    "breed_items": [
        "seagrass"
    ]
}
```

### wolf.json
```JSON
"minecraft:breedable": {
    "require_tame": true,
    "breeds_with": {
        "mate_type": "minecraft:wolf",
        "baby_type": "minecraft:wolf",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "muttonRaw",
        "muttonCooked",
        "porkchop",
        "cooked_porkchop",
        "rabbit",
        "cooked_rabbit",
        "rotten_flesh"
    ]
}
```

# minecraft:bribeable
### dolphin.json
```JSON
"minecraft:bribeable": {
    "bribe_items": [
        "fish",
        "salmon"
    ]
}
```

# minecraft:burns_in_daylight
### drowned.json
```JSON
"minecraft:burns_in_daylight": {}
```

### magma_cube.json
```JSON
"minecraft:burns_in_daylight": false
```

### phantom.json
```JSON
"minecraft:burns_in_daylight": {}
```

### skeleton.json
```JSON
"minecraft:burns_in_daylight": {}
```

### stray.json
```JSON
"minecraft:burns_in_daylight": {}
```

### zombie.json
```JSON
"minecraft:burns_in_daylight": {}
```

### zombie_pigman.json
```JSON
"minecraft:burns_in_daylight": false
```

### zombie_villager.json
```JSON
"minecraft:burns_in_daylight": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:burns_in_daylight": {}
```

# minecraft:can_climb
### blaze.json
```JSON
"minecraft:can_climb": {}
```

### cat.json
```JSON
"minecraft:can_climb": {}
```

### cave_spider.json
```JSON
"minecraft:can_climb": {}
```

### chicken.json
```JSON
"minecraft:can_climb": {}
```

### cow.json
```JSON
"minecraft:can_climb": {}
```

### creeper.json
```JSON
"minecraft:can_climb": {}
```

### dolphin.json
```JSON
"minecraft:can_climb": {}
```

### drowned.json
```JSON
"minecraft:can_climb": {}
```

### enderman.json
```JSON
"minecraft:can_climb": {}
```

### endermite.json
```JSON
"minecraft:can_climb": {}
```

### evocation_illager.json
```JSON
"minecraft:can_climb": {}
```

### fox.json
```JSON
"minecraft:can_climb": {}
```

### husk.json
```JSON
"minecraft:can_climb": {}
```

### iron_golem.json
```JSON
"minecraft:can_climb": {}
```

### magma_cube.json
```JSON
"minecraft:can_climb": {}
```

### mooshroom.json
```JSON
"minecraft:can_climb": {}
```

### ocelot.json
```JSON
"minecraft:can_climb": {}
```

### panda.json
```JSON
"minecraft:can_climb": {}
```

### pig.json
```JSON
"minecraft:can_climb": {}
```

### player.json
```JSON
"minecraft:can_climb": {}
```

### polar_bear.json
```JSON
"minecraft:can_climb": {}
```

### rabbit.json
```JSON
"minecraft:can_climb": {}
```

### sheep.json
```JSON
"minecraft:can_climb": {}
```

### silverfish.json
```JSON
"minecraft:can_climb": {}
```

### skeleton.json
```JSON
"minecraft:can_climb": {}
```

### slime.json
```JSON
"minecraft:can_climb": {}
```

### snow_golem.json
```JSON
"minecraft:can_climb": {}
```

### spider.json
```JSON
"minecraft:can_climb": {}
```

### squid.json
```JSON
"minecraft:can_climb": {}
```

### stray.json
```JSON
"minecraft:can_climb": {}
```

### vex.json
```JSON
"minecraft:can_climb": {}
```

### villager.json
```JSON
"minecraft:can_climb": {}
```

### villager_v2.json
```JSON
"minecraft:can_climb": {}
```

### wandering_trader.json
```JSON
"minecraft:can_climb": {}
```

### witch.json
```JSON
"minecraft:can_climb": {}
```

### wither.json
```JSON
"minecraft:can_climb": {}
```

### wither_skeleton.json
```JSON
"minecraft:can_climb": {}
```

### wolf.json
```JSON
"minecraft:can_climb": {}
```

### zombie.json
```JSON
"minecraft:can_climb": {}
```

### zombie_pigman.json
```JSON
"minecraft:can_climb": {}
```

### zombie_villager.json
```JSON
"minecraft:can_climb": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:can_climb": {}
```

# minecraft:can_fly
### bat.json
```JSON
"minecraft:can_fly": {}
```

### blaze.json
```JSON
"minecraft:can_fly": {
    "value": true
}
```

### ghast.json
```JSON
"minecraft:can_fly": {}
```

### parrot.json
```JSON
"minecraft:can_fly": {
    "value": true
}
```

### wither.json
```JSON
"minecraft:can_fly": {}
```

# minecraft:can_power_jump
### donkey.json
```JSON
"minecraft:can_power_jump": {}
```

### horse.json
```JSON
"minecraft:can_power_jump": {}
```

### mule.json
```JSON
"minecraft:can_power_jump": {}
```

### skeleton_horse.json
```JSON
"minecraft:can_power_jump": {}
```

# minecraft:collision_box
### armor_stand.json
```JSON
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.975
}
```

### arrow.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### bat.json
```JSON
"minecraft:collision_box": {
    "width": 0.5,
    "height": 0.9
}
```

### blaze.json
```JSON
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.8
}
```

### boat.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 0.455
}
```

### cat.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### cave_spider.json
```JSON
"minecraft:collision_box": {
    "width": 0.7,
    "height": 0.5
}
```

### chest_minecart.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### chicken.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.8
}
```

### command_block_minecart.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### cow.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### creeper.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.8
}
```

### dolphin.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.6
}
```

### donkey.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### dragon_fireball.json
```JSON
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### drowned.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### egg.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### elder_guardian.json
```JSON
"minecraft:collision_box": {
    "width": 1.99,
    "height": 1.99
}
```

### enderman.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 2.9
}
```

### endermite.json
```JSON
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.3
}
```

### ender_crystal.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.98
}
```

### ender_dragon.json
```JSON
"minecraft:collision_box": {
    "width": 13,
    "height": 4
}
```

### ender_pearl.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### evocation_illager.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### eye_of_ender_signal.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### fireball.json
```JSON
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### fireworks_rocket.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### fish.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.3
}
```

### fishing_hook.json
```JSON
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### fox.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### ghast.json
```JSON
"minecraft:collision_box": {
    "width": 4,
    "height": 4
}
```

### guardian.json
```JSON
"minecraft:collision_box": {
    "width": 0.85,
    "height": 0.85
}
```

### hopper_minecart.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### horse.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### husk.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### iron_golem.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 2.9
}
```

### lingering_potion.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### llama.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.87
}
```

### llama_spit.json
```JSON
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### magma_cube.json
```JSON
"minecraft:collision_box": {
    "width": 2.08,
    "height": 2.08
}
```

```JSON
"minecraft:collision_box": {
    "width": 0.78,
    "height": 0.78
}
```

```JSON
"minecraft:collision_box": {
    "width": 0.52,
    "height": 0.52
}
```

### minecart.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### mooshroom.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### mule.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### ocelot.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.7
}
```

### panda.json
```JSON
"minecraft:collision_box": {
    "width": 1.7,
    "height": 1.5
}
```

### parrot.json
```JSON
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1
}
```

### phantom.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.5
}
```

### pig.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 0.9
}
```

### pillager.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### player.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.8
}
```

### polar_bear.json
```JSON
"minecraft:collision_box": {
    "width": 1.3,
    "height": 1.4
}
```

### pufferfish.json
```JSON
"minecraft:collision_box": {
    "width": 0.8,
    "height": 0.8
}
```

### rabbit.json
```JSON
"minecraft:collision_box": {
    "width": 0.67,
    "height": 0.67
}
```

### ravager.json
```JSON
"minecraft:collision_box": {
    "height": 1.9,
    "width": 1.2
}
```

### salmon.json
```JSON
"minecraft:collision_box": {
    "width": 0.5,
    "height": 0.5
}
```

### sheep.json
```JSON
"minecraft:collision_box": {
    "width": 0.9,
    "height": 1.3
}
```

### shulker_bullet.json
```JSON
"minecraft:collision_box": {
    "width": 0.625,
    "height": 0.625
}
```

### silverfish.json
```JSON
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.3
}
```

### skeleton.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### skeleton_horse.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### slime.json
```JSON
"minecraft:collision_box": {
    "width": 2.08,
    "height": 2.08
}
```

```JSON
"minecraft:collision_box": {
    "width": 1.04,
    "height": 1.04
}
```

```JSON
"minecraft:collision_box": {
    "width": 0.52,
    "height": 0.52
}
```

### small_fireball.json
```JSON
"minecraft:collision_box": {
    "width": 0.31,
    "height": 0.31
}
```

### snowball.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### snow_golem.json
```JSON
"minecraft:collision_box": {
    "width": 0.4,
    "height": 1.8
}
```

### spider.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 0.9
}
```

### splash_potion.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### squid.json
```JSON
"minecraft:collision_box": {
    "width": 0.95,
    "height": 0.95
}
```

### stray.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### thrown_trident.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.35
}
```

### tnt.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.98
}
```

### tnt_minecart.json
```JSON
"minecraft:collision_box": {
    "width": 0.98,
    "height": 0.7
}
```

### tripod_camera.json
```JSON
"minecraft:collision_box": {
    "width": 0.75,
    "height": 1.8
}
```

### tropicalfish.json
```JSON
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.4
}
```

### turtle.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.2
}
```

```JSON
"minecraft:collision_box": {
    "width": 1.2,
    "height": 0.4
}
```

### vex.json
```JSON
"minecraft:collision_box": {
    "width": 0.4,
    "height": 0.8
}
```

### villager.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### villager_v2.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### vindicator.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### wandering_trader.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### witch.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### wither.json
```JSON
"minecraft:collision_box": {
    "width": 1,
    "height": 3
}
```

### wither_skeleton.json
```JSON
"minecraft:collision_box": {
    "width": 0.72,
    "height": 2.01
}
```

### wither_skull.json
```JSON
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### wither_skull_dangerous.json
```JSON
"minecraft:collision_box": {
    "width": 0.15,
    "height": 0.15
}
```

### wolf.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 0.8
}
```

### xp_bottle.json
```JSON
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

### zombie.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_horse.json
```JSON
"minecraft:collision_box": {
    "width": 1.4,
    "height": 1.6
}
```

### zombie_pigman.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager_v2.json
```JSON
"minecraft:collision_box": {
    "width": 0.6,
    "height": 1.9
}
```

# minecraft:color
### cat.json
```JSON
"minecraft:color": {
    "value": 14
}
```

### sheep.json
```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 12
}
```

```JSON
"minecraft:color": {
    "value": 15
}
```

```JSON
"minecraft:color": {
    "value": 8
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 6
}
```

```JSON
"minecraft:color": {
    "value": 14
}
```

### tropicalfish.json
```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 1
}
```

```JSON
"minecraft:color": {
    "value": 2
}
```

```JSON
"minecraft:color": {
    "value": 3
}
```

```JSON
"minecraft:color": {
    "value": 4
}
```

```JSON
"minecraft:color": {
    "value": 5
}
```

```JSON
"minecraft:color": {
    "value": 6
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 8
}
```

```JSON
"minecraft:color": {
    "value": 9
}
```

```JSON
"minecraft:color": {
    "value": 10
}
```

```JSON
"minecraft:color": {
    "value": 11
}
```

```JSON
"minecraft:color": {
    "value": 12
}
```

```JSON
"minecraft:color": {
    "value": 13
}
```

```JSON
"minecraft:color": {
    "value": 14
}
```

```JSON
"minecraft:color": {
    "value": 1
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 11
}
```

```JSON
"minecraft:color": {
    "value": 1
}
```

```JSON
"minecraft:color": {
    "value": 6
}
```

```JSON
"minecraft:color": {
    "value": 10
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 9
}
```

```JSON
"minecraft:color": {
    "value": 5
}
```

```JSON
"minecraft:color": {
    "value": 14
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 14
}
```

```JSON
"minecraft:color": {
    "value": 0
}
```

```JSON
"minecraft:color": {
    "value": 14
}
```

```JSON
"minecraft:color": {
    "value": 7
}
```

```JSON
"minecraft:color": {
    "value": 4
}
```

```JSON
"minecraft:color": {
    "value": 9
}
```

### wolf.json
```JSON
"minecraft:color": {
    "value": 14
}
```

# minecraft:color2
### tropicalfish.json
```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 1
}
```

```JSON
"minecraft:color2": {
    "value": 2
}
```

```JSON
"minecraft:color2": {
    "value": 3
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

```JSON
"minecraft:color2": {
    "value": 5
}
```

```JSON
"minecraft:color2": {
    "value": 6
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 8
}
```

```JSON
"minecraft:color2": {
    "value": 9
}
```

```JSON
"minecraft:color2": {
    "value": 10
}
```

```JSON
"minecraft:color2": {
    "value": 11
}
```

```JSON
"minecraft:color2": {
    "value": 12
}
```

```JSON
"minecraft:color2": {
    "value": 13
}
```

```JSON
"minecraft:color2": {
    "value": 14
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 3
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 3
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

```JSON
"minecraft:color2": {
    "value": 14
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

```JSON
"minecraft:color2": {
    "value": 7
}
```

```JSON
"minecraft:color2": {
    "value": 1
}
```

```JSON
"minecraft:color2": {
    "value": 6
}
```

```JSON
"minecraft:color2": {
    "value": 3
}
```

```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 14
}
```

```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 0
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

```JSON
"minecraft:color2": {
    "value": 4
}
```

# minecraft:damage_over_time
### dolphin.json
```JSON
"minecraft:damage_over_time": {
    "damage_per_hurt": 1,
    "time_between_hurt": 0
}
```

# minecraft:damage_sensor
### bat.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### blaze.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### cat.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### chicken.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### creeper.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            },
            "event": "minecraft:become_charged"
        },
        "deals_damage": false
    }
}
```

### ender_dragon.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### fox.json
```JSON
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_block",
                    "subject": "block",
                    "value": "minecraft:sweet_berry_bush"
                }
            },
            "deals_damage": false
        }
    ]
}
```

### ghast.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### iron_golem.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### llama.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": true,
        "on_damage": {
            "filters": {
                "test": "in_caravan",
                "value": false
            },
            "event": "minecraft:become_angry"
        }
    }
}
```

```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": true
    }
}
```

### magma_cube.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### mooshroom.json
```JSON
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 0
                        }
                    ]
                },
                "event": "minecraft:become_brown"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        },
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "lightning"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        }
                    ]
                },
                "event": "minecraft:become_red"
            },
            "deals_damage": false,
            "on_damage_sound_event": "convert_mooshroom"
        }
    ]
}
```

### ocelot.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### parrot.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### pig.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            },
            "event": "become_zombie"
        },
        "deals_damage": false
    }
}
```

### pillager.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### skeleton.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "other_with_families": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### skeleton_horse.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "lightning"
            }
        },
        "deals_damage": false
    }
}
```

### snow_golem.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### turtle.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "lightning",
        "deals_damage": true,
        "damage_multiplier": 2000.0
    }
}
```

### villager.json
```JSON
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "lightning"
                },
                "event": "become_witch"
            },
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "zombie"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "husk"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "has_damage",
                            "value": "fatal"
                        }
                    ]
                },
                "event": "become_zombie"
            }
        }
    ]
}
```

### vindicator.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

### wandering_trader.json
```JSON
"minecraft:damage_sensor": {
    "triggers": [
        {
            "cause": "entity_attack",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "projectile",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        },
        {
            "cause": "magic",
            "deals_damage": true,
            "on_damage": {
                "event": "minecraft:become_scared"
            }
        }
    ]
}
```

### wither.json
```JSON
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "undead"
            }
        },
        "deals_damage": false
    }
}
```

# minecraft:despawn
### wandering_trader.json
```JSON
"minecraft:despawn": {
    "remove_child_entities": true,
    "filters": {
        "all_of": [
            {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "self",
                        "value": "wandering_trader_despawning"
                    },
                    {
                        "test": "has_trade_supply",
                        "subject": "self",
                        "value": false
                    }
                ]
            },
            {
                "test": "distance_to_nearest_player",
                "operator": ">",
                "value": 24
            }
        ]
    }
}
```

# minecraft:dweller
### cat.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "passive",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

### evocation_illager.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### iron_golem.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "defender",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

### pillager.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### ravager.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### villager_v2.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "farmer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "fisherman",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "shepherd",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "fletcher",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "librarian",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "cartographer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "cleric",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "armorer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "weaponsmith",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "toolsmith",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "butcher",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "leatherworker",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "mason",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

### vindicator.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

### witch.json
```JSON
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": false,
    "first_founding_reward": 0
}
```

# minecraft:economy_trade_table
### villager_v2.json
```JSON
"minecraft:economy_trade_table": {}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/economy_trades/farmer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/economy_trades/fisherman_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.shepherd",
    "table": "trading/economy_trades/shepherd_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.fletcher",
    "table": "trading/economy_trades/fletcher_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.librarian",
    "table": "trading/economy_trades/librarian_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.cartographer",
    "table": "trading/economy_trades/cartographer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.cleric",
    "table": "trading/economy_trades/cleric_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.armor",
    "table": "trading/economy_trades/armorer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.weapon",
    "table": "trading/economy_trades/weapon_smith_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.tool",
    "table": "trading/economy_trades/tool_smith_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.butcher",
    "table": "trading/economy_trades/butcher_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.leather",
    "table": "trading/economy_trades/leather_worker_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.mason",
    "table": "trading/economy_trades/stone_mason_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

### wandering_trader.json
```JSON
"minecraft:economy_trade_table": {
    "display_name": "entity.wandering_trader.name",
    "table": "trading/economy_trades/wandering_trader_trades.json",
    "new_screen": true
}
```

# minecraft:entity_sensor
### pufferfish.json
```JSON
"minecraft:entity_sensor": {
    "sensor_range": 1.5,
    "minimum_count": 1,
    "event_filters": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "mob"
            },
            {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "none_of": {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    }
                ]
            }
        ]
    },
    "event": "minecraft:to_full_puff"
}
```

```JSON
"minecraft:entity_sensor": {
    "sensor_range": 10,
    "require_all": true,
    "event_filters": {
        "none_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "mob"
            },
            {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "none_of": {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    }
                ]
            }
        ]
    },
    "event": "minecraft:from_full_puff"
}
```

# minecraft:environment_sensor
### cave_spider.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": "<",
            "value": 0.49
        },
        "event": "minecraft:become_hostile"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": ">",
            "value": 0.49
        },
        "event": "minecraft:become_neutral"
    }
}
```

### dolphin.json
```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    },
                    {
                        "test": "in_water",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:navigation_on_land"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:stop_dryingout"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:navigation_off_land"
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "!=",
                "value": true
            },
            "event": "minecraft:start_dryingout"
        }
    ]
}
```

### fox.json
```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_daytime",
                "value": false
            },
            "event": "minecraft:fox_configure_night"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": true
            },
            "event": "minecraft:fox_configure_day"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": true
                    },
                    {
                        "test": "has_target",
                        "operator": "==",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_docile_day"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": false
                    },
                    {
                        "test": "has_target",
                        "operator": "==",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_docile_night"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_weather",
                        "operator": "!=",
                        "value": "thunderstorm"
                    },
                    {
                        "test": "is_daytime",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:fox_configure_day"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_weather",
                        "operator": "!=",
                        "value": "thunderstorm"
                    },
                    {
                        "test": "is_daytime",
                        "value": false
                    }
                ]
            },
            "event": "minecraft:fox_configure_night"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_weather",
                "value": "thunderstorm"
            },
            "event": "minecraft:fox_configure_thunderstorm"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": false
            },
            "event": "minecraft:fox_configure_night"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_weather",
                "value": "thunderstorm"
            },
            "event": "minecraft:fox_configure_thunderstorm"
        },
        {
            "filters": {
                "test": "is_daytime",
                "value": true
            },
            "event": "minecraft:fox_configure_day"
        }
    ]
}
```

### husk.json
```JSON
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:start_transforming"
        }
    ]
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:stop_transforming"
    }
}
```

### llama.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "all_of": [
                {
                    "test": "is_leashed",
                    "subject": "self",
                    "value": false
                },
                {
                    "test": "has_component",
                    "subject": "self",
                    "operator": "!=",
                    "value": "minecraft:is_tamed"
                }
            ]
        },
        "event": "minecraft:on_tame"
    }
}
```

### pillager.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_water",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:ranged_mode"
    }
}
```

### player.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "all_of": [
                {
                    "test": "has_mob_effect",
                    "subject": "self",
                    "value": "bad_omen"
                },
                {
                    "test": "is_in_village",
                    "subject": "self",
                    "value": true
                }
            ]
        },
        "event": "minecraft:trigger_raid"
    }
}
```

### skeleton.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_water",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:ranged_mode"
    }
}
```

### spider.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": "<",
            "value": 0.49
        },
        "event": "minecraft:become_hostile"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_brightness",
            "operator": ">",
            "value": 0.49
        },
        "event": "minecraft:become_neutral"
    }
}
```

### stray.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:melee_mode"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "in_water",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:ranged_mode"
    }
}
```

### zombie.json
```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

```JSON
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "subject": "self",
            "operator": "==",
            "value": false
        },
        "event": "minecraft:stop_transforming"
    }
}
```

# minecraft:equipment
### drowned.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_ranged_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

### fox.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/fox_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.mainhand",
            "drop_chance": 1.0
        }
    ]
}
```

### husk.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### pillager.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/pillager_gear.json"
}
```

```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/pillager_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/pillager_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

### skeleton.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### stray.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### vex.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/vex_gear.json"
}
```

### vindicator.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/vindicator_gear.json"
}
```

```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/vindicator_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/vindicator_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

### wither_skeleton.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/wither_skeleton_gear.json"
}
```

### zombie.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### zombie_pigman.json
```JSON
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_pigman_gear.json"
}
```

# minecraft:equippable
### donkey.json
```JSON
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:donkey_saddled"
            },
            "on_unequip": {
                "event": "minecraft:donkey_unsaddled"
            }
        }
    ]
}
```

### horse.json
```JSON
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:horse_saddled"
            },
            "on_unequip": {
                "event": "minecraft:horse_unsaddled"
            }
        },
        {
            "slot": 1,
            "item": "horsearmoriron",
            "accepted_items": [
                "horsearmorleather",
                "horsearmoriron",
                "horsearmorgold",
                "horsearmordiamond"
            ]
        }
    ]
}
```

### llama.json
```JSON
"minecraft:equippable": {
    "slots": [
        {
            "slot": 1,
            "item": "carpet",
            "accepted_items": [
                "carpet"
            ]
        }
    ]
}
```

### mule.json
```JSON
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:mule_saddled"
            },
            "on_unequip": {
                "event": "minecraft:mule_unsaddled"
            }
        }
    ]
}
```

# minecraft:experience_reward
### blaze.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### cat.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cave_spider.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### chicken.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cow.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### creeper.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### dolphin.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### donkey.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### drowned.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### elder_guardian.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### enderman.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### endermite.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 3 : 0"
}
```

### evocation_illager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "10"
}
```

### fish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### fox.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ghast.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### guardian.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### horse.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### husk.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### llama.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### magma_cube.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### mooshroom.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### mule.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ocelot.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### panda.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### parrot.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### phantom.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### pig.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### pillager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### player.json
```JSON
"minecraft:experience_reward": {
    "on_death": "Math.Min(query.player_level * 7, 100)"
}
```

### polar_bear.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### pufferfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### rabbit.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ravager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 20 : 0"
}
```

### salmon.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### sheep.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### shulker.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### silverfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### skeleton.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### skeleton_horse.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### slime.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### spider.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### squid.json
```JSON
"minecraft:experience_reward": {
    "on_death": "!query.is_baby && query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### stray.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### tropicalfish.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### turtle.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,4) : 0"
}
```

### vex.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### vindicator.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### witch.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### wither.json
```JSON
"minecraft:experience_reward": {
    "on_death": "50"
}
```

### wither_skeleton.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### wolf.json
```JSON
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_horse.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie_pigman.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager_v2.json
```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```JSON
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

# minecraft:explode
### creeper.json
```JSON
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```JSON
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```JSON
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```JSON
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### ender_crystal.json
```JSON
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### fireball.json
```JSON
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": true,
    "fire_affected_by_griefing": true,
    "destroy_affected_by_griefing": true
}
```

### tnt.json
```JSON
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

```JSON
"minecraft:explode": {
    "fuse_length": {
        "range_min": 0.5,
        "range_max": 2.0
    },
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

### tnt_minecart.json
```JSON
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

```JSON
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

### wither_skull.json
```JSON
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### wither_skull_dangerous.json
```JSON
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": false,
    "max_resistance": 4.0,
    "destroy_affected_by_griefing": true
}
```

# minecraft:fire_immune
### blaze.json
```JSON
"minecraft:fire_immune": true
```

### ender_crystal.json
```JSON
"minecraft:fire_immune": true
```

### ender_dragon.json
```JSON
"minecraft:fire_immune": true
```

### ghast.json
```JSON
"minecraft:fire_immune": true
```

### magma_cube.json
```JSON
"minecraft:fire_immune": true
```

### vex.json
```JSON
"minecraft:fire_immune": true
```

### wither.json
```JSON
"minecraft:fire_immune": true
```

### wither_skeleton.json
```JSON
"minecraft:fire_immune": true
```

### zombie_pigman.json
```JSON
"minecraft:fire_immune": true
```

# minecraft:flocking
### dolphin.json
```JSON
"minecraft:flocking": {
    "in_water": false,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 6.0,
    "breach_influence": 0.0,
    "separation_weight": 1.75,
    "separation_threshold": 3.0,
    "cohesion_weight": 1.85,
    "cohesion_threshold": 6.5,
    "innner_cohesion_threshold": 3.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.0
}
```

### fish.json
```JSON
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

### pufferfish.json
```JSON
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

### salmon.json
```JSON
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.25,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.75
}
```

### tropicalfish.json
```JSON
"minecraft:flocking": {
    "in_water": true,
    "match_variants": true,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.75,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

# minecraft:flying_speed
### ender_dragon.json
```JSON
"minecraft:flying_speed": {
    "value": 0.6
}
```

# minecraft:follow_range
### blaze.json
```JSON
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

### dolphin.json
```JSON
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

### elder_guardian.json
```JSON
"minecraft:follow_range": {
    "value": 16,
    "max": 16
}
```

### enderman.json
```JSON
"minecraft:follow_range": {
    "value": 32,
    "max": 32
}
```

### evocation_illager.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

### ghast.json
```JSON
"minecraft:follow_range": {
    "value": 64,
    "max": 64
}
```

### guardian.json
```JSON
"minecraft:follow_range": {
    "value": 16,
    "max": 16
}
```

### iron_golem.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

### llama.json
```JSON
"minecraft:follow_range": {
    "value": 40,
    "max": 40
}
```

### phantom.json
```JSON
"minecraft:follow_range": {
    "value": 64,
    "max": 64
}
```

### pillager.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

### polar_bear.json
```JSON
"minecraft:follow_range": {
    "value": 48
}
```

### ravager.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

### turtle.json
```JSON
"minecraft:follow_range": {
    "value": 1024
}
```

### villager_v2.json
```JSON
"minecraft:follow_range": {
    "value": 128
}
```

### vindicator.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

### witch.json
```JSON
"minecraft:follow_range": {
    "value": 64
}
```

# minecraft:genetics
### panda.json
```JSON
"minecraft:genetics": {
    "mutation_rate": 0.03125,
    "genes": [
        {
            "name": "panda_variant",
            "allele_range": {
                "range_min": 0,
                "range_max": 15
            },
            "genetic_variants": [
                {
                    "main_allele": 0,
                    "birth_event": {
                        "event": "minecraft:panda_lazy",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 1,
                    "birth_event": {
                        "event": "minecraft:panda_worried",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 2,
                    "birth_event": {
                        "event": "minecraft:panda_playful",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 3,
                    "birth_event": {
                        "event": "minecraft:panda_aggressive",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 4,
                        "range_max": 7
                    },
                    "birth_event": {
                        "event": "minecraft:panda_weak",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 8,
                        "range_max": 9
                    },
                    "birth_event": {
                        "event": "minecraft:panda_brown",
                        "target": "self"
                    }
                }
            ]
        }
    ]
}
```

# minecraft:giveable
```JSON
"minecraft:giveable": {
    "triggers": {
        "cooldown": 3.0,
        "items": [
            "bamboo",
            "cake"
        ],
        "on_give": {
            "event": "minecraft:on_calm",
            "target": "self"
        }
    }
}
```

# minecraft:healable
### cat.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "fish",
            "heal_amount": 2
        },
        {
            "item": "salmon",
            "heal_amount": 2
        }
    ]
}
```

### donkey.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### horse.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### llama.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "hay_block",
            "heal_amount": 10
        }
    ]
}
```

### mule.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

### parrot.json
```JSON
"minecraft:healable": {
    "force_use": true,
    "filters": {
        "test": "is_riding",
        "operator": "!=",
        "value": true
    },
    "items": [
        {
            "item": "cookie",
            "heal_amount": 0,
            "effects": [
                {
                    "name": "fatal_poison",
                    "chance": 1.0,
                    "duration": 1000,
                    "amplifier": 0
                }
            ]
        }
    ]
}
```

### wolf.json
```JSON
"minecraft:healable": {
    "items": [
        {
            "item": "porkchop",
            "heal_amount": 3
        },
        {
            "item": "cooked_porkchop",
            "heal_amount": 8
        },
        {
            "item": "fish",
            "heal_amount": 2
        },
        {
            "item": "salmon",
            "heal_amount": 2
        },
        {
            "item": "clownfish",
            "heal_amount": 1
        },
        {
            "item": "pufferfish",
            "heal_amount": 1
        },
        {
            "item": "cooked_fish",
            "heal_amount": 5
        },
        {
            "item": "cooked_salmon",
            "heal_amount": 6
        },
        {
            "item": "beef",
            "heal_amount": 3
        },
        {
            "item": "cooked_beef",
            "heal_amount": 8
        },
        {
            "item": "chicken",
            "heal_amount": 2
        },
        {
            "item": "cooked_chicken",
            "heal_amount": 6
        },
        {
            "item": "muttonRaw",
            "heal_amount": 2
        },
        {
            "item": "muttonCooked",
            "heal_amount": 6
        },
        {
            "item": "rotten_flesh",
            "heal_amount": 4
        },
        {
            "item": "rabbit",
            "heal_amount": 3
        },
        {
            "item": "cooked_rabbit",
            "heal_amount": 5
        },
        {
            "item": "rabbit_stew",
            "heal_amount": 10
        }
    ]
}
```

# minecraft:health
### armor_stand.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### bat.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### blaze.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### cat.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### cave_spider.json
```JSON
"minecraft:health": {
    "value": 12,
    "max": 12
}
```

### chicken.json
```JSON
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### cow.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### creeper.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### dolphin.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### donkey.json
```JSON
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### drowned.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### elder_guardian.json
```JSON
"minecraft:health": {
    "value": 80,
    "max": 80
}
```

### enderman.json
```JSON
"minecraft:health": {
    "value": 40,
    "max": 40
}
```

### endermite.json
```JSON
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### ender_crystal.json
```JSON
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### ender_dragon.json
```JSON
"minecraft:health": {
    "value": 200,
    "max": 200
}
```

### evocation_illager.json
```JSON
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### fish.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### fox.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### ghast.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### guardian.json
```JSON
"minecraft:health": {
    "value": 30,
    "max": 30
}
```

### horse.json
```JSON
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### husk.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### iron_golem.json
```JSON
"minecraft:health": {
    "value": 100,
    "max": 100
}
```

### llama.json
```JSON
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### magma_cube.json
```JSON
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

```JSON
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

```JSON
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### mooshroom.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### mule.json
```JSON
"minecraft:health": {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### ocelot.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### panda.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### parrot.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### phantom.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### pig.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### pillager.json
```JSON
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### polar_bear.json
```JSON
"minecraft:health": {
    "value": 30
}
```

### pufferfish.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### rabbit.json
```JSON
"minecraft:health": {
    "value": 3,
    "max": 3
}
```

### ravager.json
```JSON
"minecraft:health": {
    "max": 100,
    "value": 100
}
```

### salmon.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### sheep.json
```JSON
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### shulker.json
```JSON
"minecraft:health": {
    "value": 30,
    "max": 30
}
```

### silverfish.json
```JSON
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

### skeleton.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### skeleton_horse.json
```JSON
"minecraft:health": {
    "value": 15,
    "max": 15
}
```

### slime.json
```JSON
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

```JSON
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

```JSON
"minecraft:health": {
    "value": 1,
    "max": 1
}
```

### snow_golem.json
```JSON
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### spider.json
```JSON
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

### squid.json
```JSON
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

### stray.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### tripod_camera.json
```JSON
"minecraft:health": {
    "value": 4,
    "max": 4
}
```

### tropicalfish.json
```JSON
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

### turtle.json
```JSON
"minecraft:health": {
    "value": 30
}
```

### vex.json
```JSON
"minecraft:health": {
    "value": 14,
    "max": 14
}
```

### villager.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### villager_v2.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### vindicator.json
```JSON
"minecraft:health": {
    "value": 24,
    "max": 24
}
```

### wandering_trader.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### witch.json
```JSON
"minecraft:health": {
    "value": 26,
    "max": 26
}
```

### wither.json
```JSON
"minecraft:health": {
    "value": 600,
    "max": 600
}
```

### wither_skeleton.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### wolf.json
```JSON
"minecraft:health": {
    "value": 8,
    "max": 8
}
```

```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_horse.json
```JSON
"minecraft:health": {
    "value": 15,
    "max": 15
}
```

### zombie_pigman.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_villager.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

### zombie_villager_v2.json
```JSON
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

# minecraft:hide
### villager_v2.json
```JSON
"minecraft:hide": {}
```

# minecraft:home
### turtle.json
```JSON
"minecraft:home": {}
```

# minecraft:horse.jump_strength
### donkey.json
```JSON
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

### horse.json
```JSON
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### mule.json
```JSON
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

### skeleton_horse.json
```JSON
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### zombie_horse.json
```JSON
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

# minecraft:hurt_on_condition
### armor_stand.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### arrow.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### bat.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### blaze.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### boat.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cat.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cave_spider.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### chicken.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### cow.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### creeper.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### dolphin.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### donkey.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### drowned.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### elder_guardian.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### enderman.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### endermite.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### evocation_illager.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### fish.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### guardian.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### horse.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### husk.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### iron_golem.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### llama.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### mooshroom.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### mule.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### ocelot.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### panda.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### parrot.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### phantom.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pig.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pillager.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### player.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### polar_bear.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### pufferfish.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### rabbit.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### ravager.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### salmon.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### sheep.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### shulker.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### silverfish.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### skeleton.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### skeleton_horse.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### slime.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### snow_golem.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        },
        {
            "filters": {
                "test": "is_temperature_value",
                "operator": ">",
                "value": 1.0
            },
            "cause": "temperature",
            "damage_per_tick": 1
        },
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "==",
                "value": true
            },
            "cause": "drowning",
            "damage_per_tick": 1
        }
    ]
}
```

### spider.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### squid.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### stray.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### tripod_camera.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### tropicalfish.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### turtle.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### villager.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### vindicator.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### wandering_trader.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### witch.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### wolf.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_horse.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_villager.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

### zombie_villager_v2.json
```JSON
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

# minecraft:input_ground_controlled
### donkey.json
```JSON
"minecraft:input_ground_controlled": {}
```

### horse.json
```JSON
"minecraft:input_ground_controlled": {}
```

### mule.json
```JSON
"minecraft:input_ground_controlled": {}
```

### skeleton_horse.json
```JSON
"minecraft:input_ground_controlled": {}
```

# minecraft:insomnia
### player.json
```JSON
"minecraft:insomnia": {
    "days_until_insomnia": 3
}
```

# minecraft:interact
### cow.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "bucket:0"
                        }
                    ]
                }
            },
            "use_item": true,
            "transform_to_item": "bucket:1",
            "play_sounds": "milk",
            "interact_text": "action.interact.milk"
        }
    ]
}
```

### creeper.json
```JSON
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "flint_and_steel"
                    },
                    {
                        "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:explode"
                    }
                ]
            },
            "event": "minecraft:start_exploding_forced",
            "target": "self"
        },
        "hurt_item": 1,
        "swing": true,
        "play_sounds": "ignite",
        "interact_text": "action.interact.creeper"
    }
}
```

### donkey.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "chest"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### llama.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "chest"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### mooshroom.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "bowl"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        }
                    ]
                },
                "event": "minecraft:flowerless",
                "target": "self"
            },
            "add_items": {
                "table": "loot_tables/gameplay/entities/mooshroom_milking.json"
            },
            "use_item": true,
            "play_sounds": "milk_suspiciously",
            "interact_text": "action.interact.moostew"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:2"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 7
                        }
                    ]
                },
                "event": "minecraft:ate_allium",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:3"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 3
                        }
                    ]
                },
                "event": "minecraft:ate_bluet",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:1"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 6
                        }
                    ]
                },
                "event": "minecraft:ate_orchid",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:9"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 1
                        }
                    ]
                },
                "event": "minecraft:ate_cornflower",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "yellow_flower"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 5
                        }
                    ]
                },
                "event": "minecraft:ate_dandelion",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:10"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 4
                        }
                    ]
                },
                "event": "minecraft:ate_lily",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:8"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 8
                        }
                    ]
                },
                "event": "minecraft:ate_daisy",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:0"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 0
                        }
                    ]
                },
                "event": "minecraft:ate_poppy",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:4"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:5"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:6"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "red_flower:7"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 2
                        }
                    ]
                },
                "event": "minecraft:ate_tulip",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "wither_rose"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        },
                        {
                            "test": "is_mark_variant",
                            "subject": "self",
                            "operator": "!=",
                            "value": 9
                        }
                    ]
                },
                "event": "minecraft:ate_rose",
                "target": "self"
            },
            "use_item": true,
            "play_sounds": "eat",
            "particle_on_start": {
                "particle_type": "smoke",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.feed"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 0
                        }
                    ]
                },
                "event": "become_cow",
                "target": "self"
            },
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "spawn_items": {
                "table": "loot_tables/entities/mooshroom_shear.json"
            },
            "particle_on_start": {
                "particle_type": "largeexplode",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.mooshear"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:transformation"
                        },
                        {
                            "test": "is_variant",
                            "subject": "self",
                            "operator": "==",
                            "value": 1
                        }
                    ]
                },
                "event": "become_cow",
                "target": "self"
            },
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "spawn_items": {
                "table": "loot_tables/entities/brown_mooshroom_shear.json"
            },
            "particle_on_start": {
                "particle_type": "largeexplode",
                "particle_y_offset": 0.25,
                "particle_offset_towards_interactor": true
            },
            "interact_text": "action.interact.mooshear"
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "bucket:0"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                }
            },
            "use_item": true,
            "transform_to_item": "bucket:1",
            "play_sounds": "milk",
            "interact_text": "action.interact.milk"
        }
    ]
}
```

### mule.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "chest"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

### pig.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "test": "has_equipment",
                    "subject": "other",
                    "domain": "hand",
                    "value": "saddle"
                },
                "event": "minecraft:on_saddled"
            },
            "use_item": true,
            "play_sounds": "saddle",
            "interact_text": "action.interact.saddle"
        }
    ]
}
```

### sheep.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "cooldown": 2.5,
            "use_item": false,
            "hurt_item": 1,
            "spawn_items": {
                "table": "loot_tables/entities/sheep_shear.json"
            },
            "play_sounds": "shear",
            "interact_text": "action.interact.shear",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:is_baby"
                        },
                        {
                            "test": "has_component",
                            "value": "minecraft:is_dyeable"
                        }
                    ]
                },
                "event": "minecraft:on_sheared",
                "target": "self"
            }
        }
    ]
}
```

### shulker.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:0"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:16"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_black"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:8"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_gray"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:7"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_silver"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:15"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:19"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_white"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:12"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_light_blue"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:14"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_orange"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:1"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_red"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:4"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:18"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_blue"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:5"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_purple"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:13"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_magenta"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:9"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_pink"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "any_of": [
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:3"
                                },
                                {
                                    "test": "has_equipment",
                                    "subject": "other",
                                    "domain": "hand",
                                    "value": "dye:17"
                                }
                            ]
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_brown"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:11"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_yellow"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:10"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_lime"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:2"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_green"
            },
            "use_item": true
        },
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "dye:6"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_ability",
                            "subject": "other",
                            "value": "instabuild"
                        }
                    ]
                },
                "event": "minecraft:turn_cyan"
            },
            "use_item": true
        }
    ]
}
```

### snow_golem.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "cooldown": 2.5,
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "interact_text": "action.interact.shear",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:is_sheared"
                        }
                    ]
                },
                "event": "minecraft:on_sheared",
                "target": "self"
            }
        }
    ]
}
```

### tnt_minecart.json
```JSON
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "fireball:0"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "flint_and_steel"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_game_rule",
                            "domain": "tntexplodes",
                            "operator": "==",
                            "value": true
                        }
                    ]
                },
                "event": "minecraft:on_prime",
                "target": "self"
            },
            "swing": true,
            "play_sounds": "ignite",
            "interact_text": "action.interact.creeper"
        },
        {
            "on_interact": {
                "filters": {
                    "any_of": [
                        {
                            "test": "has_component",
                            "subject": "other",
                            "value": "fire_aspect"
                        }
                    ],
                    "all_of": [
                        {
                            "test": "is_game_rule",
                            "domain": "tntexplodes",
                            "operator": "==",
                            "value": true
                        }
                    ]
                },
                "event": "minecraft:on_prime",
                "target": "self"
            },
            "swing": true,
            "interact_text": "action.interact.creeper"
        }
    ]
}
```

### zombie_villager.json
```JSON
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "golden_apple"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "value": "minecraft:effect.weakness"
                    }
                ]
            },
            "event": "villager_converted",
            "target": "self"
        },
        "use_item": true,
        "interact_text": "action.interact.cure"
    }
}
```

### zombie_villager_v2.json
```JSON
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "golden_apple"
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "value": "minecraft:effect.weakness"
                    }
                ]
            },
            "event": "villager_converted",
            "target": "self"
        },
        "use_item": true,
        "interact_text": "action.interact.cure"
    }
}
```

# minecraft:inventory
### chest_minecart.json
```JSON
"minecraft:inventory": {
    "container_type": "minecart_chest",
    "inventory_size": 27,
    "can_be_siphoned_from": true
}
```

### command_block_minecart.json
```JSON
"minecraft:inventory": {}
```

### donkey.json
```JSON
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### hopper_minecart.json
```JSON
"minecraft:inventory": {
    "container_type": "minecart_hopper",
    "inventory_size": 5,
    "can_be_siphoned_from": true
}
```

### horse.json
```JSON
"minecraft:inventory": {
    "inventory_size": 2,
    "container_type": "horse"
}
```

### llama.json
```JSON
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse",
    "additional_slots_per_strength": 3
}
```

### mule.json
```JSON
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### panda.json
```JSON
"minecraft:inventory": {
    "inventory_size": 1,
    "private": true
}
```

### villager.json
```JSON
"minecraft:inventory": {
    "inventory_size": 8,
    "private": true
}
```

### villager_v2.json
```JSON
"minecraft:inventory": {
    "inventory_size": 8,
    "private": true
}
```

# minecraft:is_baby
### cat.json
```JSON
"minecraft:is_baby": {}
```

### chicken.json
```JSON
"minecraft:is_baby": {}
```

### cow.json
```JSON
"minecraft:is_baby": {}
```

### dolphin.json
```JSON
"minecraft:is_baby": {}
```

### donkey.json
```JSON
"minecraft:is_baby": {}
```

### drowned.json
```JSON
"minecraft:is_baby": {}
```

### fox.json
```JSON
"minecraft:is_baby": {}
```

### horse.json
```JSON
"minecraft:is_baby": {}
```

### husk.json
```JSON
"minecraft:is_baby": {}
```

### llama.json
```JSON
"minecraft:is_baby": {}
```

### mooshroom.json
```JSON
"minecraft:is_baby": {}
```

### mule.json
```JSON
"minecraft:is_baby": {}
```

### ocelot.json
```JSON
"minecraft:is_baby": {}
```

### panda.json
```JSON
"minecraft:is_baby": {}
```

### pig.json
```JSON
"minecraft:is_baby": {}
```

### polar_bear.json
```JSON
"minecraft:is_baby": {}
```

### rabbit.json
```JSON
"minecraft:is_baby": {}
```

### sheep.json
```JSON
"minecraft:is_baby": {}
```

### skeleton_horse.json
```JSON
"minecraft:is_baby": {}
```

### squid.json
```JSON
"minecraft:is_baby": {}
```

### turtle.json
```JSON
"minecraft:is_baby": {}
```

### villager.json
```JSON
"minecraft:is_baby": {}
```

### villager_v2.json
```JSON
"minecraft:is_baby": {}
```

### wolf.json
```JSON
"minecraft:is_baby": {}
```

### zombie.json
```JSON
"minecraft:is_baby": {}
```

### zombie_horse.json
```JSON
"minecraft:is_baby": {}
```

### zombie_pigman.json
```JSON
"minecraft:is_baby": {}
```

### zombie_villager.json
```JSON
"minecraft:is_baby": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:is_baby": {}
```

# minecraft:is_charged
### creeper.json
```JSON
"minecraft:is_charged": {}
```

# minecraft:is_chested
### donkey.json
```JSON
"minecraft:is_chested": {}
```

### llama.json
```JSON
"minecraft:is_chested": {}
```

### mule.json
```JSON
"minecraft:is_chested": {}
```

# minecraft:is_dyeable
### cat.json
```JSON
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

### sheep.json
```JSON
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

### wolf.json
```JSON
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

# minecraft:is_hidden_when_invisible
### player.json
```JSON
"minecraft:is_hidden_when_invisible": {}
```

### wandering_trader.json
```JSON
"minecraft:is_hidden_when_invisible": {}
```

# minecraft:is_ignited
### tnt_minecart.json
```JSON
"minecraft:is_ignited": {}
```

```JSON
"minecraft:is_ignited": {}
```

# minecraft:is_illager_captain
### pillager.json
```JSON
"minecraft:is_illager_captain": {}
```

```JSON
"minecraft:is_illager_captain": {}
```

### vindicator.json
```JSON
"minecraft:is_illager_captain": {}
```

```JSON
"minecraft:is_illager_captain": {}
```

# minecraft:is_saddled
### donkey.json
```JSON
"minecraft:is_saddled": {}
```

### horse.json
```JSON
"minecraft:is_saddled": {}
```

### mule.json
```JSON
"minecraft:is_saddled": {}
```

### pig.json
```JSON
"minecraft:is_saddled": {}
```

# minecraft:is_shaking
### husk.json
```JSON
"minecraft:is_shaking": {}
```

```JSON
"minecraft:is_shaking": {}
```

### zombie.json
```JSON
"minecraft:is_shaking": {}
```

```JSON
"minecraft:is_shaking": {}
```

### zombie_villager.json
```JSON
"minecraft:is_shaking": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:is_shaking": {}
```

# minecraft:is_sheared
### sheep.json
```JSON
"minecraft:is_sheared": {}
```

### snow_golem.json
```JSON
"minecraft:is_sheared": {}
```

# minecraft:is_stackable
### boat.json
```JSON
"minecraft:is_stackable": {}
```

### chest_minecart.json
```JSON
"minecraft:is_stackable": {
    "value": true
}
```

### hopper_minecart.json
```JSON
"minecraft:is_stackable": {}
```

### minecart.json
```JSON
"minecraft:is_stackable": {}
```

### tnt_minecart.json
```JSON
"minecraft:is_stackable": {}
```

# minecraft:is_stunned
### ravager.json
```JSON
"minecraft:is_stunned": {}
```

# minecraft:is_tamed
### cat.json
```JSON
"minecraft:is_tamed": {}
```

### donkey.json
```JSON
"minecraft:is_tamed": {}
```

### horse.json
```JSON
"minecraft:is_tamed": {}
```

### llama.json
```JSON
"minecraft:is_tamed": {}
```

### mule.json
```JSON
"minecraft:is_tamed": {}
```

### ocelot.json
```JSON
"minecraft:is_tamed": {}
```

### parrot.json
```JSON
"minecraft:is_tamed": {}
```

### skeleton_horse.json
```JSON
"minecraft:is_tamed": {}
```

### wolf.json
```JSON
"minecraft:is_tamed": {}
```

### zombie_horse.json
```JSON
"minecraft:is_tamed": {}
```

# minecraft:item_controllable
### pig.json
```JSON
"minecraft:item_controllable": {
    "control_items": "carrotOnAStick"
}
```

# minecraft:item_hopper
### hopper_minecart.json
```JSON
"minecraft:item_hopper": {}
```

# minecraft:jump.dynamic
### rabbit.json
```JSON
"minecraft:jump.dynamic": {}
```

# minecraft:jump.static
### bat.json
```JSON
"minecraft:jump.static": {}
```

### blaze.json
```JSON
"minecraft:jump.static": {}
```

### cat.json
```JSON
"minecraft:jump.static": {}
```

### cave_spider.json
```JSON
"minecraft:jump.static": {}
```

### chicken.json
```JSON
"minecraft:jump.static": {}
```

### cow.json
```JSON
"minecraft:jump.static": {}
```

### creeper.json
```JSON
"minecraft:jump.static": {}
```

### dolphin.json
```JSON
"minecraft:jump.static": {
    "jump_power": 0.6
}
```

### donkey.json
```JSON
"minecraft:jump.static": {}
```

### drowned.json
```JSON
"minecraft:jump.static": {}
```

### elder_guardian.json
```JSON
"minecraft:jump.static": {}
```

### enderman.json
```JSON
"minecraft:jump.static": {}
```

### endermite.json
```JSON
"minecraft:jump.static": {}
```

### evocation_illager.json
```JSON
"minecraft:jump.static": {}
```

### fox.json
```JSON
"minecraft:jump.static": {}
```

### ghast.json
```JSON
"minecraft:jump.static": {}
```

### guardian.json
```JSON
"minecraft:jump.static": {}
```

### horse.json
```JSON
"minecraft:jump.static": {}
```

### husk.json
```JSON
"minecraft:jump.static": {}
```

### iron_golem.json
```JSON
"minecraft:jump.static": {}
```

### llama.json
```JSON
"minecraft:jump.static": {}
```

### magma_cube.json
```JSON
"minecraft:jump.static": {}
```

### mooshroom.json
```JSON
"minecraft:jump.static": {}
```

### mule.json
```JSON
"minecraft:jump.static": {}
```

### ocelot.json
```JSON
"minecraft:jump.static": {}
```

### panda.json
```JSON
"minecraft:jump.static": {}
```

### parrot.json
```JSON
"minecraft:jump.static": {}
```

### pig.json
```JSON
"minecraft:jump.static": {}
```

### pillager.json
```JSON
"minecraft:jump.static": {}
```

### polar_bear.json
```JSON
"minecraft:jump.static": {}
```

### ravager.json
```JSON
"minecraft:jump.static": {}
```

### sheep.json
```JSON
"minecraft:jump.static": {}
```

### silverfish.json
```JSON
"minecraft:jump.static": {}
```

### skeleton.json
```JSON
"minecraft:jump.static": {}
```

### skeleton_horse.json
```JSON
"minecraft:jump.static": {}
```

### slime.json
```JSON
"minecraft:jump.static": {}
```

### snow_golem.json
```JSON
"minecraft:jump.static": {}
```

### spider.json
```JSON
"minecraft:jump.static": {}
```

### squid.json
```JSON
"minecraft:jump.static": {}
```

### stray.json
```JSON
"minecraft:jump.static": {}
```

### turtle.json
```JSON
"minecraft:jump.static": {}
```

### vex.json
```JSON
"minecraft:jump.static": {}
```

### villager.json
```JSON
"minecraft:jump.static": {}
```

### villager_v2.json
```JSON
"minecraft:jump.static": {}
```

### vindicator.json
```JSON
"minecraft:jump.static": {}
```

### wandering_trader.json
```JSON
"minecraft:jump.static": {}
```

### witch.json
```JSON
"minecraft:jump.static": {}
```

### wither.json
```JSON
"minecraft:jump.static": {}
```

### wither_skeleton.json
```JSON
"minecraft:jump.static": {}
```

### wolf.json
```JSON
"minecraft:jump.static": {}
```

### zombie.json
```JSON
"minecraft:jump.static": {}
```

### zombie_horse.json
```JSON
"minecraft:jump.static": {}
```

### zombie_pigman.json
```JSON
"minecraft:jump.static": {}
```

### zombie_villager.json
```JSON
"minecraft:jump.static": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:jump.static": {}
```

# minecraft:knockback_resistance
### ender_dragon.json
```JSON
"minecraft:knockback_resistance": {
    "value": 100,
    "max": 100
}
```

### iron_golem.json
```JSON
"minecraft:knockback_resistance": {
    "value": 1.0
}
```

### ravager.json
```JSON
"minecraft:knockback_resistance": {
    "value": 0.5
}
```

# minecraft:leashable
### boat.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cat.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### chicken.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cow.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### donkey.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### fox.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### horse.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### iron_golem.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### llama.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "can_be_stolen": true
}
```

### mooshroom.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### mule.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### ocelot.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
    },
    "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
    }
}
```

### pig.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### rabbit.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### sheep.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### skeleton_horse.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### snow_golem.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### squid.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### wolf.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "on_leash": {
        "event": "minecraft:on_leash",
        "target": "self"
    },
    "on_unleash": {
        "event": "minecraft:on_unleash",
        "target": "self"
    }
}
```

### zombie_horse.json
```JSON
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

# minecraft:lookat
### enderman.json
```JSON
"minecraft:lookat": {
    "search_radius": 64.0,
    "set_target": true,
    "look_cooldown": 5.0,
    "filters": {
        "all_of": [
            {
                "subject": "other",
                "test": "is_family",
                "value": "player"
            },
            {
                "test": "has_equipment",
                "domain": "head",
                "subject": "other",
                "operator": "not",
                "value": "carved_pumpkin"
            }
        ]
    }
}
```

# minecraft:loot
### armor_stand.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/armor_stand.json"
}
```

### blaze.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/blaze.json"
}
```

### boat.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/boat.json"
}
```

### cat.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/cat.json"
}
```

### cave_spider.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/spider.json"
}
```

### chicken.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/chicken.json"
}
```

### cow.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/cow.json"
}
```

### creeper.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/creeper.json"
}
```

### dolphin.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/dolphin.json"
}
```

### donkey.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### drowned.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/drowned.json"
}
```

### elder_guardian.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/elder_guardian.json"
}
```

### enderman.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/enderman.json"
}
```

### evocation_illager.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/evocation_illager.json"
}
```

### fish.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/fish.json"
}
```

### fishing_hook.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/gameplay/fishing.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/gameplay/jungle_fishing.json"
}
```

### fox.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/fox.json"
}
```

### ghast.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/ghast.json"
}
```

### guardian.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/guardian.json"
}
```

### horse.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### husk.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### iron_golem.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/iron_golem.json"
}
```

### llama.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/llama.json"
}
```

### magma_cube.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/magma_cube.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/magma_cube.json"
}
```

### mooshroom.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/mooshroom.json"
}
```

### mule.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/horse.json"
}
```

### ocelot.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/ocelot.json"
}
```

### panda.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/panda.json"
}
```

### parrot.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/parrot.json"
}
```

### phantom.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/phantom.json"
}
```

### pig.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/pig.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/pig_saddled.json"
}
```

### pillager.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/pillager.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/pillager_raid.json"
}
```

### player.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/empty.json"
}
```

### polar_bear.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/polar_bear.json"
}
```

### pufferfish.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/pufferfish.json"
}
```

### rabbit.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/rabbit.json"
}
```

### ravager.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/ravager.json"
}
```

### salmon.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/salmon_normal.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/salmon_normal.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/salmon_large.json"
}
```

### sheep.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/sheep_sheared.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/sheep.json"
}
```

### shulker.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/shulker.json"
}
```

### silverfish.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/silverfish.json"
}
```

### skeleton.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/skeleton.json"
}
```

### skeleton_horse.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/skeleton_horse.json"
}
```

### slime.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/slime.json"
}
```

### snow_golem.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/snowman.json"
}
```

### spider.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/spider.json"
}
```

### squid.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/squid.json"
}
```

### stray.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/stray.json"
}
```

### tripod_camera.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/empty.json"
}
```

### tropicalfish.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/tropicalfish.json"
}
```

### turtle.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/sea_turtle.json"
}
```

### vindicator.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/vindication_illager.json"
}
```

```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/vindicator_raid.json"
}
```

### witch.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/witch.json"
}
```

### wither.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/wither_boss.json"
}
```

### wither_skeleton.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/wither_skeleton.json"
}
```

### wolf.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/wolf.json"
}
```

### zombie.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_horse.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie_horse.json"
}
```

### zombie_pigman.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie_pigman.json"
}
```

### zombie_villager.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_villager_v2.json
```JSON
"minecraft:loot": {
    "table": "loot_tables/entities/zombie.json"
}
```

# minecraft:managed_wandering_trader
### wandering_trader.json
```JSON
"minecraft:managed_wandering_trader": {}
```

# minecraft:mark_variant
### horse.json
```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

### llama.json
```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

### mooshroom.json
```JSON
"minecraft:mark_variant": {
    "value": -1
}
```

```JSON
"minecraft:mark_variant": {
    "value": -1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 6
}
```

```JSON
"minecraft:mark_variant": {
    "value": 7
}
```

```JSON
"minecraft:mark_variant": {
    "value": 8
}
```

```JSON
"minecraft:mark_variant": {
    "value": 9
}
```

### tropicalfish.json
```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

### villager_v2.json
```JSON
"minecraft:mark_variant": {
    "value": 0
}
```

```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 6
}
```

### zombie_villager_v2.json
```JSON
"minecraft:mark_variant": {
    "value": 1
}
```

```JSON
"minecraft:mark_variant": {
    "value": 2
}
```

```JSON
"minecraft:mark_variant": {
    "value": 3
}
```

```JSON
"minecraft:mark_variant": {
    "value": 4
}
```

```JSON
"minecraft:mark_variant": {
    "value": 5
}
```

```JSON
"minecraft:mark_variant": {
    "value": 6
}
```

# minecraft:mob_effect
### pufferfish.json
```JSON
"minecraft:mob_effect": {
    "effect_range": 0.2,
    "mob_effect": "poison",
    "effect_time": 10,
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

# minecraft:movement
### bat.json
```JSON
"minecraft:movement": {
    "value": 0.1
}
```

### blaze.json
```JSON
"minecraft:movement": {
    "value": 0.23
}
```

### cat.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### cave_spider.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### chicken.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### cow.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### creeper.json
```JSON
"minecraft:movement": {
    "value": 0.2
}
```

### dolphin.json
```JSON
"minecraft:movement": {
    "value": 0.1
}
```

### donkey.json
```JSON
"minecraft:movement": {
    "value": 0.175
}
```

### drowned.json
```JSON
"minecraft:movement": {
    "value": 0.23
}
```

```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### elder_guardian.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### enderman.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

```JSON
"minecraft:movement": {
    "value": 0.45
}
```

### endermite.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### ender_dragon.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### evocation_illager.json
```JSON
"minecraft:movement": {
    "value": 0.5
}
```

### fish.json
```JSON
"minecraft:movement": {
    "value": 0.1
}
```

### fox.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### ghast.json
```JSON
"minecraft:movement": {
    "value": 0.03
}
```

### guardian.json
```JSON
"minecraft:movement": {
    "value": 0.12
}
```

### horse.json
```JSON
"minecraft:movement": {
    "value": {
        "range_min": 0.1125,
        "range_max": 0.3375
    }
}
```

### husk.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

```JSON
"minecraft:movement": {
    "value": 0.23
}
```

### iron_golem.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### llama.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### magma_cube.json
```JSON
"minecraft:movement": {
    "value": 0.75
}
```

```JSON
"minecraft:movement": {
    "value": 0.66
}
```

```JSON
"minecraft:movement": {
    "value": 0.6
}
```

### mooshroom.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### mule.json
```JSON
"minecraft:movement": {
    "value": 0.175
}
```

### ocelot.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### panda.json
```JSON
"minecraft:movement": {
    "value": 0.15
}
```

```JSON
"minecraft:movement": {
    "value": 0.07
}
```

### parrot.json
```JSON
"minecraft:movement": {
    "value": 0.4
}
```

### phantom.json
```JSON
"minecraft:movement": {
    "value": 1.8
}
```

### pig.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### pillager.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

### player.json
```JSON
"minecraft:movement": {
    "value": 0.1
}
```

### polar_bear.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### pufferfish.json
```JSON
"minecraft:movement": {
    "value": 0.13
}
```

### rabbit.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### ravager.json
```JSON
"minecraft:movement": {
    "value": 0.0
}
```

```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### salmon.json
```JSON
"minecraft:movement": {
    "value": 0.12
}
```

### sheep.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### shulker.json
```JSON
"minecraft:movement": {
    "value": 0.0,
    "max": 0.0
}
```

### silverfish.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### skeleton.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### skeleton_horse.json
```JSON
"minecraft:movement": {
    "value": 0.2
}
```

### slime.json
```JSON
"minecraft:movement": {
    "value": 0.6
}
```

```JSON
"minecraft:movement": {
    "value": 0.4
}
```

```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### snow_golem.json
```JSON
"minecraft:movement": {
    "value": 0.2
}
```

### spider.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### squid.json
```JSON
"minecraft:movement": {
    "value": 0.2
}
```

### stray.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### tropicalfish.json
```JSON
"minecraft:movement": {
    "value": 0.12
}
```

### turtle.json
```JSON
"minecraft:movement": {
    "value": 0.1
}
```

### vex.json
```JSON
"minecraft:movement": {
    "value": 1.0
}
```

### villager.json
```JSON
"minecraft:movement": {
    "value": 0.5
}
```

### villager_v2.json
```JSON
"minecraft:movement": {
    "value": 0.5
}
```

### vindicator.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

### wandering_trader.json
```JSON
"minecraft:movement": {
    "value": 0.5
}
```

### witch.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### wither.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### wither_skeleton.json
```JSON
"minecraft:movement": {
    "value": 0.25
}
```

### wolf.json
```JSON
"minecraft:movement": {
    "value": 0.3
}
```

### zombie.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

```JSON
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_horse.json
```JSON
"minecraft:movement": {
    "value": 0.2
}
```

### zombie_pigman.json
```JSON
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_villager.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

```JSON
"minecraft:movement": {
    "value": 0.23
}
```

### zombie_villager_v2.json
```JSON
"minecraft:movement": {
    "value": 0.35
}
```

```JSON
"minecraft:movement": {
    "value": 0.23
}
```

# minecraft:movement.amphibious
### turtle.json
```JSON
"minecraft:movement.amphibious": {
    "max_turn": 5.0
}
```

# minecraft:movement.basic
### bat.json
```JSON
"minecraft:movement.basic": {}
```

### blaze.json
```JSON
"minecraft:movement.basic": {}
```

### cat.json
```JSON
"minecraft:movement.basic": {}
```

### cave_spider.json
```JSON
"minecraft:movement.basic": {}
```

### chicken.json
```JSON
"minecraft:movement.basic": {}
```

### cow.json
```JSON
"minecraft:movement.basic": {}
```

### creeper.json
```JSON
"minecraft:movement.basic": {}
```

### donkey.json
```JSON
"minecraft:movement.basic": {}
```

### enderman.json
```JSON
"minecraft:movement.basic": {}
```

### endermite.json
```JSON
"minecraft:movement.basic": {}
```

### evocation_illager.json
```JSON
"minecraft:movement.basic": {}
```

### fox.json
```JSON
"minecraft:movement.basic": {}
```

### horse.json
```JSON
"minecraft:movement.basic": {}
```

### husk.json
```JSON
"minecraft:movement.basic": {}
```

### iron_golem.json
```JSON
"minecraft:movement.basic": {}
```

### llama.json
```JSON
"minecraft:movement.basic": {}
```

### mooshroom.json
```JSON
"minecraft:movement.basic": {}
```

### mule.json
```JSON
"minecraft:movement.basic": {}
```

### ocelot.json
```JSON
"minecraft:movement.basic": {}
```

### panda.json
```JSON
"minecraft:movement.basic": {}
```

### pig.json
```JSON
"minecraft:movement.basic": {}
```

### pillager.json
```JSON
"minecraft:movement.basic": {}
```

### polar_bear.json
```JSON
"minecraft:movement.basic": {}
```

### ravager.json
```JSON
"minecraft:movement.basic": {}
```

### sheep.json
```JSON
"minecraft:movement.basic": {}
```

### shulker.json
```JSON
"minecraft:movement.basic": {}
```

### silverfish.json
```JSON
"minecraft:movement.basic": {}
```

### skeleton.json
```JSON
"minecraft:movement.basic": {}
```

### skeleton_horse.json
```JSON
"minecraft:movement.basic": {}
```

### snow_golem.json
```JSON
"minecraft:movement.basic": {}
```

### spider.json
```JSON
"minecraft:movement.basic": {}
```

### squid.json
```JSON
"minecraft:movement.basic": {}
```

### stray.json
```JSON
"minecraft:movement.basic": {}
```

### vex.json
```JSON
"minecraft:movement.basic": {}
```

### villager.json
```JSON
"minecraft:movement.basic": {}
```

### villager_v2.json
```JSON
"minecraft:movement.basic": {}
```

### vindicator.json
```JSON
"minecraft:movement.basic": {}
```

### wandering_trader.json
```JSON
"minecraft:movement.basic": {}
```

### witch.json
```JSON
"minecraft:movement.basic": {}
```

### wither.json
```JSON
"minecraft:movement.basic": {
    "max_turn": 180.0
}
```

### wither_skeleton.json
```JSON
"minecraft:movement.basic": {}
```

### wolf.json
```JSON
"minecraft:movement.basic": {}
```

### zombie.json
```JSON
"minecraft:movement.basic": {}
```

### zombie_horse.json
```JSON
"minecraft:movement.basic": {}
```

### zombie_pigman.json
```JSON
"minecraft:movement.basic": {}
```

### zombie_villager.json
```JSON
"minecraft:movement.basic": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:movement.basic": {}
```

# minecraft:movement.fly
### parrot.json
```JSON
"minecraft:movement.fly": {}
```

# minecraft:movement.generic
### drowned.json
```JSON
"minecraft:movement.generic": {}
```

# minecraft:movement.glide
### phantom.json
```JSON
"minecraft:movement.glide": {
    "start_speed": 0.1,
    "speed_when_turning": 0.2
}
```

# minecraft:movement.jump
### magma_cube.json
```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        0.667,
        2.0
    ]
}
```

### slime.json
```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```JSON
"minecraft:movement.jump": {
    "jump_delay": [
        0.16,
        0.5
    ]
}
```

# minecraft:movement.skip
### rabbit.json
```JSON
"minecraft:movement.skip": {}
```

# minecraft:movement.sway
### elder_guardian.json
```JSON
"minecraft:movement.sway": {}
```

### fish.json
```JSON
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### guardian.json
```JSON
"minecraft:movement.sway": {}
```

### pufferfish.json
```JSON
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### salmon.json
```JSON
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

### tropicalfish.json
```JSON
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

# minecraft:nameable
### armor_stand.json
```JSON
"minecraft:nameable": {}
```

### bat.json
```JSON
"minecraft:nameable": {}
```

### blaze.json
```JSON
"minecraft:nameable": {}
```

### cat.json
```JSON
"minecraft:nameable": {}
```

### cave_spider.json
```JSON
"minecraft:nameable": {}
```

### chicken.json
```JSON
"minecraft:nameable": {}
```

### cow.json
```JSON
"minecraft:nameable": {}
```

### creeper.json
```JSON
"minecraft:nameable": {}
```

### dolphin.json
```JSON
"minecraft:nameable": {}
```

### donkey.json
```JSON
"minecraft:nameable": {}
```

### drowned.json
```JSON
"minecraft:nameable": {}
```

### elder_guardian.json
```JSON
"minecraft:nameable": {}
```

### enderman.json
```JSON
"minecraft:nameable": {}
```

### endermite.json
```JSON
"minecraft:nameable": {}
```

### evocation_illager.json
```JSON
"minecraft:nameable": {}
```

### fish.json
```JSON
"minecraft:nameable": {}
```

### fox.json
```JSON
"minecraft:nameable": {}
```

### ghast.json
```JSON
"minecraft:nameable": {}
```

### guardian.json
```JSON
"minecraft:nameable": {}
```

### horse.json
```JSON
"minecraft:nameable": {}
```

### husk.json
```JSON
"minecraft:nameable": {}
```

### iron_golem.json
```JSON
"minecraft:nameable": {}
```

### llama.json
```JSON
"minecraft:nameable": {}
```

### magma_cube.json
```JSON
"minecraft:nameable": {}
```

### mooshroom.json
```JSON
"minecraft:nameable": {}
```

### mule.json
```JSON
"minecraft:nameable": {}
```

### ocelot.json
```JSON
"minecraft:nameable": {}
```

### panda.json
```JSON
"minecraft:nameable": {}
```

### parrot.json
```JSON
"minecraft:nameable": {}
```

### phantom.json
```JSON
"minecraft:nameable": {}
```

### pig.json
```JSON
"minecraft:nameable": {}
```

### pillager.json
```JSON
"minecraft:nameable": {}
```

### player.json
```JSON
"minecraft:nameable": {
    "always_show": true,
    "allow_name_tag_renaming": false
}
```

### polar_bear.json
```JSON
"minecraft:nameable": {}
```

### pufferfish.json
```JSON
"minecraft:nameable": {}
```

### rabbit.json
```JSON
"minecraft:nameable": {}
```

### ravager.json
```JSON
"minecraft:nameable": {}
```

### salmon.json
```JSON
"minecraft:nameable": {}
```

### sheep.json
```JSON
"minecraft:nameable": {}
```

### shulker.json
```JSON
"minecraft:nameable": {}
```

### silverfish.json
```JSON
"minecraft:nameable": {}
```

### skeleton.json
```JSON
"minecraft:nameable": {}
```

### skeleton_horse.json
```JSON
"minecraft:nameable": {}
```

### slime.json
```JSON
"minecraft:nameable": {}
```

### snow_golem.json
```JSON
"minecraft:nameable": {}
```

### spider.json
```JSON
"minecraft:nameable": {}
```

### squid.json
```JSON
"minecraft:nameable": {}
```

### stray.json
```JSON
"minecraft:nameable": {}
```

### tropicalfish.json
```JSON
"minecraft:nameable": {}
```

### turtle.json
```JSON
"minecraft:nameable": {}
```

### vex.json
```JSON
"minecraft:nameable": {}
```

### villager.json
```JSON
"minecraft:nameable": {}
```

### villager_v2.json
```JSON
"minecraft:nameable": {}
```

### vindicator.json
```JSON
"minecraft:nameable": {
    "default_trigger": {
        "event": "minecraft:stop_johnny",
        "target": "self"
    },
    "name_actions": [
        {
            "name_filter": "Johnny",
            "on_named": {
                "event": "minecraft:start_johnny",
                "target": "self"
            }
        }
    ]
}
```

### witch.json
```JSON
"minecraft:nameable": {}
```

### wither.json
```JSON
"minecraft:nameable": {}
```

### wither_skeleton.json
```JSON
"minecraft:nameable": {}
```

### wolf.json
```JSON
"minecraft:nameable": {}
```

### zombie.json
```JSON
"minecraft:nameable": {}
```

### zombie_horse.json
```JSON
"minecraft:nameable": {}
```

### zombie_pigman.json
```JSON
"minecraft:nameable": {}
```

### zombie_villager.json
```JSON
"minecraft:nameable": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:nameable": {}
```

# minecraft:navigation.climb
### cave_spider.json
```JSON
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

### spider.json
```JSON
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

# minecraft:navigation.float
### bat.json
```JSON
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

### ghast.json
```JSON
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

# minecraft:navigation.fly
### parrot.json
```JSON
"minecraft:navigation.fly": {
    "can_path_over_water": true
}
```

# minecraft:navigation.generic
### dolphin.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

### drowned.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": true,
    "can_walk": true,
    "avoid_sun": true
}
```

```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

### elder_guardian.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### fish.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### guardian.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### pufferfish.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### salmon.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### tropicalfish.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### turtle.json
```JSON
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": true,
    "can_sink": false,
    "avoid_damage_blocks": true
}
```

# minecraft:navigation.walk
### blaze.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### cat.json
```JSON
"minecraft:navigation.walk": {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### chicken.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### cow.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### creeper.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### donkey.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### enderman.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": false,
    "avoid_water": true
}
```

### endermite.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### evocation_illager.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### fox.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### horse.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### husk.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_portals": false
}
```

### iron_golem.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": false,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### llama.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### magma_cube.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### mooshroom.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### mule.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### ocelot.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### panda.json
```JSON
"minecraft:navigation.walk": {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### pig.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### pillager.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### polar_bear.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### rabbit.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### ravager.json
```JSON
"minecraft:navigation.walk": {
    "avoid_damage_blocks": true,
    "can_path_over_water": true,
    "can_sink": false
}
```

### sheep.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### shulker.json
```JSON
"minecraft:navigation.walk": {}
```

### silverfish.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### skeleton.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### skeleton_horse.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_water": true
}
```

### slime.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### snow_golem.json
```JSON
"minecraft:navigation.walk": {
    "avoid_water": true
}
```

### squid.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_sink": false
}
```

### stray.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### vex.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

### villager.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "can_walk": true,
    "avoid_water": true
}
```

### villager_v2.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### vindicator.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true
}
```

```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_break_doors": true
}
```

### wandering_trader.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### witch.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": false
}
```

### wither.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### wither_skeleton.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### wolf.json
```JSON
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### zombie.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_walk": true,
    "can_break_doors": true
}
```

### zombie_horse.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_water": true
}
```

### zombie_pigman.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_portals": true
}
```

### zombie_villager.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_sun": false
}
```

```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

### zombie_villager_v2.json
```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_sun": false
}
```

```JSON
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

# minecraft:on_death
### ender_dragon.json
```JSON
"minecraft:on_death": {
    "event": "minecraft:start_death",
    "target": "self"
}
```

# minecraft:on_friendly_anger
### llama.json
```JSON
"minecraft:on_friendly_anger": {
    "event": "minecraft:defend_wandering_trader",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### pillager.json
```JSON
"minecraft:on_friendly_anger": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```JSON
"minecraft:on_friendly_anger": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

### polar_bear.json
```JSON
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

# minecraft:on_hurt
### ender_crystal.json
```JSON
"minecraft:on_hurt": {
    "event": "minecraft:crystal_explode",
    "target": "self"
}
```

### pillager.json
```JSON
"minecraft:on_hurt": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```JSON
"minecraft:on_hurt": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

# minecraft:on_hurt_by_player
```JSON
"minecraft:on_hurt_by_player": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```JSON
"minecraft:on_hurt_by_player": {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

# minecraft:on_start_landing
### ender_dragon.json
```JSON
"minecraft:on_start_landing": {
    "event": "minecraft:start_land",
    "target": "self"
}
```

# minecraft:on_start_takeoff
```JSON
"minecraft:on_start_takeoff": {
    "event": "minecraft:start_fly",
    "target": "self"
}
```

# minecraft:on_target_acquired
### cave_spider.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### dolphin.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

```JSON
"minecraft:on_target_acquired": {}
```

### drowned.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:has_target",
    "target": "self"
}
```

### enderman.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### llama.json
```JSON
"minecraft:on_target_acquired": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:mad_at_wolf",
    "target": "self"
}
```

### magma_cube.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

```JSON
"minecraft:on_target_acquired": {}
```

### polar_bear.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### silverfish.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### slime.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### spider.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

### vindicator.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_aggro",
    "target": "self"
}
```

### wolf.json
```JSON
"minecraft:on_target_acquired": {}
```

```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### zombie_pigman.json
```JSON
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

# minecraft:on_target_escape
### creeper.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:stop_exploding",
    "target": "self"
}
```

```JSON
"minecraft:on_target_escape": {}
```

```JSON
"minecraft:on_target_escape": {}
```

### dolphin.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### drowned.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:lost_target",
    "target": "self"
}
```

### llama.json
```JSON
"minecraft:on_target_escape": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### magma_cube.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### panda.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### pillager.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:calm",
    "target": "self"
}
```

```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:calm",
    "target": "self"
}
```

### slime.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### vindicator.json
```JSON
"minecraft:on_target_escape": {
    "event": "minecraft:stop_aggro",
    "target": "self"
}
```

# minecraft:on_wake_with_owner
### cat.json
```JSON
"minecraft:on_wake_with_owner": {
    "event": "minecraft:pet_slept_with_owner",
    "target": "self"
}
```

# minecraft:peek
### shulker.json
```JSON
"minecraft:peek": {
    "on_open": {
        "event": "minecraft:on_open"
    },
    "on_close": {
        "event": "minecraft:on_close"
    },
    "on_target_open": {
        "event": "minecraft:on_open"
    }
}
```

# minecraft:persistent
### armor_stand.json
```JSON
"minecraft:persistent": {}
```

### ender_dragon.json
```JSON
"minecraft:persistent": {}
```

### evocation_illager.json
```JSON
"minecraft:persistent": {}
```

### iron_golem.json
```JSON
"minecraft:persistent": {}
```

### snow_golem.json
```JSON
"minecraft:persistent": {}
```

### villager.json
```JSON
"minecraft:persistent": {}
```

### villager_v2.json
```JSON
"minecraft:persistent": {}
```

### wither.json
```JSON
"minecraft:persistent": {}
```

# minecraft:physics
### area_effect_cloud.json
```JSON
"minecraft:physics": {
    "has_collision": false
}
```

### armor_stand.json
```JSON
"minecraft:physics": {}
```

### arrow.json
```JSON
"minecraft:physics": {}
```

### bat.json
```JSON
"minecraft:physics": {}
```

### blaze.json
```JSON
"minecraft:physics": {}
```

### boat.json
```JSON
"minecraft:physics": {}
```

### cat.json
```JSON
"minecraft:physics": {}
```

### cave_spider.json
```JSON
"minecraft:physics": {}
```

### chest_minecart.json
```JSON
"minecraft:physics": {}
```

### chicken.json
```JSON
"minecraft:physics": {}
```

### command_block_minecart.json
```JSON
"minecraft:physics": {}
```

### cow.json
```JSON
"minecraft:physics": {}
```

### creeper.json
```JSON
"minecraft:physics": {}
```

### dolphin.json
```JSON
"minecraft:physics": {}
```

### donkey.json
```JSON
"minecraft:physics": {}
```

### drowned.json
```JSON
"minecraft:physics": {}
```

### egg.json
```JSON
"minecraft:physics": {}
```

### elder_guardian.json
```JSON
"minecraft:physics": {}
```

### enderman.json
```JSON
"minecraft:physics": {}
```

### endermite.json
```JSON
"minecraft:physics": {}
```

### ender_crystal.json
```JSON
"minecraft:physics": {}
```

### ender_dragon.json
```JSON
"minecraft:physics": {
    "has_gravity": false,
    "has_collision": false
}
```

### ender_pearl.json
```JSON
"minecraft:physics": {}
```

### evocation_illager.json
```JSON
"minecraft:physics": {}
```

### eye_of_ender_signal.json
```JSON
"minecraft:physics": {}
```

### fireball.json
```JSON
"minecraft:physics": {}
```

### fireworks_rocket.json
```JSON
"minecraft:physics": {}
```

### fish.json
```JSON
"minecraft:physics": {
    "has_gravity": false
}
```

### fishing_hook.json
```JSON
"minecraft:physics": {}
```

### fox.json
```JSON
"minecraft:physics": {}
```

### ghast.json
```JSON
"minecraft:physics": {}
```

### guardian.json
```JSON
"minecraft:physics": {}
```

### hopper_minecart.json
```JSON
"minecraft:physics": {}
```

### horse.json
```JSON
"minecraft:physics": {}
```

### husk.json
```JSON
"minecraft:physics": {}
```

### iron_golem.json
```JSON
"minecraft:physics": {}
```

### lingering_potion.json
```JSON
"minecraft:physics": {}
```

### llama.json
```JSON
"minecraft:physics": {}
```

### llama_spit.json
```JSON
"minecraft:physics": {}
```

### magma_cube.json
```JSON
"minecraft:physics": {}
```

### minecart.json
```JSON
"minecraft:physics": {}
```

### mooshroom.json
```JSON
"minecraft:physics": {}
```

### mule.json
```JSON
"minecraft:physics": {}
```

### ocelot.json
```JSON
"minecraft:physics": {}
```

### panda.json
```JSON
"minecraft:physics": {}
```

### parrot.json
```JSON
"minecraft:physics": {}
```

### phantom.json
```JSON
"minecraft:physics": {
    "has_gravity": false
}
```

### pig.json
```JSON
"minecraft:physics": {}
```

### pillager.json
```JSON
"minecraft:physics": {}
```

### player.json
```JSON
"minecraft:physics": {}
```

### polar_bear.json
```JSON
"minecraft:physics": {}
```

### pufferfish.json
```JSON
"minecraft:physics": {
    "has_gravity": false
}
```

### rabbit.json
```JSON
"minecraft:physics": {}
```

### ravager.json
```JSON
"minecraft:physics": {}
```

### salmon.json
```JSON
"minecraft:physics": {
    "has_gravity": false
}
```

### sheep.json
```JSON
"minecraft:physics": {}
```

### shulker.json
```JSON
"minecraft:physics": {}
```

### shulker_bullet.json
```JSON
"minecraft:physics": {
    "has_collision": false
}
```

### silverfish.json
```JSON
"minecraft:physics": {}
```

### skeleton.json
```JSON
"minecraft:physics": {}
```

### skeleton_horse.json
```JSON
"minecraft:physics": {}
```

### slime.json
```JSON
"minecraft:physics": {}
```

### small_fireball.json
```JSON
"minecraft:physics": {}
```

### snowball.json
```JSON
"minecraft:physics": {}
```

### snow_golem.json
```JSON
"minecraft:physics": {}
```

### spider.json
```JSON
"minecraft:physics": {}
```

### splash_potion.json
```JSON
"minecraft:physics": {}
```

### squid.json
```JSON
"minecraft:physics": {}
```

### stray.json
```JSON
"minecraft:physics": {}
```

### thrown_trident.json
```JSON
"minecraft:physics": {}
```

### tnt.json
```JSON
"minecraft:physics": {}
```

### tnt_minecart.json
```JSON
"minecraft:physics": {}
```

### tripod_camera.json
```JSON
"minecraft:physics": {}
```

### tropicalfish.json
```JSON
"minecraft:physics": {
    "has_gravity": false
}
```

### turtle.json
```JSON
"minecraft:physics": {}
```

### vex.json
```JSON
"minecraft:physics": {
    "has_gravity": false,
    "has_collision": false
}
```

### villager.json
```JSON
"minecraft:physics": {}
```

### villager_v2.json
```JSON
"minecraft:physics": {}
```

### vindicator.json
```JSON
"minecraft:physics": {}
```

### wandering_trader.json
```JSON
"minecraft:physics": {}
```

### witch.json
```JSON
"minecraft:physics": {}
```

### wither.json
```JSON
"minecraft:physics": {}
```

### wither_skeleton.json
```JSON
"minecraft:physics": {}
```

### wither_skull.json
```JSON
"minecraft:physics": {}
```

### wither_skull_dangerous.json
```JSON
"minecraft:physics": {}
```

### wolf.json
```JSON
"minecraft:physics": {}
```

### xp_bottle.json
```JSON
"minecraft:physics": {}
```

### zombie.json
```JSON
"minecraft:physics": {}
```

### zombie_horse.json
```JSON
"minecraft:physics": {}
```

### zombie_pigman.json
```JSON
"minecraft:physics": {}
```

### zombie_villager.json
```JSON
"minecraft:physics": {}
```

### zombie_villager_v2.json
```JSON
"minecraft:physics": {}
```

# minecraft:player.exhaustion
### player.json
```JSON
"minecraft:player.exhaustion": {
    "value": 0,
    "max": 4
}
```

# minecraft:player.experience
```JSON
"minecraft:player.experience": {
    "value": 0,
    "max": 1
}
```

# minecraft:player.level
```JSON
"minecraft:player.level": {
    "value": 0,
    "max": 24791
}
```

# minecraft:player.saturation
```JSON
"minecraft:player.saturation": {
    "value": 20
}
```

# minecraft:preferred_path
### iron_golem.json
```JSON
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

```JSON
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 20,
    "default_block_cost": 3,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "stone_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

# minecraft:projectile
### arrow.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                4
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                5
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": true,
            "semi_random_diff_damage": true,
            "destroy_on_hit": true,
            "max_critical_damage": 10,
            "min_critical_damage": 9,
            "power_multiplier": 0.97
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 5.0,
    "gravity": 0.05,
    "uncertainty_base": 1,
    "uncertainty_multiplier": 0,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                3,
                6
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {}
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

### dragon_fireball.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "spawn_aoe_cloud": {
            "radius": 6.0,
            "radius_on_use": 0,
            "potion": 23,
            "particle": "dragonbreath",
            "duration": 120,
            "color": [
                220,
                0,
                239
            ],
            "affect_owner": false
        },
        "remove_on_hit": {}
    },
    "power": 1.3,
    "gravity": 0.0,
    "inertia": 1,
    "anchor": 2,
    "offset": [
        0,
        0.5,
        0
    ],
    "semi_random_diff_damage": true,
    "uncertainty_base": 10.0,
    "reflect_on_hurt": true,
    "hit_sound": "explode"
}
```

### egg.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 0,
            "knockback": true,
            "destroy_on_hit": true
        },
        "spawn_chance": {
            "first_spawn_chance": 8,
            "second_spawn_chance": 32,
            "first_spawn_count": 1,
            "second_spawn_count": 4,
            "spawn_definition": "minecraft:chicken",
            "spawn_baby": true
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "iconcrack",
            "num_particles": 6,
            "on_entity_hit": true,
            "on_other_hit": true
        }
    },
    "power": 1.5,
    "gravity": 0.03,
    "angle_offset": 0.0
}
```

### ender_pearl.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "spawn_chance": {
            "first_spawn_percent_chance": 5.0,
            "first_spawn_count": 1,
            "spawn_definition": "minecraft:endermite"
        },
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

```JSON
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

### fireball.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        }
    },
    "power": 1.6,
    "gravity": 0.0,
    "inertia": 1,
    "liquid_inertia": 1,
    "uncertainty_base": 0,
    "uncertainty_multiplier": 0,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "reflect_on_hurt": true,
    "catch_fire": true
}
```

### fishing_hook.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "stick_in_ground": {}
    }
}
```

### lingering_potion.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "douse_fire": {},
        "spawn_aoe_cloud": {
            "radius": 3.0,
            "radius_on_use": -0.5,
            "duration": 30,
            "reapplication_delay": 40
        },
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

### llama_spit.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": false
        },
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.06,
    "inertia": 1,
    "uncertainty_base": 10,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "reflect_on_hurt": true
}
```

### shulker_bullet.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 4,
            "knockback": true,
            "should_bounce": true
        },
        "mob_effect": {
            "effect": "levitation",
            "durationeasy": 200,
            "durationnormal": 200,
            "durationhard": 200,
            "amplifier": 1
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "largeexplode",
            "on_other_hit": true
        }
    },
    "hit_sound": "bullet.hit",
    "destroyOnHurt": true,
    "crit_particle_on_hurt": true,
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "homing": true
}
```

### small_fireball.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 5,
            "knockback": false,
            "catch_fire": true,
            "semi_random_diff_damage": false
        },
        "catch_fire": {
            "fire_affected_by_griefing": true
        },
        "remove_on_hit": {}
    },
    "power": 1.3,
    "gravity": 0.0,
    "inertia": 1,
    "liquid_inertia": 1,
    "anchor": 2,
    "offset": [
        0,
        0.5,
        0
    ],
    "semi_random_diff_damage": true,
    "uncertainty_base": 10.0,
    "reflect_on_hurt": true
}
```

### snowball.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "filter": "blaze",
            "damage": 3,
            "knockback": true
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "snowballpoof",
            "num_particles": 6,
            "on_entity_hit": true,
            "on_other_hit": true
        }
    },
    "power": 1.5,
    "gravity": 0.03,
    "angle_offset": 0.0
}
```

### splash_potion.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "douse_fire": {},
        "thrown_potion_effect": {},
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

### thrown_trident.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 8,
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": false
        },
        "stick_in_ground": {
            "shake_time": 0
        }
    },
    "liquid_inertia": 0.99,
    "hit_sound": "item.trident.hit",
    "hit_ground_sound": "item.trident.hit_ground",
    "power": 4,
    "gravity": 0.1,
    "uncertainty_base": 1,
    "uncertainty_multiplier": 0,
    "stop_on_hurt": true,
    "anchor": 1,
    "should_bounce": true,
    "multiple_targets": false,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

### wither_skull.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        },
        "mob_effect": {
            "effect": "wither",
            "durationeasy": 0,
            "durationnormal": 200,
            "durationhard": 800,
            "amplifier": 1
        }
    },
    "power": 1.2,
    "gravity": 0.0,
    "uncertainty_base": 7.5,
    "uncertainty_multiplier": 1,
    "shoot_sound": "bow",
    "hit_sound": "bow.hit",
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "inertia": 1.0,
    "liquid_inertia": 1.0,
    "shoot_target": false
}
```

### wither_skull_dangerous.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "minecraft:explode",
                "target": "self"
            }
        },
        "mob_effect": {
            "effect": "wither",
            "durationeasy": 0,
            "durationnormal": 200,
            "durationhard": 800,
            "amplifier": 1
        }
    },
    "power": 0.6,
    "gravity": 0.0,
    "uncertainty_base": 7.5,
    "uncertainty_multiplier": 1,
    "shoot_sound": "bow",
    "hit_sound": "bow.hit",
    "anchor": 1,
    "offset": [
        0,
        -0.1,
        0
    ],
    "is_dangerous": true,
    "inertia": 1.0,
    "liquid_inertia": 1.0,
    "shoot_target": false,
    "reflect_on_hurt": true
}
```

### xp_bottle.json
```JSON
"minecraft:projectile": {
    "on_hit": {
        "grant_xp": {
            "minXP": 3,
            "maxXP": 11
        },
        "remove_on_hit": {}
    },
    "power": 0.5,
    "gravity": 0.05,
    "angle_offset": -20.0,
    "hit_sound": "glass"
}
```

# minecraft:pushable
### armor_stand.json
```JSON
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### arrow.json
```JSON
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### blaze.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### boat.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cat.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cave_spider.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chest_minecart.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chicken.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### command_block_minecart.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cow.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### creeper.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### dolphin.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### donkey.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### drowned.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### egg.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### elder_guardian.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### enderman.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### endermite.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_crystal.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_pearl.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### evocation_illager.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### eye_of_ender_signal.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireball.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireworks_rocket.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fish.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fishing_hook.json
```JSON
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### fox.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ghast.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### guardian.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### hopper_minecart.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### horse.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### husk.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### iron_golem.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### lingering_potion.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama_spit.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### magma_cube.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### minecart.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mooshroom.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mule.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ocelot.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### panda.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### parrot.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### phantom.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pig.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pillager.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### player.json
```JSON
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### polar_bear.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pufferfish.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### rabbit.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ravager.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### salmon.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### sheep.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### silverfish.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton_horse.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### slime.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### small_fireball.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snowball.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snow_golem.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### spider.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### splash_potion.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### squid.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### stray.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### thrown_trident.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tnt.json
```JSON
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### tnt_minecart.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tropicalfish.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### turtle.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager_v2.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### vindicator.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wandering_trader.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### witch.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skeleton.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull_dangerous.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wolf.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### xp_bottle.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_horse.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_pigman.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager_v2.json
```JSON
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

# minecraft:raid_trigger
### player.json
```JSON
"minecraft:raid_trigger": {
    "triggered_event": {
        "event": "minecraft:remove_raid_trigger",
        "target": "self"
    }
}
```

# minecraft:rail_movement
### chest_minecart.json
```JSON
"minecraft:rail_movement": {}
```

### command_block_minecart.json
```JSON
"minecraft:rail_movement": {}
```

### hopper_minecart.json
```JSON
"minecraft:rail_movement": {}
```

### minecart.json
```JSON
"minecraft:rail_movement": {}
```

### tnt_minecart.json
```JSON
"minecraft:rail_movement": {}
```

# minecraft:rail_sensor
### command_block_minecart.json
```JSON
"minecraft:rail_sensor": {
    "check_block_types": true,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_deactivate": {
        "event": "minecraft:command_block_deactivate"
    }
}
```

```JSON
"minecraft:rail_sensor": {
    "check_block_types": false,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_activate": {
        "event": "minecraft:command_block_activate"
    }
}
```

### hopper_minecart.json
```JSON
"minecraft:rail_sensor": {
    "on_activate": {
        "event": "minecraft:hopper_deactivate"
    }
}
```

```JSON
"minecraft:rail_sensor": {
    "on_deactivate": {
        "event": "minecraft:hopper_activate"
    }
}
```

### minecart.json
```JSON
"minecraft:rail_sensor": {
    "eject_on_activate": true
}
```

### tnt_minecart.json
```JSON
"minecraft:rail_sensor": {}
```

```JSON
"minecraft:rail_sensor": {}
```

```JSON
"minecraft:rail_sensor": {
    "on_activate": {
        "filters": {
            "all_of": [
                {
                    "test": "is_game_rule",
                    "domain": "tntexplodes",
                    "operator": "==",
                    "value": true
                }
            ]
        },
        "event": "minecraft:on_prime"
    }
}
```

# minecraft:ravager_blocked
### ravager.json
```JSON
"minecraft:ravager_blocked": {
    "knockback_strength": 3.0,
    "reaction_choices": [
        {
            "weight": 1,
            "value": {
                "event": "minecraft:become_stunned",
                "target": "self"
            }
        },
        {
            "weight": 1
        }
    ]
}
```

# minecraft:rideable
### boat.json
```JSON
"minecraft:rideable": {
    "seat_count": 2,
    "interact_text": "action.interact.ride.boat",
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.0,
                -0.2,
                0.0
            ],
            "min_rider_count": 0,
            "max_rider_count": 1,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                0.2,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                -0.6,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "lock_rider_rotation": 90
        }
    ]
}
```

### cat.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.35,
            0.0
        ]
    }
}
```

### cave_spider.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            0.0
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            -0.1
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            -0.1
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.25,
            -0.1
        ]
    }
}
```

### chicken.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.4,
            0.0
        ]
    }
}
```

### cow.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### donkey.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            0.925,
            -0.2
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            0.925,
            -0.2
        ]
    }
}
```

### horse.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

### husk.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### llama.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            1.25,
            -0.3
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.2
        ]
    }
}
```

### minecart.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "interact_text": "action.interact.ride.minecart",
    "pull_in_entities": true,
    "seats": {
        "position": [
            0.0,
            -0.2,
            0.0
        ]
    }
}
```

### mooshroom.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### mule.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "zombie"
    ],
    "interact_text": "action.interact.mount",
    "seats": {
        "position": [
            0.0,
            0.975,
            -0.2
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "crouching_skip_interact": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            0.975,
            -0.2
        ]
    }
}
```

### ocelot.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.35,
            0.0
        ]
    }
}
```

### panda.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.105,
            0.0
        ]
    }
}
```

### pig.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.63,
            0.0
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "interact_text": "action.interact.mount",
    "family_types": [
        "player"
    ],
    "seats": {
        "position": [
            0.0,
            0.63,
            0.0
        ]
    }
}
```

### player.json
```JSON
"minecraft:rideable": {
    "seat_count": 2,
    "family_types": [
        "parrot_tame"
    ],
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.4,
                -0.2,
                -0.1
            ],
            "min_rider_count": 0,
            "max_rider_count": 0,
            "lock_rider_rotation": 0
        },
        {
            "position": [
                -0.4,
                -0.2,
                -0.1
            ],
            "min_rider_count": 1,
            "max_rider_count": 2,
            "lock_rider_rotation": 0
        }
    ]
}
```

### ravager.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "pillager",
        "vindicator",
        "evocation_illager"
    ],
    "seats": {
        "position": [
            0.0,
            2.1,
            -0.3
        ]
    }
}
```

### sheep.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.9,
            0.0
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.975,
            0.0
        ]
    }
}
```

### skeleton_horse.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "skeleton",
        "zombie"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.2,
            -0.2
        ]
    }
}
```

```JSON
"minecraft:rideable": {}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "player",
        "skeleton",
        "zombie"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.2,
            -0.2
        ]
    }
}
```

### spider.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            -0.1
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            0.0
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            0.0
        ]
    }
}
```

```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.54,
            0.0
        ]
    }
}
```

### wolf.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.675,
            -0.1
        ]
    }
}
```

### zombie.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### zombie_horse.json
```JSON
"minecraft:rideable": {
    "priority": 0,
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": {
        "position": [
            0.0,
            1.2,
            -0.2
        ]
    }
}
```

### zombie_pigman.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ],
        "lock_rider_rotation": 0
    }
}
```

### zombie_villager.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ]
    }
}
```

### zombie_villager_v2.json
```JSON
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            1.1,
            -0.35
        ]
    }
}
```

# minecraft:scaffolding_climber
### player.json
```JSON
"minecraft:scaffolding_climber": {}
```

# minecraft:scale
### cat.json
```JSON
"minecraft:scale": {
    "value": 0.4
}
```

```JSON
"minecraft:scale": {
    "value": 0.8
}
```

### chicken.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### cow.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### dolphin.json
```JSON
"minecraft:scale": {
    "value": 0.65
}
```

### drowned.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### fish.json
```JSON
"minecraft:scale": {
    "value": 1.0
}
```

### fox.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### husk.json
```JSON
"minecraft:scale": {
    "value": 0.53125
}
```

```JSON
"minecraft:scale": {
    "value": 1.0625
}
```

### llama.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### mooshroom.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### ocelot.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

```JSON
"minecraft:scale": {
    "value": 1
}
```

### panda.json
```JSON
"minecraft:scale": {
    "value": 1.0
}
```

```JSON
"minecraft:scale": {
    "value": 0.4
}
```

### pig.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### polar_bear.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### pufferfish.json
```JSON
"minecraft:scale": {
    "value": 1.2
}
```

### rabbit.json
```JSON
"minecraft:scale": {
    "value": 0.4
}
```

```JSON
"minecraft:scale": {
    "value": 0.6
}
```

### salmon.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

```JSON
"minecraft:scale": {
    "value": 1
}
```

```JSON
"minecraft:scale": {
    "value": 1.5
}
```

### sheep.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### squid.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### tropicalfish.json
```JSON
"minecraft:scale": {
    "value": 1.3
}
```

### turtle.json
```JSON
"minecraft:scale": {
    "value": 0.16
}
```

### villager.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### villager_v2.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### wither_skeleton.json
```JSON
"minecraft:scale": {
    "value": 1.2
}
```

### wolf.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### zombie.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_pigman.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_villager.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

### zombie_villager_v2.json
```JSON
"minecraft:scale": {
    "value": 0.5
}
```

# minecraft:scale_by_age
### donkey.json
```JSON
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### horse.json
```JSON
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### mule.json
```JSON
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### skeleton_horse.json
```JSON
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### zombie_horse.json
```JSON
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

# minecraft:scheduler
### fox.json
```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 0,
    "scheduled_events": [
        {
            "filters": [
                {
                    "test": "is_sleeping",
                    "value": true
                }
            ],
            "event": "minecraft:ambient_sleep"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": false
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 16
                    }
                ]
            },
            "event": "minecraft:ambient_night"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_sleeping",
                        "value": false
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": true
                            },
                            {
                                "test": "distance_to_nearest_player",
                                "operator": "<=",
                                "value": 16
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:ambient_normal"
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_play_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 2000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 13000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 13000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 14000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 14000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 2000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_fisher"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_fisher"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_librarian"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_librarian"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```JSON
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_farmer"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_farmer"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

# minecraft:shareables
### fox.json
```JSON
"minecraft:shareables": {
    "all_items": true,
    "all_items_max_amount": 1,
    "items": [
        {
            "item": "minecraft:apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:appleEnchanted",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:baked_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot_soup",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:bread",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chorus_fruit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:clownfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cookie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:dried_kelp",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:melon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:mushroom_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonCooked",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonRaw",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:poisonous_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pufferfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pumpkin_pie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rotten_flesh",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:spider_eye",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:sweet_berries",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:suspicious_stew",
            "priority": 0,
            "max_amount": 1
        }
    ]
}
```

### villager.json
```JSON
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 60,
            "surplus_amount": 4
        },
        {
            "item": "minecraft:potato",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:wheat_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:beetroot_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:wheat",
            "want_amount": 45,
            "surplus_amount": 18,
            "craft_into": "minecraft:bread"
        }
    ]
}
```

```JSON
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 12,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:potato",
            "want_amount": 12,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 12,
            "surplus_amount": 24
        }
    ]
}
```

### villager_v2.json
```JSON
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 60,
            "surplus_amount": 4
        },
        {
            "item": "minecraft:potato",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:wheat_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:beetroot_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:wheat",
            "want_amount": 45,
            "surplus_amount": 18,
            "craft_into": "minecraft:bread"
        }
    ]
}
```

```JSON
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 60,
            "surplus_amount": 4
        },
        {
            "item": "minecraft:potato",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 60,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:wheat_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:beetroot_seeds",
            "want_amount": 64,
            "surplus_amount": 64
        },
        {
            "item": "minecraft:wheat",
            "want_amount": 45,
            "surplus_amount": 18,
            "craft_into": "minecraft:bread"
        }
    ]
}
```

```JSON
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:bread",
            "want_amount": 3,
            "surplus_amount": 6
        },
        {
            "item": "minecraft:carrot",
            "want_amount": 12,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:potato",
            "want_amount": 12,
            "surplus_amount": 24
        },
        {
            "item": "minecraft:beetroot",
            "want_amount": 12,
            "surplus_amount": 24
        }
    ]
}
```

# minecraft:shooter
### blaze.json
```JSON
"minecraft:shooter": {
    "type": "smallfireball",
    "def": "minecraft:small_fireball"
}
```

### drowned.json
```JSON
"minecraft:shooter": {
    "def": "minecraft:thrown_trident"
}
```

### ender_dragon.json
```JSON
"minecraft:shooter": {
    "type": "dragonfireball",
    "def": "minecraft:dragon_fireball"
}
```

### ghast.json
```JSON
"minecraft:shooter": {
    "type": "largefireball",
    "def": "minecraft:fireball"
}
```

### llama.json
```JSON
"minecraft:shooter": {
    "type": "llamaspit",
    "def": "minecraft:llama_spit"
}
```

### pillager.json
```JSON
"minecraft:shooter": {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

### shulker.json
```JSON
"minecraft:shooter": {
    "type": "ShulkerBullet",
    "def": "minecraft:shulker_bullet"
}
```

### skeleton.json
```JSON
"minecraft:shooter": {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

```JSON
"minecraft:shooter": {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

### snow_golem.json
```JSON
"minecraft:shooter": {
    "def": "minecraft:snowball"
}
```

### stray.json
```JSON
"minecraft:shooter": {
    "type": "Arrow",
    "def": "minecraft:arrow",
    "aux_val": 19
}
```

```JSON
"minecraft:shooter": {
    "type": "Arrow",
    "def": "minecraft:arrow",
    "aux_val": 19
}
```

# minecraft:sittable
### cat.json
```JSON
"minecraft:sittable": {}
```

### ocelot.json
```JSON
"minecraft:sittable": {}
```

### parrot.json
```JSON
"minecraft:sittable": {}
```

### wolf.json
```JSON
"minecraft:sittable": {}
```

# minecraft:skin_id
### villager_v2.json
```JSON
"minecraft:skin_id": {
    "value": 0
}
```

```JSON
"minecraft:skin_id": {
    "value": 1
}
```

```JSON
"minecraft:skin_id": {
    "value": 2
}
```

```JSON
"minecraft:skin_id": {
    "value": 3
}
```

```JSON
"minecraft:skin_id": {
    "value": 4
}
```

```JSON
"minecraft:skin_id": {
    "value": 5
}
```

### zombie_villager_v2.json
```JSON
"minecraft:skin_id": {
    "value": 0
}
```

```JSON
"minecraft:skin_id": {
    "value": 1
}
```

```JSON
"minecraft:skin_id": {
    "value": 2
}
```

```JSON
"minecraft:skin_id": {
    "value": 3
}
```

```JSON
"minecraft:skin_id": {
    "value": 4
}
```

```JSON
"minecraft:skin_id": {
    "value": 5
}
```

# minecraft:spawn_entity
### chicken.json
```JSON
"minecraft:spawn_entity": {
    "min_wait_time": 300,
    "max_wait_time": 600,
    "spawn_sound": "plop",
    "spawn_item": "egg",
    "filters": {
        "test": "rider_count",
        "subject": "self",
        "operator": "==",
        "value": 0
    }
}
```

### wandering_trader.json
```JSON
"minecraft:spawn_entity": [
    {
        "min_wait_time": 0,
        "max_wait_time": 0,
        "spawn_entity": "llama",
        "spawn_event": "minecraft:from_wandering_trader",
        "single_use": true,
        "num_to_spawn": 2,
        "should_leash": true
    }
]
```

# minecraft:spell_effects
### player.json
```JSON
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "bad_omen",
            "duration": 6000,
            "display_on_screen_animation": true
        }
    ]
}
```

```JSON
"minecraft:spell_effects": {}
```

```JSON
"minecraft:spell_effects": {
    "remove_effects": "bad_omen"
}
```

### zombie_villager.json
```JSON
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 100
        },
        {
            "effect": "heal",
            "duration": 100
        }
    ],
    "remove_effects": "weakness"
}
```

### zombie_villager_v2.json
```JSON
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 100
        },
        {
            "effect": "heal",
            "duration": 100
        }
    ],
    "remove_effects": "weakness"
}
```

# minecraft:strength
### llama.json
```JSON
"minecraft:strength": {
    "value": 1,
    "max": 5
}
```

```JSON
"minecraft:strength": {
    "value": 2,
    "max": 5
}
```

```JSON
"minecraft:strength": {
    "value": 3,
    "max": 5
}
```

```JSON
"minecraft:strength": {
    "value": 4,
    "max": 5
}
```

```JSON
"minecraft:strength": {
    "value": 5,
    "max": 5
}
```

# minecraft:tameable
### cat.json
```JSON
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "fish",
        "salmon"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### parrot.json
```JSON
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "wheat_seeds",
        "pumpkin_seeds",
        "melon_seeds",
        "beetroot_seeds"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### wolf.json
```JSON
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": "bone",
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

# minecraft:tamemount
### donkey.json
```JSON
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### horse.json
```JSON
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### llama.json
```JSON
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 30,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "hay_block",
            "temper_mod": 6
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

### mule.json
```JSON
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

# minecraft:target_nearby_sensor
### creeper.json
```JSON
"minecraft:target_nearby_sensor": {
    "inside_range": 2.5,
    "outside_range": 6.0,
    "must_see": true,
    "on_inside_range": {
        "event": "minecraft:start_exploding",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    },
    "on_vision_lost_inside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    }
}
```

```JSON
"minecraft:target_nearby_sensor": {}
```

```JSON
"minecraft:target_nearby_sensor": {}
```

### drowned.json
```JSON
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 5.0,
    "on_inside_range": {
        "event": "minecraft:switch_to_melee",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:switch_to_ranged",
        "target": "self"
    }
}
```

### guardian.json
```JSON
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

```JSON
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

# minecraft:teleport
### enderman.json
```JSON
"minecraft:teleport": {
    "random_teleports": true,
    "max_random_teleport_time": 30,
    "random_teleport_cube": [
        32,
        32,
        32
    ],
    "target_distance": 16,
    "target_teleport_chance": 0.05,
    "light_teleport_chance": 0.05
}
```

# minecraft:timer
### dolphin.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 20,
    "time_down_event": {
        "event": "minecraft:dried_out"
    }
}
```

### guardian.json
```JSON
"minecraft:timer": {
    "time": [
        1,
        3
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:target_far_enough",
        "target": "self"
    }
}
```

### husk.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_zombie"
    }
}
```

### player.json
```JSON
"minecraft:timer": {
    "time": [
        0.0,
        0.0
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:clear_add_bad_omen",
        "target": "self"
    }
}
```

### pufferfish.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 0.05,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_full_puff"
    }
}
```

```JSON
"minecraft:timer": {
    "looping": false,
    "time": 1,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_normal_puff"
    }
}
```

```JSON
"minecraft:timer": {
    "looping": false,
    "time": 10,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_deflate"
    }
}
```

### ravager.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 2,
    "time_down_event": {
        "event": "minecraft:start_roar"
    }
}
```

### wandering_trader.json
```JSON
"minecraft:timer": {
    "looping": false,
    "random_time_choices": [
        {
            "weight": 50,
            "value": 2400
        },
        {
            "weight": 50,
            "value": 3600
        }
    ],
    "time_down_event": {
        "event": "minecraft:start_despawn",
        "target": "self"
    }
}
```

### zombie.json
```JSON
"minecraft:timer": {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_drowned"
    }
}
```

# minecraft:trade_resupply
### villager_v2.json
```JSON
"minecraft:trade_resupply": {}
```

# minecraft:trade_table
### villager.json
```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/farmer_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/fisherman_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.shepherd",
    "table": "trading/shepherd_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.fletcher",
    "table": "trading/fletcher_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.librarian",
    "table": "trading/librarian_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.cartographer",
    "table": "trading/cartographer_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.cleric",
    "table": "trading/cleric_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.armor",
    "table": "trading/armorer_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.weapon",
    "table": "trading/weapon_smith_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.tool",
    "table": "trading/tool_smith_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.butcher",
    "table": "trading/butcher_trades.json",
    "convert_trades_economy": true
}
```

```JSON
"minecraft:trade_table": {
    "display_name": "entity.villager.leather",
    "table": "trading/leather_worker_trades.json",
    "convert_trades_economy": true
}
```

# minecraft:trail
### snow_golem.json
```JSON
"minecraft:trail": {
    "block_type": "minecraft:snow_layer",
    "spawn_filter": {
        "test": "is_temperature_value",
        "operator": "<",
        "value": 0.81
    }
}
```

# minecraft:transformation
### husk.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### mooshroom.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:cow"
}
```

### pig.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:pig_zombie",
    "delay": 0.5
}
```

### stray.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:skeleton",
    "delay": 0.5
}
```

### villager.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "keep_level": true
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager"
}
```

### villager_v2.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": true
}
```

### zombie.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### zombie_villager.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": false
}
```

```JSON
"minecraft:transformation": {
    "into": "minecraft:villager",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

### zombie_villager_v2.json
```JSON
"minecraft:transformation": {
    "into": "minecraft:villager_v2",
    "begin_transform_sound": "remedy",
    "transformation_sound": "unfect",
    "keep_level": true,
    "delay": {
        "value": 100,
        "block_assist_chance": 0.01,
        "block_radius": 4,
        "block_chance": 0.3,
        "block_types": [
            "minecraft:bed",
            "minecraft:iron_bars"
        ]
    }
}
```

# minecraft:trust
### fox.json
```JSON
"minecraft:trust": {}
```

# minecraft:trusting
### ocelot.json
```JSON
"minecraft:trusting": {
    "probability": 0.33,
    "trust_items": [
        "fish",
        "salmon"
    ],
    "trust_event": {
        "event": "minecraft:on_trust",
        "target": "self"
    }
}
```

# minecraft:type_family
### armor_stand.json
```JSON
"minecraft:type_family": {
    "family": [
        "armor_stand",
        "inanimate",
        "mob"
    ]
}
```

### bat.json
```JSON
"minecraft:type_family": {
    "family": [
        "bat",
        "mob"
    ]
}
```

### blaze.json
```JSON
"minecraft:type_family": {
    "family": [
        "blaze",
        "monster",
        "mob"
    ]
}
```

### boat.json
```JSON
"minecraft:type_family": {
    "family": [
        "boat",
        "inanimate"
    ]
}
```

### cat.json
```JSON
"minecraft:type_family": {
    "family": [
        "cat",
        "mob"
    ]
}
```

### cave_spider.json
```JSON
"minecraft:type_family": {
    "family": [
        "cavespider",
        "monster",
        "arthropod",
        "mob"
    ]
}
```

### chest_minecart.json
```JSON
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### chicken.json
```JSON
"minecraft:type_family": {
    "family": [
        "chicken",
        "mob"
    ]
}
```

### command_block_minecart.json
```JSON
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### cow.json
```JSON
"minecraft:type_family": {
    "family": [
        "cow",
        "mob"
    ]
}
```

### creeper.json
```JSON
"minecraft:type_family": {
    "family": [
        "creeper",
        "monster",
        "mob"
    ]
}
```

### dolphin.json
```JSON
"minecraft:type_family": {
    "family": [
        "dolphin",
        "mob"
    ]
}
```

### donkey.json
```JSON
"minecraft:type_family": {
    "family": [
        "donkey",
        "mob"
    ]
}
```

### drowned.json
```JSON
"minecraft:type_family": {
    "family": [
        "drowned",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### elder_guardian.json
```JSON
"minecraft:type_family": {
    "family": [
        "guardian_elder",
        "monster",
        "mob"
    ]
}
```

### enderman.json
```JSON
"minecraft:type_family": {
    "family": [
        "enderman",
        "monster",
        "mob"
    ]
}
```

### endermite.json
```JSON
"minecraft:type_family": {
    "family": [
        "endermite",
        "arthropod",
        "monster",
        "mob"
    ]
}
```

### ender_dragon.json
```JSON
"minecraft:type_family": {
    "family": [
        "dragon",
        "mob"
    ]
}
```

### evocation_illager.json
```JSON
"minecraft:type_family": {
    "family": [
        "evocation_illager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### fish.json
```JSON
"minecraft:type_family": {
    "family": [
        "cod",
        "fish"
    ]
}
```

### fox.json
```JSON
"minecraft:type_family": {
    "family": [
        "fox",
        "mob"
    ]
}
```

### ghast.json
```JSON
"minecraft:type_family": {
    "family": [
        "ghast",
        "monster",
        "mob"
    ]
}
```

### guardian.json
```JSON
"minecraft:type_family": {
    "family": [
        "guardian",
        "monster",
        "mob"
    ]
}
```

### hopper_minecart.json
```JSON
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### horse.json
```JSON
"minecraft:type_family": {
    "family": [
        "horse",
        "mob"
    ]
}
```

### husk.json
```JSON
"minecraft:type_family": {
    "family": [
        "husk",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### iron_golem.json
```JSON
"minecraft:type_family": {
    "family": [
        "irongolem",
        "mob"
    ]
}
```

### lightning_bolt.json
```JSON
"minecraft:type_family": {
    "family": [
        "lightning"
    ]
}
```

### llama.json
```JSON
"minecraft:type_family": {
    "family": [
        "llama",
        "mob"
    ]
}
```

### magma_cube.json
```JSON
"minecraft:type_family": {
    "family": [
        "magmacube",
        "monster",
        "mob"
    ]
}
```

### minecart.json
```JSON
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### mooshroom.json
```JSON
"minecraft:type_family": {
    "family": [
        "mushroomcow",
        "mob"
    ]
}
```

### mule.json
```JSON
"minecraft:type_family": {
    "family": [
        "mule",
        "mob"
    ]
}
```

### ocelot.json
```JSON
"minecraft:type_family": {
    "family": [
        "ocelot",
        "mob"
    ]
}
```

### panda.json
```JSON
"minecraft:type_family": {
    "family": [
        "panda"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "panda",
        "panda_aggressive",
        "mob"
    ]
}
```

### parrot.json
```JSON
"minecraft:type_family": {
    "family": [
        "parrot_wild",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "parrot_tame",
        "mob"
    ]
}
```

### phantom.json
```JSON
"minecraft:type_family": {
    "family": [
        "phantom",
        "undead",
        "monster",
        "mob"
    ]
}
```

### pig.json
```JSON
"minecraft:type_family": {
    "family": [
        "pig",
        "mob"
    ]
}
```

### pillager.json
```JSON
"minecraft:type_family": {
    "family": [
        "pillager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### player.json
```JSON
"minecraft:type_family": {
    "family": [
        "player"
    ]
}
```

### polar_bear.json
```JSON
"minecraft:type_family": {
    "family": [
        "polarbear",
        "mob"
    ]
}
```

### pufferfish.json
```JSON
"minecraft:type_family": {
    "family": [
        "pufferfish",
        "fish"
    ]
}
```

### rabbit.json
```JSON
"minecraft:type_family": {
    "family": [
        "rabbit",
        "mob"
    ]
}
```

### ravager.json
```JSON
"minecraft:type_family": {
    "family": [
        "monster",
        "illager",
        "ravager",
        "mob"
    ]
}
```

### salmon.json
```JSON
"minecraft:type_family": {
    "family": [
        "salmon",
        "fish"
    ]
}
```

### sheep.json
```JSON
"minecraft:type_family": {
    "family": [
        "sheep",
        "mob"
    ]
}
```

### shulker.json
```JSON
"minecraft:type_family": {
    "family": [
        "shulker",
        "monster",
        "mob"
    ]
}
```

### silverfish.json
```JSON
"minecraft:type_family": {
    "family": [
        "silverfish",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### skeleton.json
```JSON
"minecraft:type_family": {
    "family": [
        "skeleton",
        "undead",
        "monster",
        "mob"
    ]
}
```

### skeleton_horse.json
```JSON
"minecraft:type_family": {
    "family": [
        "skeletonhorse",
        "undead",
        "mob"
    ]
}
```

### slime.json
```JSON
"minecraft:type_family": {
    "family": [
        "slime",
        "monster",
        "mob"
    ]
}
```

### snow_golem.json
```JSON
"minecraft:type_family": {
    "family": [
        "snowgolem",
        "mob"
    ]
}
```

### spider.json
```JSON
"minecraft:type_family": {
    "family": [
        "spider",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### squid.json
```JSON
"minecraft:type_family": {
    "family": [
        "squid",
        "mob"
    ]
}
```

### stray.json
```JSON
"minecraft:type_family": {
    "family": [
        "stray",
        "skeleton",
        "monster",
        "mob",
        "undead"
    ]
}
```

### tnt.json
```JSON
"minecraft:type_family": {
    "family": [
        "tnt",
        "inanimate"
    ]
}
```

### tnt_minecart.json
```JSON
"minecraft:type_family": {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### tripod_camera.json
```JSON
"minecraft:type_family": {
    "family": [
        "tripodcamera",
        "inanimate",
        "mob"
    ]
}
```

### tropicalfish.json
```JSON
"minecraft:type_family": {
    "family": [
        "tropicalfish",
        "fish"
    ]
}
```

### turtle.json
```JSON
"minecraft:type_family": {
    "family": [
        "turtle",
        "baby_turtle",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "turtle",
        "mob"
    ]
}
```

### vex.json
```JSON
"minecraft:type_family": {
    "family": [
        "vex",
        "monster",
        "mob"
    ]
}
```

### villager.json
```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

### villager_v2.json
```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "artisan",
        "stone_mason",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "villager",
        "peasant",
        "nitwit",
        "mob"
    ]
}
```

### vindicator.json
```JSON
"minecraft:type_family": {
    "family": [
        "vindicator",
        "monster",
        "illager",
        "mob"
    ]
}
```

### wandering_trader.json
```JSON
"minecraft:type_family": {
    "family": [
        "wandering_trader",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "wandering_trader",
        "wandering_trader_despawning",
        "mob"
    ]
}
```

### witch.json
```JSON
"minecraft:type_family": {
    "family": [
        "witch",
        "monster",
        "mob"
    ]
}
```

### wither.json
```JSON
"minecraft:type_family": {
    "family": [
        "wither",
        "skeleton",
        "monster",
        "undead",
        "mob"
    ]
}
```

### wither_skeleton.json
```JSON
"minecraft:type_family": {
    "family": [
        "wither",
        "monster",
        "undead",
        "skeleton",
        "mob"
    ]
}
```

### wolf.json
```JSON
"minecraft:type_family": {
    "family": [
        "wolf",
        "mob"
    ]
}
```

### zombie.json
```JSON
"minecraft:type_family": {
    "family": [
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_horse.json
```JSON
"minecraft:type_family": {
    "family": [
        "zombiehorse",
        "undead",
        "mob"
    ]
}
```

### zombie_pigman.json
```JSON
"minecraft:type_family": {
    "family": [
        "zombie_pigman",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_villager.json
```JSON
"minecraft:type_family": {
    "family": [
        "farmer",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "fisherman",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "shepherd",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "fletcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "librarian",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "cartographer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "cleric",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "armorer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "weaponsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "toolsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "butcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "leatherworker",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_villager_v2.json
```JSON
"minecraft:type_family": {
    "family": [
        "unskilled",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "nitwit",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "farmer",
        "zombie",
        "zombie_villager",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "fisherman",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "shepherd",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "fletcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "librarian",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "cartographer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "cleric",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "armorer",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "weaponsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "toolsmith",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "butcher",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "leatherworker",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

```JSON
"minecraft:type_family": {
    "family": [
        "mason",
        "zombie_villager",
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

# minecraft:underwater_movement
### dolphin.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.15
}
```

### drowned.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.06
}
```

```JSON
"minecraft:underwater_movement": {
    "value": 0.08
}
```

### elder_guardian.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.3
}
```

### fish.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.1
}
```

### guardian.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### pufferfish.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.13
}
```

### salmon.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### skeleton_horse.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.08
}
```

### tropicalfish.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.12
}
```

### turtle.json
```JSON
"minecraft:underwater_movement": {
    "value": 0.06
}
```

```JSON
"minecraft:underwater_movement": {
    "value": 0.12
}
```

# minecraft:variant
### cat.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 5
}
```

```JSON
"minecraft:variant": {
    "value": 6
}
```

```JSON
"minecraft:variant": {
    "value": 7
}
```

```JSON
"minecraft:variant": {
    "value": 8
}
```

```JSON
"minecraft:variant": {
    "value": 9
}
```

```JSON
"minecraft:variant": {
    "value": 10
}
```

### fox.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

### horse.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 5
}
```

```JSON
"minecraft:variant": {
    "value": 6
}
```

### husk.json
```JSON
"minecraft:variant": {
    "value": 2
}
```

### llama.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

### mooshroom.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

### panda.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 5
}
```

```JSON
"minecraft:variant": {
    "value": 6
}
```

### parrot.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

### pillager.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

### pufferfish.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

### rabbit.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 5
}
```

### shulker.json
```JSON
"minecraft:variant": {
    "value": 5
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 6
}
```

```JSON
"minecraft:variant": {
    "value": 8
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 12
}
```

```JSON
"minecraft:variant": {
    "value": 10
}
```

```JSON
"minecraft:variant": {
    "value": 13
}
```

```JSON
"minecraft:variant": {
    "value": 14
}
```

```JSON
"minecraft:variant": {
    "value": 9
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 7
}
```

```JSON
"minecraft:variant": {
    "value": 16
}
```

```JSON
"minecraft:variant": {
    "value": 15
}
```

```JSON
"minecraft:variant": {
    "value": 11
}
```

### tropicalfish.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

### villager.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

### villager_v2.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 5
}
```

```JSON
"minecraft:variant": {
    "value": 6
}
```

```JSON
"minecraft:variant": {
    "value": 7
}
```

```JSON
"minecraft:variant": {
    "value": 8
}
```

```JSON
"minecraft:variant": {
    "value": 9
}
```

```JSON
"minecraft:variant": {
    "value": 10
}
```

```JSON
"minecraft:variant": {
    "value": 11
}
```

```JSON
"minecraft:variant": {
    "value": 12
}
```

```JSON
"minecraft:variant": {
    "value": 13
}
```

```JSON
"minecraft:variant": {
    "value": 14
}
```

### vindicator.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

### zombie_villager.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 1
}
```

```JSON
"minecraft:variant": {
    "value": 2
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 3
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

```JSON
"minecraft:variant": {
    "value": 4
}
```

### zombie_villager_v2.json
```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

```JSON
"minecraft:variant": {
    "value": 0
}
```

# minecraft:water_movement
### panda.json
```JSON
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

### polar_bear.json
```JSON
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

### turtle.json
```JSON
"minecraft:water_movement": {
    "drag_factor": 0.9
}
```

