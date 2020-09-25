---
layout: page
title: Software and preparation;
parent: Beginners Guide
---

#### **You will:** 
- [ ] Download the necessary [**tools and software**](#downloading-the-software);
- [ ] Locate and understand your [**com.mojang folder**](#the-com.mojang-folder-and-your-workspace);
- [ ] Be introduced to [**referencing**](learning-to-reference).  

___
___

## Downloading the software.

In order to be able to code add-ons you'll need a certain set of software installed. While Windows 10 offers the largest variet of tools, alternatives can be foundy

 1. The official **Minecraft v.1.16.0+**, _Bedrock Codebase_
    - Windows 10: [Minecraft](https://www.microsoft.com/en-us/p/minecraft-for-windows-10/9nblggh2jhxj?activetab=pivot:overviewtab) [_Wind10 Edition, Bedrock_] from Microsoft Store;
    - [Android](https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en) and [iOS](https://apps.apple.com/us/app/minecraft/id479516143): the official Minecraft from the respective stores;

1. **A code editor**. This can be any text editor (even the Windows-pre-installed Notepad would do), however it's much more comfortable to work in a dedicated Code Editor, like [Visual Studio Code](https://code.visualstudio.com/), which I prefer. [Sublime Text](https://www.sublimetext.com/) is another great code editor with huge theme customization capabilities. [CoreCoder](https://hanprog.itch.io/core-coder) is a unique Code Editor developed specifically for Add-On creation.   Alternatives for mobile:
   - Android: _ES File Explorer_;
   - iOS: [_Kodex_](https://apps.apple.com/us/app/kodex/id1038574481);  

   Alternatively, you can use [_Bridge_](https://github.com/bridge-core/bridge.), a visual software for Minecraft Add-On development. It offers JSON in tree view, which I personally do not prefer over "pure" JSON in a code editor such as VSC. However, the process of creating add-ons in bridge is parallel to creating them in a Code editor, so once you grasped the basics you could easily switch to using Bridge.

![VSC Workspace](/assets/guide/vsc_workspace.png)

3. [**Blockbench**](https://blockbench.net/) is a 'boxy 3D model editor ' typically used to create Minecraft entity/block models, textures and animations. Also provides a web-browser version compatible with mobile.  An image editor, like GIMP, Photoshop or paint.net, is recommended to be used along.

![Blockbench Workspace](/assets/guide/blockbench_workspace.png)



As a further note, you may might other recommended software like [AJG](https://kaifireborn.itch.io/add-on-json-generator) for repetitious task automation (e.g mass weapon generation) or [FRG](https://machine-builder.itch.io/frg-v2) for quick custom structure creation helpful.

___

   Now that you have your tools installed, let's move onto some pre-organisation:

## The com.mojang folder and your Workspace
The com.mojang folder is the folder we're going to be working with throughout the Guide and Add-On development in general. It's the way to communicate with your game - you can find it in: 
 - Windows: `C:\Users\USERNAME\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang`;
- Android: `Phone>games>com.mojang`;
- iOS: `My iDevice>Minecaraft>games>com.mojang`);  
 I strongly recommend creating a shortcut to the folder on your Desktop, in order to be able to easily access it at any time.  
   You'll find a lot of folders and files in the folder, among them: `behavior_packs`, `development_behavior_packs`, `resource_packs`, `development_resource_packs`.

![com.mojang folder](/assets/guide/com_mojang_folder.png)


 `development_..._packs` are for developing add-ons -  if you do some changes to them, _then exit and re-enter a world with the packs applied_, the packs will _update_. That way you can quickly test the changes without having to change the pack version and reloading the game. Thus we'll work with these folders.  
 (In `..._packs`, on the other hand, stable add-ons, including those imported via `.mcpack` are stored. They're also used to submit add-ons to Realms. We do not need them right now.)  




____
Let's create you first add-on workspace in Visual Studio Code now.
1. Open VSC(*Visual Studio Code, the code editor*);
1. Create a folder named "`YourPackName res`" in `development_resource_packs`. **I'll refer to this folder as `res`**.
1. Create a folder "`YourPackName bhv`" in `development_behavior_packs`. **I'll refer to this folder as `bhv`**.
1. Go to `File>Add folder to workspace...`  and choose `bhv`. Do the same with `res`.
1. Press `File>Save Workpsace as...` to save the workspace file to your Desktop. Whenever you're working on your add-on, all you have to do is open the workspace in VSC for quick access to both add-on folders.

## Learning to reference
 Referencing means looking at other add-ons to find out how certain results are achieved. Minecraft's unmodified files are a good place to start. Download these zips of the Example resource packs and Example behavior packs and get creative! I recommend adding them to your workspace, but not changing them.

The most important thing to check all the time are the official documentations. bedrock.dev is an amazing collection of all  the documentations and schemes, and typing `bedrock.dev/r` in your search window will immediately show you the documentations of the most recent official Minecraft release. (`bedrock.dev/b` results in the latest beta's docs.)

 Once you are though with this guide, you could download and reference some open-source add-ons from, for example, MCPEDL.com (You might also share your own ones there).


___
___

## Your progress so far:
**What you've done:**

- [x] Installed the necessary software;
- [x] Downloaded the Vanilla Example files;
- [x] Located your com.mojang folder and created your add-on's workspace.
**What you are to do next:**
- [ ] Create your add-ons manifests, pack icons;
- [ ] Learn to use `.mcfunction`, .`mcstructure`, `.mcpack` and `.mcaddon.`
