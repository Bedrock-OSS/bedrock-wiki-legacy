---
layout: page
title: Manifest; Custom Function; .mc file extensions
parent: Beginners Guide
---

___
___
<!-- #### **You will:**  -->
- [Manifests](#manifests);
- [Testing World](#creating-your-testing-world);
- [Files with .mc extensions](mc-file-extensions):
   - [.mcstructure](#.mcstructure)
   - [.mcfunction](#.mcfunction)
   - [.mcpack, .mcaddon & .mcworld](#.mcpack,-.mcaddon-&-.mcworld)


___
___

## Manifests
A manifest is a file that defines your pack to Minecraft. It stores all sorts of important info about your pack.
Like all other code files in your pack, it's written in JSON [Java Script Object Notation].\

### **JSON Syntax Rules:**
- **Data is in name/value pairs;**
- **Data is separated by commas;**
- **Curly braces hold objects;**
- **Square brackets hold arrays;**
- **Every `{` must be closed by `}`, every `[` with `]`, same with `{}`, `[]`, `""`, `''`, etc.**

You can learn more about JSON [here](https://www.w3schools.com/whatis/whatis_json.asp).
___
Let's create our Resource Pack manifest first by copying the code below into `res/manifest.json` (I*n other words, in a '`manifest.json`' file in your resource pack folder, which is located in '`development_resource_packs`'*).


```jsonc
{
    "format_version": 2,
    "header": {
        "name": "kf:Tutorial Resources",
        "description": "A great place to start creating your very own add-ons. Organized by KaiFireborn#1551 on Discord.",
        "uuid": "2f85891a-bd3d-439d-a1ec-238ea8b22abf",
        "version": [
            1,
            0,
            0
        ],
        "min_engine_version": [
            1,
            14,
            0
        ]
    },
    "modules": [
        {
            "type": "resources",
            "uuid": "d7a1fd29-1e22-454e-94ba-50a13a4c10d9",
            "version": [
                1,
                0,
                0
            ]
        }
    ]
}
```

Let's break up the code now.

- "`format_version`" defines what version of manifest syntax you are using. Version 2 is the most recent stable version, use it. 

- "`name`" is the name of your behavior pack. "description" will show up under it in-game.

- The "`uuid`" field is a very important one. A UUID(*Universally Unique IDentifier*) identifies your pack for other programs(in this case, Minecraft) to read. NEVER USE THE SAME UUID TWICE. You can generate your own UUIDs [here](https://www.uuidgenerator.net/version4) or, if you use VSC, you can install [this](https://marketplace.visualstudio.com/items?itemName=netcorext.uuid-generator) extension. Many other tools like *Bridge*, *AJG* and *CoreCoder* generate UUIDS automatically.. Every manifest file uses 2 different UUIDs.

- "`version`" defines the version of your add-on. When you import an add-on with a newer version on a device where an older version was installed, the newer version will overwrite the older one. You don't need to change the version if you have the add-on in `development_*_packs` folders and only use them on private worlds. 

- "`min_engine_version`" defines the minimum Minecraft client version that'll be able to read your add-on. Set it to `1.16.0` or the latest versionof Minecraft.

- In "`modules`", write the same "`version`" number, a new UUID under "uuid" and define the "`type`" to be "`resources`". This makes your pack a *Resource Pack*, also called a *Client pack* or a *Texture pack*. It changes things in-game visually.



###### Note: if Mojang decides to add something else to the manifest syntax, they'll create a newer format version. Your manifests can left unchanged, but it's recommended to create the new ones with "format_version" set to the new number and the new syntax used. If this ever happens, it will be mentioned in a changelog, and this site will be updated.

#
The next step is, naturally, creating your `bhv/manifest.json`. it is very much like a Resource pack manifest, except the "`type`" is "`data`"(for a *Data Pack*/*Behavior Pack*). There's also an optional field "`dependencies`", where you can define the needed resource packs by including their main UUID. Dependent resource packs will be applied to any world with the behavior pack automatically, if they exist on the device.

*Remember that same UUIDs cannot be used twice, which means that you have to generate NEW ones for the behavior manifest, and not use the ones already used in the resource manifest.*

```jsonc
{
    "format_version": 2,
    "header": {
        "name": "kf:Tutorial Behaviors",
        "description": "A great place to start creating your very own add-ons. Organized by KaiFireborn#1551 on Discord.",
        "uuid": "1e77f741-228e-4085-af8d-cd53d4c6612b",
        "version": [
            1,
            0,
            0
        ],
        "min_engine_version": [
            1,
            14,
            0
        ]
    },
    "modules": [
        {
            "type": "data",
            "uuid": "b7d5851a-fa82-48cd-aaf4-6aea8e9d3d3b",
            "version": [
                1,
                0,
                0
            ]
        }
    ],
    "dependencies": [
        {
            "uuid": "2f85891a-bd3d-439d-a1ec-238ea8b22abf",
            "version": [
                1,
                0,
                0
            ]
        }
    ]
}
```
#

The last thing to do is to add your `pack_icon.png` file to both bhv and ``res``. I'm going to use this image here for now.

![Pack icon](/assets/guide/pack_icon.png)

If you have done everything correctly, your packs should show up in Minecraft now!
![](/assets/guide/behavior_pack_existing.jpg)
___

## Creating your testing world.
Now to create a testing world to test your new add-on!

1. Click "**Create new world**";

2. Set the following settings like on the images below, so it'll be easier to test your add-on in the future:
 - The '**Experimental Gameplay**' **MUST** be **on** for some add-on features (*like Scripting, Biomes, Features, Feature Rules, etc*), double check if it's on after applying your packs.
- You might need to turn some settings, like '*TNT explodes*', '*fire spreads*', '*do daylight cycle*', '*Mobs spawning*' etc, depending on what you're testing. It's easy to do with the `/gamerule` command in-game.

3. Turn on both '**settings>profile>content_log_file**' and '**settings>profile>content_log_gui**'. This will show you any errors in your add-on when you enter a world with it applied. You can also open the content log GUI by pressing `ctrl+h`.

![](/assets/guide/world_params_1.jpg)
![](/assets/guide/world_params_2.jpg)
![](/assets/guide/world_params_3.jpg)

Now activate your behavior pack. If you haven't set up dependencies in the manifest, apply your resource pack too, otherwise, it'll be applied automatically). Check if **[EX]**(Experimental Gameplay) is turned on, and click '**Create**'. You might need a separate '*Infinite*' world to test entity spawning too.
![](/assets/guide/behavior_pack_applied.jpg)

_____________
___

## .mc file extensions;
Now it's time to talk about some file extensions you'll be using during the development.
___
### .mcstructure 
An  `.mcstructure`  file literally includes a Minecraft structure, consisting of blocks and entities. It can be exported via a Structure Block(`*/give @s structure_block*`) and is Win10 Edition only. 
If you store one of these files in the `bhv/structures` folder you'll be able to '**load**' the structure from structure blocks on any world with the pack applied. (*A reliable method to transfer structures between worlds!*). See the Custom Structures article to make your Structures automatically generate in your world!   
![Structure Block Example](/assets/guide/structure_block_example.jpg)
___
### .mcfunction
An  `.mcfunction` file is a file holding a function, a.k.a a bundle of commands.. Let's create one in `bhv/functions/`. VSC will treat it like a normal .txt file.   
Let's name the new text file `diamond_tools.mcfunction` and write a set of simple *slash commands*[but without slashes(`/`)], which can otherwise be executed from in-game chat, like these:   
![.mcstructure in VSC](/assets/guide/function_code.jpg)
##### Note: if a command's syntax in the function is incorrect, the function won't parse. Watch your *content log* for errors.

Now you can run the function by typing `/function diamond_tools` (*`/function {filename}`*) in the in-game chat!   
![function in-game](/assets/guide/function_in_game.jpg)   
___
## .mcpack, .mcaddon & .mcworld
Next up are `.mcpack` files. These are used to *import external add-ons*. To create one, all you have to do is *right_click* your `bhv` or your `res`, and zip it (*choose `send to>compressed(zipped) folder`*). Now simply change the extension [*by renaming the file*] from `.zip` to `.mcpack`, to create a file like on the image below. When a user clicks on the file, it'll be automatically opened by and imported to Minecraft, for them to use (Win10 and iOS). (It'll be located in `com.mojang/..._packs`)   

![](/assets/guide/transpiled_mcpack.png)

What if you want both your resource pack and your behavior pack to be imported at once? Make both `.mcpacks`, then select them and choose `send to>compressed(zipped) folder`. Then change `.zip` to `.mcaddon`. Done!
##### Note: Some external programs like AJG and bridge do that automatically.

*Note: same method can be used to compile a world folder from com.mojang/minecraftWorlds and changing the `.zip` to `.mcworld`. On Win10 devices one can click "*Export world*" in the world settings to achieve the same result. `.mcworld`s usually include all add-ons applied (as long as they come from `..._packs`.).*
___
___
## Your progress so far:
**What you've done:**
- [x] Created the manifest and pack_icon files;
- [x] Learned about all the different `.mc` file extensions and how to use them;
- [x] Learned to transfer structures between worlds using Behavior Packs and `.mcstructure` files;
- [x] Created your own function that can be ran like a normal command!

**What are you to do next:**
- [ ] Learn to create custom items;
- [ ] Learn to define texture short-names;
