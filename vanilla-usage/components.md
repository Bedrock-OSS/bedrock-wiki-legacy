---
layout: page
title: Components
parent: Vanilla Usage
---

# Components
This documentation is stripped from the vanilla files using an automated script. If there is an issue, please bring it to the authors attention by contacting him on discord: `SirLich#1658`

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
 - [minecraft:behavior.move_to_block](#minecraftbehaviormove_to_block)
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
 - [minecraft:behavior.random_hover](#minecraftbehaviorrandom_hover)
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
 - [minecraft:block_sensor](#minecraftblock_sensor)
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
 - [minecraft:grows_crop](#minecraftgrows_crop)
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
 - [minecraft:movement.hover](#minecraftmovementhover)
 - [minecraft:movement.jump](#minecraftmovementjump)
 - [minecraft:movement.skip](#minecraftmovementskip)
 - [minecraft:movement.sway](#minecraftmovementsway)
 - [minecraft:nameable](#minecraftnameable)
 - [minecraft:navigation.climb](#minecraftnavigationclimb)
 - [minecraft:navigation.float](#minecraftnavigationfloat)
 - [minecraft:navigation.fly](#minecraftnavigationfly)
 - [minecraft:navigation.generic](#minecraftnavigationgeneric)
 - [minecraft:navigation.hover](#minecraftnavigationhover)
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
```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton.stray"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton.wither"
}
```

### ravager.json
```json
"minecraft:addrider:" {
    "entity_type": "minecraft:pillager"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:evocation_illager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:vindicator"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:vindicator",
    "spawn_event": "minecraft:spawn_as_illager_captain"
}
```

### spider.json
```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton.stray"
}
```

```json
"minecraft:addrider:" {
    "entity_type": "minecraft:skeleton.wither"
}
```

# minecraft:ageable
### bee.json
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### cat.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### dolphin.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": "sweet_berries",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### horse.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### mule.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": "bamboo",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### pig.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### rabbit.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### skeleton_horse.json
```json
"minecraft:ageable:" {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### turtle.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### villager_v2.json
```json
"minecraft:ageable:" {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

### wolf.json
```json
"minecraft:ageable:" {
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
```json
"minecraft:ageable:" {
    "duration": 1200,
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

# minecraft:ambient_sound_interval
### bee.json
```json
"minecraft:ambient_sound_interval:" {
    "event_name": "ambient.pollinate",
    "range": 3.0,
    "value": 2.0
}
```

```json
"minecraft:ambient_sound_interval:" {
    "event_name": "ambient",
    "range": 0.0,
    "value": 0.0
}
```

### evocation_illager.json
```json
"minecraft:ambient_sound_interval:" {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### fox.json
```json
"minecraft:ambient_sound_interval:" {
    "event_name": "ambient"
}
```

```json
"minecraft:ambient_sound_interval:" {
    "event_name": "sleep"
}
```

```json
"minecraft:ambient_sound_interval:" {
    "event_name": "screech",
    "value": 80,
    "range": 160
}
```

### pillager.json
```json
"minecraft:ambient_sound_interval:" {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### ravager.json
```json
"minecraft:ambient_sound_interval:" {
    "value": 4.0,
    "range": 8.0,
    "event_name": "ambient.in.raid"
}
```

### vindicator.json
```json
"minecraft:ambient_sound_interval:" {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

### witch.json
```json
"minecraft:ambient_sound_interval:" {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

# minecraft:angry
### bee.json
```json
"minecraft:angry:" {
    "duration": 25,
    "broadcastAnger": true,
    "broadcastRange": 20,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "!=",
        "value": "pacified"
    },
    "calm_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

### cave_spider.json
```json
"minecraft:angry:" {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### dolphin.json
```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
    "duration": 25,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### llama.json
```json
"minecraft:angry:" {
    "duration": 4,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry:" {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry:" {
    "duration": 10,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

### panda.json
```json
"minecraft:angry:" {
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

```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
    "duration": -1,
    "broadcast_anger": true,
    "broadcast_range": 8
}
```

### polar_bear.json
```json
"minecraft:angry:" {
    "duration": 1,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "calm_event": {
        "event": "minecraft:baby_on_calm",
        "target": "self"
    }
}
```

```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:become_calm",
        "target": "self"
    }
}
```

### vindicator.json
```json
"minecraft:angry:" {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:stop_aggro",
        "target": "self"
    }
}
```

### wandering_trader.json
```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
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
```json
"minecraft:angry:" {
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
```json
"minecraft:annotation.break_door:" {}
```

### husk.json
```json
"minecraft:annotation.break_door:" {}
```

### vindicator.json
```json
"minecraft:annotation.break_door:" {
    "break_time": 30,
    "min_difficulty": "normal"
}
```

### zombie.json
```json
"minecraft:annotation.break_door:" {}
```

### zombie_villager.json
```json
"minecraft:annotation.break_door:" {}
```

# minecraft:annotation.open_door
### villager.json
```json
"minecraft:annotation.open_door:" {}
```

### villager_v2.json
```json
"minecraft:annotation.open_door:" {}
```

# minecraft:area_attack
### pufferfish.json
```json
"minecraft:area_attack:" {
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
### bee.json
```json
"minecraft:attack:" {
    "damage": 2
}
```

```json
"minecraft:attack:" {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 10
}
```

```json
"minecraft:attack:" {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 18
}
```

### blaze.json
```json
"minecraft:attack:" {
    "damage": 6
}
```

### cave_spider.json
```json
"minecraft:attack:" {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 0
}
```

```json
"minecraft:attack:" {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 7
}
```

```json
"minecraft:attack:" {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 15
}
```

### creeper.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### dolphin.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### drowned.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### elder_guardian.json
```json
"minecraft:attack:" {
    "damage": 5
}
```

### enderman.json
```json
"minecraft:attack:" {
    "damage": 7
}
```

### endermite.json
```json
"minecraft:attack:" {
    "damage": 2
}
```

### ender_dragon.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### fox.json
```json
"minecraft:attack:" {
    "damage": 2
}
```

### guardian.json
```json
"minecraft:attack:" {
    "damage": 5
}
```

### husk.json
```json
"minecraft:attack:" {
    "damage": 3,
    "effect_name": "hunger",
    "effect_duration": 30
}
```

### iron_golem.json
```json
"minecraft:attack:" {
    "damage": {
        "range_min": 7,
        "range_max": 21
    }
}
```

### magma_cube.json
```json
"minecraft:attack:" {
    "damage": 6
}
```

```json
"minecraft:attack:" {
    "damage": 4
}
```

```json
"minecraft:attack:" {
    "damage": 2
}
```

### panda.json
```json
"minecraft:attack:" {
    "damage": 2.0
}
```

```json
"minecraft:attack:" {
    "damage": 6.0
}
```

### phantom.json
```json
"minecraft:attack:" {
    "damage": 6
}
```

### pillager.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### player.json
```json
"minecraft:attack:" {
    "damage": 1
}
```

### polar_bear.json
```json
"minecraft:attack:" {
    "damage": 6.0
}
```

### ravager.json
```json
"minecraft:attack:" {
    "damage": 12.0
}
```

### silverfish.json
```json
"minecraft:attack:" {
    "damage": 1
}
```

### skeleton.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### slime.json
```json
"minecraft:attack:" {
    "damage": 4
}
```

```json
"minecraft:attack:" {
    "damage": 2
}
```

```json
"minecraft:attack:" {
    "damage": 0
}
```

### snow_golem.json
```json
"minecraft:attack:" {
    "damage": 2
}
```

### spider.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### stray.json
```json
"minecraft:attack:" {
    "damage": 3,
    "effect_name": "slowness",
    "effect_duration": 10
}
```

### vex.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### vindicator.json
```json
"minecraft:attack:" {
    "damage": 8
}
```

### wither_skeleton.json
```json
"minecraft:attack:" {
    "damage": 4,
    "effect_name": "wither",
    "effect_duration": 10
}
```

### wolf.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

```json
"minecraft:attack:" {
    "damage": 4
}
```

### zombie.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### zombie_pigman.json
```json
"minecraft:attack:" {
    "damage": 5
}
```

### zombie_villager.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

### zombie_villager_v2.json
```json
"minecraft:attack:" {
    "damage": 3
}
```

# minecraft:attack_damage
### cat.json
```json
"minecraft:attack_damage:" {
    "value": 4
}
```

### ocelot.json
```json
"minecraft:attack_damage:" {
    "value": 4
}
```

# minecraft:balloonable
### chicken.json
```json
"minecraft:balloonable:" {
    "mass": 0.6
}
```

### cow.json
```json
"minecraft:balloonable:" {}
```

### donkey.json
```json
"minecraft:balloonable:" {}
```

### fox.json
```json
"minecraft:balloonable:" {}
```

### horse.json
```json
"minecraft:balloonable:" {}
```

### iron_golem.json
```json
"minecraft:balloonable:" {}
```

### llama.json
```json
"minecraft:balloonable:" {}
```

### mooshroom.json
```json
"minecraft:balloonable:" {}
```

### mule.json
```json
"minecraft:balloonable:" {}
```

### panda.json
```json
"minecraft:balloonable:" {}
```

### pig.json
```json
"minecraft:balloonable:" {
    "mass": 0.75
}
```

### rabbit.json
```json
"minecraft:balloonable:" {
    "mass": 0.75
}
```

### sheep.json
```json
"minecraft:balloonable:" {
    "mass": 0.75
}
```

### skeleton_horse.json
```json
"minecraft:balloonable:" {}
```

### snow_golem.json
```json
"minecraft:balloonable:" {}
```

### squid.json
```json
"minecraft:balloonable:" {}
```

### zombie_horse.json
```json
"minecraft:balloonable:" {}
```

# minecraft:behavior.avoid_mob_type
### cat.json
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.avoid_mob_type:" {
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
```json
"minecraft:behavior.beg:" {
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
```json
"minecraft:behavior.break_door:" {
    "priority": 1
}
```

# minecraft:behavior.breed
### bee.json
```json
"minecraft:behavior.breed:" {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

### cat.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### chicken.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### cow.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### donkey.json
```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### fox.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### horse.json
```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### llama.json
```json
"minecraft:behavior.breed:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### mooshroom.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### ocelot.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### panda.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### pig.json
```json
"minecraft:behavior.breed:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### rabbit.json
```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 0.8
}
```

```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### sheep.json
```json
"minecraft:behavior.breed:" {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

### turtle.json
```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

### wolf.json
```json
"minecraft:behavior.breed:" {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.celebrate
### evocation_illager.json
```json
"minecraft:behavior.celebrate:" {
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
```json
"minecraft:behavior.celebrate:" {
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
```json
"minecraft:behavior.celebrate:" {
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
```json
"minecraft:behavior.celebrate:" {
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
```json
"minecraft:behavior.celebrate:" {
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
```json
"minecraft:behavior.charge_attack:" {
    "priority": 4
}
```

# minecraft:behavior.charge_held_item
### pillager.json
```json
"minecraft:behavior.charge_held_item:" {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

# minecraft:behavior.circle_around_anchor
### phantom.json
```json
"minecraft:behavior.circle_around_anchor:" {
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
```json
"minecraft:behavior.controlled_by_player:" {
    "priority": 0
}
```

# minecraft:behavior.defend_trusted_target
### fox.json
```json
"minecraft:behavior.defend_trusted_target:" {
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
```json
"minecraft:behavior.defend_village_target:" {
    "priority": 1
}
```

# minecraft:behavior.delayed_attack
### ravager.json
```json
"minecraft:behavior.delayed_attack:" {
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
```json
"minecraft:behavior.dragonchargeplayer:" {
    "priority": 1
}
```

# minecraft:behavior.dragondeath
```json
"minecraft:behavior.dragondeath:" {
    "priority": 0
}
```

# minecraft:behavior.dragonflaming
```json
"minecraft:behavior.dragonflaming:" {
    "priority": 1
}
```

# minecraft:behavior.dragonholdingpattern
```json
"minecraft:behavior.dragonholdingpattern:" {
    "priority": 3
}
```

# minecraft:behavior.dragonlanding
```json
"minecraft:behavior.dragonlanding:" {
    "priority": 0
}
```

# minecraft:behavior.dragonscanning
```json
"minecraft:behavior.dragonscanning:" {
    "priority": 2
}
```

# minecraft:behavior.dragonstrafeplayer
```json
"minecraft:behavior.dragonstrafeplayer:" {
    "priority": 2
}
```

# minecraft:behavior.dragontakeoff
```json
"minecraft:behavior.dragontakeoff:" {
    "priority": 0
}
```

# minecraft:behavior.drink_potion
### wandering_trader.json
```json
"minecraft:behavior.drink_potion:" {
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
```json
"minecraft:behavior.drop_item_for:" {
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
```json
"minecraft:behavior.eat_block:" {
    "priority": 6,
    "on_eat": {
        "event": "minecraft:on_eat_block",
        "target": "self"
    }
}
```

# minecraft:behavior.eat_carried_item
### fox.json
```json
"minecraft:behavior.eat_carried_item:" {
    "priority": 12,
    "delay_before_eating": 28
}
```

# minecraft:behavior.enderman_leave_block
### enderman.json
```json
"minecraft:behavior.enderman_leave_block:" {
    "priority": 10
}
```

# minecraft:behavior.enderman_take_block
```json
"minecraft:behavior.enderman_take_block:" {
    "priority": 11
}
```

# minecraft:behavior.explore_outskirts
### villager_v2.json
```json
"minecraft:behavior.explore_outskirts:" {}
```

```json
"minecraft:behavior.explore_outskirts:" {
    "priority": 9,
    "explore_dist": 6.0,
    "wait_time": 200,
    "speed_multiplier": 0.6
}
```

# minecraft:behavior.find_cover
### fox.json
```json
"minecraft:behavior.find_cover:" {
    "priority": 0,
    "speed_multiplier": 1,
    "cooldown_time": 0.0
}
```

```json
"minecraft:behavior.find_cover:" {
    "priority": 9,
    "speed_multiplier": 1,
    "cooldown_time": 5.0
}
```

# minecraft:behavior.find_mount
### husk.json
```json
"minecraft:behavior.find_mount:" {
    "priority": 1,
    "within_radius": 16
}
```

### parrot.json
```json
"minecraft:behavior.find_mount:" {
    "priority": 3,
    "within_radius": 16,
    "avoid_water": true,
    "start_delay": 100,
    "target_needed": false,
    "mount_distance": 2.0
}
```

### zombie.json
```json
"minecraft:behavior.find_mount:" {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

### zombie_villager.json
```json
"minecraft:behavior.find_mount:" {
    "priority": 1,
    "within_radius": 16
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.find_mount:" {
    "priority": 1,
    "within_radius": 16
}
```

# minecraft:behavior.find_underwater_treasure
### dolphin.json
```json
"minecraft:behavior.find_underwater_treasure:" {
    "priority": 2,
    "speed_multiplier": 2.0,
    "search_range": 30,
    "stop_distance": 50
}
```

# minecraft:behavior.flee_sun
### drowned.json
```json
"minecraft:behavior.flee_sun:" {
    "priority": 2,
    "speed_multiplier": 1
}
```

### skeleton.json
```json
"minecraft:behavior.flee_sun:" {
    "priority": 2,
    "speed_multiplier": 1
}
```

### stray.json
```json
"minecraft:behavior.flee_sun:" {
    "priority": 2,
    "speed_multiplier": 1
}
```

### zombie_villager.json
```json
"minecraft:behavior.flee_sun:" {
    "priority": 4,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.flee_sun:" {
    "priority": 4,
    "speed_multiplier": 1
}
```

# minecraft:behavior.float
### bat.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### bee.json
```json
"minecraft:behavior.float:" {
    "priority": 20
}
```

### blaze.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### cat.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### cave_spider.json
```json
"minecraft:behavior.float:" {
    "priority": 1
}
```

### chicken.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### cow.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### creeper.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### donkey.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### enderman.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### endermite.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### evocation_illager.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### fox.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### ghast.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### horse.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### llama.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### mooshroom.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### mule.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### ocelot.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### panda.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### parrot.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### pig.json
```json
"minecraft:behavior.float:" {
    "priority": 2
}
```

### pillager.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### polar_bear.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### rabbit.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### ravager.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### sheep.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### silverfish.json
```json
"minecraft:behavior.float:" {
    "priority": 1
}
```

### spider.json
```json
"minecraft:behavior.float:" {
    "priority": 1
}
```

### vex.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### villager.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### villager_v2.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### vindicator.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### wandering_trader.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

### witch.json
```json
"minecraft:behavior.float:" {
    "priority": 1
}
```

### wither.json
```json
"minecraft:behavior.float:" {
    "priority": 1
}
```

### wolf.json
```json
"minecraft:behavior.float:" {
    "priority": 0
}
```

# minecraft:behavior.float_wander
### bat.json
```json
"minecraft:behavior.float_wander:" {
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
```json
"minecraft:behavior.float_wander:" {
    "priority": 2,
    "must_reach": true
}
```

# minecraft:behavior.follow_caravan
### llama.json
```json
"minecraft:behavior.follow_caravan:" {
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
```json
"minecraft:behavior.follow_mob:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "stop_distance": 3,
    "search_range": 20
}
```

# minecraft:behavior.follow_owner
### cat.json
```json
"minecraft:behavior.follow_owner:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### ocelot.json
```json
"minecraft:behavior.follow_owner:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

### parrot.json
```json
"minecraft:behavior.follow_owner:" {
    "priority": 2,
    "speed_multiplier": 1.0,
    "start_distance": 5,
    "stop_distance": 1
}
```

### wolf.json
```json
"minecraft:behavior.follow_owner:" {
    "priority": 6,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

# minecraft:behavior.follow_parent
### bee.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 8,
    "speed_multiplier": 1.1
}
```

### chicken.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

### cow.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent:" {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### dolphin.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.1
}
```

### donkey.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### fox.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 9,
    "speed_multiplier": 1.1
}
```

### horse.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### llama.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### mooshroom.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent:" {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### mule.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### panda.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 13,
    "speed_multiplier": 1.1
}
```

### pig.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### polar_bear.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.25
}
```

### rabbit.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### sheep.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json
"minecraft:behavior.follow_parent:" {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

### skeleton_horse.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### zombie_horse.json
```json
"minecraft:behavior.follow_parent:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.follow_target_captain
### pillager.json
```json
"minecraft:behavior.follow_target_captain:" {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

### vindicator.json
```json
"minecraft:behavior.follow_target_captain:" {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

# minecraft:behavior.go_home
### bee.json
```json
"minecraft:behavior.go_home:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "interval": 1,
    "goal_radius": 1.2,
    "on_home": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "find_hive_event",
            "target": "self"
        }
    ],
    "on_failed": {
        "event": "find_hive_event",
        "target": "self"
    }
}
```

### turtle.json
```json
"minecraft:behavior.go_home:" {
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
```json
"minecraft:behavior.guardian_attack:" {
    "priority": 4
}
```

### guardian.json
```json
"minecraft:behavior.guardian_attack:" {
    "priority": 4
}
```

```json
"minecraft:behavior.guardian_attack:" {
    "priority": 4
}
```

# minecraft:behavior.harvest_farm_block
### villager.json
```json
"minecraft:behavior.harvest_farm_block:" {
    "priority": 9,
    "speed_multiplier": 0.5
}
```

### villager_v2.json
```json
"minecraft:behavior.harvest_farm_block:" {}
```

```json
"minecraft:behavior.harvest_farm_block:" {
    "priority": 8,
    "speed_multiplier": 0.5
}
```

# minecraft:behavior.hide
```json
"minecraft:behavior.hide:" {
    "priority": 0,
    "speed_multiplier": 0.8,
    "poi_type": "bed",
    "duration": 30.0
}
```

# minecraft:behavior.hold_ground
### pillager.json
```json
"minecraft:behavior.hold_ground:" {
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

```json
"minecraft:behavior.hold_ground:" {
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
### bee.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 2
}
```

### blaze.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### cave_spider.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### creeper.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 2
}
```

### dolphin.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### drowned.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### enderman.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 3
}
```

### evocation_illager.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### ghast.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### husk.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### iron_golem.json
```json
"minecraft:behavior.hurt_by_target:" {
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

```json
"minecraft:behavior.hurt_by_target:" {
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
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1,
    "hurt_owner": true
}
```

### panda.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### pillager.json
```json
"minecraft:behavior.hurt_by_target:" {
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
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### ravager.json
```json
"minecraft:behavior.hurt_by_target:" {
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
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 2
}
```

### silverfish.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1,
    "alert_same_type": true
}
```

### skeleton.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### spider.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### stray.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### turtle.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### vex.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### vindicator.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### witch.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### wither.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 2
}
```

### wither_skeleton.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### wolf.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 3
}
```

### zombie.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### zombie_pigman.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### zombie_villager.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.hurt_by_target:" {
    "priority": 1
}
```

# minecraft:behavior.inspect_bookshelf
### villager_v2.json
```json
"minecraft:behavior.inspect_bookshelf:" {}
```

```json
"minecraft:behavior.inspect_bookshelf:" {
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
```json
"minecraft:behavior.knockback_roar:" {
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
```json
"minecraft:behavior.lay_down:" {
    "priority": 5,
    "interval": 400,
    "random_stop_interval": 2000
}
```

# minecraft:behavior.lay_egg
### turtle.json
```json
"minecraft:behavior.lay_egg:" {
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
```json
"minecraft:behavior.leap_at_target:" {
    "priority": 3,
    "target_dist": 0.3
}
```

### cave_spider.json
```json
"minecraft:behavior.leap_at_target:" {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

```json
"minecraft:behavior.leap_at_target:" {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### ocelot.json
```json
"minecraft:behavior.leap_at_target:" {
    "priority": 3,
    "target_dist": 0.3
}
```

### spider.json
```json
"minecraft:behavior.leap_at_target:" {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

### wolf.json
```json
"minecraft:behavior.leap_at_target:" {
    "priority": 4,
    "target_dist": 0.4
}
```

# minecraft:behavior.look_at_entity
### evocation_illager.json
```json
"minecraft:behavior.look_at_entity:" {
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
```json
"minecraft:behavior.look_at_entity:" {
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
```json
"minecraft:behavior.look_at_entity:" {
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
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9
}
```

### cave_spider.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### chicken.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### cow.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### creeper.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "look_distance": 8
}
```

### dolphin.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 6
}
```

### donkey.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### drowned.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### elder_guardian.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### enderman.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 8.0,
    "probability": 8.0
}
```

### evocation_illager.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9,
    "look_distance": 3.0,
    "probability": 1.0
}
```

### fox.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 14,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### guardian.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 12.0,
    "probability": 0.01
}
```

### horse.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### husk.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### iron_golem.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### llama.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mooshroom.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### mule.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### ocelot.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9
}
```

### panda.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### parrot.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 1,
    "look_distance": 8.0
}
```

### pig.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### pillager.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 8
}
```

### polar_bear.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### rabbit.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 11
}
```

### ravager.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6,
    "angle_of_view_horizontal": 45,
    "probability": 1
}
```

### sheep.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### shulker.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 1,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### skeleton.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "look_distance": 8
}
```

### skeleton_horse.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### snow_golem.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 3,
    "look_distance": 6.0
}
```

### spider.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### stray.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "look_distance": 8
}
```

### turtle.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### vex.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### villager.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 12,
    "look_distance": 8,
    "probability": 0.02
}
```

### villager_v2.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### vindicator.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 10,
    "look_distance": 8,
    "probability": 0.02
}
```

### wandering_trader.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 8,
    "probability": 0.02
}
```

### witch.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "look_distance": 8
}
```

### wither_skeleton.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "look_distance": 8
}
```

### wolf.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 6,
    "target_distance": 6.0,
    "probability": 0.02
}
```

### zombie.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_horse.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_pigman.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 8,
    "look_distance": 6.0,
    "probability": 0.02
}
```

### zombie_villager.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9,
    "look_distance": 6,
    "probability": 0.02
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.look_at_player:" {
    "priority": 9,
    "look_distance": 6,
    "probability": 0.02
}
```

# minecraft:behavior.look_at_target
### wither.json
```json
"minecraft:behavior.look_at_target:" {
    "priority": 5
}
```

# minecraft:behavior.look_at_trading_player
### villager.json
```json
"minecraft:behavior.look_at_trading_player:" {
    "priority": 2
}
```

### villager_v2.json
```json
"minecraft:behavior.look_at_trading_player:" {
    "priority": 7
}
```

### wandering_trader.json
```json
"minecraft:behavior.look_at_trading_player:" {
    "priority": 4
}
```

# minecraft:behavior.make_love
### villager.json
```json
"minecraft:behavior.make_love:" {
    "priority": 6
}
```

### villager_v2.json
```json
"minecraft:behavior.make_love:" {
    "priority": 5
}
```

# minecraft:behavior.melee_attack
### bee.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "target_dist": 1.2,
    "track_target": false,
    "attack_once": true,
    "reach_multiplier": 2.0,
    "look_distance": 30,
    "untrackable_cooldown_delay": 17,
    "speed_multiplier": 9,
    "target_tracking": {
        "refresh_period_min": 4,
        "refresh_period_max": 11,
        "backoff": [
            {
                "distance_squared_gt": 256,
                "refresh_period_delta": 50
            },
            {
                "distance_squared_gt": 1024,
                "refresh_period_delta": 100
            }
        ]
    },
    "on_attack": {
        "event": "countdown_to_perish_event",
        "target": "self"
    }
}
```

### blaze.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "max_dist": 3,
    "speed_multiplier": 1,
    "random_stop_interval": 2.0,
    "track_target": true
}
```

### cave_spider.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "random_stop_interval": 100,
    "reach_multiplier": 0.8
}
```

```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 1.4
}
```

### creeper.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "track_target": false,
    "reach_multiplier": 0.0
}
```

### dolphin.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 2,
    "track_target": true
}
```

### drowned.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false,
    "require_complete_path": true
}
```

### enderman.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 2,
    "speed_multiplier": 1.0,
    "track_target": false
}
```

### endermite.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": true
}
```

### fox.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 10,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

```json
"minecraft:behavior.melee_attack:" {
    "priority": 1,
    "target_dist": 1.2,
    "track_target": true,
    "require_complete_path": true,
    "reach_multiplier": 1.5
}
```

### husk.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### iron_golem.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 1,
    "target_dist": 1.0,
    "track_target": true
}
```

### panda.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "attack_once": true,
    "reach_multiplier": 1.0
}
```

```json
"minecraft:behavior.melee_attack:" {
    "priority": 2,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### pillager.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1,
    "track_target": true
}
```

### silverfish.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "track_target": true
}
```

### skeleton.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### spider.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "track_target": true,
    "reach_multiplier": 0.8
}
```

### stray.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### vindicator.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### wither_skeleton.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 4,
    "target_dist": 1.2,
    "speed_multiplier": 1.25,
    "track_target": true
}
```

### wolf.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 5,
    "target_dist": 1.2,
    "track_target": true,
    "reach_multiplier": 1.0
}
```

### zombie.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_pigman.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 3,
    "speed_multiplier": 1.5,
    "track_target": false
}
```

### zombie_villager.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.melee_attack:" {
    "priority": 6,
    "speed_multiplier": 1,
    "track_target": false
}
```

# minecraft:behavior.mingle
### villager_v2.json
```json
"minecraft:behavior.mingle:" {}
```

```json
"minecraft:behavior.mingle:" {
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
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### cave_spider.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### chicken.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### cow.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### donkey.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### horse.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### husk.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### llama.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### mooshroom.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### mule.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### ocelot.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### panda.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### pig.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### ravager.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### sheep.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### skeleton_horse.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 4.0,
    "track_target": true
}
```

### spider.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### wolf.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_horse.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_pigman.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

### zombie_villager.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.mount_pathing:" {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

# minecraft:behavior.move_indoors
### villager.json
```json
"minecraft:behavior.move_indoors:" {
    "priority": 4,
    "speed_multiplier": 0.8
}
```

### villager_v2.json
```json
"minecraft:behavior.move_indoors:" {
    "priority": 6,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

# minecraft:behavior.move_through_village
### iron_golem.json
```json
"minecraft:behavior.move_through_village:" {
    "priority": 3,
    "speed_multiplier": 0.6,
    "only_at_night": true
}
```

# minecraft:behavior.move_to_block
### bee.json
```json
"minecraft:behavior.move_to_block:" {
    "priority": 11,
    "tick_interval": 1,
    "start_chance": 0.5,
    "search_range": 6,
    "search_height": 4,
    "goal_radius": 1.0,
    "stay_duration": 20.0,
    "target_selection_method": "random",
    "target_offset": [
        0,
        0.25,
        0
    ],
    "target_blocks": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sweet_berry_bush",
        "minecraft:double_plant:8",
        "minecraft:double_plant:9",
        "minecraft:double_plant:12",
        "minecraft:double_plant:13"
    ],
    "on_stay_completed": [
        {
            "event": "collected_nectar",
            "target": "self"
        }
    ]
}
```

```json
"minecraft:behavior.move_to_block:" {
    "priority": 11,
    "search_range": 16,
    "search_height": 10,
    "tick_interval": 1,
    "goal_radius": 0.633,
    "target_blocks": [
        "bee_nest",
        "beehive"
    ],
    "on_reach": [
        {
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        }
    ]
}
```

# minecraft:behavior.move_to_land
### turtle.json
```json
"minecraft:behavior.move_to_land:" {
    "priority": 6,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 0.5
}
```

# minecraft:behavior.move_to_random_block
### pillager.json
```json
"minecraft:behavior.move_to_random_block:" {
    "priority": 6,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

### vindicator.json
```json
"minecraft:behavior.move_to_random_block:" {
    "priority": 5,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

# minecraft:behavior.move_to_village
### evocation_illager.json
```json
"minecraft:behavior.move_to_village:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### pillager.json
```json
"minecraft:behavior.move_to_village:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### ravager.json
```json
"minecraft:behavior.move_to_village:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### vindicator.json
```json
"minecraft:behavior.move_to_village:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

### witch.json
```json
"minecraft:behavior.move_to_village:" {
    "priority": 3,
    "speed_multiplier": 1.2,
    "goal_radius": 2.0
}
```

# minecraft:behavior.move_to_water
### dolphin.json
```json
"minecraft:behavior.move_to_water:" {
    "priority": 1,
    "search_range": 15,
    "search_height": 5
}
```

### turtle.json
```json
"minecraft:behavior.move_to_water:" {
    "priority": 4,
    "search_range": 16,
    "search_height": 5,
    "search_count": 1,
    "goal_radius": 0.1
}
```

```json
"minecraft:behavior.move_to_water:" {
    "priority": 1,
    "search_range": 15,
    "search_height": 5,
    "goal_radius": 0.1
}
```

# minecraft:behavior.move_towards_restriction
### cat.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 7
}
```

### drowned.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### elder_guardian.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "control_flags": [
        "move",
        "look"
    ]
}
```

### guardian.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "control_flags": [
        "move",
        "look"
    ]
}
```

### husk.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### iron_golem.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 4,
    "speed_multiplier": 1
}
```

### villager.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 7,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### wandering_trader.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 7,
    "speed_multiplier": 0.6
}
```

### zombie.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### zombie_pigman.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 5
}
```

### zombie_villager.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 7,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.move_towards_restriction:" {
    "priority": 7,
    "speed_multiplier": 1
}
```

# minecraft:behavior.move_towards_target
### iron_golem.json
```json
"minecraft:behavior.move_towards_target:" {
    "priority": 2,
    "speed_multiplier": 0.9,
    "within_radius": 32
}
```

# minecraft:behavior.nap
### fox.json
```json
"minecraft:behavior.nap:" {
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
### bee.json
```json
"minecraft:behavior.nearest_attackable_target:" {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10
        }
    ]
}
```

### blaze.json
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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

```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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

```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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

```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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

```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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

```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_attackable_target:" {
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
```json
"minecraft:behavior.nearest_prioritized_attackable_target:" {
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

```json
"minecraft:behavior.nearest_prioritized_attackable_target:" {
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
```json
"minecraft:behavior.ocelot_sit_on_block:" {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### ocelot.json
```json
"minecraft:behavior.ocelot_sit_on_block:" {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

# minecraft:behavior.ocelotattack
### cat.json
```json
"minecraft:behavior.ocelotattack:" {
    "priority": 4,
    "walk_speed_multiplier": 0.8,
    "sprint_speed_multiplier": 1.33,
    "sneak_speed_multiplier": 0.6
}
```

### ocelot.json
```json
"minecraft:behavior.ocelotattack:" {
    "priority": 4,
    "walk_speed_multiplier": 0.8,
    "sprint_speed_multiplier": 1.33,
    "sneak_speed_multiplier": 0.6
}
```

# minecraft:behavior.offer_flower
### iron_golem.json
```json
"minecraft:behavior.offer_flower:" {
    "priority": 5
}
```

# minecraft:behavior.open_door
### villager.json
```json
"minecraft:behavior.open_door:" {
    "priority": 6,
    "close_door_after": true
}
```

### wandering_trader.json
```json
"minecraft:behavior.open_door:" {
    "priority": 6,
    "close_door_after": true
}
```

# minecraft:behavior.owner_hurt_by_target
### wolf.json
```json
"minecraft:behavior.owner_hurt_by_target:" {
    "priority": 1
}
```

# minecraft:behavior.owner_hurt_target
```json
"minecraft:behavior.owner_hurt_target:" {
    "priority": 2
}
```

# minecraft:behavior.panic
### bee.json
```json
"minecraft:behavior.panic:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "force": true
}
```

```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "force": true
}
```

### cat.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### chicken.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.5
}
```

### cow.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### dolphin.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### donkey.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### fox.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```json
"minecraft:behavior.panic:" {
    "priority": 2,
    "speed_multiplier": 1.25
}
```

### horse.json
```json
"minecraft:behavior.panic:" {
    "priority": 3,
    "speed_multiplier": 1.2
}
```

### llama.json
```json
"minecraft:behavior.panic:" {
    "priority": 4,
    "speed_multiplier": 1.2
}
```

### mooshroom.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### mule.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### ocelot.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### panda.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 2.5
}
```

```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "ignore_mob_damage": true
}
```

### parrot.json
```json
"minecraft:behavior.panic:" {
    "priority": 0,
    "speed_multiplier": 1.25
}
```

### pig.json
```json
"minecraft:behavior.panic:" {
    "priority": 3,
    "speed_multiplier": 1.25
}
```

### polar_bear.json
```json
"minecraft:behavior.panic:" {
    "priority": 2,
    "speed_multiplier": 2.0
}
```

### rabbit.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 2.2
}
```

### sheep.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

### skeleton_horse.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### turtle.json
```json
"minecraft:behavior.panic:" {
    "priority": 0,
    "prefer_water": true,
    "speed_multiplier": 1.2
}
```

### villager.json
```json
"minecraft:behavior.panic:" {
    "priority": 3,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### wandering_trader.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 0.6
}
```

### zombie_horse.json
```json
"minecraft:behavior.panic:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.pet_sleep_with_owner
### cat.json
```json
"minecraft:behavior.pet_sleep_with_owner:" {
    "priority": 2,
    "speed_multiplier": 1.2,
    "search_radius": 10,
    "search_height": 10,
    "goal_radius": 1.0
}
```

# minecraft:behavior.pickup_items
### fox.json
```json
"minecraft:behavior.pickup_items:" {
    "priority": 11,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

### villager.json
```json
"minecraft:behavior.pickup_items:" {
    "priority": 9,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

### villager_v2.json
```json
"minecraft:behavior.pickup_items:" {
    "priority": 4,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

# minecraft:behavior.play
### villager.json
```json
"minecraft:behavior.play:" {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

### villager_v2.json
```json
"minecraft:behavior.play:" {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

# minecraft:behavior.player_ride_tamed
### donkey.json
```json
"minecraft:behavior.player_ride_tamed:" {}
```

### horse.json
```json
"minecraft:behavior.player_ride_tamed:" {}
```

### mule.json
```json
"minecraft:behavior.player_ride_tamed:" {}
```

### skeleton_horse.json
```json
"minecraft:behavior.player_ride_tamed:" {}
```

### zombie_horse.json
```json
"minecraft:behavior.player_ride_tamed:" {}
```

# minecraft:behavior.raid_garden
### fox.json
```json
"minecraft:behavior.raid_garden:" {
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
```json
"minecraft:behavior.raid_garden:" {
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
```json
"minecraft:behavior.random_breach:" {
    "priority": 6,
    "interval": 50,
    "xz_dist": 6,
    "cooldown_time": 2.0
}
```

# minecraft:behavior.random_fly
### parrot.json
```json
"minecraft:behavior.random_fly:" {
    "priority": 2,
    "xz_dist": 15,
    "y_dist": 1,
    "y_offset": 0,
    "speed_multiplier": 1.0,
    "can_land_on_trees": true,
    "avoid_damage_blocks": true
}
```

# minecraft:behavior.random_hover
### bee.json
```json
"minecraft:behavior.random_hover:" {
    "priority": 12,
    "xz_dist": 8,
    "y_dist": 8,
    "y_offset": -1,
    "interval": 1,
    "hover_height": [
        1,
        4
    ]
}
```

# minecraft:behavior.random_look_around
### blaze.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 6
}
```

### cave_spider.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### chicken.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### cow.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### creeper.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 6
}
```

### dolphin.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### donkey.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### drowned.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### elder_guardian.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### enderman.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### fox.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 15
}
```

### guardian.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### horse.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### husk.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### iron_golem.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### llama.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### mooshroom.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### mule.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### panda.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### pig.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### pillager.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### polar_bear.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### sheep.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### shulker.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### skeleton.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 6
}
```

### skeleton_horse.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### snow_golem.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 4
}
```

### spider.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### stray.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 6
}
```

### wandering_trader.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### witch.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 5,
    "look_distance": 8.0
}
```

### wither.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### wither_skeleton.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 6
}
```

### zombie.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 7
}
```

### zombie_horse.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 8
}
```

### zombie_pigman.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### zombie_villager.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.random_look_around:" {
    "priority": 9
}
```

# minecraft:behavior.random_look_around_and_sit
### fox.json
```json
"minecraft:behavior.random_look_around_and_sit:" {
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
```json
"minecraft:behavior.random_sitting:" {
    "priority": 5,
    "start_chance": 0.01,
    "stop_chance": 0.3,
    "cooldown": 30,
    "min_sit_time": 10
}
```

```json
"minecraft:behavior.random_sitting:" {
    "priority": 6,
    "start_chance": 0.02,
    "stop_chance": 0.2,
    "cooldown": 25,
    "min_sit_time": 15
}
```

# minecraft:behavior.random_stroll
### blaze.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

### cat.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### cave_spider.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### chicken.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

### cow.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### creeper.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### donkey.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### drowned.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1
}
```

### elder_guardian.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 0.5
}
```

### enderman.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### endermite.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1
}
```

