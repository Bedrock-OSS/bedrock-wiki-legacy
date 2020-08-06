---
layout: page
title: tick.json
parent: Knowledge
---
 
# Running functions through tick.json
 
`Tick.json` is server-side file located as `(Root Behavior Folder)/functions/tick.json` that lets you execute function files.

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

While this is a useful file when you're trying to stray away from using repeating command blocks in-game, it's known for executing function files before the world has fully loaded im. This might cause unintended command behavior and crashes, and it's recommended to wait for a more official release of this file.
