---
layout: page
title: The Editor
parent: Knowledge
---

# The Editor

The coding world is filled with editors. Ranging from command-line tools like VIM or Emacs, all the way up to full IDEs such as InteliJ or Eclipse. 

For editing JSON files, something in the middle is probably the best. Something that offers you a good amount of power, without the bloat of a full on IDE.

## Features to Look For:

 - **Opening Folders:** When editing Addons, it is very convenient to open an entire folder as a project, instead of just individual files. This allows you to edit the files in both the Behavior Pack and Resource Pack at the same time, and quickly switch between tasks. 
 - **Json Linting/Prettify:** Linting is the ability to validate code as correct in real-time. Linting for json will mark things like missing commas, misplaced parens, or other formatting issues so that you can fix them. [Linting can also be found online](https://jsonlint.com/), but having real-time linting built directly into your editor is very much preferred.
 - **Built in Terminal:** I find a terminal built into my editor to be very useful. I often use python scripting to supplement my workflow, and having easy access to a terminal speeds up that workflow.

## VSCode
For those who want a more bare-bones editor, I recommend using Microsoft Studio Code. It contains all of the features I that I feel are important, and it contains little/no bloat.

`Warning:` Do not accidentally install Microsoft Visual *Studio*. This is a different Editor, and not advised. 

[VSCode can be found at this link.](https://code.visualstudio.com/) 

### Setting it up:
Many packaged exist for VSCode that make editing addons easier:
 - [.mcfunction support](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction)
 - [.lang support](https://marketplace.visualstudio.com/items?itemName=zz5840.minecraft-lang-colorizer)
 - [Bedrock Definitions](https://marketplace.visualstudio.com/items?itemName=destruc7i0n.vscode-bedrock-definitions)
 - [Prettt-json](https://marketplace.visualstudio.com/items?itemName=mohsen1.prettify-json)
 - [Spell Checker (for writing wiki)](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
 - [Snowstorm Particle Editor](https://marketplace.visualstudio.com/items?itemName=JannisX11.snowstorm)
 - [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
 - [UUID Generator](https://marketplace.visualstudio.com/items?itemName=netcorext.uuid-generator)

## Bridge
For those new to addons, or for those who want more support while creating addons, I recommend bridge.

[Bridge](https://github.com/bridge-core/bridge.) is an Editor designed specifically for editing Minecraft addons. It has some very powerful features, such as auto-complete, file validation and easy creation of new packs.

If you choose to use Bridge, you should be aware that it is a application that you benefit most from when you use it exclusively for editing your addon. Switching between a different editor and Bridge creates a bit of an overhead in your workflow (more later). The app builds up a knowledge base of your files as you use the editor. This enables very fast and dynamic auto-completions and file validation but also means that all of your files are cached in the background by default. There are two ways to workaround Bridge's caching strategy:
1) Increase or remove the `bridge-file-version: #11` comment the app leaves in your files after editing a file without Bridge
2) Add files that you want to edit without Bridge to a .no-cache file at the root of your behavior pack

Due to the nature of the file versioning system, most scripts and tools will continue to work as expected.

For further guidance on the editor, feel free to contact [solvedDev](https://twitter.com/solvedDev).

## Other good editors:
 - Sublime text
 - Notepad++
 - Atom