### evocation_illager.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 0.6
}
```

### fox.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 13,
    "speed_multiplier": 0.8
}
```

### guardian.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 1.0,
    "interval": 80
}
```

### horse.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### husk.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1
}
```

### iron_golem.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1,
    "xz_dist": 16
}
```

### llama.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### mooshroom.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### mule.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### ocelot.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

### panda.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 14,
    "speed_multiplier": 0.8
}
```

### pig.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### pillager.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 1
}
```

### polar_bear.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5
}
```

### rabbit.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.6,
    "xz_dist": 2,
    "y_dist": 1
}
```

### ravager.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.4
}
```

### sheep.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 0.8
}
```

### skeleton.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### skeleton_horse.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### snow_golem.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 2,
    "speed_multiplier": 1
}
```

### spider.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

### stray.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### turtle.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 9,
    "interval": 100
}
```

### villager.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 11,
    "speed_multiplier": 0.6
}
```

### villager_v2.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 10,
    "speed_multiplier": 0.6
}
```

### vindicator.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 9,
    "speed_multiplier": 1
}
```

### witch.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

### wither.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### wither_skeleton.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 5,
    "speed_multiplier": 1
}
```

### wolf.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 1.0
}
```

### zombie.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 1
}
```

### zombie_horse.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

### zombie_pigman.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

### zombie_villager.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 1
}
```

