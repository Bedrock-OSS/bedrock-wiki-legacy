---
layout: page
title: Tellraw
parent: Documentation
---

# What is tellraw
tellraw sends a JSON message to selected or all players
being usefull for sending plain messages to players ingame
![](/assets/images/Documentation/tellrawshow.png)
# Format
```tellraw <target: target> <raw json message: json>```
this is how the tell raw command is formated
## broken down
``` <target: target>```
The target is expressed as a playername or player groups such as ``@a`` ``@r`` ``@s`` ``@p``
```<raw json message: json>```
this is expressed with `{"rawtext":[{"text":""}]}`
# Examples
This sends the words in the last set of quotes
```/tellraw @a {"rawtext":[{"text":"Hello"}]}```

To use quotaitons in a tellraw message place a backslash to the left side of the quotation mark
```/tellraw @a {"rawtext":[{"text":"§bColor text"}]}```

To insert a line break use \n
```/tellraw @a {"rawtext":[{"text":"Text1\nText2"}]}```

 To have a language changing text
``` /tellraw @a {"rawtext":[{"translate":"accessibility.downloading.complete"}]}```
please note you will need to edit each languages files for this to work

### The titleraw command follows the same theme
