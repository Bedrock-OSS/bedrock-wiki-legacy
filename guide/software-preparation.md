---
layout: guide
title: Software and preparation
parent: Beginners Guide
nav_order: 1
badge: 1
badge_color: guide
badge_justification: left
---

# Software and Preparation

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

___

## Downloading the software.

In order to be able to code add-ons you'll need a certain set of software installed. While Windows 10 offers the largest variet of tools, alternatives can be found on other platforms, including mobile.

 1. The official **Minecraft v.1.16.0+**, _Bedrock Codebase_
    - Windows 10: [Minecraft](https://www.microsoft.com/en-us/p/minecraft-for-windows-10/9nblggh2jhxj?activetab=pivot:overviewtab) [_Wind10 Edition, Bedrock_] from Microsoft Store;
    - [Android](https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en) and [iOS](https://apps.apple.com/us/app/minecraft/id479516143): the official Minecraft from the respective stores;

2. **A code editor**. This can be any text editor (even the Windows-pre-installed Notepad would do), however it's much more comfortable to work in a dedicated Code Editor, like VSC, which I prefer.    

 - [_Visual Studio Code_](https://code.visualstudio.com/) - is optimal in many cases. Also has a variety of extensions for Add-On development available (*See below*). (*Warning*: not *Visual Studio*, which is an IDE)
 - [_Sublime Text_](https://www.sublimetext.com/) is another great code editor with huge theme customization capabilities. 
- [_CoreCoder_](https://hanprog.itch.io/core-coder) is a unique Code Editor developed specifically for Add-On creation.   
- [_Atom_](https://atom.io/) 
- Alternatives for mobile:
    - Android: _ES File Explorer_;
    - iOS: [_Kodex_](https://apps.apple.com/us/app/kodex/id1038574481);

- [_Bridge_](https://github.com/bridge-core/bridge.), a visual software for Minecraft Add-On development. It offers JSON in tree view. However, the process of creating add-ons in bridge is parallel to creating them in a Code editor, so once you grasped the basics you could easily switch to using Bridge. (*See note below*)

___
### Notes


<details> 

   <summary>
      Features to look for in a Code Editor
   </summary>

   - **Opening Folders:** When editing Addons, it is very convenient to open an entire folder as a project, instead of just individual files. This allows you to edit the files in both the Behavior Pack and Resource Pack at the same time, and quickly switch between tasks. 
   - **Json Linting/Prettify:** Linting is the ability to validate code as correct in real-time. Linting for json will mark things like missing commas, misplaced parens, or other formatting issues so that you can fix them. [Linting can also be found online](https://jsonlint.com/), but having real-time linting built directly into your editor is very much preferred.
   - **Built in Terminal:** I find a terminal built into my editor to be very useful. I often use python scripting to supplement my workflow, and having easy access to a terminal speeds up that workflow.

</details>


<details>

   <summary>
      VSC Extensions for Add-On developing
   </summary>

Many packages exist for VSCode that make editing addons easier:
 - [Blockceptions Minecraft Bedrock Development](https://marketplace.visualstudio.com/items?itemName=BlockceptionLtd.blockceptionvscodeminecraftbedrockdevelopmentextension)
 - [.mcfunction support](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction)
 - [.lang support](https://marketplace.visualstudio.com/items?itemName=zz5840.minecraft-lang-colorizer)
 - [Bedrock Definitions](https://marketplace.visualstudio.com/items?itemName=destruc7i0n.vscode-bedrock-definitions)
 - [Prettt-json](https://marketplace.visualstudio.com/items?itemName=mohsen1.prettify-json)
 - [Spell Checker (for writing wiki)](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
 - [Snowstorm Particle Editor](https://marketplace.visualstudio.com/items?itemName=JannisX11.snowstorm)
 - [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
 - [UUID Generator](https://marketplace.visualstudio.com/items?itemName=netcorext.uuid-generator)

</details>



<details>

   <summary>
      If you choose to use bridge.
   </summary>

   You should be aware that it is a application that you benefit most from when you use it exclusively for editing your addon. Switching between a different editor and bridge. creates a bit of an overhead in your workflow (more later). The program builds up a knowledge base of your files as you use the editor. This enables very fast and dynamic auto-completions and file validation but also means that all of your files are cached in the background by default. There are two ways to workaround Bridge's caching strategy:
1) Increase or remove the `bridge-file-version: #11` comment the app leaves in your files after editing a file without bridge.
2) Add files that you want to edit without bridge. to a `.no-cache` file at the root of your behavior pack

Due to the nature of the file versioning system, most scripts and tools will continue to work as expected.

For further guidance on the editor, feel free to contact [solvedDev](https://twitter.com/solvedDev). bridge. also has an [official Discord server](https://discord.gg/wcRJZN3), with announcements, plugin discussion, add-on help, and more.

</details>

<br>

___


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
1. Create a folder named "`your_pack_name_RP`" in `development_resource_packs`. **I'll refer to this folder as `RP`**, according to the[Style Guide](https://wiki.bedrock.dev/knowledge/style-guide.html).
1. Create a folder "`your_pack_name_BP`" in `development_behavior_packs`. **I'll refer to this folder as `BP`**.
1. Go to `File>Add folder to workspace...`  and choose `BP`. Do the same with `RP`.
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
