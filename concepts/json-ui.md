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
All editable vanilla UIs are stored in `RP/ui/` in `.json` files. Though the file can have any extension since it will always be read as a JSON file.

They can be divided into two groups:
- System files:
  - `_global_varibles.json` - for variables used in multiple files
  - `_ui_defs.json` - for referencing the files used on the UI
- Screens:
  - `hud_screen.json`
  - `inventory_screen.json`
  - etc.

Additional files: (templates, like `ui_common.json`, `ui_templates_*.json` etc.

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

## Bindings
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
- `"binding_name"`
- `"source_control_name"` - name of the object to be evaluated
- `"source_property_name"` - property name from the `source_control_name` object
- `"target_property_name"` - property that its value will be override by the `source_property_name` value
- `"binding_name_override"` - property that its value will be override by the `binding_name` value
- `"binding_collection_name"`
- `"binding_collection_prefix"`
- `"binding_condition"` is for deciding when binding happens, it may take any boolean variable or these values:
  - `always` - binding works constantly
  - `always_when_visible` - binding works when visible and does it constantly
  - `once` - seems to happen only once when the element is created
  - `visibility_changed` - seems to happen only when the visibility of the element has changed
  - `visible` - when the element is visible
- `"resolve_sibling_scope"` - boolean

## Button Mappings
- `"from_button_id"` - button (action) id that fires
- `"to_button_id"` - button (action) id that results
- `"handle_select` - boolean 
- `"handle_deselect` - boolean 
- `"mapping_type"`
  - `pressed`
  - `focused`
  - `global`
- `"scope"`
  - `view`
  - `controller` 
- `"input_mode_condition"`
  - `gamepad_and_not_gaze`
  - `not_gaze` 
- `"button_up_right_of_first_refusal"` - boolean 

## Hardcoded magic
If you have looked through vanilla UI files, you may have noticed some thing that don't have any origin. As you may guess, they are hardcoded. What we know about them so far:

### Binding names
Seems that all binding names that are put in `"binding_name"` are hardcoded variables.

### Collections
It's a hardcoded collection of specific items. Inventory items, hotbar items, armor items and etc. are stored in collections.

### Access to data
Some #names only work on specific screens.

## Common Properties
- `size`- width and height of the element `[width, height]`. Possible values:
  - `default` default value
  - `0` raw number of pixels
  - `"0px"` number of pixels. It's the same as `0` but it's put inside a string with `px` at the end. It's used when you want to sum a percentage based value with a specific number of pixels. (e.g. `"75% + 12px"`)
  - `"0%"` percentage of relative to the parent element
  - `"0%c"` percentage of the total width/height of the element children
  - `"0%cm"` percentage of the width/height of the biggest child of that element
  - `"0%sm"` percentage of the width/height of the sibling element
  - `"0%y"` percentage of the element height
  - `"0%x"` percentage of the element width
  - `"fill"` expands to the size of the parent element
- `max_size` - max width and height for the element
- `min_size` - min width and height the element can have
- `anchor_from` and `anchor_to` - position origin of the element. Possible values for both of them are `top_left`, `top_middle`, `top_right`, `left_middle`, `center` (default value), `right_middle`, `bottom_left`, `bottom_middle` and `bottom_right`
- `offset`- how far in pixels or percentage from the position origin the element is (`[x_offset, y_offset]`). Possible values include `0`, `"0px"`, `"0%"`, `"0%c"`, `"100%cm"`, `"0%y"` and `"0%x"
- `clips_children` - boolean
- `allow_clipping` - boolean
- `layer` - a number (positive or negative). the layer (like `z-index` in CSS) of the element relative to it's parent and so on. An element with a greater layer will be in front of an element with a lower layer.
- `visible` - a boolean. if false, element takes place, but isn't rendered (unlike ignored). It's by default true so you don't have to mention it every time you create a new element
- `ignored` - a boolean. Ignores element like if it isn't there (unlike not visible)
- `enabled` - a boolean. If false it will disable all input elements inside of it.
- `alpha` - number from 0.0 to 1.0. Opacity of the image or text. If it's defined in any other type it won't affect any image/text child inside of it. For that you need to enable `propagate_alpha`
- `locked_alpha` - same as `alpha`. It will be applied instead of `alpah` if the parent element is locked
- `propagate_alpha` - boolean. Propagate the alpha property to any image or text child.
- `anims`
- `animation_reset_name`
- `variables`
- `property_bag`
- `controls`
- `bindings`

## Focus Properties
- `focus_identifier`
- `focus_enabled` - boolean
- `focus_wrap_enabled` - boolean 
- `focus_magnet_enabled` - boolean 
- `default_focus_precedence` - number
- `focus_container` - boolean
- `use_last_focus`- boolean
- `focus_change_up` - possible values are `FOCUS_OVERRIDE_STOP` or the `focus_identifier` of the object you want to focus when on `button.menu_up`
- `focus_change_down` - possible values are `FOCUS_OVERRIDE_STOP` or the `focus_identifier` of the object you want to focus when on `button.menu_down`
- `focus_change_left` - possible values are `FOCUS_OVERRIDE_STOP` or the `focus_identifier` of the object you want to focus when on `button.menu_left`
- `focus_change_right` - possible values are `FOCUS_OVERRIDE_STOP` or the `focus_identifier` of the object you want to focus when on `button.menu_right`
- `focus_nagivation_mode_up` - possible values are  `none`, `stop`, `custom` and `contained`
- `focus_nagivation_mode_down` - possible values are  `none`, `stop`, `custom` and `contained`
- `focus_nagivation_mode_left` - possible values are  `none`, `stop`, `custom` and `contained`
- `focus_nagivation_mode_right` - possible values are  `none`, `stop`, `custom` and `contained`
- `focus_container_custom_up`
- `focus_container_custom_down`
- `focus_container_custom_left`
- `focus_container_custom_right`

## TTS Properties
- `tts_name`
- `tts_control_header`
- `tts_section_header`
- `tts_control_type_order_priority` - number
- `tts_index_priority` - number
- `tts_override_control_value`
- `tts_ignore_count` - boolean
- `tts_inherit_siblings` - boolean
 

## Element Types

### Panel
Like `<div>` in HTML, `panel` is a usual container.

### Stack Panel
`stack_panel` is a panel that stacks children depending on `orientation` property value (`horizontal` or `vertical` (default)).

### Input Panel
`input_panel` is a panel that can receive input.

Specific properties:
- `modal` - boolean 
- `inline_modal` - boolean
- `hover_enabled` - boolean
- `prevent_touch_input` - boolean
- `gesture_tracking_button` - button (action) id
- `always_handle_controller_direction` - boolean

### Grid
An element that draws a grid of elements. Grid properties:
- `grid_dimensions` - number of rows and columns in form of `[x_size, y_size]`
- `maximum_grid_items` - numbers of items the grid has
- `grid_rescaling_type` - grid rescaling orientation and possible values are `"vertical"` and `"horizontal"`
- `grid_fill_direction` - possible values are `"vertical"` and `"horizontal"`
- `grid_item_template` - an element capable of handling collections (e.g. `"common.container_item"`)
- `collection_name` - what collection will be parsed (`"hotbar_items"`, `"container_items"`, `"inventory_items"` and etc.)
- `grid_dimension_binding` - binding name for grid dimensions

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
- `shadow` - a boolean. Adds a shadow to text
- `localize` - a boolean. Translate the text using the *_*.lang files
- `enable_profanity_filter` - a boolean. Filters bad words included on the `profanity_filter.wlist` file
- `hide_hyphen` - a boolean. Hide all hyphens in the text
- `notify_on_ellipses`

### Image
`image` is a textured element. Its properties are:
- `texture` - required, a path string (e.g. `"textures/ui/title
- `tiled` - tiles the image. Can be a boolean or a string with possible values being `x` and `y` (which orientation it tiles)
- `tiled_scale` - sets the scale of the tiles (if tiled property is true)
- `bilinear` - a boolean. Applies bilinear filtering to the image
- `grayscale`- a boolean. Makes image black and white
- `fill` - boolean
- `$fit_to_width`- boolean
- `keep_ratio` - boolean. Keep the image ratio
- `clip_direction` - when `#clip_ratio` is used, tells in which direction will clip go (`down` will tell to clip from the top to the bottom), possible values are `"up"`,`"down"`,`"left"`,`"right"`.
- `uv` - `[x_offset, y_offset]`
- `uv_size` - `[width, height]`
- `nineslice_size` - a number, `[x, y]` or `[x1, y1, x2, y2]`
- `base_size` - `[base_width, base_height]`
- `zip_folder`
- `texture_file_system`
- `force_texture_reload` - boolean

To use clipping, bind a `#*_ratio` binding name to a `#clip-ratio` property with binding condition `"always"`. Progress arrow and fuel images in furnace UI work like this.

### Button
`button` is a button and it can have 4 states (default, hover, pressed and locked). It's recommended to use ready templates if you're not very experienced with them.

Specific properties:
- `default_control` - name of the child that will be displayed only in default state.
- `hover_control` - name of the child that will be displayed only in hover state.
- `pressed_control` - name of the child that will be displayed only in pressed state.
- `locked_control` - name of the child that will be displayed only in locked state.
- `sound_name` - name of the sound defined in the `sounds/sound_definitions.json` file that plays when the button is clicked
- `sound_volume` - number
- `sound_pitch` - number

### Toggle
`toggle` is a toggle and it has 2 states (checked or unchecked). Each state has a hover and locked varient. It's recommended to use ready templates if you're not very experienced with them.
Their toggle state can be binded to something by using `"#toggle_state"`.

Specific properties:
- `toggle_name`
- `toggle_default_state`
- `radio_toggle_group` - boolean.
- `toggle_group_forced_index` 
- `toggle_group_default_selected`
- `toggle_grid_collection_name`
- `enable_directional_toggling` - boolean
- `toggle_on_button` - toggle (action) id
- `toggle_off_button` - toggle (action) id
- `reset_on_focus_lost` - boolean
- `checked_control` - name of the child that will be displayed only in checked state.
- `unchecked_control` - name of the child that will be displayed only in unchecked state.
- `checked_hover_control` - name of the child that will be displayed only in checked and hovered state.
- `unchecked_hover_control` - name of the child that will be displayed only in unchecked and hovered state.
- `checked_locked_control` - name of the child that will be displayed only in locked state.
- `unchecked_locked_control` - name of the child that will be displayed only in locked state.
- `checked_locked_hover_control` - does not work
- `unchecked_locked_hover_control` - does not work
- `sound_name` - name of the sound defined in the `sounds/sound_definitions.json` file that plays when the toggle is clicked
- `sound_volume` - number
- `sound_pitch` - number

Specific TTS:
- `tts_toggle_on`
- `tts_toggle_off`

Specific property bag:
- `#toggle_state` - boolean

### Slider
`slider` is a slider.

Specific properties:
- `slider_name`
- `slider_direction` - the orientation of the slider. Possible values `vertical` and `horizontal`
- `slider_steps` - number of possible values
- `slider_track_button` - button (action) id
- `slider_small_decrease_button` - button (action) id
- `slider_small_increase_button` - button (action) id
- `slider_selected_button` - button (action) id
- `slider_deselected_button` - button (action) id
- `slider_collection_name` - name of the collection the slider belongs to
- `default_control` - name of the child that will be displayed only in default state
- `hover_control` - name of the child that will be displayed only in hover state
- `background_control` - name of the object used as the slider background only in default state
- `background_hover_control` - name of the object used as the slide background only in hover state
- `progress_control` - name of the object used as the progress background only in default state
- `progress_hover_control` - name of the object used as the progress background only in hover state
- `slider_box_control` - name of the child that will be used as the scroll "thumb"/button
- `slider_select_on_hover` -  boolean. Focus slider when it's hovered.

Specific TTS
- `tts_value_changed`

Specific property bag:
- `#slider_steps` - number
- `#slider_value` - number

Specific factory names and control ids:
- `slider_step_factory`. Control IDs: `slider_step`, `slider_step_hover`, `slider_step_progress` and `slider_step_progress_hover`

### Slider Box
`slider_box` is the slider button that you use to change the slider value.

Specific properties:
- `default_control` - name of the child that will be displayed only in default state.
- `hover_control` - name of the child that will be displayed only in hover state.
- `locked_control` - name of the child that will be displayed only in locked state.
- `indent_control` - name of the child that will be displayed only in indent state.

### Edit Box
`edit_box` is a text field element. By default it's single-lined.

Specific properties:
- `text_box_name`
- `text_edit_box_grid_collection_name` - name of the collection the `edit_box` belongs to
- `text_type` - type of characters that the user is allowed to type in th text field
- `max_length` - max number of characters allow in the text field
- `enabled_newline` - boolean. Allows multiline text
- `default_control` - name of the child that will be displayed only in default state
- `hover_control` - name of the child that will be displayed only in hover state
- `pressed_control` - name of the child that will be displayed only in pressed state
- `locked_control` - name of the child that will be displayed only in locked state
- `text_control` - name of the child that will be used for display the text
- `place_holder_control` - name of the child that will be used for display the placeholder text
- `virtual_keyboard_buffer_control`

### Scroll View
`scroll_view` creates a scrolling panel element.

Specific properties:
- `scroll_speed` number. Scrolling speed.
- `always_handle_scrolling` - boolean
- `jump_to_bottom_on_update` - boolean
- `touch_mode` - boolean
- `scrollbar_track_button` - button (action) id
- `scrollbar_touch_button`- button (action) id
- `scrollbar_track` - name of the child to be used as the scrollbar track
- `scrollbar_box` - name of the child to be used as the scrollbar "thumb"/button
- `scroll_content` - name of the child that will have the scrolling panel content
- `scroll_view_port` - name of the child to be used as the scrolling panel viewport
- `scroll_box_and_track_panel` - name of the child that contains the scroll bar and track

### Scroll Track
`scroll_track` is the scrollbar track.

### Scrollbar Box
`scrollbar_box` is the scrollbar "thumb"/button. The draggable scrolling handle. By default is oriented vertically.

Specific properties:
- `draggable` - which orientation it scrolls with possible value `vertical` (default), `horizontal`
- `contained` - a boolean

### Dropdown
`dropdown` is a toggle for dropdown purposes.

Specific properties (includes toggle properties):
- `dropdown_name`
- `dropdown_content_control` - name of the child that will have the dropdown content
- `dropdown_area`

### Factory
`factory`

Specific properties:
- `control_ids`

### Custom
`custom`

- `renderer`- name of the hardcoded renderer. Possible values:
  - `flying_item_renderer` - the flying item when you change an item from a slot to another
  - `inventory_item_renderer` - renders an item icon. It only work in screens when in-game
  - `credits_renderer` - the credits and end poem
  - `vignette_renderer` - a vignette
  - `name_tag_renderer` - it's something like the playername above the player head or the name above animals when used a nametag on them
  - `paper_doll_renderer` - a skin model
  - `debug_screen_renderer` - the debug text that appears on the beta versions
  - `enchanting_book_renderer` - the enchantment table book. It opens when there's an item to be enchanted
  - `gradient_renderer` - draws a gradient
  - `live_horse_renderer` - the horse/donkey/... model
  - `live_player_renderer` - the player model
  - `hud_player_renderer` - the player model that imitates what the player is doing
  - `hotbar_renderer` - gets the hotbar slot image for each slot
  - `hotbar_cooldown_renderer` - draws the item cooldown
  - `heart_renderer` - draws the player health
  - `horse_heart_renderer` - draws the horse/donkey/... health
  - `armor_renderer` - draws the player armor
  - `horse_jump_renderer` - draws the horse jumping progress bar
  - `hunger_renderer` - draws the player hunger
  - `bubbles_renderer` - draws the respiration bubbles
  - `mob_effects_renderer` - draws the effects that are applied to the player
  - `cursor_renderer` - draws the crosshair in the center of the screen
  - `progress_indicator` - mysterious
  - `camera_renderer` - used for the camera item
  - `web_view_renderer` - shows a website
  - `banner_pattern_renderer` - renders a banner
  - `actor_portrait_renderer` - draws an portrait
  - `trial_time_renderer` - in the trial version of the game it renders the time left to be able to use the world
  - `progress_bar_renderer` - draws a progress bar. It has more than one type
  - `3d_structure_renderer` - renders the structure block structure
  - `splash_text_renderer` - gets and renders a random splash text from the `splashes.json` file
  - `hover_text_renderer` - draws a tooltip
  - `ui_holo_cursor`
  - `panorama_renderer` - It's not the panoramas that appear behind the menus. It's the panorama of the worlds on the store.
  
Specific properties, property bag, etc depends of the renderer being used.

### Screen
`screen`

Specific properties:
- `send_telemetry` - boolean
- `screen_not_flushable` - boolean
- `is_modal` - boolean. It's a screen modal
- `is_showing_menu` - boolean
- `render_game_behind` - boolean. Doesn't prevent screen below of being able to receive input from the user
- `low_frequency_rendering` - boolean. Uses less memory to render the screen
- `should_steal_mouse` - boolean. Removes the mouse pointer/cursor
- `render_only_when_topmost` - boolean. If false it will always render/draw the screen below all of others
- `screen_draws_last` - boolean. It's the last screen to be drawn/rendered
- `force_render_below` - boolean. Renders previous screen below current screen
- `always_accepts_input` - boolean. Accepts input from the user
- `close_on_player_hurt` - boolean. Closes the screen if the player is hurted

## Animations
`anim_type`

- `initial_uv` - `[0, 0]`
- `frame_count` - number
- `frame_steps` - number
- `reversible` - boolean
- `scale_from_starting_alpha` - boolean
- `fps` - number of frames per second
- `easing` - possible values are `linear`, `spring`, `in_sine`, `in_quart`, `in_quint`, `in_expo`, `out_expo`, `out_cubic` and `out_back` 
- `duration` - number. Duration of the animation
- `from` - number (`anim_type` alpha) or a `size`/`offset` array (`anim_type` size/offset)
- `to` - number (`anim_type` alpha) or a `size`/`offset` array (`anim_type` size/offset) 
- `destroy_at_end` - name of the object to destroy (stop rendering/ignored) when the animation ends
- `next` - name of the animation that will play after this ends
- `resettable` - boolean
- `play_event` - name of the event when the animation starts 
- `end_event` - name of the event when the animation ends 

## Hardcoded Variables
- `$trial` - if it is in the trial version of the game
- `$is_publish` - if it is public and not a developer version
- `$is_pregame` - if it is "outgame" not ingame
- `$is_xbox_live_enabled` 
- `$desktop_screen` - if the classic UI is selected
- `$pocket_screen` - if the pocket UI is selected
- `$win10_edition`
- `$pocket_edition`
- `$education_edition`
- `$education_edition_china`
- `$console_edition`
- `$osx_edition`
- `$nx_edition`
- `$fire_tv`
- `$gear_vr`
- `$supports_cross_platform_play_toggle`
- `$ignore_profile_switch_account_button`
- `$ignore_profile_sso_toggle`
- `$is_settopbox`
- `$is_reality_mode`
- `$storage_location_switch_enabled`
- `$thirdpartyconsole`
- `$is_ps4`
- `$psvr`
- `$supports_hand_controllers`
- `$is_ios` or `$ios`
- `$is_android`
- `$is_win10_arm`
- `$display_copyright_info`
- `$is_windows_10_mobile`
- `$device_must_be_removed_for_xbl_signin`
- `$build_platform_UWP`
- `$requires_xbl_signin_to_play`
- `$supports_user_configured_safezone`
- `$can_splitscreen`
- ...

## Hardcoded Button IDs
Some of them only work in specific screens.

- `button.menu_exit`
- `button.menu_play`
- `$play_button_target` (hardcoded variable)
- `button.menu_store`
- `button.menu_achievements`
- `button.menu_settings`
- `button.signin`
- `button.menu_skins`
- `button.to_profile_screen`
- `button.menu_courses`
- `button.menu_tutorial`
- `button.featured_world`
- `button.switch_accounts`
- `button.launch_editions`
- `button.edu_feedback`
- `button.edu_resources`
- `button.menu_buy_game`
- `button.menu_invite_notification`
- `button.search`
- `button.select_offer`
- `button.action_button`
- `button.create_realm`
- `button.tos_hyperlink`
- `button.privpol_hyperlink`
- `button.tos_popup`
- `button.privpol_popup`
- `button.binding_button`
- `button.reset_binding`
- `button.reset_keyboard_bindings`
- `button.view_account_errors`
- `button.switch_accounts`
- `button.open_content_log_history`
- `button.clear_content_log_files`
- `button.clear_msa_token_button`
- `button.terms_and_conditions_popup`
- `button.credits`
- `button.unlink_msa`
- `button.attribute_popup`
- `button.licensed_content`
- `button.font_license`
- ...

Keyboard Keys/Mouse/Controller Buttons/etc IDs (`from_button_id`):
- `button.menu_exit`
- `button.menu_cancel`
- `button.menu_inventory_cancel`
- `button.menu_ok`
- `button.menu_select`
- `button.controller_select`
- `button.menu_secondary_select`
- `button.controller_secondary_select`
- `button.controller_secondary_select_left`
- `button.controller_secondary_select_right`
- `button.controller_start`
- `button.menu_up`
- `button.menu_down`
- `button.menu_left`
- `button.menu_right`
- `button.menu_tab_left`
- `button.menu_tab_right`
- `button.menu_alternate_tab_left`
- `button.menu_alternate_tab_right`
- `button.menu_autocomplete`
- `button.menu_autocomplete_back`
- `button.controller_autocomplete`
- `button.controller_autocomplete_back`
- `button.menu_textedit_up`
- `button.menu_textedit_down`
- `button.controller_textedit_up`
- `button.controller_textedit_down`
- `button.menu_auto_place`
- `button.menu_inventory_drop`
- `button.menu_inventory_drop_all`
- `button.menu_clear`
- `button.chat`
- `button.mobeffects`
- `key.emote`
- `button.slot1` (Emote Wheel)
- `button.slot2` (Emote Wheel)
- `button.slot3` (Emote Wheel)
- `button.slot4` (Emote Wheel)
- `button.slot5` (Emote Wheel)
- `button.slot6` (Emote Wheel)
- `button.inventory_right`
- `button.inventory_left`
- `button.scoreboard`
- `button.hide_gui`
- `button.hide_tooltips`
- `button.hide_paperdoll`
- `button.slot0`
- `button.slot1`
- `button.slot2`
- `button.slot3`
- `button.slot4`
- `button.slot5`
- `button.slot6`
- `button.slot7`
- `button.slot8`
- `button.slot9`
- `button.menu_vr_realign`
- `any` (literally the name of it)

Button IDs (`to_button_id`):
- `button.anvil_take_all_place_all`
- ...
