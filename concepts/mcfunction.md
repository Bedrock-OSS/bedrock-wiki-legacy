---
layout: page
title: .mcfunction
parent: Concepts
---

# Understanding .mcfunction

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

`mcfunction` files are stored in your BP as `BP/functions/my_function.mcfunction`. You can add as many functions as you like. 

Functions are used to group multiple Minecraft `commands` (such as `/say` or `/teleport`) into managable chunks (or functions). Function files do not begin with `/`.

Example:
```
tag @s add dev
gamemode creative
effect @s night_vision 100000 1 true
```

Functions can be executed in game by typing `/function name_of_function`. This will execute all the commands in the function file, all in a single tick. Nested functions will also run in the same tick as the parent function.

Function files can be nested, for example: `BP/functions/teleport/home.mcfunction` will create a new function called `teleport/home`, which can be called in game like `/function teleport/home`.

Functions can be reloaded from file without leaving the game with the `/reload` command.

# Running functions through tick.json
 
`tick.json` is server-side file located as `BP/functions/tick.json` that lets you execute function files.

Functions will be run each tick, as if placed in a repeating command block.


## Creating tick.json
 
Create a file called tick.json in your root function folder. The format is this:
 
```json
{
    "values": [
        "function_file_name_one",
        "function_file_name_two"
    ]
}
```


## Known Issues

While this is a useful file when you're trying to stray away from using repeating command blocks in-game, it's known for executing function files before the world has fully loaded in. This might cause unintended command behavior and crashes, and it's recommended to wait for a more official release of this file.