### zombie_villager_v2.json
```json
"minecraft:behavior.random_stroll:" {
    "priority": 8,
    "speed_multiplier": 1
}
```

# minecraft:behavior.random_swim
### dolphin.json
```json
"minecraft:behavior.random_swim:" {
    "priority": 5,
    "interval": 0,
    "xz_dist": 20
}
```

### fish.json
```json
"minecraft:behavior.random_swim:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### pufferfish.json
```json
"minecraft:behavior.random_swim:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### salmon.json
```json
"minecraft:behavior.random_swim:" {
    "speed_multiplier": 1.0,
    "priority": 3,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### tropicalfish.json
```json
"minecraft:behavior.random_swim:" {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

### turtle.json
```json
"minecraft:behavior.random_swim:" {
    "priority": 7,
    "interval": 0,
    "xz_dist": 30,
    "y_dist": 15
}
```

# minecraft:behavior.ranged_attack
### blaze.json
```json
"minecraft:behavior.ranged_attack:" {
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
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 3,
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 10
}
```

### ghast.json
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 1,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### llama.json
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

```json
"minecraft:behavior.ranged_attack:" {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

```json
"minecraft:behavior.ranged_attack:" {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

### pillager.json
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 4,
    "attack_interval_min": 1,
    "attack_interval_max": 1,
    "attack_radius": 8
}
```

### shulker.json
```json
"minecraft:behavior.ranged_attack:" {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### skeleton.json
```json
"minecraft:behavior.ranged_attack:" {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

```json
"minecraft:behavior.ranged_attack:" {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### snow_golem.json
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 1,
    "speed_multiplier": 1.25,
    "attack_interval": 1,
    "attack_radius": 10
}
```

### stray.json
```json
"minecraft:behavior.ranged_attack:" {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

```json
"minecraft:behavior.ranged_attack:" {
    "attack_interval_min": 1,
    "attack_interval_max": 3,
    "attack_radius": 15
}
```

### witch.json
```json
"minecraft:behavior.ranged_attack:" {
    "priority": 2,
    "speed_multiplier": 1.0,
    "attack_interval_min": 3,
    "attack_interval_max": 3,
    "attack_radius": 10.0
}
```

# minecraft:behavior.receive_love
### villager.json
```json
"minecraft:behavior.receive_love:" {
    "priority": 7
}
```

### villager_v2.json
```json
"minecraft:behavior.receive_love:" {
    "priority": 6
}
```

# minecraft:behavior.restrict_open_door
### villager.json
```json
"minecraft:behavior.restrict_open_door:" {
    "priority": 5
}
```

### wandering_trader.json
```json
"minecraft:behavior.restrict_open_door:" {
    "priority": 5
}
```

# minecraft:behavior.roll
### panda.json
```json
"minecraft:behavior.roll:" {
    "priority": 12,
    "probability": 0.0016
}
```

```json
"minecraft:behavior.roll:" {
    "priority": 12,
    "probability": 0.013
}
```

# minecraft:behavior.run_around_like_crazy
### donkey.json
```json
"minecraft:behavior.run_around_like_crazy:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### horse.json
```json
"minecraft:behavior.run_around_like_crazy:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### llama.json
```json
"minecraft:behavior.run_around_like_crazy:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

### mule.json
```json
"minecraft:behavior.run_around_like_crazy:" {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

# minecraft:behavior.scared
### panda.json
```json
"minecraft:behavior.scared:" {
    "priority": 1,
    "sound_interval": 20
}
```

# minecraft:behavior.send_event
### evocation_illager.json
```json
"minecraft:behavior.send_event:" {
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
```json
"minecraft:behavior.share_items:" {
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
```json
"minecraft:behavior.share_items:" {
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
```json
"minecraft:behavior.silverfish_merge_with_stone:" {
    "priority": 5
}
```

# minecraft:behavior.silverfish_wake_up_friends
```json
"minecraft:behavior.silverfish_wake_up_friends:" {
    "priority": 1
}
```

# minecraft:behavior.skeleton_horse_trap
### skeleton_horse.json
```json
"minecraft:behavior.skeleton_horse_trap:" {
    "within_radius": 10.0,
    "duration": 900.0,
    "priority": 2
}
```

# minecraft:behavior.sleep
### villager_v2.json
```json
"minecraft:behavior.sleep:" {}
```

```json
"minecraft:behavior.sleep:" {
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
```json
"minecraft:behavior.slime_attack:" {
    "priority": 3
}
```

### slime.json
```json
"minecraft:behavior.slime_attack:" {
    "priority": 3
}
```

# minecraft:behavior.slime_float
### magma_cube.json
```json
"minecraft:behavior.slime_float:" {
    "priority": 1
}
```

### slime.json
```json
"minecraft:behavior.slime_float:" {
    "priority": 1
}
```

# minecraft:behavior.slime_keep_on_jumping
### magma_cube.json
```json
"minecraft:behavior.slime_keep_on_jumping:" {
    "priority": 5
}
```

### slime.json
```json
"minecraft:behavior.slime_keep_on_jumping:" {
    "priority": 5
}
```

# minecraft:behavior.slime_random_direction
### magma_cube.json
```json
"minecraft:behavior.slime_random_direction:" {
    "priority": 4
}
```

### slime.json
```json
"minecraft:behavior.slime_random_direction:" {
    "priority": 4
}
```

# minecraft:behavior.snacking
### panda.json
```json
"minecraft:behavior.snacking:" {
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

```json
"minecraft:behavior.snacking:" {
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
```json
"minecraft:behavior.sneeze:" {
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

```json
"minecraft:behavior.sneeze:" {
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
```json
"minecraft:behavior.squid_dive:" {
    "priority": 2
}
```

# minecraft:behavior.squid_flee
```json
"minecraft:behavior.squid_flee:" {
    "priority": 2
}
```

# minecraft:behavior.squid_idle
```json
"minecraft:behavior.squid_idle:" {
    "priority": 2
}
```

# minecraft:behavior.squid_move_away_from_ground
```json
"minecraft:behavior.squid_move_away_from_ground:" {
    "priority": 1
}
```

# minecraft:behavior.squid_out_of_water
```json
"minecraft:behavior.squid_out_of_water:" {
    "priority": 2
}
```

# minecraft:behavior.stalk_and_pounce_on_target
### fox.json
```json
"minecraft:behavior.stalk_and_pounce_on_target:" {
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
```json
"minecraft:behavior.stay_while_sitting:" {
    "priority": 3
}
```

### ocelot.json
```json
"minecraft:behavior.stay_while_sitting:" {
    "priority": 3
}
```

### parrot.json
```json
"minecraft:behavior.stay_while_sitting:" {
    "priority": 1
}
```

### wolf.json
```json
"minecraft:behavior.stay_while_sitting:" {
    "priority": 3
}
```

# minecraft:behavior.stomp_attack
### polar_bear.json
```json
"minecraft:behavior.stomp_attack:" {
    "priority": 1,
    "track_target": true,
    "require_complete_path": true
}
```

# minecraft:behavior.stomp_turtle_egg
### drowned.json
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stomp_turtle_egg:" {
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
```json
"minecraft:behavior.stroll_towards_village:" {
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
```json
"minecraft:behavior.summon_entity:" {
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
```json
"minecraft:behavior.swell:" {
    "start_distance": 2.5,
    "stop_distance": 6.0,
    "priority": 2
}
```

# minecraft:behavior.swim_idle
### fish.json
```json
"minecraft:behavior.swim_idle:" {
    "priority": 5
}
```

### salmon.json
```json
"minecraft:behavior.swim_idle:" {
    "priority": 5
}
```

### tropicalfish.json
```json
"minecraft:behavior.swim_idle:" {
    "priority": 5
}
```

# minecraft:behavior.swim_wander
### fish.json
```json
"minecraft:behavior.swim_wander:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 10,
    "look_ahead": 2.0
}
```

### pufferfish.json
```json
"minecraft:behavior.swim_wander:" {
    "priority": 5,
    "speed_multiplier": 1.0,
    "interval": 0,
    "look_ahead": 2.0
}
```

### salmon.json
```json
"minecraft:behavior.swim_wander:" {
    "priority": 4,
    "speed_multiplier": 0.014,
    "interval": 60
}
```

### tropicalfish.json
```json
"minecraft:behavior.swim_wander:" {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 10,
    "look_ahead": 2.0
}
```

# minecraft:behavior.swoop_attack
### phantom.json
```json
"minecraft:behavior.swoop_attack:" {
    "priority": 2,
    "delay_range": [
        10.0,
        20.0
    ]
}
```

# minecraft:behavior.take_flower
### villager.json
```json
"minecraft:behavior.take_flower:" {
    "priority": 7
}
```

### villager_v2.json
```json
"minecraft:behavior.take_flower:" {
    "priority": 9
}
```

# minecraft:behavior.target_when_pushed
### iron_golem.json
```json
"minecraft:behavior.target_when_pushed:" {
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
### bee.json
```json
"minecraft:behavior.tempt:" {
    "priority": 7,
    "speed_multiplier": 1.25,
    "within_radius": 8,
    "can_tempt_vertically": true,
    "items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ]
}
```

### cat.json
```json
"minecraft:behavior.tempt:" {
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

```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### donkey.json
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### mule.json
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
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

```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "bamboo"
    ]
}
```

### pig.json
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
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
```json
"minecraft:behavior.tempt:" {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

### turtle.json
```json
"minecraft:behavior.tempt:" {
    "priority": 3,
    "speed_multiplier": 1.1,
    "items": [
        "seagrass"
    ]
}
```

# minecraft:behavior.trade_interest
### villager_v2.json
```json
"minecraft:behavior.trade_interest:" {}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json
"minecraft:behavior.trade_interest:" {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

### wandering_trader.json
```json
"minecraft:behavior.trade_interest:" {
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
```json
"minecraft:behavior.trade_with_player:" {
    "priority": 1
}
```

### villager_v2.json
```json
"minecraft:behavior.trade_with_player:" {
    "priority": 2
}
```

### wandering_trader.json
```json
"minecraft:behavior.trade_with_player:" {
    "priority": 1
}
```

# minecraft:behavior.wither_random_attack_pos_goal
### wither.json
```json
"minecraft:behavior.wither_random_attack_pos_goal:" {
    "priority": 3
}
```

# minecraft:behavior.wither_target_highest_damage
```json
"minecraft:behavior.wither_target_highest_damage:" {
    "priority": 1
}
```

# minecraft:behavior.work
### villager_v2.json
```json
"minecraft:behavior.work:" {}
```

```json
"minecraft:behavior.work:" {
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

```json
"minecraft:behavior.work:" {
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

```json
"minecraft:behavior.work:" {
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

```json
"minecraft:behavior.work:" {
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

# minecraft:block_sensor
### bee.json
```json
"minecraft:block_sensor:" {
    "sensor_radius": 16,
    "on_break": [
        {
            "block_list": [
                "minecraft:beehive",
                "minecraft:bee_nest"
            ],
            "on_block_broken": "hive_destroyed"
        }
    ]
}
```

# minecraft:boostable
### pig.json
```json
"minecraft:boostable:" {
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
```json
"minecraft:boss:" {
    "should_darken_sky": false,
    "hud_range": 125
}
```

### wither.json
```json
"minecraft:boss:" {
    "should_darken_sky": true,
    "hud_range": 55
}
```

# minecraft:break_blocks
### ravager.json
```json
"minecraft:break_blocks:" {
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
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### bee.json
```json
"minecraft:breathable:" {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

### cat.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cave_spider.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### chicken.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### cow.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### creeper.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### dolphin.json
```json
"minecraft:breathable:" {
    "total_supply": 240,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false,
    "generates_bubbles": false
}
```

### donkey.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### drowned.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### elder_guardian.json
```json
"minecraft:breathable:" {
    "breathes_water": true
}
```

### enderman.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### endermite.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### evocation_illager.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### fish.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### fox.json
```json
"minecraft:breathable:" {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

### ghast.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### guardian.json
```json
"minecraft:breathable:" {
    "breathes_water": true
}
```

### horse.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### husk.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### llama.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### magma_cube.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_lava": true
}
```

### mooshroom.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### mule.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ocelot.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### panda.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### parrot.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### phantom.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": false
}
```

### pig.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pillager.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### player.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": -1,
    "inhale_time": 3.75,
    "generates_bubbles": false
}
```

### polar_bear.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### pufferfish.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### rabbit.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### ravager.json
```json
"minecraft:breathable:" {
    "suffocate_time": 0,
    "total_supply": 15
}
```

### salmon.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### sheep.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### shulker.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### silverfish.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### skeleton.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### skeleton_horse.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### slime.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### snow_golem.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### spider.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### squid.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### stray.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### tropicalfish.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": false,
    "breathes_water": true
}
```

### turtle.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true,
    "breathes_air": true,
    "generates_bubbles": false
}
```

### villager.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### villager_v2.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### vindicator.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wandering_trader.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### witch.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### wither_skeleton.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### wolf.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0
}
```

### zombie.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_air": true,
    "breathes_water": true
}
```

### zombie_horse.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_pigman.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

### zombie_villager_v2.json
```json
"minecraft:breathable:" {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

# minecraft:breedable
### bee.json
```json
"minecraft:breedable:" {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:bee",
        "baby_type": "minecraft:bee",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "minecraft:red_flower",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:double_plant:0",
        "minecraft:double_plant:1",
        "minecraft:double_plant:4",
        "minecraft:double_plant:5"
    ]
}
```

### cat.json
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:sheep",
        "baby_type": "minecraft:sheep"
    },
    "breed_items": "wheat"
}
```

### turtle.json
```json
"minecraft:breedable:" {
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
```json
"minecraft:breedable:" {
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
```json
"minecraft:bribeable:" {
    "bribe_items": [
        "fish",
        "salmon"
    ]
}
```

# minecraft:burns_in_daylight
### drowned.json
```json
"minecraft:burns_in_daylight:" {}
```

### magma_cube.json
```json
"minecraft:burns_in_daylight:" false
```

### phantom.json
```json
"minecraft:burns_in_daylight:" {}
```

### skeleton.json
```json
"minecraft:burns_in_daylight:" {}
```

### stray.json
```json
"minecraft:burns_in_daylight:" {}
```

### zombie.json
```json
"minecraft:burns_in_daylight:" {}
```

### zombie_pigman.json
```json
"minecraft:burns_in_daylight:" false
```

### zombie_villager.json
```json
"minecraft:burns_in_daylight:" {}
```

### zombie_villager_v2.json
```json
"minecraft:burns_in_daylight:" {}
```

# minecraft:can_climb
### blaze.json
```json
"minecraft:can_climb:" {}
```

### cat.json
```json
"minecraft:can_climb:" {}
```

### cave_spider.json
```json
"minecraft:can_climb:" {}
```

### chicken.json
```json
"minecraft:can_climb:" {}
```

### cow.json
```json
"minecraft:can_climb:" {}
```

### creeper.json
```json
"minecraft:can_climb:" {}
```

### dolphin.json
```json
"minecraft:can_climb:" {}
```

### drowned.json
```json
"minecraft:can_climb:" {}
```

### enderman.json
```json
"minecraft:can_climb:" {}
```

### endermite.json
```json
"minecraft:can_climb:" {}
```

### evocation_illager.json
```json
"minecraft:can_climb:" {}
```

### fox.json
```json
"minecraft:can_climb:" {}
```

### husk.json
```json
"minecraft:can_climb:" {}
```

### iron_golem.json
```json
"minecraft:can_climb:" {}
```

### magma_cube.json
```json
"minecraft:can_climb:" {}
```

### mooshroom.json
```json
"minecraft:can_climb:" {}
```

### ocelot.json
```json
"minecraft:can_climb:" {}
```

### panda.json
```json
"minecraft:can_climb:" {}
```

### pig.json
```json
"minecraft:can_climb:" {}
```

### player.json
```json
"minecraft:can_climb:" {}
```

### polar_bear.json
```json
"minecraft:can_climb:" {}
```

### rabbit.json
```json
"minecraft:can_climb:" {}
```

### sheep.json
```json
"minecraft:can_climb:" {}
```

### silverfish.json
```json
"minecraft:can_climb:" {}
```

### skeleton.json
```json
"minecraft:can_climb:" {}
```

### slime.json
```json
"minecraft:can_climb:" {}
```

### snow_golem.json
```json
"minecraft:can_climb:" {}
```

### spider.json
```json
"minecraft:can_climb:" {}
```

### squid.json
```json
"minecraft:can_climb:" {}
```

### stray.json
```json
"minecraft:can_climb:" {}
```

### vex.json
```json
"minecraft:can_climb:" {}
```

### villager.json
```json
"minecraft:can_climb:" {}
```

### villager_v2.json
```json
"minecraft:can_climb:" {}
```

### wandering_trader.json
```json
"minecraft:can_climb:" {}
```

### witch.json
```json
"minecraft:can_climb:" {}
```

### wither.json
```json
"minecraft:can_climb:" {}
```

### wither_skeleton.json
```json
"minecraft:can_climb:" {}
```

### wolf.json
```json
"minecraft:can_climb:" {}
```

### zombie.json
```json
"minecraft:can_climb:" {}
```

### zombie_pigman.json
```json
"minecraft:can_climb:" {}
```

### zombie_villager.json
```json
"minecraft:can_climb:" {}
```

### zombie_villager_v2.json
```json
"minecraft:can_climb:" {}
```

# minecraft:can_fly
### bat.json
```json
"minecraft:can_fly:" {}
```

### bee.json
```json
"minecraft:can_fly:" {}
```

### blaze.json
```json
"minecraft:can_fly:" {
    "value": true
}
```

### ghast.json
```json
"minecraft:can_fly:" {}
```

### parrot.json
```json
"minecraft:can_fly:" {
    "value": true
}
```

### wither.json
```json
"minecraft:can_fly:" {}
```

# minecraft:can_power_jump
### donkey.json
```json
"minecraft:can_power_jump:" {}
```

### horse.json
```json
"minecraft:can_power_jump:" {}
```

### mule.json
```json
"minecraft:can_power_jump:" {}
```

### skeleton_horse.json
```json
"minecraft:can_power_jump:" {}
```

# minecraft:collision_box
### armor_stand.json
```json
"minecraft:collision_box:" {
    "width": 0.5,
    "height": 1.975
}
```

### arrow.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### bat.json
```json
"minecraft:collision_box:" {
    "width": 0.5,
    "height": 0.9
}
```

### bee.json
```json
"minecraft:collision_box:" {
    "width": 0.55,
    "height": 0.5
}
```

### blaze.json
```json
"minecraft:collision_box:" {
    "width": 0.5,
    "height": 1.8
}
```

### boat.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 0.455
}
```

### cat.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.7
}
```

### cave_spider.json
```json
"minecraft:collision_box:" {
    "width": 0.7,
    "height": 0.5
}
```

### chest_minecart.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.7
}
```

### chicken.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.8
}
```

### command_block_minecart.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.7
}
```

### cow.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 1.3
}
```

### creeper.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.8
}
```

### dolphin.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 0.6
}
```

### donkey.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 1.6
}
```

### dragon_fireball.json
```json
"minecraft:collision_box:" {
    "width": 0.31,
    "height": 0.31
}
```

### drowned.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### egg.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### elder_guardian.json
```json
"minecraft:collision_box:" {
    "width": 1.99,
    "height": 1.99
}
```

### enderman.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 2.9
}
```

### endermite.json
```json
"minecraft:collision_box:" {
    "width": 0.4,
    "height": 0.3
}
```

### ender_crystal.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.98
}
```

### ender_dragon.json
```json
"minecraft:collision_box:" {
    "width": 13,
    "height": 4
}
```

### ender_pearl.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### evocation_illager.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### eye_of_ender_signal.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### fireball.json
```json
"minecraft:collision_box:" {
    "width": 0.31,
    "height": 0.31
}
```

### fireworks_rocket.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### fish.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.3
}
```

### fishing_hook.json
```json
"minecraft:collision_box:" {
    "width": 0.15,
    "height": 0.15
}
```

### fox.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.7
}
```

### ghast.json
```json
"minecraft:collision_box:" {
    "width": 4,
    "height": 4
}
```

### guardian.json
```json
"minecraft:collision_box:" {
    "width": 0.85,
    "height": 0.85
}
```

### hopper_minecart.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.7
}
```

### horse.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 1.6
}
```

### husk.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### iron_golem.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 2.9
}
```

### lingering_potion.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### llama.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 1.87
}
```

### llama_spit.json
```json
"minecraft:collision_box:" {
    "width": 0.31,
    "height": 0.31
}
```

### magma_cube.json
```json
"minecraft:collision_box:" {
    "width": 2.08,
    "height": 2.08
}
```

```json
"minecraft:collision_box:" {
    "width": 0.78,
    "height": 0.78
}
```

```json
"minecraft:collision_box:" {
    "width": 0.52,
    "height": 0.52
}
```

### minecart.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.7
}
```

### mooshroom.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 1.3
}
```

### mule.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 1.6
}
```

### ocelot.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.7
}
```

### panda.json
```json
"minecraft:collision_box:" {
    "width": 1.7,
    "height": 1.5
}
```

### parrot.json
```json
"minecraft:collision_box:" {
    "width": 0.5,
    "height": 1
}
```

### phantom.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 0.5
}
```

