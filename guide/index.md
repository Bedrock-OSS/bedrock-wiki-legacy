---
layout: guide
title: Beginners Guide
has_children: true
nav_order: 3
sitemap:
    priority: 0.73
    changefreq: 'weekly'
---

# Beginners Guide

### **What is this guide?**
The guide is a beginner tutorial, created in order to make it possible for more people to start 'modding' Minecraft Bedrock Edition. The guide will guide you from the very fundamentals to being able to create advanced packs yourself.

### **What exactly are Add-ons?**
An add-on is basically the Minecraft Bedrock Edition(Windows 10, iOS, Android, Console) equivalent to Java mods. However, it's development is done officially by Mojang, who plan to make it so everything that is in the game will eventually be possible to fully recreate with add-ons.  \
### **What do I need in order to create Add-ons?**
This guide will be focusing on creating add-ons on a Windows 10 PC for any Bedrock platform. However, the process is much the same when working on Android or iOS, even if I do not prefer it. If something works differently on a mobile device, a note will state that.



Currently the latest release version of Minecraft is 1.16.0 and everything in this guide will work flawlessly in this version (you can check your minecraft version in the bottom-right corner of the start screen). Many things won't work in previous versions, and some will be changed in later ones. I will keep the guide as up-to-date is possible, so no need to worry.


### Content
Let's start by setting up your tools, which you will use throughout the development of your add-ons. In this section I'll show you exactly what software is needed, where to set up your add-ons, how to create a workspace and where to get additional info on the syntax.

- [Tools and Software; com.mojang folder; Referencing;](/guide/software-preparation.html);

You will make your first steps in creating an add-on here, by learning to create manifests and pack_icons, as well as learn to use some of the .mc file extensions. No previous coding experience required. After you'll create a testing World where you'll be able to test the first feature of your add-on - a custom /function.

- [Defining the pack with manifest.json; .mc file extensions; Custom Function;](/guide/manifest-function-extension.html)

Now it's time to begin writing the first features of you add-on. In this section you'll create a simple "Gem" item, and a custom food, as well as you'll learn linking textures via short names.

- [Custom Items; Linking Textures(short names); ](/guide/custom_blocks.html)

Next up are custom blocks. You'll create a simple block, an animated block with a flipbook texture, a "Compass" block that has different textures for every direction and a block that imitates a Log.

- [Custom blocks; Terrain and Flipbook textures;](/guide/custom_blocks.html)

Since you can now easily create custom blocks and items, it's time to learn about their custom Loot Tables and Recipes. While we're about it, we'll take a short look on entity Spawn Rules too.

- [Custom: Loot Tables; Recipes; Spawn Rules;]()

Now we're finally ready to create... Custom Entities. Make sure to polish your existing knowledge a bit before starting this chapter, as it will be a bit more complicated. First, we'll be using Blockbench to create the visuals, and then we'll define the Behaviors!

 - [Creating entity visuals in Blockbench: Modelling, Texturing, Animating;]()

 - [Custom entity full Resource and Behavior definition; Attributes, Components;]()

It's time to learn controlling how your Entity renders and what animations are played on a higher level:

 - [Render controllers; Entity Texture Variations;]

 - [Animation Controllers - Attack AI; Behavior animations - Entity Commands]()

The next sub-chapter: Here you'll create custom particles and sounds and learn to trigger them via animations are auto triggers.

 - [Custom Particles, Particles in Animation, Custom Sounds Definition;]()

Let's move to something way different now: World generation!

 - [Custom Generation: Biomes, Features, Feature Rules;]()



Something way different from everything we've done before: a Bonus tutorial the creation of custom Skin packs!

- [Custom Skin Packs](/guide/custom-skin-packs)

The guide will be updated regularly, in order to eventually lead you from "Beginner" to "I can create whatever I want".

*Currently the guide is being ported from guide.bedrock.dev to wiki.bedrock.dev/guide/. All help is greatly appreciated. Once the exiting subpages are migrated, guide.bedrock.dev will start pointing to the new directory.

###### The Guide has been originally written by KaiFireborn#1551 on Discord [here](https://sites.google.com/view/mcbe-add-on-tutorial/-?authuser=0), which was previosuly accessible by the subdomain of this subsite, `guide.bedrock.dev` and it's maintanance is discountinued. Instead, the Guide is now OOS and being [ported] maintained by the Bedrock Wiki community.
