---
layout: page
title: Troubleshooting
has_children: true
---

# Entity Troubleshooting

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Creating Addons for Minecraft is a fairly easy process *once you get a hang of it*. The first time is usually a difficult, bug-prone process. This document contains some tips and tricks for fixing those dastardly bugs, as well as best practice information.

## The Environment

The best way to prevent *invisible entity syndrome* and other nasty bugs is by setting yourself the correct environment. You should review [the editor document](/knowledge/the_editor) for my editor recommendations. The most important part is getting a json-linter, ([or using an online json-linter](https://jsonlint.com/)).

## Content Log

The next thing you should do is turn on your content log. This can be done like: `Settings > Profile > Enable Content Log GUI`. Then press `ctrl+h` in-game to see any errors or output that might pop-up. Errors in the content log will show up every time you open the world, and also during gameplay if more errors occur.

`warning:` Errors are not cleared between runs, so it is possible the errors you see in the content log are *old* errors, from prior runs.

### Content log file

The content log is saved in `.txt` format at: `C:\Users\YOUR_USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\logs`

## Using Vanilla Resources

You should download the vanilla resource and behavior pack. You can find [the vanilla resource and behavior pack here](https://www.minecraft.net/en-us/addons/). You can compare against the vanilla files if you have any issues.

## JSON-Schemas

JSON-Schemas are a valuable tool for file validation. You can learn more about [JSON-Schemas here](/knowledge/using-schemas).

## Reload

Reload MC. Just do it.

---

# Step-by-step Entity Debugging

# Missing/Invisible Entity Syndrome Troubleshooting Guide

## Step 0.0.0 - You messed up:
Accept that something somewhere is wrong, and more often than not, it's a really simple beginner level issue that'll make you facepalm repeatedly when you find it. NOBODY at any level is immune to these messups so don't get offended and think "Of course I did that! I'm not stupid!" and skip a step while you're going through these.

## Step 1.0.0 - Are both packs active?:
Make sure both the resource pack and behavior pack are active for the world (a good way to avoid accidentally having this issue is to set each pack as a dependency of the other in both packs' manifest.json files so that adding or removing one of the packs automatically adds/removes the other)

## Step 2.0.0 - Determine whether the issue is in the resource pack or the behavior pack:
The issue you're suffering can be narrowed down significantly by how your entity's spawn egg appears in the creative inventory. Even if you don't want the entity to have a spawn egg, make the following changes just for now until you locate the issue:

### In the RP:
Make sure the .entity file has a custom spawn_egg object like:
```json
"spawn_egg":{
	"base_color": "#FF0000",
	"overlay_color": "#FFFF00"
}
```

The colors you choose will need to be something other than "#000000" for this guide.

### In the BP:
Make sure "is_spawnable" and "is_summonable" are set to true, and that "is_experimental" is set to false in the description object:

```json
"description":{
	"identifier": "foxy:example_entity",
	"is_spawnable": true,
	"is_summonable": true,
	"is_experimental": false
}
```

This object is only used in behavior files that are format verion 1.8.0 or higher. If you're still using something like format version 1.2.0 (what the hell are you doing), then they'll be locked to true, true, and false respectively, but you should REALLY consider updating your file.

### Results:
*"I don't see a spawn egg at all"*
 - See "Step 3.1.0 - BP"

*"I see a spawn egg for my entity but it's just black and the entity doesn't appear when I spawn or summon it"*
 - See "Step 3.2.0 - RP .entity"

*"I see a spawn egg for my entity and it has the colors I chose, but the entity still doesn't appear when I spawn or summon it"*
 - See "Step 3.3.0 - RP resources"

---

## Step 3.0.0 - Locating the specific issue:

## Step 3.1.0 - BP:
*You don't see a spawn egg for your entity in the creative inventory, even after making sure "is_spawnable" is set to true in the behavior file.*

This means the game isn't detecting a behavior file for the entity at all. Some common reasons for this include:
 - Syntax error in your behavior file
 - Misnamed folder

### Step 3.1.1 - Syntax error:
A single syntax error in a .json file causes the entire file to break and be ignored. To check that your file is free of syntax errors, visit [Json Lint](https://jsonlint.com/), paste the contents of your behavior file into the big box, then click "Validate JSON".
(NOTE: Although this site will mark // comments as errors, Minecraft DOES allow .json files to contain them)

### Step 3.1.2 - Misnamed folder:
Make sure the folder that contains your behavior files is named "entities" and not "entity". In behavior packs, folders tend to be named "entities" while in resource packs, they'll usually be "entity". I know. It's annoying.

---

## Step 3.2.0 - RP .entity:
*You DO see a spawn egg for your entity in the creative inventory, but it's black (and probably has a weird name like "item.spawn_egg.entity.something:your_mob.name") and nothing appears when you spawn/summon it.*

This means you have a working behavior file, but for whatever reason, the game isn't connecting it to the corresponding .entity file in your resource pack. Some common reasons for this include:
 - Syntax error in your .entity file
 - The entity's identifiers don't match
 - One or more of the resources your .entity file directs to are invalid

### Step 3.2.1 - Syntax error:
A single syntax error in a .json file causes the entire file to break and be ignored. To check that your file is free of syntax errors, visit https://jsonlint.com/, paste the contents of your behavior file into the big box, then click "Validate JSON".
(NOTE: Although this site will mark // comments as errors, Minecraft DOES allow .json files to contain them)

### Step 3.2.2 - Identifiers don't match:
The "identifier" in your behavior file must be EXACTLY the same as the one in your .entity file, including the namespace (the part before the colon like `minecraft` in `minecraft:bat`) and neither should be using `minecraft` as the namespace unless it's a default mob.

Your identifiers should also NOT contain any spaces or special characters (aside from the colon between the namespace and ID), and, for rare fringe case bug reasons, you should AVOID having the namespace or ID start with anything other than a lowercase letter. Starting with a number or capital letter *shouldn't* be an issue anymore, but this was not always the case in earlier versions of the game, and because of this, bugs have sporadically appeared in the past where starting with a number or capital letter had unexpected effects. Therefore it's better to avoid this if possible.

### Step 3.2.3 - Invalid resources:
The entity's ID in the .entity file does not match the ID you used in the behavior file

--- 

## Step 3.3.0 - RP resources: (still writing because this is going to be extensive)
*You DO see a spawn egg for your entity in the creative inventory and it DOES has the proper colors you specified in the .entity file's "spawn_egg" object, but nothing appears when you spawn/summon it or there's just a shadow.*

This means you have a working `.behavior` and `.entity` file, but something in the `.entity` file is directing to either a broken file, or another valid file that directs to a broken file.

To start with:
- invisible, no shadow -> bad RP reference
- invisible, yes shadow -> geometry issue
- visible, weird texture -> texture issue
- visible, weird visibility stuff -> material issue