### pig.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 0.9
}
```

### pillager.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### player.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.8
}
```

### polar_bear.json
```json
"minecraft:collision_box:" {
    "width": 1.3,
    "height": 1.4
}
```

### pufferfish.json
```json
"minecraft:collision_box:" {
    "width": 0.8,
    "height": 0.8
}
```

### rabbit.json
```json
"minecraft:collision_box:" {
    "width": 0.67,
    "height": 0.67
}
```

### ravager.json
```json
"minecraft:collision_box:" {
    "height": 1.9,
    "width": 1.2
}
```

### salmon.json
```json
"minecraft:collision_box:" {
    "width": 0.5,
    "height": 0.5
}
```

### sheep.json
```json
"minecraft:collision_box:" {
    "width": 0.9,
    "height": 1.3
}
```

### shulker_bullet.json
```json
"minecraft:collision_box:" {
    "width": 0.625,
    "height": 0.625
}
```

### silverfish.json
```json
"minecraft:collision_box:" {
    "width": 0.4,
    "height": 0.3
}
```

### skeleton.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### skeleton_horse.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 1.6
}
```

### slime.json
```json
"minecraft:collision_box:" {
    "width": 2.08,
    "height": 2.08
}
```

```json
"minecraft:collision_box:" {
    "width": 1.04,
    "height": 1.04
}
```

```json
"minecraft:collision_box:" {
    "width": 0.52,
    "height": 0.52
}
```

### small_fireball.json
```json
"minecraft:collision_box:" {
    "width": 0.31,
    "height": 0.31
}
```

### snowball.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### snow_golem.json
```json
"minecraft:collision_box:" {
    "width": 0.4,
    "height": 1.8
}
```

### spider.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 0.9
}
```

### splash_potion.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### squid.json
```json
"minecraft:collision_box:" {
    "width": 0.95,
    "height": 0.95
}
```

### stray.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### thrown_trident.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.35
}
```

### tnt.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.98
}
```

### tnt_minecart.json
```json
"minecraft:collision_box:" {
    "width": 0.98,
    "height": 0.7
}
```

### tripod_camera.json
```json
"minecraft:collision_box:" {
    "width": 0.75,
    "height": 1.8
}
```

### tropicalfish.json
```json
"minecraft:collision_box:" {
    "width": 0.4,
    "height": 0.4
}
```

### turtle.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.2
}
```

```json
"minecraft:collision_box:" {
    "width": 1.2,
    "height": 0.4
}
```

### vex.json
```json
"minecraft:collision_box:" {
    "width": 0.4,
    "height": 0.8
}
```

### villager.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### villager_v2.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### vindicator.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### wandering_trader.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### witch.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### wither.json
```json
"minecraft:collision_box:" {
    "width": 1,
    "height": 3
}
```

### wither_skeleton.json
```json
"minecraft:collision_box:" {
    "width": 0.72,
    "height": 2.01
}
```

### wither_skull.json
```json
"minecraft:collision_box:" {
    "width": 0.15,
    "height": 0.15
}
```

### wither_skull_dangerous.json
```json
"minecraft:collision_box:" {
    "width": 0.15,
    "height": 0.15
}
```

### wolf.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 0.8
}
```

### xp_bottle.json
```json
"minecraft:collision_box:" {
    "width": 0.25,
    "height": 0.25
}
```

### zombie.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_horse.json
```json
"minecraft:collision_box:" {
    "width": 1.4,
    "height": 1.6
}
```

### zombie_pigman.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

### zombie_villager_v2.json
```json
"minecraft:collision_box:" {
    "width": 0.6,
    "height": 1.9
}
```

# minecraft:color
### cat.json
```json
"minecraft:color:" {
    "value": 14
}
```

### sheep.json
```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 12
}
```

```json
"minecraft:color:" {
    "value": 15
}
```

```json
"minecraft:color:" {
    "value": 8
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 6
}
```

```json
"minecraft:color:" {
    "value": 14
}
```

### tropicalfish.json
```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 1
}
```

```json
"minecraft:color:" {
    "value": 2
}
```

```json
"minecraft:color:" {
    "value": 3
}
```

```json
"minecraft:color:" {
    "value": 4
}
```

```json
"minecraft:color:" {
    "value": 5
}
```

```json
"minecraft:color:" {
    "value": 6
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 8
}
```

```json
"minecraft:color:" {
    "value": 9
}
```

```json
"minecraft:color:" {
    "value": 10
}
```

```json
"minecraft:color:" {
    "value": 11
}
```

```json
"minecraft:color:" {
    "value": 12
}
```

```json
"minecraft:color:" {
    "value": 13
}
```

```json
"minecraft:color:" {
    "value": 14
}
```

```json
"minecraft:color:" {
    "value": 1
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 11
}
```

```json
"minecraft:color:" {
    "value": 1
}
```

```json
"minecraft:color:" {
    "value": 6
}
```

```json
"minecraft:color:" {
    "value": 10
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 9
}
```

```json
"minecraft:color:" {
    "value": 5
}
```

```json
"minecraft:color:" {
    "value": 14
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 14
}
```

```json
"minecraft:color:" {
    "value": 0
}
```

```json
"minecraft:color:" {
    "value": 14
}
```

```json
"minecraft:color:" {
    "value": 7
}
```

```json
"minecraft:color:" {
    "value": 4
}
```

```json
"minecraft:color:" {
    "value": 9
}
```

### wolf.json
```json
"minecraft:color:" {
    "value": 14
}
```

# minecraft:color2
### tropicalfish.json
```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 1
}
```

```json
"minecraft:color2:" {
    "value": 2
}
```

```json
"minecraft:color2:" {
    "value": 3
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

```json
"minecraft:color2:" {
    "value": 5
}
```

```json
"minecraft:color2:" {
    "value": 6
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 8
}
```

```json
"minecraft:color2:" {
    "value": 9
}
```

```json
"minecraft:color2:" {
    "value": 10
}
```

```json
"minecraft:color2:" {
    "value": 11
}
```

```json
"minecraft:color2:" {
    "value": 12
}
```

```json
"minecraft:color2:" {
    "value": 13
}
```

```json
"minecraft:color2:" {
    "value": 14
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 3
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 3
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

```json
"minecraft:color2:" {
    "value": 14
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

```json
"minecraft:color2:" {
    "value": 7
}
```

```json
"minecraft:color2:" {
    "value": 1
}
```

```json
"minecraft:color2:" {
    "value": 6
}
```

```json
"minecraft:color2:" {
    "value": 3
}
```

```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 14
}
```

```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 0
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

```json
"minecraft:color2:" {
    "value": 4
}
```

# minecraft:damage_over_time
### dolphin.json
```json
"minecraft:damage_over_time:" {
    "damage_per_hurt": 1,
    "time_between_hurt": 0
}
```

# minecraft:damage_sensor
### bat.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### bee.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### blaze.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### cat.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### chicken.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### creeper.json
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### fox.json
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### iron_golem.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### llama.json
```json
"minecraft:damage_sensor:" {
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

```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "all",
        "deals_damage": true
    }
}
```

### magma_cube.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### mooshroom.json
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### parrot.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### pig.json
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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

```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

### turtle.json
```json
"minecraft:damage_sensor:" {
    "triggers": {
        "cause": "lightning",
        "deals_damage": true,
        "damage_multiplier": 2000.0
    }
}
```

### villager.json
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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

```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:damage_sensor:" {
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
```json
"minecraft:despawn:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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

