---
layout: page
title: JSON UI
parent: Concepts
badge: NEW
badge_color: blue
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
All editable vanilla UIs are stored in `RP/ui/` in `.json` files. Though the file can have any extension since it will be read always as a JSON file.

They can be divided into three groups:
- Screens: `hud_screen.json`, `inventory_screen.json` etc.
- System files: `_global_varibles.json` and `_ui_defs.json`
- Additional files: (templates, like `ui_common.json`, `ui_templates_*.json` etc.

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
Variables can store numbers, booleans, strings and arrays. It's unknown if they can store elements.

{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "cool_element":{
    ...
    "$foo": 100,         // a number variable
    "$bar": "string",    // a string variable
    "$arr": [10,10],     // an array variable
    "$elem": "template_elem" // a string pointing at the element
    ...
    // How to use
    "size": "$arr"           // puts the value of $arr into the size property
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
You should remember that `controls` property is an array and if you add it to a derived element, it will completely replace the superior one. More about that later.

Also you can use a string variable after `@`, its value will be interpreted as a superior element name. You may use it before `@` as well, its value will become the derived element name, but that'd be a strange move.

### Binding names
There are `#things` that have a hash sign in the beginning. They're mostly used in `"property_bag"` objects in form of `"#property": "value"` and in `"bindings"` arrays. They can store the same types that `$variables` can store. More about binding later.

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

WARNING! Don't create new files using vanilla pre-existing namespaces.


## UI Elements
Most of the element have `type`, `size` and `controls` (**if they have children**).
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

## Binding
Binding allows to bind some hardcoded variable to an element property. Here's an example of binding the game variable to the element property:
{% include filepath.html path="RP/ui/example_file.json # some_object"%}
```jsonc
{
  ...
  "bindings": [
    {
      "binding_name": "#some_binding_name", // a binding name that refers to some hardcoded variable
      "binding_name_override": "#overriden_property", // element property to be overriden
    }
  ]
}
```
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
- `"binding_type"` It may have values of `"collection"`, `"collection_details"`, `"view"` and `"global"`.
- `"binding_condition"` is for deciding when binding happens, it may take any boolean variable or these values:
  - `always` - binding works constantly
  - `always_when_visible` - binding works when visible and does it constantly
  - `once` - seems to happen only once when the element is created
  - `visibility_changed` - seems to happen only when the visibility of the element has changed
  - `visible` - when the element is visible

## Hardcoded magic
If you have looked through vanilla UI files, you may have noticed some thing that don't have any origin. As you may guess, they are hardcoded. What we know about them so far:

### Renderers
**All of them** are hardcoded! No exceptions!

### Binding names
Seems that all binding names that are put in `"binding_name"` are hardcoded variables.

### Collections
It's a hardcoded collection of specific items. Inventory items, hotbar items, armor items and etc. are stored in collections.

### Access to data
Some #names only work on specific screens.

## Element types

### Panel
Like `<div>` in html, `panel` is a usual container.

### Stack Panel
`stack_panel` is a panel that stacks children depending on `orientation` property value (`horizontal` or `vertical`).

### Grid
An element that draws a grid of elements. Grid properties:
- `grid_dimensions` - number of rows and columns in form of `[x_size, y_size]`
- `maximum_grid_items` - numbers of items the grid has
- `grid_rescaling_type` - grid rescaling orientation and possible values are `"vertical"` and `"horizontal"`
- `grid_fill_direction` - possible values are `"vertical"` and `"horizontal"`
- `grid_item_template` - an element capable of handling collections (e.g. `"common.container_item"`)
- `collection_name` - what collection will be parsed (`"hotbar_items"`, `"container_items"`, `"inventory_items"` and etc.)

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

### Label
`label` is a text element. Its properties are:
- `text` - text to display
- `color` - text color, an array of R,G,B with values from 0.0 to 1.0 (e.g. `[0.0, 0.6, 1.0]`)
- `locked_color` - same as `color`. It will be applied instead of `color` if the parent element is locked.
- `text_alignment` - text alignment, takes values `"left"`, `"right"` and `"center".`
- `font_type` - a string. Possible values are `default` (default value), `smooth`, `rune` (enchantment font), `MinecraftSeven`, `MinecraftTen`, `MinecraftTenEmoticon` or a custom font type/family.
- `font_size` - a string. Possible values are `small`, `normal` (default), `large` and `extra-large`
- `font_scale_factor` - a float or an integer. It scales the size of the text.`1` is the default value (It's better to use this rather than `font_size`).
- `shadow` - a boolean

### Image
`image` is a textured element. Its properties are:
- `texture` - required, a path string (e.g. `"textures/ui/title
- `tiled` - tiles the image. Can be a boolean or a string with possible values being `x` and `y` (which orientation it tiles)
- `tiled_scale` - sets the scale of the tiles (if tiled property is true)
- `bilinear` - a boolean. Applies bilinear filtering to the image.
- `grayscale`- a boolean. Makes image black and white.
- `clip_direction` - when `#clip_ratio` is used, tells in which direction will clip go (`down` will tell to clip from the top to the bottom), possible values are `"up"`,`"down"`,`"left"`,`"right"`.

To use clipping, bind a `#*_ratio` binding name to a `#clip-ratio` property with binding condition `"always"`. Progress arrow and fuel images in furnace UI work like this.

### Button
`button` is a button and it can have 4 states (default, hover, pressed and locked). It's recommended to use ready templates if you're not very experienced with them. Properties to be documented.

### Toggle
`toggle` is a toggle and it has 2 states (checked or unchecked). Each state has a hover and locked varient. It's recommended to use ready templates if you're not very experienced with them. Properties to be documented.
Their toggle state can be binded to something by using `"#toggle_state"`.

### Other known types
`dropdown`, `carousel_label`, `slider_box`, `input_panel`, `slider`, `edit_box`, `custom`, `factory`, `scroll_view`, `scroll_track`, `scrollbar_box` and more to be discovered.

