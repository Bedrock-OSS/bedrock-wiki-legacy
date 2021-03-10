---
layout: page
title: Bedrock Modeling Introduction
parent: Knowledge
---

# Bedrock Modeling Introduction 

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

This will be a guide with tips, tricks, and things you should know when modeling for Minecraft Bedrock Edition.

## Texture Glitch
Sometimes the texture on some (smaller) faces are glitched or invisible. This is because size of cubes is floored for the UV map calculation. This means that any size smaller than 1 will result in a 0 pixel wide UV map, which will look glitchy. To prevent this make sure all of your cubes are at least 1 unit long in each direction. To create smaller cubes, use the Inflate slider.
Another trick to solve this if you _must_ have smaller textures, is by **increasing the element size by 1 in each direction** and then **inflating the element by -1** though note that this will make you have smaller pixels, and if textured incorrectly will lead to mixels.

## Vertex Snap
Vertex snap is a very useful tool in blockbench any modeler should use. It's specially useful when doing rounded things like wheels.
You can find this tool right top next to the movement & scale tools. It has 2 modes, Move & Scale. How this tool works can be seen in the following gif.
[Vertex Snap Gif](https://cdn.discordapp.com/attachments/549198394925514753/609491083369512960/vertex_snap.gif "https://cdn.discordapp.com/attachments/549198394925514753/609491083369512960/vertex_snap.gif")

## Transparency
If you use semi-transparent textures (like colored glass) you need to move elements with that texture to the bottom of the element list. Otherwise elements behind these semi-transparent ones won't render ingame.

## Texturing
When learning to texture your best bet is practicing with references on how others textured similar objects & surfaces. Patterns for wood & metal are different and you should take that into consideration. Good guides are
[Masteriano's Texturing Tips](https://blockbench.net/2019/10/02/minecraft-modeling-texturing-tips "https://blockbench.net/2019/10/02/minecraft-modeling-texturing-tips")
And in general any on pixel art.

## Materials
Whether or no the transparency or emissive textures in your models work in-game, it's decided by the materials applied to it.

|Material        |Description                     
|----------------|-------------------------------|
|entity|basic opaque material         |
|entity_alphatest|supports transparent pixels         |
|entity_alphablend|supports translucent pixels|
|entity_emissive|solid, alpha channel is used as the emissive channel         |
|entity_emissive_alpha|alpha channel is used for emissiveness, completely black + transparent pixels are rendered transparently|

## Z fighting
Z fighting is called when you have the face of 2 elements in the same place and you can see both or half of them at the same time, like seen in the following picture.
[Example](https://cdn.discordapp.com/attachments/632982024176533546/740312078291697787/unknown.png "https://cdn.discordapp.com/attachments/632982024176533546/740312078291697787/unknown.png")
You can solve this by inflating one of them by `0.01` or `-0.01` depending which one should have priority. 

## Basics of Animations
When animating in Blockbench, you can set each keyframe by hand, or you can use variables & functions.
Here you will learn the basics.
Lets start with this picture
[Example](https://cdn.discordapp.com/attachments/306562251987615744/740313755551924234/unknown.png "https://cdn.discordapp.com/attachments/306562251987615744/740313755551924234/unknown.png")
the name, or `animation.cuack` is very important. You can't have symbols or caps there, and it must start with `animation.` for the animations to work without problems.
Now the function we will be using it
`Base + Math.sin((query.life_time + Offset) * Speed) * pitch`
* Base is the starting rotation/position the bone has
* Sin is the math function we all know
* `query.life_time` is a variable. Is a number that will be increasing as the animation continues
* Offset is a number we use to have the animation to start earlier or later than it's "original" position
* Speed is the time it will take from going from top to down
* Pitch is how far it goes from the origin

The movement this equation creates can be seen in the following gif
[Movement](https://cdn.discordapp.com/attachments/306562251987615744/740316045121683586/G1.gif "https://cdn.discordapp.com/attachments/306562251987615744/740316045121683586/G1.gif")

Function used: `Math.sin((query.life_time+0.5)*150)*15`
one on position & the other on rotation.

NOTE: Graph the equation on an online graphicator to better understand what's going on

Don't forget that for the animation to be a perfect loop, you need to correlate the sin equation `speed` & the animation `time`. (seen on the first picture under Animation Basics)
Here's a table with values to get a perfect loop, though there are more you can discover.

|Speed|Time|Group
|----------------|-------------------------------|----|
|150|2.4         |1
|100|3.6         |2

These numbers can be multiplied but not divided, so these will also work
But only multiples of the same option

|Speed|Time|Group
|----------------|-------------------------------|-
|150|4.8         |1
|200|3.6         |2
|300|2.4         |1
|300|3.6         |1 & 2

Now not all of these will "loop" together. And that is the Group column. The ones with the same number will work together, otherwhise they will have a visible "glitch" in the loop.

NOTE: you can have an animation in loop clicking on the following setting
[Setting Image](https://cdn.discordapp.com/attachments/306562251987615744/740315853219692624/unknown.png "https://cdn.discordapp.com/attachments/306562251987615744/740315853219692624/unknown.png")

Is with this function & creativity that animals & dinosaurs are animated into walking, running & attacking.
You can learn more about queries & functions at the following link:
[https://bedrock.dev/docs/stable/MoLang](https://bedrock.dev/docs/stable/MoLang)
