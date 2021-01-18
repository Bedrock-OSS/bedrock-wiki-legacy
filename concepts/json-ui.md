  ---
layout: page
title: JSON UI
parent: Concepts
---

# JSON UI

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


## Introduction
All editable vanilla UI files are stored in `RP/ui/` in `.json` files. Though the file can have any extension since it will always be read as a JSON file.

They can be divided into three groups:
- System files:
  - `_global_varibles.json` - for variables used in multiple files
  - `_ui_defs.json` - for referencing the files used on the UI.
- Screens:
  - `hud_screen.json`
  - `inventory_screen.json`
  - etc.
- Additional files: (templates, like `ui_common.json`, `ui_templates_*.json` etc.

## UI Defs
In `_ui_defs.json` you add all the files that will be used on the UI.

Imagine I created the files `RP/ui/button.json` and `RP/my_ui/main_menu.json`:

{% include filepath.html path="RP/ui/_ui_defs.json"%}
```jsonc
{
  "ui_defs": [
    "ui/button.json",
    "my_ui/main_menu.json"
  ]
}
```

Three things to notice:
- You have to add the whole directory starting from the RP folder
- You can have files wherever you want. Even `RP/textures/folder_1/papers/sound/scrollpane.json`
- The `_ui_defs.json` in your RP doesn't need to have the vanilla files because all related UI files will not be replaced. Only overwritten.

## Global Variables
Let's say you have a variable `"$info_text_color": [0.8, 0.8, 0.8]` that stores a color for the information texts.
If you use the same value in multiple files instead of repeatedly writing `"color": [0.8, 0.8, 0.8]` you can just reference the variable (`"color": "$info_text_color"`) and put the variable on the `_global_variables.json` file.
Another good advantage of doing that is you only need to change in one place and all the elements that use the variable will have the value updated.

{% include filepath.html path="RP/ui/_global_variables.json"%}
```jsonc
{
 "$info_text_color": [0.8, 0.8, 0.8]
}
```

{% include filepath.html path="RP/my_ui/file1.json"%}
```jsonc
{
  "some_info": {
    ...
    "text": "Hey",
    "color": "$info_text_color"
  }
}
```

{% include filepath.html path="RP/my_ui/file2.json"%}
```jsonc
{
  "info": {
    ...
    "text": "Information",
    "color": "$info_text_color"
  }
}
```

## Namespaces
Namespaces are identifiers for the UI files. They are used to access elements in some file across all other files.
They must be unique and short if possible because you may use it a lot of times.

An example:
{% include filepath.html path="RP/ui/file_a.json"%}
```jsonc
{
  "namespace":"stuff",
  ...
  "foobar": {...} // some UI element
}
```

{% include filepath.html path="RP/ui/file_b.json"%}
```jsonc
{
  "fizzbuzz@stuff.foobar": {...} 
  // "fizzbuzz" extends "foobar" from "stuff" namespace
}
```

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
Variables can store numbers, booleans, strings and arrays.

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "cool_element": {
    ...
    "$foo": 100,         // a number variable
    "$bar": "string",    // a string variable
    "$arr": [10, 10],     // an array variable
    "$elem": "my_button.template_button" // a string pointing at the element
    ...
    // How to use
    "size": "$arr"           // puts the value of $arr into the size property
    "text": "$bar"   // sets text to the value of $bar
    "controls": [
      { "tplt_element@$elem": {} }
    ]
  }
}
```

### Deriving
To derive some element from another you should use `new@super` notation. An example:

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "foobar": {
    ...
    "color": "white",
    "$cool_variable": 777,
    "$fixbugs": false
  },

  // "fizzbuzz" extends "foobar"
  // and replaces $cool_variable value with 666.
  // $fixbugs is still false for fizzbuzz, because it wasn't changed
  "fizzbuzz@foobar": {
    "color": "red",
    "$cool_variable": 666
  } 
}
```

Any property you add to the derive element will completely replace the superior one.
Also you can use a string variable after `@`, its value will be interpreted as a superior element name. You may use it before `@` as well, its value will become the derived element name.

## UI Elements
All the elements must have the `type` property because its value will define what kind of element it is.

Here's an example:

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  ...
  "example_element": {
    "type": "label",
    "text": "Hello World"
    ...
  }
  ...
}
```

Here the element is `type` `label`. So it will render a text.

### Binding names
There are `#things` that have a hash sign in the beginning. They're mostly used in `"property_bag"` objects in form of `"#property": "value"` and in `"bindings"` arrays. They can store the same types that `$variables` can store. More about binding later.



## Element Types
### Grid
If you want to pick an element inside of a grid, create a child derived from the item template and with `"grid_position"` property:

{% include filepath.html path="RP/ui/example_file.json # some_grid"%}
```jsonc
...
  "grid_item_template": "item_template",
  "controls": [
    {
      "grid_element@item_template": {
        "grid_position": [0,0], // grid indexes start from 0
        "offset": [13,42] // for example
      }
    }
  ]
...
```

