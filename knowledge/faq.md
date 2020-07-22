---
layout: page
title: FAQ
parent: Knowledge
---

### FAQ

This page contains a list of frequently asked questions in the technical-bedrock community that do not deserve a long-form wiki entry. Please contribute your own questions/answers, so we can grow this resource!

`tip:` Use ctrl+f to quickly find content.

### How can I remove a spawn egg of an entity from creative menu?

 - Make the spawnable component false inside the behavior file
 - And delete the spawn egg component inside the resource file

### What is the default friction of vanilla blocks?
0.5

### Can I make custom, transparent blocks?
No

### How can I make animation that always runs?
Make the animation looping and don't let it transition to another animation

### Where can I find the error/output logs for Bedrock?
`C:\Users\YOUR_USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\logs`

### How can I make a completely invisible shadow under the entity, without changing the collision boxe? 
 - 1) use runtime of armor stand
 - 2) edit the shadow.material

### How can I remove clouds?
Change the RP cloud texture to be completely alpha

### Can I add knockback to entity's attack without using minecraft:behavior.knockback_roar?
No
 
### Can I make a directional facing custom block?
No

### How can I test if a player is in the Nether or End?
You can't

### How do I stop my entity from being pushed around?
```json
"minecraft:push_through": {
  "value": 0
}
```
### How do I stop my entity from being pushed by water?
You can't

### Are variables saved?
No, they are reset when the entity unloads (like on world exit, or chunk-unload)

### How can I make a mob glow?
Use the `entity_emissive` or `entity_emissive_alpha` material, it uses the alpha layer of images to make things "glow". See spider eyes for an example.

### Is it possible to give yourself a spawner with already mobs inside?
No

### Is it possible to do "on_entry":["/execute @e[name=variable.some_name] ..."]?
No

### Where can I download the bedrock resources?
The [bedrock resources can be found here](https://discordapp.com/channels/523663022053392405/523663022498250762/715962598843089008).

### Is it possible to only damage an entity when holding specific item?
Set up a damage_sensor and set deals_damage to false when they're not holding the item.

### Where do I find the molang variable list?
The [molang variable list can be found here](https://bedrock.dev/1.14.0.0/1.14.30.51/MoLang).

### Can I use /give to get shulker box with items?
 - No
 - The workaround: Clone a chest to the player and /fill destroy it.
 - Another work-around: Spawn a dummy-entity with a loot-table, and then kill it.

 ### What is the max seconds in a /effect command?
  - 2147483647