```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:dweller:" {
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
```json
"minecraft:economy_trade_table:" {}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.farmer",
    "table": "trading/economy_trades/farmer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.fisherman",
    "table": "trading/economy_trades/fisherman_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.shepherd",
    "table": "trading/economy_trades/shepherd_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.fletcher",
    "table": "trading/economy_trades/fletcher_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.librarian",
    "table": "trading/economy_trades/librarian_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.cartographer",
    "table": "trading/economy_trades/cartographer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.cleric",
    "table": "trading/economy_trades/cleric_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.armor",
    "table": "trading/economy_trades/armorer_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.weapon",
    "table": "trading/economy_trades/weapon_smith_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.tool",
    "table": "trading/economy_trades/tool_smith_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.butcher",
    "table": "trading/economy_trades/butcher_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.leather",
    "table": "trading/economy_trades/leather_worker_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.villager.mason",
    "table": "trading/economy_trades/stone_mason_trades.json",
    "new_screen": true,
    "persist_trades": true
}
```

### wandering_trader.json
```json
"minecraft:economy_trade_table:" {
    "display_name": "entity.wandering_trader.name",
    "table": "trading/economy_trades/wandering_trader_trades.json",
    "new_screen": true
}
```

# minecraft:entity_sensor
### pufferfish.json
```json
"minecraft:entity_sensor:" {
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

```json
"minecraft:entity_sensor:" {
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
### bee.json
```json
"minecraft:environment_sensor:" {
    "triggers": [
        {
            "event": "seek_shelter",
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": false
                            },
                            {
                                "test": "is_weather",
                                "value": "clear",
                                "operator": "!="
                            }
                        ]
                    },
                    {
                        "test": "has_component",
                        "value": "minecraft:is_charged",
                        "operator": "!="
                    },
                    {
                        "test": "has_biome_tag",
                        "value": "overworld"
                    }
                ]
            }
        }
    ]
}
```

```json
"minecraft:environment_sensor:" {
    "triggers": [
        {
            "event": "abort_sheltering",
            "filters": {
                "all_of": [
                    {
                        "test": "is_weather",
                        "value": "clear"
                    },
                    {
                        "test": "is_daytime",
                        "value": true
                    }
                ]
            }
        }
    ]
}
```

### cave_spider.json
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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

```json
"minecraft:environment_sensor:" {
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
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/drowned_ranged_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

```json
"minecraft:equipment:" {
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
```json
"minecraft:equipment:" {
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
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### pillager.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/pillager_gear.json"
}
```

```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/pillager_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

```json
"minecraft:equipment:" {
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
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### stray.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

### vex.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/vex_gear.json"
}
```

### vindicator.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/vindicator_gear.json"
}
```

```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/vindicator_captain_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.armor.chest",
            "drop_chance": 1.0
        }
    ]
}
```

```json
"minecraft:equipment:" {
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
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/wither_skeleton_gear.json"
}
```

### zombie.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

### zombie_pigman.json
```json
"minecraft:equipment:" {
    "table": "loot_tables/entities/zombie_pigman_gear.json"
}
```

# minecraft:equippable
### donkey.json
```json
"minecraft:equippable:" {
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
```json
"minecraft:equippable:" {
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
```json
"minecraft:equippable:" {
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
```json
"minecraft:equippable:" {
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
### bee.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### blaze.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### cat.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cave_spider.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### chicken.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### cow.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### creeper.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### dolphin.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### donkey.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### drowned.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### elder_guardian.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### enderman.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### endermite.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 3 : 0"
}
```

### evocation_illager.json
```json
"minecraft:experience_reward:" {
    "on_death": "10"
}
```

### fish.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### fox.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ghast.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### guardian.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

### horse.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### husk.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### llama.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### magma_cube.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### mooshroom.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### mule.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ocelot.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### panda.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### parrot.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### phantom.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### pig.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### pillager.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### player.json
```json
"minecraft:experience_reward:" {
    "on_death": "Math.Min(query.player_level * 7, 100)"
}
```

### polar_bear.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### pufferfish.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### rabbit.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### ravager.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 20 : 0"
}
```

### salmon.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### sheep.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### shulker.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### silverfish.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### skeleton.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### skeleton_horse.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### slime.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? query.variant : 0"
}
```

### spider.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 : 0"
}
```

### squid.json
```json
"minecraft:experience_reward:" {
    "on_death": "!query.is_baby && query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### stray.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### tropicalfish.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### turtle.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### vex.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### vindicator.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### witch.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? (query.is_baby ? 12 : 5) + (Math.die_roll(query.equipment_count,1,3)) : 0"
}
```

### wither.json
```json
"minecraft:experience_reward:" {
    "on_death": "50"
}
```

### wither_skeleton.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### wolf.json
```json
"minecraft:experience_reward:" {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_horse.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

### zombie_pigman.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

### zombie_villager_v2.json
```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 12 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

```json
"minecraft:experience_reward:" {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

# minecraft:explode
### creeper.json
```json
"minecraft:explode:" {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json
"minecraft:explode:" {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json
"minecraft:explode:" {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json
"minecraft:explode:" {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### ender_crystal.json
```json
"minecraft:explode:" {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### fireball.json
```json
"minecraft:explode:" {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": true,
    "fire_affected_by_griefing": true,
    "destroy_affected_by_griefing": true
}
```

### tnt.json
```json
"minecraft:explode:" {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

```json
"minecraft:explode:" {
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
```json
"minecraft:explode:" {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

```json
"minecraft:explode:" {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

### wither_skull.json
```json
"minecraft:explode:" {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

### wither_skull_dangerous.json
```json
"minecraft:explode:" {
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
```json
"minecraft:fire_immune:" true
```

### ender_crystal.json
```json
"minecraft:fire_immune:" true
```

### ender_dragon.json
```json
"minecraft:fire_immune:" true
```

### ghast.json
```json
"minecraft:fire_immune:" true
```

### magma_cube.json
```json
"minecraft:fire_immune:" true
```

### vex.json
```json
"minecraft:fire_immune:" true
```

### wither.json
```json
"minecraft:fire_immune:" true
```

### wither_skeleton.json
```json
"minecraft:fire_immune:" true
```

### zombie_pigman.json
```json
"minecraft:fire_immune:" true
```

# minecraft:flocking
### dolphin.json
```json
"minecraft:flocking:" {
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
```json
"minecraft:flocking:" {
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
```json
"minecraft:flocking:" {
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
```json
"minecraft:flocking:" {
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
```json
"minecraft:flocking:" {
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
### bee.json
```json
"minecraft:flying_speed:" {
    "value": 0.15
}
```

### ender_dragon.json
```json
"minecraft:flying_speed:" {
    "value": 0.6
}
```

# minecraft:follow_range
### bee.json
```json
"minecraft:follow_range:" {
    "value": 1024
}
```

### blaze.json
```json
"minecraft:follow_range:" {
    "value": 48,
    "max": 48
}
```

### dolphin.json
```json
"minecraft:follow_range:" {
    "value": 48,
    "max": 48
}
```

### elder_guardian.json
```json
"minecraft:follow_range:" {
    "value": 16,
    "max": 16
}
```

### enderman.json
```json
"minecraft:follow_range:" {
    "value": 32,
    "max": 32
}
```

### evocation_illager.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

### ghast.json
```json
"minecraft:follow_range:" {
    "value": 64,
    "max": 64
}
```

### guardian.json
```json
"minecraft:follow_range:" {
    "value": 16,
    "max": 16
}
```

### iron_golem.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

### llama.json
```json
"minecraft:follow_range:" {
    "value": 40,
    "max": 40
}
```

### phantom.json
```json
"minecraft:follow_range:" {
    "value": 64,
    "max": 64
}
```

### pillager.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

### polar_bear.json
```json
"minecraft:follow_range:" {
    "value": 48
}
```

### ravager.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

### turtle.json
```json
"minecraft:follow_range:" {
    "value": 1024
}
```

### villager_v2.json
```json
"minecraft:follow_range:" {
    "value": 128
}
```

### vindicator.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

### witch.json
```json
"minecraft:follow_range:" {
    "value": 64
}
```

# minecraft:genetics
### panda.json
```json
"minecraft:genetics:" {
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
```json
"minecraft:giveable:" {
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

# minecraft:grows_crop
### bee.json
```json
"minecraft:grows_crop:" {
    "charges": 10,
    "chance": 0.03
}
```

# minecraft:healable
### cat.json
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:healable:" {
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
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### bat.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### bee.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### blaze.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### cat.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### cave_spider.json
```json
"minecraft:health:" {
    "value": 12,
    "max": 12
}
```

### chicken.json
```json
"minecraft:health:" {
    "value": 4,
    "max": 4
}
```

### cow.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### creeper.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### dolphin.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### donkey.json
```json
"minecraft:health:" {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### drowned.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### elder_guardian.json
```json
"minecraft:health:" {
    "value": 80,
    "max": 80
}
```

### enderman.json
```json
"minecraft:health:" {
    "value": 40,
    "max": 40
}
```

### endermite.json
```json
"minecraft:health:" {
    "value": 8,
    "max": 8
}
```

### ender_crystal.json
```json
"minecraft:health:" {
    "value": 1,
    "max": 1
}
```

### ender_dragon.json
```json
"minecraft:health:" {
    "value": 200,
    "max": 200
}
```

### evocation_illager.json
```json
"minecraft:health:" {
    "value": 24,
    "max": 24
}
```

### fish.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### fox.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### ghast.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### guardian.json
```json
"minecraft:health:" {
    "value": 30,
    "max": 30
}
```

### horse.json
```json
"minecraft:health:" {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### husk.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### iron_golem.json
```json
"minecraft:health:" {
    "value": 100,
    "max": 100
}
```

### llama.json
```json
"minecraft:health:" {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### magma_cube.json
```json
"minecraft:health:" {
    "value": 16,
    "max": 16
}
```

```json
"minecraft:health:" {
    "value": 4,
    "max": 4
}
```

```json
"minecraft:health:" {
    "value": 1,
    "max": 1
}
```

### mooshroom.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### mule.json
```json
"minecraft:health:" {
    "value": {
        "range_min": 15,
        "range_max": 30
    }
}
```

### ocelot.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### panda.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### parrot.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### phantom.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### pig.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### pillager.json
```json
"minecraft:health:" {
    "value": 24,
    "max": 24
}
```

### polar_bear.json
```json
"minecraft:health:" {
    "value": 30
}
```

### pufferfish.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### rabbit.json
```json
"minecraft:health:" {
    "value": 3,
    "max": 3
}
```

### ravager.json
```json
"minecraft:health:" {
    "max": 100,
    "value": 100
}
```

### salmon.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### sheep.json
```json
"minecraft:health:" {
    "value": 8,
    "max": 8
}
```

### shulker.json
```json
"minecraft:health:" {
    "value": 30,
    "max": 30
}
```

### silverfish.json
```json
"minecraft:health:" {
    "value": 8,
    "max": 8
}
```

### skeleton.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### skeleton_horse.json
```json
"minecraft:health:" {
    "value": 15,
    "max": 15
}
```

### slime.json
```json
"minecraft:health:" {
    "value": 16,
    "max": 16
}
```

```json
"minecraft:health:" {
    "value": 4,
    "max": 4
}
```

```json
"minecraft:health:" {
    "value": 1,
    "max": 1
}
```

### snow_golem.json
```json
"minecraft:health:" {
    "value": 4,
    "max": 4
}
```

### spider.json
```json
"minecraft:health:" {
    "value": 16,
    "max": 16
}
```

### squid.json
```json
"minecraft:health:" {
    "value": 10,
    "max": 10
}
```

### stray.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### tripod_camera.json
```json
"minecraft:health:" {
    "value": 4,
    "max": 4
}
```

### tropicalfish.json
```json
"minecraft:health:" {
    "value": 6,
    "max": 6
}
```

### turtle.json
```json
"minecraft:health:" {
    "value": 30
}
```

### vex.json
```json
"minecraft:health:" {
    "value": 14,
    "max": 14
}
```

### villager.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### villager_v2.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### vindicator.json
```json
"minecraft:health:" {
    "value": 24,
    "max": 24
}
```

### wandering_trader.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### witch.json
```json
"minecraft:health:" {
    "value": 26,
    "max": 26
}
```

### wither.json
```json
"minecraft:health:" {
    "value": 600,
    "max": 600
}
```

### wither_skeleton.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### wolf.json
```json
"minecraft:health:" {
    "value": 8,
    "max": 8
}
```

```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### zombie.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### zombie_horse.json
```json
"minecraft:health:" {
    "value": 15,
    "max": 15
}
```

### zombie_pigman.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### zombie_villager.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

### zombie_villager_v2.json
```json
"minecraft:health:" {
    "value": 20,
    "max": 20
}
```

# minecraft:hide
### villager_v2.json
```json
"minecraft:hide:" {}
```

# minecraft:home
### bee.json
```json
"minecraft:home:" {}
```

### turtle.json
```json
"minecraft:home:" {}
```

# minecraft:horse.jump_strength
### donkey.json
```json
"minecraft:horse.jump_strength:" {
    "value": 0.5
}
```

### horse.json
```json
"minecraft:horse.jump_strength:" {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### mule.json
```json
"minecraft:horse.jump_strength:" {
    "value": 0.5
}
```

### skeleton_horse.json
```json
"minecraft:horse.jump_strength:" {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

### zombie_horse.json
```json
"minecraft:horse.jump_strength:" {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

# minecraft:hurt_on_condition
### armor_stand.json
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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

### bee.json
```json
"minecraft:hurt_on_condition:" {
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

```json
"minecraft:hurt_on_condition:" {
    "damage_conditions": [
        {
            "cause": "none",
            "damage_per_tick": 999
        }
    ]
}
```

### blaze.json
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:hurt_on_condition:" {
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
```json
"minecraft:input_ground_controlled:" {}
```

### horse.json
```json
"minecraft:input_ground_controlled:" {}
```

### mule.json
```json
"minecraft:input_ground_controlled:" {}
```

### skeleton_horse.json
```json
"minecraft:input_ground_controlled:" {}
```

# minecraft:insomnia
### player.json
```json
"minecraft:insomnia:" {
    "days_until_insomnia": 3
}
```

# minecraft:interact
### cow.json
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:interact:" {
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
```json
"minecraft:inventory:" {
    "container_type": "minecart_chest",
    "inventory_size": 27,
    "can_be_siphoned_from": true
}
```

### command_block_minecart.json
```json
"minecraft:inventory:" {}
```

### donkey.json
```json
"minecraft:inventory:" {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### hopper_minecart.json
```json
"minecraft:inventory:" {
    "container_type": "minecart_hopper",
    "inventory_size": 5,
    "can_be_siphoned_from": true
}
```

### horse.json
```json
"minecraft:inventory:" {
    "inventory_size": 2,
    "container_type": "horse"
}
```

### llama.json
```json
"minecraft:inventory:" {
    "inventory_size": 16,
    "container_type": "horse",
    "additional_slots_per_strength": 3
}
```

### mule.json
```json
"minecraft:inventory:" {
    "inventory_size": 16,
    "container_type": "horse"
}
```

### panda.json
```json
"minecraft:inventory:" {
    "inventory_size": 1,
    "private": true
}
```

### villager.json
```json
"minecraft:inventory:" {
    "inventory_size": 8,
    "private": true
}
```

### villager_v2.json
```json
"minecraft:inventory:" {
    "inventory_size": 8,
    "private": true
}
```

# minecraft:is_baby
### bee.json
```json
"minecraft:is_baby:" {}
```

### cat.json
```json
"minecraft:is_baby:" {}
```

### chicken.json
```json
"minecraft:is_baby:" {}
```

### cow.json
```json
"minecraft:is_baby:" {}
```

### dolphin.json
```json
"minecraft:is_baby:" {}
```

### donkey.json
```json
"minecraft:is_baby:" {}
```

### drowned.json
```json
"minecraft:is_baby:" {}
```

### fox.json
```json
"minecraft:is_baby:" {}
```

### horse.json
```json
"minecraft:is_baby:" {}
```

### husk.json
```json
"minecraft:is_baby:" {}
```

### llama.json
```json
"minecraft:is_baby:" {}
```

### mooshroom.json
```json
"minecraft:is_baby:" {}
```

### mule.json
```json
"minecraft:is_baby:" {}
```

### ocelot.json
```json
"minecraft:is_baby:" {}
```

### panda.json
```json
"minecraft:is_baby:" {}
```

### pig.json
```json
"minecraft:is_baby:" {}
```

### polar_bear.json
```json
"minecraft:is_baby:" {}
```

### rabbit.json
```json
"minecraft:is_baby:" {}
```

### sheep.json
```json
"minecraft:is_baby:" {}
```

### skeleton_horse.json
```json
"minecraft:is_baby:" {}
```

### squid.json
```json
"minecraft:is_baby:" {}
```

### turtle.json
```json
"minecraft:is_baby:" {}
```

### villager.json
```json
"minecraft:is_baby:" {}
```

### villager_v2.json
```json
"minecraft:is_baby:" {}
```

### wolf.json
```json
"minecraft:is_baby:" {}
```

### zombie.json
```json
"minecraft:is_baby:" {}
```

### zombie_horse.json
```json
"minecraft:is_baby:" {}
```

### zombie_pigman.json
```json
"minecraft:is_baby:" {}
```

### zombie_villager.json
```json
"minecraft:is_baby:" {}
```

### zombie_villager_v2.json
```json
"minecraft:is_baby:" {}
```

# minecraft:is_charged
### bee.json
```json
"minecraft:is_charged:" {}
```

### creeper.json
```json
"minecraft:is_charged:" {}
```

# minecraft:is_chested
### donkey.json
```json
"minecraft:is_chested:" {}
```

### llama.json
```json
"minecraft:is_chested:" {}
```

### mule.json
```json
"minecraft:is_chested:" {}
```

# minecraft:is_dyeable
### cat.json
```json
"minecraft:is_dyeable:" {
    "interact_text": "action.interact.dye"
}
```

### sheep.json
```json
"minecraft:is_dyeable:" {
    "interact_text": "action.interact.dye"
}
```

### wolf.json
```json
"minecraft:is_dyeable:" {
    "interact_text": "action.interact.dye"
}
```

# minecraft:is_hidden_when_invisible
### player.json
```json
"minecraft:is_hidden_when_invisible:" {}
```

### wandering_trader.json
```json
"minecraft:is_hidden_when_invisible:" {}
```

# minecraft:is_ignited
### tnt_minecart.json
```json
"minecraft:is_ignited:" {}
```

```json
"minecraft:is_ignited:" {}
```

# minecraft:is_illager_captain
### pillager.json
```json
"minecraft:is_illager_captain:" {}
```

```json
"minecraft:is_illager_captain:" {}
```

### vindicator.json
```json
"minecraft:is_illager_captain:" {}
```

```json
"minecraft:is_illager_captain:" {}
```

# minecraft:is_saddled
### donkey.json
```json
"minecraft:is_saddled:" {}
```

### horse.json
```json
"minecraft:is_saddled:" {}
```

### mule.json
```json
"minecraft:is_saddled:" {}
```

### pig.json
```json
"minecraft:is_saddled:" {}
```

# minecraft:is_shaking
### husk.json
```json
"minecraft:is_shaking:" {}
```

```json
"minecraft:is_shaking:" {}
```

### zombie.json
```json
"minecraft:is_shaking:" {}
```

```json
"minecraft:is_shaking:" {}
```

### zombie_villager.json
```json
"minecraft:is_shaking:" {}
```

### zombie_villager_v2.json
```json
"minecraft:is_shaking:" {}
```

# minecraft:is_sheared
### sheep.json
```json
"minecraft:is_sheared:" {}
```

### snow_golem.json
```json
"minecraft:is_sheared:" {}
```

# minecraft:is_stackable
### boat.json
```json
"minecraft:is_stackable:" {}
```

### chest_minecart.json
```json
"minecraft:is_stackable:" {
    "value": true
}
```

### hopper_minecart.json
```json
"minecraft:is_stackable:" {}
```

### minecart.json
```json
"minecraft:is_stackable:" {}
```

### tnt_minecart.json
```json
"minecraft:is_stackable:" {}
```

# minecraft:is_stunned
### ravager.json
```json
"minecraft:is_stunned:" {}
```

# minecraft:is_tamed
### cat.json
```json
"minecraft:is_tamed:" {}
```

### donkey.json
```json
"minecraft:is_tamed:" {}
```

### horse.json
```json
"minecraft:is_tamed:" {}
```

### llama.json
```json
"minecraft:is_tamed:" {}
```

### mule.json
```json
"minecraft:is_tamed:" {}
```

### ocelot.json
```json
"minecraft:is_tamed:" {}
```

### parrot.json
```json
"minecraft:is_tamed:" {}
```

### skeleton_horse.json
```json
"minecraft:is_tamed:" {}
```

### wolf.json
```json
"minecraft:is_tamed:" {}
```

### zombie_horse.json
```json
"minecraft:is_tamed:" {}
```

# minecraft:item_controllable
### pig.json
```json
"minecraft:item_controllable:" {
    "control_items": "carrotOnAStick"
}
```

# minecraft:item_hopper
### hopper_minecart.json
```json
"minecraft:item_hopper:" {}
```

# minecraft:jump.dynamic
### rabbit.json
```json
"minecraft:jump.dynamic:" {}
```

# minecraft:jump.static
### bat.json
```json
"minecraft:jump.static:" {}
```

### bee.json
```json
"minecraft:jump.static:" {}
```

### blaze.json
```json
"minecraft:jump.static:" {}
```

### cat.json
```json
"minecraft:jump.static:" {}
```

### cave_spider.json
```json
"minecraft:jump.static:" {}
```

### chicken.json
```json
"minecraft:jump.static:" {}
```

### cow.json
```json
"minecraft:jump.static:" {}
```

### creeper.json
```json
"minecraft:jump.static:" {}
```

### dolphin.json
```json
"minecraft:jump.static:" {
    "jump_power": 0.6
}
```

### donkey.json
```json
"minecraft:jump.static:" {}
```

### drowned.json
```json
"minecraft:jump.static:" {}
```

### elder_guardian.json
```json
"minecraft:jump.static:" {}
```

### enderman.json
```json
"minecraft:jump.static:" {}
```

### endermite.json
```json
"minecraft:jump.static:" {}
```

### evocation_illager.json
```json
"minecraft:jump.static:" {}
```

### fox.json
```json
"minecraft:jump.static:" {}
```

### ghast.json
```json
"minecraft:jump.static:" {}
```

### guardian.json
```json
"minecraft:jump.static:" {}
```

### horse.json
```json
"minecraft:jump.static:" {}
```

### husk.json
```json
"minecraft:jump.static:" {}
```

### iron_golem.json
```json
"minecraft:jump.static:" {}
```

### llama.json
```json
"minecraft:jump.static:" {}
```

### magma_cube.json
```json
"minecraft:jump.static:" {}
```

### mooshroom.json
```json
"minecraft:jump.static:" {}
```

### mule.json
```json
"minecraft:jump.static:" {}
```

### ocelot.json
```json
"minecraft:jump.static:" {}
```

### panda.json
```json
"minecraft:jump.static:" {}
```

### parrot.json
```json
"minecraft:jump.static:" {}
```

### pig.json
```json
"minecraft:jump.static:" {}
```

### pillager.json
```json
"minecraft:jump.static:" {}
```

### polar_bear.json
```json
"minecraft:jump.static:" {}
```

### ravager.json
```json
"minecraft:jump.static:" {}
```

### sheep.json
```json
"minecraft:jump.static:" {}
```

### silverfish.json
```json
"minecraft:jump.static:" {}
```

### skeleton.json
```json
"minecraft:jump.static:" {}
```

### skeleton_horse.json
```json
"minecraft:jump.static:" {}
```

### slime.json
```json
"minecraft:jump.static:" {}
```

### snow_golem.json
```json
"minecraft:jump.static:" {}
```

### spider.json
```json
"minecraft:jump.static:" {}
```

### squid.json
```json
"minecraft:jump.static:" {}
```

### stray.json
```json
"minecraft:jump.static:" {}
```

### turtle.json
```json
"minecraft:jump.static:" {}
```

### vex.json
```json
"minecraft:jump.static:" {}
```

### villager.json
```json
"minecraft:jump.static:" {}
```

### villager_v2.json
```json
"minecraft:jump.static:" {}
```

### vindicator.json
```json
"minecraft:jump.static:" {}
```

### wandering_trader.json
```json
"minecraft:jump.static:" {}
```

### witch.json
```json
"minecraft:jump.static:" {}
```

### wither.json
```json
"minecraft:jump.static:" {}
```

### wither_skeleton.json
```json
"minecraft:jump.static:" {}
```

### wolf.json
```json
"minecraft:jump.static:" {}
```

### zombie.json
```json
"minecraft:jump.static:" {}
```

### zombie_horse.json
```json
"minecraft:jump.static:" {}
```

### zombie_pigman.json
```json
"minecraft:jump.static:" {}
```

### zombie_villager.json
```json
"minecraft:jump.static:" {}
```

### zombie_villager_v2.json
```json
"minecraft:jump.static:" {}
```

# minecraft:knockback_resistance
### ender_dragon.json
```json
"minecraft:knockback_resistance:" {
    "value": 100,
    "max": 100
}
```

### iron_golem.json
```json
"minecraft:knockback_resistance:" {
    "value": 1.0
}
```

### ravager.json
```json
"minecraft:knockback_resistance:" {
    "value": 0.5
}
```

# minecraft:leashable
### bee.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### boat.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cat.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### chicken.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### cow.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### dolphin.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### donkey.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### fox.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### horse.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### iron_golem.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### llama.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0,
    "can_be_stolen": true
}
```

### mooshroom.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### mule.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### ocelot.json
```json
"minecraft:leashable:" {
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

### parrot.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### pig.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### polar_bear.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### rabbit.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### sheep.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### skeleton_horse.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### snow_golem.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### squid.json
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

### wolf.json
```json
"minecraft:leashable:" {
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
```json
"minecraft:leashable:" {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

# minecraft:lookat
### enderman.json
```json
"minecraft:lookat:" {
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
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/armor_stand.json"
}
```

### blaze.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/blaze.json"
}
```

### boat.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/boat.json"
}
```

### cat.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/cat.json"
}
```

### cave_spider.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/spider.json"
}
```

### chicken.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/chicken.json"
}
```

### cow.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/cow.json"
}
```

### creeper.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/creeper.json"
}
```

### dolphin.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/dolphin.json"
}
```

### donkey.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/horse.json"
}
```

### drowned.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/drowned.json"
}
```

### elder_guardian.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/elder_guardian.json"
}
```

### enderman.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/enderman.json"
}
```

### evocation_illager.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/evocation_illager.json"
}
```

### fish.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/fish.json"
}
```

### fishing_hook.json
```json
"minecraft:loot:" {
    "table": "loot_tables/gameplay/fishing.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/gameplay/jungle_fishing.json"
}
```

### fox.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/fox.json"
}
```

### ghast.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/ghast.json"
}
```

### guardian.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/guardian.json"
}
```

### horse.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/horse.json"
}
```

### husk.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie.json"
}
```

### iron_golem.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/iron_golem.json"
}
```

### llama.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/llama.json"
}
```

### magma_cube.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/magma_cube.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/magma_cube.json"
}
```

### mooshroom.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/mooshroom.json"
}
```

### mule.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/horse.json"
}
```

### ocelot.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/ocelot.json"
}
```

### panda.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/panda.json"
}
```

### parrot.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/parrot.json"
}
```

### phantom.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/phantom.json"
}
```

### pig.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/pig.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/pig_saddled.json"
}
```

### pillager.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/pillager.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/pillager_raid.json"
}
```

### player.json
```json
"minecraft:loot:" {
    "table": "loot_tables/empty.json"
}
```

### polar_bear.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/polar_bear.json"
}
```

### pufferfish.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/pufferfish.json"
}
```

### rabbit.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/rabbit.json"
}
```

### ravager.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/ravager.json"
}
```