## Properties
### Bindings
And here's an example of binding one element property to other element property:
{% include filepath.html path="RP/ui/example_file.json # other_element"%}
```jsonc
{
  ...
  "bindings": [
    {
      "binding_type": "view",
      "source_control_name": "some_toggle_element", // source element, which state we want to get
      "source_property_name": "#toggle_state", // source element property
      "target_property_name": "#visible" // this element property that we want to change
    } // so, if "some_toggle_element" is toggled off, this element will become invisible, 
    //and if it's toggled on, this element will become visible
  ]
}
```
Some binding combinations:
```jsonc
{
  "element": {
    ...
    "bindings": [
      {
        "binding_type": "view",
        "source_property_name": "(not #texture = '')",
        "target_property_name": "#visible"
      }
    ]
  }
}
```
```jsonc
{
  "element": {
    ...
    "bindings": [
      {
        "binding_type": "global",
        "binding_name": "#templates_visible",
        "binding_name_override": "#visible"
      }
    ]
  }
}
```
Evaluates two different binding names.
```jsonc
{
  "element": {
    ...
    "bindings": [
      {
        "binding_name": "#using_touch"
      },
      {
        "binding_name": "#is_using_gamepad"
      },
      {
        "binding_type": "view",
        "source_property_name": "(#is_using_gamepad and not #using_touch)",
        "target_property_name": "#visible"
      }
    ]
  }
}
```
Uses a binding name from a collection.
```jsonc
{
  "element": {
    ...
    "bindings": [
      {
        "binding_type": "collection",
        "binding_name": "#pick_item_visible",
        "binding_name_override": "#visible",
        "binding_collection_name": "pick_collection"
      }
    ]
  }
}
```

### Button Mappings
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "button": {
    ...
    "button_mappings": [
      {
        "from_button_id": "button.menu_select",
        "to_button_id": "button.menu_exit", // When clicked it will exit the current screen
        "mapping_type": "pressed"
      },
      {
        "from_button_id": "button.menu_select",
        "to_button_id": "button.menu_exit", // When double clicked it will exit the current screen
        "mapping_type": "double_pressed"
      },
      {
        "from_button_id": "button.menu_ok",
        "to_button_id": "button.menu_exit", // When focused and pressed Enter it will exit the current screen
        "mapping_type": "focused"
      }
    ]
  }
}
```
You can ignore a mapping using the `ignored` property
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "toggle": {
    ...
    "$ignore_double_click_mapping|default": true,
    "button_mappings": [
      {
        "ignored": "$ignore_double_click_mapping",
        "from_button_id": "button.menu_select",
        "to_button_id": "button.menu_exit",
        "mapping_type": "double_pressed"
      }
    ]
  }
}
```

## Operators

| Operator Name          | Operator   | Examples                                                                          |
|------------------------|------------|-----------------------------------------------------------------------------------|
| Addiction              | +          | `"100% + 420px"` `($text + ' my')` `($index + 2)` `('#' + $bdg_nm + '_name')`     |
| Subtraction            | -          | `"100% - 69px"` `($text - ' my')` `($index - 13)`                                 |
| Division               | /          | `($var / 12)` `(#value / 2)`                                                      |
| Equal to               | =          | `($var = 12)` `($var = 'this_text')` `(#name = 'Wither')`                         |
| Greater than           | >          | `(#value > 13)`                                                                   |
| Less than              | <          | `($var < 4)`                                                                      |
| Greater or equal than  | > or =     | `(#value > 2 or #value = 2)`                                                      |
| Less or equal than     | < or =     | `(#value < 2 or #value = 2)`                                                      |
| Logical AND            | and        | `($is_school and $is_open)`                                                       |
| Logical OR             | or         | `($is_cool or $is_awesome)`                                                       |
| Logical NOT            | not        | `(not #name)` `(not #name = 'text')`                                              |

## Animations
`offset` animation example.
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "namespace": "example_nm",

  "anim_offset": {
    "anim_type": "offset",
    "from": [0, 0],
    "to": [10, 10],
    "duration": 2
  },

  "element": {
    ...
    "offset": "@example_nm.anim_offset"
  } 
}
```

`Wait` animation example. It's used when you want no animation between two other animtions.
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "namespace": "example_nm",

  "anim_size_0": {
    "anim_type": "size",
    "from": ["100%", 27],
    "to": ["100% + 3px", 30],
    "duration": 1.25,
    "next": "@example_nm.anim_wait"
  },

  "anim_wait": {
    "anim_type": "wait",
    "duration": 1,
    "next": "@example_nm.anim_size_1"
  },

  "anim_size_1": {
    "anim_type": "size",
    "from": ["100% + 3px", 30],
    "to": ["100%", 27],
    "duration": 1.25,
    "next": "@example_nm.anim_size_0"
  },

  "element": {
    ...
    "size": "@example_nm.anim_size_0"
  } 
}
```

`flip_book` animation example.
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "namespace": "example_nm",

  "anim_flip_book": {
    "anim_type": "flip_book",
    "initial_uv": [0, 0],
    "frame_count": 50,
    "frame_step": 1,
    "fps": 15
    ...
  },

  "image": {
    ...
    "uv": "@example_nm.anim_flip_book"
  } 
}
```

Instead of saying `"offset": "@..."`, `"size": "@..."`, `"alpha": "@..."`, etc, you can reference the animations that will be applied to the element using the `anims` property.
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "namespace": "example_nm",

  "anim_size": {
    "anim_type": "size",
    "from": ["100%", 27],
    "to": ["100% + 3px", 30],
    "duration": 1.25,
    "next": "@..."
  },

  "anim_alpha": {
    "anim_type": "alpha",
    "from": 1,
    "to": 0.5,
    "duration": 2,
    "next": "@..."
  },

  "element": {
    ...
    "anims": [
      "@example_nm.anim_size",
      "@example_nm.anim_alpha"
    ]
  } 
}
```
