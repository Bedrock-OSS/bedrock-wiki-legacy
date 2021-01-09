---
layout: page
title: Json-UI
parent: Concepts
badge: New!
badge_color: blue
---

# Items [BETA]

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


# Json UI

## Introduction
All editable vanilla UIs are stored in `RP/ui/` in `.json` files.

They can be divided into three groups:
- Screens: `hud_screen.json`, `inventory_screen.json` etc.
- Additional files: (templates, like `ui_common.json`, `ui_templates_*.json` etc.
- System files: `_global_varibles.json` and `_ui_defs.json`

## Screens
Screen files contain UIs which are shown in appropriate situations:
- `hud_screen` is used in HUD
- `inventory_screen` is used in Inventory screen
- etc.

All files are pretty self-explanatory. An important thing to notice is that **different screens can access different variables**. More about that later.

## Notations
So, what are variables and how can elements derive from others?

### Variables
Everything that has `$` as the first letter of its name is a variable.
Variables can store numbers, strings and arrays. It's unknown if they can store elements, but it'd be pointless then.

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "cool_element":{
    ...
    "$foo": 100,         // a number variable
    "$bar": "string",    // a string variable
    "$arr": [10,10],     // an array variable
    ...
    // How to use
    "size": "$arr"           // puts the value of $arr into the size parameter
    "string_param": "$bar"   // sets string_param to the value of $bar
  }
}
```

### Deriving
To derive some element from another you should use `new@super` notation. An example:

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "foobar": {
    "$cool_variable": 777,
    "$fixbugs": false
  },

  // "fizzbuzz" extends "foobar"
  // and replaces $cool_variable value with 666.
  // $fixbugs is still false for fizzbuzz, because it wasn't changed
  "fizzbuzz@foobar": {
    "$cool_variable": 666
  } 
}
```
You should remember that `controls` parameter is an array and if you add it to a derived element, it will completely replace superior one. More about that later.

## Namespaces
Namespaces are used to access elements in some file across all other files.
An example:


{% include filepath.html path="RP/ui/file_a.json"%}
```json
{
  "namespace":"stuff",
  ...
  "foobar": {...} // some UI element
}
```

{% include filepath.html path="RP/ui/file_b.json"%}
```json
{
  "fizzbuzz@stuff.foobar": {...} 
  // "fizzbuzz" extends "foobar" from "stuff" namespace
}
```

This definitely works with UI elements. It is unknown if it works with variables yet.

## UI Elements
Most of the element have `type`, `size` and `controls` (if they have children).
A typical element looks like this:


{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  ...
  "typical_element@common.template_element": { //"common" is ui_common.json namespace
    "size": [32, 32],
    "$template_var": "new_value",

    //and if we want it to have children
    "controls": [
      {
        "child1@some_other_template": {...}
      }, 
      ...
    ]
  }
  ...
}
```

## Hardcoded magic

If you looked through vanilla UI files, you may noticed some thing that don't have any origin. As you may guess, they are hardcoded. What we know about them so far:

### Renderers
**All of them** are hardcoded! No exceptions!

### Hash-names
These are somehow connected to binding (`#example_thing`). Also, none of them can be changed and there's no full list of them.

### Access to variables
Different screens can access different variables.
It's a trial and error experience, but what we know so far:
- HUD can't access inventory collection (only hotbar), armor collection and perspective change (so, no F5 addons, also F1 works differently)