### salmon.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/salmon_normal.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/salmon_normal.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/salmon_large.json"
}
```

### sheep.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/sheep_sheared.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/sheep.json"
}
```

### shulker.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/shulker.json"
}
```

### silverfish.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/silverfish.json"
}
```

### skeleton.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/skeleton.json"
}
```

### skeleton_horse.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/skeleton_horse.json"
}
```

### slime.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/slime.json"
}
```

### snow_golem.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/snowman.json"
}
```

### spider.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/spider.json"
}
```

### squid.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/squid.json"
}
```

### stray.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/stray.json"
}
```

### tripod_camera.json
```json
"minecraft:loot:" {
    "table": "loot_tables/empty.json"
}
```

### tropicalfish.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/tropicalfish.json"
}
```

### turtle.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/sea_turtle.json"
}
```

### vindicator.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/vindication_illager.json"
}
```

```json
"minecraft:loot:" {
    "table": "loot_tables/entities/vindicator_raid.json"
}
```

### witch.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/witch.json"
}
```

### wither.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/wither_boss.json"
}
```

### wither_skeleton.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/wither_skeleton.json"
}
```

### wolf.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/wolf.json"
}
```

### zombie.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_horse.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie_horse.json"
}
```

### zombie_pigman.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie_pigman.json"
}
```

### zombie_villager.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie.json"
}
```

### zombie_villager_v2.json
```json
"minecraft:loot:" {
    "table": "loot_tables/entities/zombie.json"
}
```

# minecraft:managed_wandering_trader
### wandering_trader.json
```json
"minecraft:managed_wandering_trader:" {}
```

# minecraft:mark_variant
### bee.json
```json
"minecraft:mark_variant:" {
    "value": 1
}
```

### horse.json
```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

### llama.json
```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

### mooshroom.json
```json
"minecraft:mark_variant:" {
    "value": -1
}
```

```json
"minecraft:mark_variant:" {
    "value": -1
}
```

```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 6
}
```

```json
"minecraft:mark_variant:" {
    "value": 7
}
```

```json
"minecraft:mark_variant:" {
    "value": 8
}
```

```json
"minecraft:mark_variant:" {
    "value": 9
}
```

### tropicalfish.json
```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

### villager_v2.json
```json
"minecraft:mark_variant:" {
    "value": 0
}
```

```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 6
}
```

### zombie_villager_v2.json
```json
"minecraft:mark_variant:" {
    "value": 1
}
```

```json
"minecraft:mark_variant:" {
    "value": 2
}
```

```json
"minecraft:mark_variant:" {
    "value": 3
}
```

```json
"minecraft:mark_variant:" {
    "value": 4
}
```

```json
"minecraft:mark_variant:" {
    "value": 5
}
```

```json
"minecraft:mark_variant:" {
    "value": 6
}
```

# minecraft:mob_effect
### pufferfish.json
```json
"minecraft:mob_effect:" {
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
```json
"minecraft:movement:" {
    "value": 0.1
}
```

### bee.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### blaze.json
```json
"minecraft:movement:" {
    "value": 0.23
}
```

### cat.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### cave_spider.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### chicken.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### cow.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### creeper.json
```json
"minecraft:movement:" {
    "value": 0.2
}
```

### dolphin.json
```json
"minecraft:movement:" {
    "value": 0.1
}
```

### donkey.json
```json
"minecraft:movement:" {
    "value": 0.175
}
```

### drowned.json
```json
"minecraft:movement:" {
    "value": 0.23
}
```

```json
"minecraft:movement:" {
    "value": 0.25
}
```

### elder_guardian.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### enderman.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

```json
"minecraft:movement:" {
    "value": 0.45
}
```

### endermite.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### ender_dragon.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### evocation_illager.json
```json
"minecraft:movement:" {
    "value": 0.5
}
```

### fish.json
```json
"minecraft:movement:" {
    "value": 0.1
}
```

### fox.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### ghast.json
```json
"minecraft:movement:" {
    "value": 0.03
}
```

### guardian.json
```json
"minecraft:movement:" {
    "value": 0.12
}
```

### horse.json
```json
"minecraft:movement:" {
    "value": {
        "range_min": 0.1125,
        "range_max": 0.3375
    }
}
```

### husk.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

```json
"minecraft:movement:" {
    "value": 0.23
}
```

### iron_golem.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### llama.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### magma_cube.json
```json
"minecraft:movement:" {
    "value": 0.75
}
```

```json
"minecraft:movement:" {
    "value": 0.66
}
```

```json
"minecraft:movement:" {
    "value": 0.6
}
```

### mooshroom.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### mule.json
```json
"minecraft:movement:" {
    "value": 0.175
}
```

### ocelot.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### panda.json
```json
"minecraft:movement:" {
    "value": 0.15
}
```

```json
"minecraft:movement:" {
    "value": 0.07
}
```

### parrot.json
```json
"minecraft:movement:" {
    "value": 0.4
}
```

### phantom.json
```json
"minecraft:movement:" {
    "value": 1.8
}
```

### pig.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### pillager.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

### player.json
```json
"minecraft:movement:" {
    "value": 0.1
}
```

### polar_bear.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### pufferfish.json
```json
"minecraft:movement:" {
    "value": 0.13
}
```

### rabbit.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### ravager.json
```json
"minecraft:movement:" {
    "value": 0.0
}
```

```json
"minecraft:movement:" {
    "value": 0.3
}
```

### salmon.json
```json
"minecraft:movement:" {
    "value": 0.12
}
```

### sheep.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### shulker.json
```json
"minecraft:movement:" {
    "value": 0.0,
    "max": 0.0
}
```

### silverfish.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### skeleton.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### skeleton_horse.json
```json
"minecraft:movement:" {
    "value": 0.2
}
```

### slime.json
```json
"minecraft:movement:" {
    "value": 0.6
}
```

```json
"minecraft:movement:" {
    "value": 0.4
}
```

```json
"minecraft:movement:" {
    "value": 0.3
}
```

### snow_golem.json
```json
"minecraft:movement:" {
    "value": 0.2
}
```

### spider.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### squid.json
```json
"minecraft:movement:" {
    "value": 0.2
}
```

### stray.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### tropicalfish.json
```json
"minecraft:movement:" {
    "value": 0.12
}
```

### turtle.json
```json
"minecraft:movement:" {
    "value": 0.1
}
```

### vex.json
```json
"minecraft:movement:" {
    "value": 1.0
}
```

### villager.json
```json
"minecraft:movement:" {
    "value": 0.5
}
```

### villager_v2.json
```json
"minecraft:movement:" {
    "value": 0.5
}
```

### vindicator.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

### wandering_trader.json
```json
"minecraft:movement:" {
    "value": 0.5
}
```

### witch.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### wither.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### wither_skeleton.json
```json
"minecraft:movement:" {
    "value": 0.25
}
```

### wolf.json
```json
"minecraft:movement:" {
    "value": 0.3
}
```

### zombie.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

```json
"minecraft:movement:" {
    "value": 0.23
}
```

### zombie_horse.json
```json
"minecraft:movement:" {
    "value": 0.2
}
```

### zombie_pigman.json
```json
"minecraft:movement:" {
    "value": 0.23
}
```

### zombie_villager.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

```json
"minecraft:movement:" {
    "value": 0.23
}
```

### zombie_villager_v2.json
```json
"minecraft:movement:" {
    "value": 0.35
}
```

```json
"minecraft:movement:" {
    "value": 0.23
}
```

# minecraft:movement.amphibious
### turtle.json
```json
"minecraft:movement.amphibious:" {
    "max_turn": 5.0
}
```

# minecraft:movement.basic
### bat.json
```json
"minecraft:movement.basic:" {}
```

### blaze.json
```json
"minecraft:movement.basic:" {}
```

### cat.json
```json
"minecraft:movement.basic:" {}
```

### cave_spider.json
```json
"minecraft:movement.basic:" {}
```

### chicken.json
```json
"minecraft:movement.basic:" {}
```

### cow.json
```json
"minecraft:movement.basic:" {}
```

### creeper.json
```json
"minecraft:movement.basic:" {}
```

### donkey.json
```json
"minecraft:movement.basic:" {}
```

### enderman.json
```json
"minecraft:movement.basic:" {}
```

### endermite.json
```json
"minecraft:movement.basic:" {}
```

### evocation_illager.json
```json
"minecraft:movement.basic:" {}
```

### fox.json
```json
"minecraft:movement.basic:" {}
```

### horse.json
```json
"minecraft:movement.basic:" {}
```

### husk.json
```json
"minecraft:movement.basic:" {}
```

### iron_golem.json
```json
"minecraft:movement.basic:" {}
```

### llama.json
```json
"minecraft:movement.basic:" {}
```

### mooshroom.json
```json
"minecraft:movement.basic:" {}
```

### mule.json
```json
"minecraft:movement.basic:" {}
```

### ocelot.json
```json
"minecraft:movement.basic:" {}
```

### panda.json
```json
"minecraft:movement.basic:" {}
```

### pig.json
```json
"minecraft:movement.basic:" {}
```

### pillager.json
```json
"minecraft:movement.basic:" {}
```

### polar_bear.json
```json
"minecraft:movement.basic:" {}
```

### ravager.json
```json
"minecraft:movement.basic:" {}
```

### sheep.json
```json
"minecraft:movement.basic:" {}
```

### shulker.json
```json
"minecraft:movement.basic:" {}
```

### silverfish.json
```json
"minecraft:movement.basic:" {}
```

### skeleton.json
```json
"minecraft:movement.basic:" {}
```

### skeleton_horse.json
```json
"minecraft:movement.basic:" {}
```

### snow_golem.json
```json
"minecraft:movement.basic:" {}
```

### spider.json
```json
"minecraft:movement.basic:" {}
```

### squid.json
```json
"minecraft:movement.basic:" {}
```

### stray.json
```json
"minecraft:movement.basic:" {}
```

### vex.json
```json
"minecraft:movement.basic:" {}
```

### villager.json
```json
"minecraft:movement.basic:" {}
```

### villager_v2.json
```json
"minecraft:movement.basic:" {}
```

### vindicator.json
```json
"minecraft:movement.basic:" {}
```

### wandering_trader.json
```json
"minecraft:movement.basic:" {}
```

### witch.json
```json
"minecraft:movement.basic:" {}
```

### wither.json
```json
"minecraft:movement.basic:" {
    "max_turn": 180.0
}
```

### wither_skeleton.json
```json
"minecraft:movement.basic:" {}
```

### wolf.json
```json
"minecraft:movement.basic:" {}
```

### zombie.json
```json
"minecraft:movement.basic:" {}
```

### zombie_horse.json
```json
"minecraft:movement.basic:" {}
```

### zombie_pigman.json
```json
"minecraft:movement.basic:" {}
```

### zombie_villager.json
```json
"minecraft:movement.basic:" {}
```

### zombie_villager_v2.json
```json
"minecraft:movement.basic:" {}
```

# minecraft:movement.fly
### parrot.json
```json
"minecraft:movement.fly:" {}
```

# minecraft:movement.generic
### drowned.json
```json
"minecraft:movement.generic:" {}
```

# minecraft:movement.glide
### phantom.json
```json
"minecraft:movement.glide:" {
    "start_speed": 0.1,
    "speed_when_turning": 0.2
}
```

# minecraft:movement.hover
### bee.json
```json
"minecraft:movement.hover:" {}
```

# minecraft:movement.jump
### magma_cube.json
```json
"minecraft:movement.jump:" {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```json
"minecraft:movement.jump:" {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```json
"minecraft:movement.jump:" {
    "jump_delay": [
        0.667,
        2.0
    ]
}
```

### slime.json
```json
"minecraft:movement.jump:" {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```json
"minecraft:movement.jump:" {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```json
"minecraft:movement.jump:" {
    "jump_delay": [
        0.16,
        0.5
    ]
}
```

# minecraft:movement.skip
### rabbit.json
```json
"minecraft:movement.skip:" {}
```

# minecraft:movement.sway
### elder_guardian.json
```json
"minecraft:movement.sway:" {}
```

### fish.json
```json
"minecraft:movement.sway:" {
    "sway_amplitude": 0.0
}
```

### guardian.json
```json
"minecraft:movement.sway:" {}
```

### pufferfish.json
```json
"minecraft:movement.sway:" {
    "sway_amplitude": 0.0
}
```

### salmon.json
```json
"minecraft:movement.sway:" {
    "sway_amplitude": 0.0
}
```

### tropicalfish.json
```json
"minecraft:movement.sway:" {
    "sway_amplitude": 0.0
}
```

# minecraft:nameable
### armor_stand.json
```json
"minecraft:nameable:" {}
```

### bat.json
```json
"minecraft:nameable:" {}
```

### bee.json
```json
"minecraft:nameable:" {}
```

### blaze.json
```json
"minecraft:nameable:" {}
```

### cat.json
```json
"minecraft:nameable:" {}
```

### cave_spider.json
```json
"minecraft:nameable:" {}
```

### chicken.json
```json
"minecraft:nameable:" {}
```

### cow.json
```json
"minecraft:nameable:" {}
```

### creeper.json
```json
"minecraft:nameable:" {}
```

### dolphin.json
```json
"minecraft:nameable:" {}
```

### donkey.json
```json
"minecraft:nameable:" {}
```

### drowned.json
```json
"minecraft:nameable:" {}
```

### elder_guardian.json
```json
"minecraft:nameable:" {}
```

### enderman.json
```json
"minecraft:nameable:" {}
```

### endermite.json
```json
"minecraft:nameable:" {}
```

### evocation_illager.json
```json
"minecraft:nameable:" {}
```

### fish.json
```json
"minecraft:nameable:" {}
```

### fox.json
```json
"minecraft:nameable:" {}
```

### ghast.json
```json
"minecraft:nameable:" {}
```

### guardian.json
```json
"minecraft:nameable:" {}
```

### horse.json
```json
"minecraft:nameable:" {}
```

### husk.json
```json
"minecraft:nameable:" {}
```

### iron_golem.json
```json
"minecraft:nameable:" {}
```

### llama.json
```json
"minecraft:nameable:" {}
```

### magma_cube.json
```json
"minecraft:nameable:" {}
```

### mooshroom.json
```json
"minecraft:nameable:" {}
```

### mule.json
```json
"minecraft:nameable:" {}
```

### ocelot.json
```json
"minecraft:nameable:" {}
```

### panda.json
```json
"minecraft:nameable:" {}
```

### parrot.json
```json
"minecraft:nameable:" {}
```

### phantom.json
```json
"minecraft:nameable:" {}
```

### pig.json
```json
"minecraft:nameable:" {}
```

### pillager.json
```json
"minecraft:nameable:" {}
```

### player.json
```json
"minecraft:nameable:" {
    "always_show": true,
    "allow_name_tag_renaming": false
}
```

### polar_bear.json
```json
"minecraft:nameable:" {}
```

### pufferfish.json
```json
"minecraft:nameable:" {}
```

### rabbit.json
```json
"minecraft:nameable:" {}
```

### ravager.json
```json
"minecraft:nameable:" {}
```

### salmon.json
```json
"minecraft:nameable:" {}
```

### sheep.json
```json
"minecraft:nameable:" {}
```

### shulker.json
```json
"minecraft:nameable:" {}
```

### silverfish.json
```json
"minecraft:nameable:" {}
```

### skeleton.json
```json
"minecraft:nameable:" {}
```

### skeleton_horse.json
```json
"minecraft:nameable:" {}
```

### slime.json
```json
"minecraft:nameable:" {}
```

### snow_golem.json
```json
"minecraft:nameable:" {}
```

### spider.json
```json
"minecraft:nameable:" {}
```

### squid.json
```json
"minecraft:nameable:" {}
```

### stray.json
```json
"minecraft:nameable:" {}
```

### tropicalfish.json
```json
"minecraft:nameable:" {}
```

### turtle.json
```json
"minecraft:nameable:" {}
```

### vex.json
```json
"minecraft:nameable:" {}
```

### villager.json
```json
"minecraft:nameable:" {}
```

### villager_v2.json
```json
"minecraft:nameable:" {}
```

### vindicator.json
```json
"minecraft:nameable:" {
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
```json
"minecraft:nameable:" {}
```

### wither.json
```json
"minecraft:nameable:" {}
```

### wither_skeleton.json
```json
"minecraft:nameable:" {}
```

### wolf.json
```json
"minecraft:nameable:" {}
```

### zombie.json
```json
"minecraft:nameable:" {}
```

### zombie_horse.json
```json
"minecraft:nameable:" {}
```

### zombie_pigman.json
```json
"minecraft:nameable:" {}
```

### zombie_villager.json
```json
"minecraft:nameable:" {}
```

### zombie_villager_v2.json
```json
"minecraft:nameable:" {}
```

# minecraft:navigation.climb
### cave_spider.json
```json
"minecraft:navigation.climb:" {
    "can_path_over_water": true
}
```

### spider.json
```json
"minecraft:navigation.climb:" {
    "can_path_over_water": true
}
```

# minecraft:navigation.float
### bat.json
```json
"minecraft:navigation.float:" {
    "can_path_over_water": true
}
```

### ghast.json
```json
"minecraft:navigation.float:" {
    "can_path_over_water": true
}
```

# minecraft:navigation.fly
### parrot.json
```json
"minecraft:navigation.fly:" {
    "can_path_over_water": true
}
```

# minecraft:navigation.generic
### dolphin.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

### drowned.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": true,
    "can_walk": true,
    "avoid_sun": true
}
```

```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

### elder_guardian.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### fish.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### guardian.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

### pufferfish.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### salmon.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### tropicalfish.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": false,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": false,
    "can_sink": false
}
```

### turtle.json
```json
"minecraft:navigation.generic:" {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": true,
    "can_sink": false,
    "avoid_damage_blocks": true
}
```

# minecraft:navigation.hover
### bee.json
```json
"minecraft:navigation.hover:" {
    "can_path_over_water": true,
    "can_sink": false,
    "can_path_from_air": true,
    "avoid_water": true,
    "avoid_damage_blocks": true,
    "avoid_sun": false
}
```

# minecraft:navigation.walk
### blaze.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### cat.json
```json
"minecraft:navigation.walk:" {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### chicken.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### cow.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### creeper.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### donkey.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### enderman.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": false,
    "avoid_water": true
}
```

### endermite.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### evocation_illager.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### fox.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### horse.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### husk.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_portals": false
}
```

### iron_golem.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": false,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### llama.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### magma_cube.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### mooshroom.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### mule.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### ocelot.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### panda.json
```json
"minecraft:navigation.walk:" {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### pig.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

### pillager.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### polar_bear.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### rabbit.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### ravager.json
```json
"minecraft:navigation.walk:" {
    "avoid_damage_blocks": true,
    "can_path_over_water": true,
    "can_sink": false
}
```

### sheep.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### shulker.json
```json
"minecraft:navigation.walk:" {}
```

### silverfish.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### skeleton.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### skeleton_horse.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "avoid_water": true
}
```

### slime.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### snow_golem.json
```json
"minecraft:navigation.walk:" {
    "avoid_water": true
}
```

### squid.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "can_sink": false
}
```

### stray.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### vex.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

### villager.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "can_walk": true,
    "avoid_water": true
}
```

### villager_v2.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### vindicator.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true
}
```

```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_break_doors": true
}
```

### wandering_trader.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true
}
```

### witch.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": false
}
```

### wither.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_water": true
}
```

### wither_skeleton.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

