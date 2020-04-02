---
layout: page
title: The Editor
parent: Knowledge
---

# The Editor

The coding world is filled with editors. Ranging from command-line tools like VIM or Emacs, all the way up to full IDEs such as InteliiJ or Eclipse. 

For editing Json files, something in the middle is probably the best. Something that offers you a good ammount of power, without the bloat of a full on IDE.

## Features to Look For:

1) **Opening Folders:** When editing Addons, it is very convient to open an entire folder as a project, instead of just individual files. This allows you to edit the files in both the Behavior Pack and Resource Pack at the same time, and quickly switch between tasks. 
2) **Json Linting/Prettify:** Linting is the ability to validate code as correct in real-time. Linting for json will mark things like missing commas, missplaced parens, or other formating issues so that you can fix them. Linting can also be found [online](https://jsonlint.com/), but having real-time linting built directly into your editor is very much preffered.
3) **Built in Terminal:** I find a terminal built into my editor to be very useful. I often use python scripting to supliment my workflow, and having easy access to a terminal speeds up that workflow.

## A note about Bridge:
[Bridge](https://github.com/bridge-core/bridge.) is an Editor designed specifically for editing Minecraft addons. It has some very powerful features, such as auto-complete, and easy creation of new packs.

Personally however, bridge has a very problematic limiting factor: Bridge does not like when you edit files outside of Bridge! This makes any and all outside scripts or tools incompatible. Since this is such an importent part of *my* workflow, I can't efficiently use Bridge.

If you choose to use Bridge, just be aware that you are tying yourself to that editor for the duration of that project. 

## My Recomendation:
I recommend using Microsoft Studio Code. It contains all of the features I that I feel are importent, and it contains little/no bloat.

Warning: Do not accidently install Microsoft Visual *Studio*. This is a different Editor, and not advised. 

[VSCode can be found at this link.](https://code.visualstudio.com/) 

### Setting it up:
I suggest getting the `prettify json` package for VSCode.