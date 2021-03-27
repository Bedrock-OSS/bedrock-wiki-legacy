---
layout: guide
title: Beginners Guide
has_children: true
sitemap:
    priority: 0.73
    changefreq: 'weekly'
---

Sometimes creating Add-Ons can be a pain, especially when you're just starting out. Fear not, for making the Beginning as comfortable as possible is the exact reason of this Guide's existance.

# Beginners Guide

### **What is this guide?**
The guide is a beginner tutorial, created to make it possible for more people to start 'modding' Minecraft Bedrock Edition. The guide will guide you from the very fundamentals to being able to create advanced packs yourself.

### **What exactly are Add-ons?**
An add-on is basically the Minecraft Bedrock Edition(Windows 10, iOS, Android, Console) equivalent to Java mods. However, it's API's development is done officially by Mojang, who plan to make it so everything that is in the game will eventually be possible to fully recreate with Add-ons.   

### **What do I need in order to create Add-ons?**
This guide will be focusing on creating add-ons on a Windows 10 PC for any Bedrock platform. However, the process is much the same when working on Android or iOS, even if it's not preferrable in some cases. If something works differently on a mobile device, a note will state that.


Currently the latest stable release of Minecraft is 1.16.0 - everything in this Guide will work flawlessly in this version (you can check your minecraft version in the bottom-right corner of the start screen). Many things won't work in previous versions, and some will be changed in later ones. We will keep the guide as up-to-date is possible, so no need to worry.


### Content
Let's start by setting up your tools, which you will use throughout the development of your add-ons. In this section I'll show you exactly what **software** is needed, where to **set up** your add-ons, how to create a **workspace** and where to get additional info on the syntax.

- [Software Preparation](/guide/software-preparation.html);

You will make your first steps in creating an add-on here, by learning to create **manifests** and **pack_icons** (a.k.a initializing an Add-On), as well as learn to use some of the .mc file extensions. No previous coding experience required. After you'll create a testing World where you'll be able to test the first feature of your add-on - a custom **/function**. We'll also learn about **transpiling Add-ons** and other **`.mc` file extensions**.

- [Getting Started](/guide/project-setup.html)

Now it's time to begin writing the first features of you add-on. In this section you'll create a **simple** "Gem" **item**, and a **custom food**, as well as learn to link textures via **short names**.

- [Custom Items](/guide/custom-items.html)

Next up are **custom blocks**. You'll create a **simple block**, an **animated block** with a flipbook texture, a "Compass" block that has different textures for every direction and a block that imitates a Log.

- [Custom Blocks](/guide/custom-blocks.html)

Since you can now easily create custom blocks and items, it's time to learn about their custom **Loot Tables** and **Recipes**. While we're about it, we'll take a short look on entity **Spawn Rules** too.

- [Loot tables & Spawn Rules](/guide/loot_tables-recipes-spawn_rules.html)

Now we're finally ready to create... **Custom Entities**. Make sure to polish your existing knowledge a bit before starting this chapter, as it will be a bit more complicated. First, we'll be using Blockbench to create the visuals, and then we'll define the Behaviors!

 - [Creating entity visuals in Blockbench: Modelling, Texturing, Animating](/guide/creating-entity-visuals.html)

 - [Custom entity full Resource and Behavior definition: Attributes, Components](/guide/custom-entity-full.html)

 And, additionally, a short **Trading** attribute tutorial:

 - [Custom trades & Trade Tables](/guide/custom_trades.html)

It's time to learn **controlling** how your Entity **renders** and what **animations** are played on a higher level:

 - [Render controllers & Entity Texture Variations](/guide/render-controllers.html)

 - [Animation Controllers - Attack AI, Behavior animations - Entity Commands](/guide/animation-controllers.html)

The next sub-chapter: Here you'll create **custom particles** and sounds and learn to trigger them via animations are auto triggers.

 - [Custom Particles, Particles in Animation, Custom Sounds Definition](/guide/custom-particles.html)

Let's move to something way different now: **World generation**!

 - [Custom Generation: Biomes, Features, Feature Rules](/guide/custom-generation.html)


And, something way different from everything we've done before: the creation of **custom Skin packs**!

- [Custom Skin Packs](/guide/custom-skin-packs.html)

What to do **next**:
 - [Scripting HelloWorld tutorial](/scripting/hello-world-tutorial.html#manifestjson) - Reading the article from the [start](/scripting/hello-world-tutorial.html) is recommended but not required: it's an alternative to [Software and Preparations](/guide/software-preparation.html) subGuide.

- The [Bedrock Wiki](https://wiki.bedrock.dev) has a lot of more advanced tutorials you might be interested to utilize.


__*Note*__: *A template Add-On, containing all code examples from this guide can be downloaded [here](https://github.com/SirLich/bedrock-wiki/tree/gh-pages/assets/images/guide/template_packs)*.



<br>

> The guide will be updated regularly, in order to eventually lead you from "Beginner" to "I can create whatever I want".

<!-- *Currently the guide is being ported from guide.bedrock.dev to wiki.bedrock.dev/guide/. All help is greatly appreciated. Once the exiting subpages are migrated, guide.bedrock.dev will start pointing to the new directory. -->

<br>


 <!--Insited to keep-->

<details> 

  <summary>

    Timeline

  </summary>

- 13.04.2020: The guide has been originally written and published by *KaiFireborn*#1551 on Discord [here](https://sites.google.com/view/mcbe-add-on-tutorial/-?authuser=0).
 - 04.05.2020: Accessible by the domain/link [`guide.bedrock.dev`](https://guide.bedrock.dev) thanks to *destruc7i0n*.
 - 09.23.2020: Migration/porting of the Guide to the Wiki agreed upon and started with *SirLich*. Maintanence of the original website discountinued.
 - 18.10.2020: Migration officially finished mostly thanks to *ckhrysze* and *KaiFireborn*. 
 Currently, the Guide is fully OSS and accepting contributions from *you*.

</details>

___