### wolf.json
```json
"minecraft:navigation.walk:" {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

### zombie.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_walk": true,
    "can_break_doors": true
}
```

### zombie_horse.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "avoid_water": true
}
```

### zombie_pigman.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_portals": true
}
```

### zombie_villager.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_break_doors": true,
    "avoid_sun": false
}
```

```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

### zombie_villager_v2.json
```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_sun": false
}
```

```json
"minecraft:navigation.walk:" {
    "is_amphibious": true,
    "can_pass_doors": true,
    "can_open_doors": true,
    "avoid_water": true,
    "avoid_sun": true
}
```

# minecraft:on_death
### ender_dragon.json
```json
"minecraft:on_death:" {
    "event": "minecraft:start_death",
    "target": "self"
}
```

# minecraft:on_friendly_anger
### llama.json
```json
"minecraft:on_friendly_anger:" {
    "event": "minecraft:defend_wandering_trader",
    "target": "self"
}
```

### panda.json
```json
"minecraft:on_friendly_anger:" {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### pillager.json
```json
"minecraft:on_friendly_anger:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```json
"minecraft:on_friendly_anger:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

### polar_bear.json
```json
"minecraft:on_friendly_anger:" {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

# minecraft:on_hurt
### ender_crystal.json
```json
"minecraft:on_hurt:" {
    "event": "minecraft:crystal_explode",
    "target": "self"
}
```

### pillager.json
```json
"minecraft:on_hurt:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```json
"minecraft:on_hurt:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

# minecraft:on_hurt_by_player
```json
"minecraft:on_hurt_by_player:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

```json
"minecraft:on_hurt_by_player:" {
    "event": "minecraft:synchronized_ranged_mode",
    "target": "self"
}
```

# minecraft:on_start_landing
### ender_dragon.json
```json
"minecraft:on_start_landing:" {
    "event": "minecraft:start_land",
    "target": "self"
}
```

# minecraft:on_start_takeoff
```json
"minecraft:on_start_takeoff:" {
    "event": "minecraft:start_fly",
    "target": "self"
}
```

# minecraft:on_target_acquired
### bee.json
```json
"minecraft:on_target_acquired:" {
    "event": "attacked",
    "target": "self"
}
```

### cave_spider.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry"
}
```

### dolphin.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired:" {}
```

### drowned.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:has_target",
    "target": "self"
}
```

### enderman.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### llama.json
```json
"minecraft:on_target_acquired:" {
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
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### panda.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired:" {}
```

### polar_bear.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:on_scared",
    "target": "self"
}
```

```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

### silverfish.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### slime.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_aggressive",
    "target": "self"
}
```

### spider.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry"
}
```

```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry"
}
```

### vindicator.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_aggro",
    "target": "self"
}
```

### wolf.json
```json
"minecraft:on_target_acquired:" {}
```

```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

### zombie_pigman.json
```json
"minecraft:on_target_acquired:" {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

# minecraft:on_target_escape
### creeper.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:stop_exploding",
    "target": "self"
}
```

```json
"minecraft:on_target_escape:" {}
```

```json
"minecraft:on_target_escape:" {}
```

### dolphin.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### drowned.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:lost_target",
    "target": "self"
}
```

### llama.json
```json
"minecraft:on_target_escape:" {
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
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### panda.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

### pillager.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:calm",
    "target": "self"
}
```

```json
"minecraft:on_target_escape:" {
    "event": "minecraft:calm",
    "target": "self"
}
```

### slime.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

### vindicator.json
```json
"minecraft:on_target_escape:" {
    "event": "minecraft:stop_aggro",
    "target": "self"
}
```

# minecraft:on_wake_with_owner
### cat.json
```json
"minecraft:on_wake_with_owner:" {
    "event": "minecraft:pet_slept_with_owner",
    "target": "self"
}
```

# minecraft:peek
### shulker.json
```json
"minecraft:peek:" {
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
```json
"minecraft:persistent:" {}
```

### ender_dragon.json
```json
"minecraft:persistent:" {}
```

### evocation_illager.json
```json
"minecraft:persistent:" {}
```

### iron_golem.json
```json
"minecraft:persistent:" {}
```

### snow_golem.json
```json
"minecraft:persistent:" {}
```

### villager.json
```json
"minecraft:persistent:" {}
```

### villager_v2.json
```json
"minecraft:persistent:" {}
```

### wither.json
```json
"minecraft:persistent:" {}
```

# minecraft:physics
### area_effect_cloud.json
```json
"minecraft:physics:" {
    "has_collision": false
}
```

### armor_stand.json
```json
"minecraft:physics:" {}
```

### arrow.json
```json
"minecraft:physics:" {}
```

### bat.json
```json
"minecraft:physics:" {}
```

### bee.json
```json
"minecraft:physics:" {}
```

### blaze.json
```json
"minecraft:physics:" {}
```

### boat.json
```json
"minecraft:physics:" {}
```

### cat.json
```json
"minecraft:physics:" {}
```

### cave_spider.json
```json
"minecraft:physics:" {}
```

### chest_minecart.json
```json
"minecraft:physics:" {}
```

### chicken.json
```json
"minecraft:physics:" {}
```

### command_block_minecart.json
```json
"minecraft:physics:" {}
```

### cow.json
```json
"minecraft:physics:" {}
```

### creeper.json
```json
"minecraft:physics:" {}
```

### dolphin.json
```json
"minecraft:physics:" {}
```

### donkey.json
```json
"minecraft:physics:" {}
```

### drowned.json
```json
"minecraft:physics:" {}
```

### egg.json
```json
"minecraft:physics:" {}
```

### elder_guardian.json
```json
"minecraft:physics:" {}
```

### enderman.json
```json
"minecraft:physics:" {}
```

### endermite.json
```json
"minecraft:physics:" {}
```

### ender_crystal.json
```json
"minecraft:physics:" {}
```

### ender_dragon.json
```json
"minecraft:physics:" {
    "has_gravity": false,
    "has_collision": false
}
```

### ender_pearl.json
```json
"minecraft:physics:" {}
```

### evocation_illager.json
```json
"minecraft:physics:" {}
```

### eye_of_ender_signal.json
```json
"minecraft:physics:" {}
```

### fireball.json
```json
"minecraft:physics:" {}
```

### fireworks_rocket.json
```json
"minecraft:physics:" {}
```

### fish.json
```json
"minecraft:physics:" {
    "has_gravity": false
}
```

### fishing_hook.json
```json
"minecraft:physics:" {}
```

### fox.json
```json
"minecraft:physics:" {}
```

### ghast.json
```json
"minecraft:physics:" {}
```

### guardian.json
```json
"minecraft:physics:" {}
```

### hopper_minecart.json
```json
"minecraft:physics:" {}
```

### horse.json
```json
"minecraft:physics:" {}
```

### husk.json
```json
"minecraft:physics:" {}
```

### iron_golem.json
```json
"minecraft:physics:" {}
```

### lingering_potion.json
```json
"minecraft:physics:" {}
```

### llama.json
```json
"minecraft:physics:" {}
```

### llama_spit.json
```json
"minecraft:physics:" {}
```

### magma_cube.json
```json
"minecraft:physics:" {}
```

### minecart.json
```json
"minecraft:physics:" {}
```

### mooshroom.json
```json
"minecraft:physics:" {}
```

### mule.json
```json
"minecraft:physics:" {}
```

### ocelot.json
```json
"minecraft:physics:" {}
```

### panda.json
```json
"minecraft:physics:" {}
```

### parrot.json
```json
"minecraft:physics:" {}
```

### phantom.json
```json
"minecraft:physics:" {
    "has_gravity": false
}
```

### pig.json
```json
"minecraft:physics:" {}
```

### pillager.json
```json
"minecraft:physics:" {}
```

### player.json
```json
"minecraft:physics:" {}
```

### polar_bear.json
```json
"minecraft:physics:" {}
```

### pufferfish.json
```json
"minecraft:physics:" {
    "has_gravity": false
}
```

### rabbit.json
```json
"minecraft:physics:" {}
```

### ravager.json
```json
"minecraft:physics:" {}
```

### salmon.json
```json
"minecraft:physics:" {
    "has_gravity": false
}
```

### sheep.json
```json
"minecraft:physics:" {}
```

### shulker.json
```json
"minecraft:physics:" {}
```

### shulker_bullet.json
```json
"minecraft:physics:" {
    "has_collision": false
}
```

### silverfish.json
```json
"minecraft:physics:" {}
```

### skeleton.json
```json
"minecraft:physics:" {}
```

### skeleton_horse.json
```json
"minecraft:physics:" {}
```

### slime.json
```json
"minecraft:physics:" {}
```

### small_fireball.json
```json
"minecraft:physics:" {}
```

### snowball.json
```json
"minecraft:physics:" {}
```

### snow_golem.json
```json
"minecraft:physics:" {}
```

### spider.json
```json
"minecraft:physics:" {}
```

### splash_potion.json
```json
"minecraft:physics:" {}
```

### squid.json
```json
"minecraft:physics:" {}
```

### stray.json
```json
"minecraft:physics:" {}
```

### thrown_trident.json
```json
"minecraft:physics:" {}
```

### tnt.json
```json
"minecraft:physics:" {}
```

### tnt_minecart.json
```json
"minecraft:physics:" {}
```

### tripod_camera.json
```json
"minecraft:physics:" {}
```

### tropicalfish.json
```json
"minecraft:physics:" {
    "has_gravity": false
}
```

### turtle.json
```json
"minecraft:physics:" {}
```

### vex.json
```json
"minecraft:physics:" {
    "has_gravity": false,
    "has_collision": false
}
```

### villager.json
```json
"minecraft:physics:" {}
```

### villager_v2.json
```json
"minecraft:physics:" {}
```

### vindicator.json
```json
"minecraft:physics:" {}
```

### wandering_trader.json
```json
"minecraft:physics:" {}
```

### witch.json
```json
"minecraft:physics:" {}
```

### wither.json
```json
"minecraft:physics:" {}
```

### wither_skeleton.json
```json
"minecraft:physics:" {}
```

### wither_skull.json
```json
"minecraft:physics:" {}
```

### wither_skull_dangerous.json
```json
"minecraft:physics:" {}
```

### wolf.json
```json
"minecraft:physics:" {}
```

### xp_bottle.json
```json
"minecraft:physics:" {}
```

### zombie.json
```json
"minecraft:physics:" {}
```

### zombie_horse.json
```json
"minecraft:physics:" {}
```

### zombie_pigman.json
```json
"minecraft:physics:" {}
```

### zombie_villager.json
```json
"minecraft:physics:" {}
```

### zombie_villager_v2.json
```json
"minecraft:physics:" {}
```

# minecraft:player.exhaustion
### player.json
```json
"minecraft:player.exhaustion:" {
    "value": 0,
    "max": 4
}
```

# minecraft:player.experience
```json
"minecraft:player.experience:" {
    "value": 0,
    "max": 1
}
```

# minecraft:player.level
```json
"minecraft:player.level:" {
    "value": 0,
    "max": 24791
}
```

# minecraft:player.saturation
```json
"minecraft:player.saturation:" {
    "value": 20
}
```

# minecraft:preferred_path
### iron_golem.json
```json
"minecraft:preferred_path:" {
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
```json
"minecraft:preferred_path:" {
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

```json
"minecraft:preferred_path:" {
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
```json
"minecraft:projectile:" {
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

```json
"minecraft:projectile:" {
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

```json
"minecraft:projectile:" {
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

```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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

```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
    "on_hit": {
        "stick_in_ground": {}
    }
}
```

### lingering_potion.json
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:projectile:" {
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
```json
"minecraft:pushable:" {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### arrow.json
```json
"minecraft:pushable:" {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### bee.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### blaze.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### boat.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cat.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cave_spider.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chest_minecart.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### chicken.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### command_block_minecart.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### cow.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### creeper.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### dolphin.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### donkey.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### drowned.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### egg.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### elder_guardian.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### enderman.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### endermite.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_crystal.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ender_pearl.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### evocation_illager.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### eye_of_ender_signal.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireball.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fireworks_rocket.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fish.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### fishing_hook.json
```json
"minecraft:pushable:" {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### fox.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ghast.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### guardian.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### hopper_minecart.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### horse.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### husk.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### iron_golem.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### lingering_potion.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### llama_spit.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### magma_cube.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### minecart.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mooshroom.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### mule.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ocelot.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### panda.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### parrot.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### phantom.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pig.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pillager.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### player.json
```json
"minecraft:pushable:" {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### polar_bear.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### pufferfish.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### rabbit.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### ravager.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### salmon.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### sheep.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### silverfish.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### skeleton_horse.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### slime.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### small_fireball.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snowball.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### snow_golem.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### spider.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### splash_potion.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### squid.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### stray.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### thrown_trident.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tnt.json
```json
"minecraft:pushable:" {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

### tnt_minecart.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### tropicalfish.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### turtle.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### villager_v2.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### vindicator.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wandering_trader.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### witch.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skeleton.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wither_skull_dangerous.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### wolf.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### xp_bottle.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_horse.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_pigman.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

### zombie_villager_v2.json
```json
"minecraft:pushable:" {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

# minecraft:raid_trigger
### player.json
```json
"minecraft:raid_trigger:" {
    "triggered_event": {
        "event": "minecraft:remove_raid_trigger",
        "target": "self"
    }
}
```

# minecraft:rail_movement
### chest_minecart.json
```json
"minecraft:rail_movement:" {}
```

### command_block_minecart.json
```json
"minecraft:rail_movement:" {}
```

### hopper_minecart.json
```json
"minecraft:rail_movement:" {}
```

### minecart.json
```json
"minecraft:rail_movement:" {}
```

### tnt_minecart.json
```json
"minecraft:rail_movement:" {}
```

# minecraft:rail_sensor
### command_block_minecart.json
```json
"minecraft:rail_sensor:" {
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

```json
"minecraft:rail_sensor:" {
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
```json
"minecraft:rail_sensor:" {
    "on_activate": {
        "event": "minecraft:hopper_deactivate"
    }
}
```

```json
"minecraft:rail_sensor:" {
    "on_deactivate": {
        "event": "minecraft:hopper_activate"
    }
}
```

### minecart.json
```json
"minecraft:rail_sensor:" {
    "eject_on_activate": true
}
```

### tnt_minecart.json
```json
"minecraft:rail_sensor:" {}
```

```json
"minecraft:rail_sensor:" {}
```

```json
"minecraft:rail_sensor:" {
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
```json
"minecraft:ravager_blocked:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {}
```

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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

```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:rideable:" {
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
```json
"minecraft:scaffolding_climber:" {}
```

# minecraft:scale
### bee.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### cat.json
```json
"minecraft:scale:" {
    "value": 0.4
}
```

```json
"minecraft:scale:" {
    "value": 0.8
}
```

### chicken.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### cow.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### dolphin.json
```json
"minecraft:scale:" {
    "value": 0.65
}
```

### drowned.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### fish.json
```json
"minecraft:scale:" {
    "value": 1.0
}
```

### fox.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### husk.json
```json
"minecraft:scale:" {
    "value": 0.53125
}
```

```json
"minecraft:scale:" {
    "value": 1.0625
}
```

### llama.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### mooshroom.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### ocelot.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

```json
"minecraft:scale:" {
    "value": 1
}
```

### panda.json
```json
"minecraft:scale:" {
    "value": 1.0
}
```

```json
"minecraft:scale:" {
    "value": 0.4
}
```

### pig.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### polar_bear.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### pufferfish.json
```json
"minecraft:scale:" {
    "value": 1.2
}
```

### rabbit.json
```json
"minecraft:scale:" {
    "value": 0.4
}
```

```json
"minecraft:scale:" {
    "value": 0.6
}
```

### salmon.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

```json
"minecraft:scale:" {
    "value": 1
}
```

```json
"minecraft:scale:" {
    "value": 1.5
}
```

### sheep.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### squid.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### tropicalfish.json
```json
"minecraft:scale:" {
    "value": 1.3
}
```

### turtle.json
```json
"minecraft:scale:" {
    "value": 0.16
}
```

### villager.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### villager_v2.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### wither_skeleton.json
```json
"minecraft:scale:" {
    "value": 1.2
}
```

### wolf.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### zombie.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### zombie_pigman.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### zombie_villager.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

### zombie_villager_v2.json
```json
"minecraft:scale:" {
    "value": 0.5
}
```

# minecraft:scale_by_age
### donkey.json
```json
"minecraft:scale_by_age:" {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### horse.json
```json
"minecraft:scale_by_age:" {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### mule.json
```json
"minecraft:scale_by_age:" {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### skeleton_horse.json
```json
"minecraft:scale_by_age:" {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

### zombie_horse.json
```json
"minecraft:scale_by_age:" {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

# minecraft:scheduler
### fox.json
```json
"minecraft:scheduler:" {
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
```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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

```json
"minecraft:scheduler:" {
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
```json
"minecraft:shareables:" {
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
```json
"minecraft:shareables:" {
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

```json
"minecraft:shareables:" {
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
```json
"minecraft:shareables:" {
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

```json
"minecraft:shareables:" {
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

```json
"minecraft:shareables:" {
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
```json
"minecraft:shooter:" {
    "type": "smallfireball",
    "def": "minecraft:small_fireball"
}
```

### drowned.json
```json
"minecraft:shooter:" {
    "def": "minecraft:thrown_trident"
}
```

### ender_dragon.json
```json
"minecraft:shooter:" {
    "type": "dragonfireball",
    "def": "minecraft:dragon_fireball"
}
```

### ghast.json
```json
"minecraft:shooter:" {
    "type": "largefireball",
    "def": "minecraft:fireball"
}
```

### llama.json
```json
"minecraft:shooter:" {
    "type": "llamaspit",
    "def": "minecraft:llama_spit"
}
```

### pillager.json
```json
"minecraft:shooter:" {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

### shulker.json
```json
"minecraft:shooter:" {
    "type": "ShulkerBullet",
    "def": "minecraft:shulker_bullet"
}
```

### skeleton.json
```json
"minecraft:shooter:" {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

```json
"minecraft:shooter:" {
    "type": "Arrow",
    "def": "minecraft:arrow"
}
```

### snow_golem.json
```json
"minecraft:shooter:" {
    "def": "minecraft:snowball"
}
```

### stray.json
```json
"minecraft:shooter:" {
    "type": "Arrow",
    "def": "minecraft:arrow",
    "aux_val": 19
}
```

```json
"minecraft:shooter:" {
    "type": "Arrow",
    "def": "minecraft:arrow",
    "aux_val": 19
}
```

# minecraft:sittable
### cat.json
```json
"minecraft:sittable:" {}
```

### ocelot.json
```json
"minecraft:sittable:" {}
```

### parrot.json
```json
"minecraft:sittable:" {}
```

### wolf.json
```json
"minecraft:sittable:" {}
```

# minecraft:skin_id
### villager_v2.json
```json
"minecraft:skin_id:" {
    "value": 0
}
```

```json
"minecraft:skin_id:" {
    "value": 1
}
```

```json
"minecraft:skin_id:" {
    "value": 2
}
```

```json
"minecraft:skin_id:" {
    "value": 3
}
```

```json
"minecraft:skin_id:" {
    "value": 4
}
```

```json
"minecraft:skin_id:" {
    "value": 5
}
```

### zombie_villager_v2.json
```json
"minecraft:skin_id:" {
    "value": 0
}
```

```json
"minecraft:skin_id:" {
    "value": 1
}
```

```json
"minecraft:skin_id:" {
    "value": 2
}
```

```json
"minecraft:skin_id:" {
    "value": 3
}
```

```json
"minecraft:skin_id:" {
    "value": 4
}
```

```json
"minecraft:skin_id:" {
    "value": 5
}
```

# minecraft:spawn_entity
### chicken.json
```json
"minecraft:spawn_entity:" {
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
```json
"minecraft:spawn_entity:" [
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
```json
"minecraft:spell_effects:" {
    "add_effects": [
        {
            "effect": "bad_omen",
            "duration": 6000,
            "display_on_screen_animation": true
        }
    ]
}
```

```json
"minecraft:spell_effects:" {}
```

```json
"minecraft:spell_effects:" {
    "remove_effects": "bad_omen"
}
```

### zombie_villager.json
```json
"minecraft:spell_effects:" {
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
```json
"minecraft:spell_effects:" {
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
```json
"minecraft:strength:" {
    "value": 1,
    "max": 5
}
```

```json
"minecraft:strength:" {
    "value": 2,
    "max": 5
}
```

```json
"minecraft:strength:" {
    "value": 3,
    "max": 5
}
```

```json
"minecraft:strength:" {
    "value": 4,
    "max": 5
}
```

```json
"minecraft:strength:" {
    "value": 5,
    "max": 5
}
```

# minecraft:tameable
### cat.json
```json
"minecraft:tameable:" {
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
```json
"minecraft:tameable:" {
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
```json
"minecraft:tameable:" {
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
```json
"minecraft:tamemount:" {
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
```json
"minecraft:tamemount:" {
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
```json
"minecraft:tamemount:" {
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
```json
"minecraft:tamemount:" {
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
```json
"minecraft:target_nearby_sensor:" {
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

```json
"minecraft:target_nearby_sensor:" {}
```

```json
"minecraft:target_nearby_sensor:" {}
```

### drowned.json
```json
"minecraft:target_nearby_sensor:" {
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
```json
"minecraft:target_nearby_sensor:" {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

```json
"minecraft:target_nearby_sensor:" {
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
```json
"minecraft:teleport:" {
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
### bee.json
```json
"minecraft:timer:" {
    "looping": false,
    "time": [
        20,
        50
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "stop_panicking_after_fire",
        "target": "self"
    }
}
```

```json
"minecraft:timer:" {
    "looping": false,
    "time": [
        10,
        60
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "perish_event",
        "target": "self"
    }
}
```

```json
"minecraft:timer:" {
    "looping": true,
    "time": 5,
    "time_down_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

```json
"minecraft:timer:" {
    "looping": true,
    "time": 180,
    "time_down_event": {
        "event": "find_flower_timeout"
    }
}
```

```json
"minecraft:timer:" {
    "looping": false,
    "time": 180,
    "time_down_event": {
        "event": "find_hive_timeout",
        "target": "self"
    }
}
```

```json
"minecraft:timer:" {
    "looping": false,
    "time": [
        5,
        20
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "find_hive_event",
        "target": "self"
    }
}
```

### dolphin.json
```json
"minecraft:timer:" {
    "looping": false,
    "time": 20,
    "time_down_event": {
        "event": "minecraft:dried_out"
    }
}
```

### guardian.json
```json
"minecraft:timer:" {
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
```json
"minecraft:timer:" {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_zombie"
    }
}
```

### player.json
```json
"minecraft:timer:" {
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
```json
"minecraft:timer:" {
    "looping": false,
    "time": 0.05,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_full_puff"
    }
}
```

```json
"minecraft:timer:" {
    "looping": false,
    "time": 1,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_normal_puff"
    }
}
```

```json
"minecraft:timer:" {
    "looping": false,
    "time": 10,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:on_deflate"
    }
}
```

### ravager.json
```json
"minecraft:timer:" {
    "looping": false,
    "time": 2,
    "time_down_event": {
        "event": "minecraft:start_roar"
    }
}
```

### wandering_trader.json
```json
"minecraft:timer:" {
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
```json
"minecraft:timer:" {
    "looping": false,
    "time": 30,
    "time_down_event": {
        "event": "minecraft:convert_to_drowned"
    }
}
```

# minecraft:trade_resupply
### villager_v2.json
```json
"minecraft:trade_resupply:" {}
```

# minecraft:trade_table
### villager.json
```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.farmer",
    "table": "trading/farmer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.fisherman",
    "table": "trading/fisherman_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.shepherd",
    "table": "trading/shepherd_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.fletcher",
    "table": "trading/fletcher_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.librarian",
    "table": "trading/librarian_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.cartographer",
    "table": "trading/cartographer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.cleric",
    "table": "trading/cleric_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.armor",
    "table": "trading/armorer_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.weapon",
    "table": "trading/weapon_smith_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.tool",
    "table": "trading/tool_smith_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.butcher",
    "table": "trading/butcher_trades.json",
    "convert_trades_economy": true
}
```

```json
"minecraft:trade_table:" {
    "display_name": "entity.villager.leather",
    "table": "trading/leather_worker_trades.json",
    "convert_trades_economy": true
}
```

# minecraft:trail
### snow_golem.json
```json
"minecraft:trail:" {
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
```json
"minecraft:transformation:" {
    "into": "minecraft:zombie<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```json
"minecraft:transformation:" {
    "into": "minecraft:zombie<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### mooshroom.json
```json
"minecraft:transformation:" {
    "into": "minecraft:cow"
}
```

### pig.json
```json
"minecraft:transformation:" {
    "into": "minecraft:pig_zombie",
    "delay": 0.5
}
```

### stray.json
```json
"minecraft:transformation:" {
    "into": "minecraft:skeleton",
    "delay": 0.5
}
```

### villager.json
```json
"minecraft:transformation:" {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```json
"minecraft:transformation:" {
    "into": "minecraft:villager_v2",
    "keep_level": true
}
```

```json
"minecraft:transformation:" {
    "into": "minecraft:zombie_villager"
}
```

### villager_v2.json
```json
"minecraft:transformation:" {
    "into": "minecraft:witch",
    "delay": 0.5
}
```

```json
"minecraft:transformation:" {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": true
}
```

### zombie.json
```json
"minecraft:transformation:" {
    "into": "minecraft:drowned<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```json
"minecraft:transformation:" {
    "into": "minecraft:drowned<minecraft:as_baby>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

### zombie_villager.json
```json
"minecraft:transformation:" {
    "into": "minecraft:zombie_villager_v2",
    "keep_level": false
}
```

```json
"minecraft:transformation:" {
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
```json
"minecraft:transformation:" {
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
```json
"minecraft:trust:" {}
```

# minecraft:trusting
### ocelot.json
```json
"minecraft:trusting:" {
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
```json
"minecraft:type_family:" {
    "family": [
        "armor_stand",
        "inanimate",
        "mob"
    ]
}
```

### bat.json
```json
"minecraft:type_family:" {
    "family": [
        "bat",
        "mob"
    ]
}
```

### bee.json
```json
"minecraft:type_family:" {
    "family": [
        "bee",
        "mob",
        "arthropod"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "bee",
        "mob",
        "arthropod",
        "pacified"
    ]
}
```

### blaze.json
```json
"minecraft:type_family:" {
    "family": [
        "blaze",
        "monster",
        "mob"
    ]
}
```

### boat.json
```json
"minecraft:type_family:" {
    "family": [
        "boat",
        "inanimate"
    ]
}
```

### cat.json
```json
"minecraft:type_family:" {
    "family": [
        "cat",
        "mob"
    ]
}
```

### cave_spider.json
```json
"minecraft:type_family:" {
    "family": [
        "cavespider",
        "monster",
        "arthropod",
        "mob"
    ]
}
```

### chest_minecart.json
```json
"minecraft:type_family:" {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### chicken.json
```json
"minecraft:type_family:" {
    "family": [
        "chicken",
        "mob"
    ]
}
```

### command_block_minecart.json
```json
"minecraft:type_family:" {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### cow.json
```json
"minecraft:type_family:" {
    "family": [
        "cow",
        "mob"
    ]
}
```

### creeper.json
```json
"minecraft:type_family:" {
    "family": [
        "creeper",
        "monster",
        "mob"
    ]
}
```

### dolphin.json
```json
"minecraft:type_family:" {
    "family": [
        "dolphin",
        "mob"
    ]
}
```

### donkey.json
```json
"minecraft:type_family:" {
    "family": [
        "donkey",
        "mob"
    ]
}
```

### drowned.json
```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
    "family": [
        "guardian_elder",
        "monster",
        "mob"
    ]
}
```

### enderman.json
```json
"minecraft:type_family:" {
    "family": [
        "enderman",
        "monster",
        "mob"
    ]
}
```

### endermite.json
```json
"minecraft:type_family:" {
    "family": [
        "endermite",
        "arthropod",
        "monster",
        "mob"
    ]
}
```

### ender_dragon.json
```json
"minecraft:type_family:" {
    "family": [
        "dragon",
        "mob"
    ]
}
```

### evocation_illager.json
```json
"minecraft:type_family:" {
    "family": [
        "evocation_illager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### fish.json
```json
"minecraft:type_family:" {
    "family": [
        "cod",
        "fish"
    ]
}
```

### fox.json
```json
"minecraft:type_family:" {
    "family": [
        "fox",
        "mob"
    ]
}
```

### ghast.json
```json
"minecraft:type_family:" {
    "family": [
        "ghast",
        "monster",
        "mob"
    ]
}
```

### guardian.json
```json
"minecraft:type_family:" {
    "family": [
        "guardian",
        "monster",
        "mob"
    ]
}
```

### hopper_minecart.json
```json
"minecraft:type_family:" {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### horse.json
```json
"minecraft:type_family:" {
    "family": [
        "horse",
        "mob"
    ]
}
```

### husk.json
```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
    "family": [
        "irongolem",
        "mob"
    ]
}
```

### lightning_bolt.json
```json
"minecraft:type_family:" {
    "family": [
        "lightning"
    ]
}
```

### llama.json
```json
"minecraft:type_family:" {
    "family": [
        "llama",
        "mob"
    ]
}
```

### magma_cube.json
```json
"minecraft:type_family:" {
    "family": [
        "magmacube",
        "monster",
        "mob"
    ]
}
```

### minecart.json
```json
"minecraft:type_family:" {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### mooshroom.json
```json
"minecraft:type_family:" {
    "family": [
        "mushroomcow",
        "mob"
    ]
}
```

### mule.json
```json
"minecraft:type_family:" {
    "family": [
        "mule",
        "mob"
    ]
}
```

### ocelot.json
```json
"minecraft:type_family:" {
    "family": [
        "ocelot",
        "mob"
    ]
}
```

### panda.json
```json
"minecraft:type_family:" {
    "family": [
        "panda"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "panda",
        "panda_aggressive",
        "mob"
    ]
}
```

### parrot.json
```json
"minecraft:type_family:" {
    "family": [
        "parrot_wild",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "parrot_tame",
        "mob"
    ]
}
```

### phantom.json
```json
"minecraft:type_family:" {
    "family": [
        "phantom",
        "undead",
        "monster",
        "mob"
    ]
}
```

### pig.json
```json
"minecraft:type_family:" {
    "family": [
        "pig",
        "mob"
    ]
}
```

### pillager.json
```json
"minecraft:type_family:" {
    "family": [
        "pillager",
        "monster",
        "illager",
        "mob"
    ]
}
```

### player.json
```json
"minecraft:type_family:" {
    "family": [
        "player"
    ]
}
```

### polar_bear.json
```json
"minecraft:type_family:" {
    "family": [
        "polarbear",
        "mob"
    ]
}
```

### pufferfish.json
```json
"minecraft:type_family:" {
    "family": [
        "pufferfish",
        "fish"
    ]
}
```

### rabbit.json
```json
"minecraft:type_family:" {
    "family": [
        "rabbit",
        "mob"
    ]
}
```

### ravager.json
```json
"minecraft:type_family:" {
    "family": [
        "monster",
        "illager",
        "ravager",
        "mob"
    ]
}
```

### salmon.json
```json
"minecraft:type_family:" {
    "family": [
        "salmon",
        "fish"
    ]
}
```

### sheep.json
```json
"minecraft:type_family:" {
    "family": [
        "sheep",
        "mob"
    ]
}
```

### shulker.json
```json
"minecraft:type_family:" {
    "family": [
        "shulker",
        "monster",
        "mob"
    ]
}
```

### silverfish.json
```json
"minecraft:type_family:" {
    "family": [
        "silverfish",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### skeleton.json
```json
"minecraft:type_family:" {
    "family": [
        "skeleton",
        "undead",
        "monster",
        "mob"
    ]
}
```

### skeleton_horse.json
```json
"minecraft:type_family:" {
    "family": [
        "skeletonhorse",
        "undead",
        "mob"
    ]
}
```

### slime.json
```json
"minecraft:type_family:" {
    "family": [
        "slime",
        "monster",
        "mob"
    ]
}
```

### snow_golem.json
```json
"minecraft:type_family:" {
    "family": [
        "snowgolem",
        "mob"
    ]
}
```

### spider.json
```json
"minecraft:type_family:" {
    "family": [
        "spider",
        "monster",
        "mob",
        "arthropod"
    ]
}
```

### squid.json
```json
"minecraft:type_family:" {
    "family": [
        "squid",
        "mob"
    ]
}
```

### stray.json
```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
    "family": [
        "tnt",
        "inanimate"
    ]
}
```

### tnt_minecart.json
```json
"minecraft:type_family:" {
    "family": [
        "minecart",
        "inanimate"
    ]
}
```

### tripod_camera.json
```json
"minecraft:type_family:" {
    "family": [
        "tripodcamera",
        "inanimate",
        "mob"
    ]
}
```

### tropicalfish.json
```json
"minecraft:type_family:" {
    "family": [
        "tropicalfish",
        "fish"
    ]
}
```

### turtle.json
```json
"minecraft:type_family:" {
    "family": [
        "turtle",
        "baby_turtle",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "turtle",
        "mob"
    ]
}
```

### vex.json
```json
"minecraft:type_family:" {
    "family": [
        "vex",
        "monster",
        "mob"
    ]
}
```

### villager.json
```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

### villager_v2.json
```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "farmer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "fisherman",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "shepherd",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "fletcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "librarian",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "cartographer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "priest",
        "cleric",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "armorer",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "weaponsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "blacksmith",
        "toolsmith",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "artisan",
        "butcher",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "artisan",
        "leatherworker",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "artisan",
        "stone_mason",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "villager",
        "peasant",
        "nitwit",
        "mob"
    ]
}
```

### vindicator.json
```json
"minecraft:type_family:" {
    "family": [
        "vindicator",
        "monster",
        "illager",
        "mob"
    ]
}
```

### wandering_trader.json
```json
"minecraft:type_family:" {
    "family": [
        "wandering_trader",
        "mob"
    ]
}
```

```json
"minecraft:type_family:" {
    "family": [
        "wandering_trader",
        "wandering_trader_despawning",
        "mob"
    ]
}
```

### witch.json
```json
"minecraft:type_family:" {
    "family": [
        "witch",
        "monster",
        "mob"
    ]
}
```

### wither.json
```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
    "family": [
        "wolf",
        "mob"
    ]
}
```

### zombie.json
```json
"minecraft:type_family:" {
    "family": [
        "zombie",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_horse.json
```json
"minecraft:type_family:" {
    "family": [
        "zombiehorse",
        "undead",
        "mob"
    ]
}
```

### zombie_pigman.json
```json
"minecraft:type_family:" {
    "family": [
        "zombie_pigman",
        "undead",
        "monster",
        "mob"
    ]
}
```

### zombie_villager.json
```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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
```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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

```json
"minecraft:type_family:" {
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
```json
"minecraft:underwater_movement:" {
    "value": 0.15
}
```

### drowned.json
```json
"minecraft:underwater_movement:" {
    "value": 0.06
}
```

```json
"minecraft:underwater_movement:" {
    "value": 0.08
}
```

### elder_guardian.json
```json
"minecraft:underwater_movement:" {
    "value": 0.3
}
```

### fish.json
```json
"minecraft:underwater_movement:" {
    "value": 0.1
}
```

### guardian.json
```json
"minecraft:underwater_movement:" {
    "value": 0.12
}
```

### pufferfish.json
```json
"minecraft:underwater_movement:" {
    "value": 0.13
}
```

### salmon.json
```json
"minecraft:underwater_movement:" {
    "value": 0.12
}
```

### skeleton_horse.json
```json
"minecraft:underwater_movement:" {
    "value": 0.08
}
```

### tropicalfish.json
```json
"minecraft:underwater_movement:" {
    "value": 0.12
}
```

### turtle.json
```json
"minecraft:underwater_movement:" {
    "value": 0.06
}
```

```json
"minecraft:underwater_movement:" {
    "value": 0.12
}
```

# minecraft:variant
### cat.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 5
}
```

```json
"minecraft:variant:" {
    "value": 6
}
```

```json
"minecraft:variant:" {
    "value": 7
}
```

```json
"minecraft:variant:" {
    "value": 8
}
```

```json
"minecraft:variant:" {
    "value": 9
}
```

```json
"minecraft:variant:" {
    "value": 10
}
```

### fox.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

### horse.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 5
}
```

```json
"minecraft:variant:" {
    "value": 6
}
```

### husk.json
```json
"minecraft:variant:" {
    "value": 2
}
```

### llama.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

### mooshroom.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

### panda.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 5
}
```

```json
"minecraft:variant:" {
    "value": 6
}
```

### parrot.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

### pillager.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

### pufferfish.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

### rabbit.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 5
}
```

### shulker.json
```json
"minecraft:variant:" {
    "value": 5
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 6
}
```

```json
"minecraft:variant:" {
    "value": 8
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 12
}
```

```json
"minecraft:variant:" {
    "value": 10
}
```

```json
"minecraft:variant:" {
    "value": 13
}
```

```json
"minecraft:variant:" {
    "value": 14
}
```

```json
"minecraft:variant:" {
    "value": 9
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 7
}
```

```json
"minecraft:variant:" {
    "value": 16
}
```

```json
"minecraft:variant:" {
    "value": 15
}
```

```json
"minecraft:variant:" {
    "value": 11
}
```

### tropicalfish.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

### villager.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

### villager_v2.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 5
}
```

```json
"minecraft:variant:" {
    "value": 6
}
```

```json
"minecraft:variant:" {
    "value": 7
}
```

```json
"minecraft:variant:" {
    "value": 8
}
```

```json
"minecraft:variant:" {
    "value": 9
}
```

```json
"minecraft:variant:" {
    "value": 10
}
```

```json
"minecraft:variant:" {
    "value": 11
}
```

```json
"minecraft:variant:" {
    "value": 12
}
```

```json
"minecraft:variant:" {
    "value": 13
}
```

```json
"minecraft:variant:" {
    "value": 14
}
```

### vindicator.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

### zombie_villager.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 1
}
```

```json
"minecraft:variant:" {
    "value": 2
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 3
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

```json
"minecraft:variant:" {
    "value": 4
}
```

### zombie_villager_v2.json
```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

```json
"minecraft:variant:" {
    "value": 0
}
```

# minecraft:water_movement
### panda.json
```json
"minecraft:water_movement:" {
    "drag_factor": 0.98
}
```

### polar_bear.json
```json
"minecraft:water_movement:" {
    "drag_factor": 0.98
}
```

### turtle.json
```json
"minecraft:water_movement:" {
    "drag_factor": 0.9
}
```

