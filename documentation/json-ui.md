---
layout: page
title: JSON UI
parent: Documentation
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

## Element Types

### Panel
Like `<div>` in HTML, `panel` is a usual container.

### Stack Panel
`stack_panel` is a panel that stacks children depending on `orientation` property value.

Specific properties:
- `orientation` - values are `vertical` (default) and `horizontal`

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
An element that draws a grid of elements.

- `collection_name` - what collection will be parsed (`"hotbar_items"`, 
  
Specific properties:
- `grid_dimensions` - number of rows and columns in form of `[x_size, y_size]`
- `maximum_grid_items` - numbers of items the grid has. An alternative to `grid_dimensions`
- `grid_rescaling_type` - grid rescaling orientation and possible values are `"vertical"` and `"horizontal"`
- `grid_fill_direction` - possible values are `"vertical"` and `"horizontal"`
- `grid_item_template` - an element capable of handling collections (e.g. `"common.container_item"`), `"container_items"`, `"inventory_items"` and etc.)
- `grid_dimension_binding` - binding name for grid dimensions

### Label
`label` is a text element. Its properties are:
- `text` - text to display
- `color` - text color, an array of R,G,B with values from 0.0 to 1.0 (e.g. `[0.0, 0.6, 1.0]`)
- `locked_color` - same as `color`. It will be applied instead of `color` if the parent element is locked.
- `text_alignment` - text alignment, takes values `"left"`, `"right"` and `"center".`
- `line_padding` - number. Space in pixels between lines.
- `font_type` - a string. Possible values are `default` (default value), `smooth`, `rune` (enchantment font), `MinecraftSeven`, `MinecraftTen`, `MinecraftTenEmoticon` or a custom font type/family.
- `font_size` - a string. Possible values are `small`, `normal` (default), `large` and `extra-large`
- `font_scale_factor` - a float or an integer. It scales the size of the text.`1` is the default value (It's better to use this rather than `font_size`).
- `shadow` - a boolean. Adds a shadow to text
- `localize` - a boolean. Translate the text using the \*_\*.lang files
- `enable_profanity_filter` - a boolean. Filters bad words included on the `profanity_filter.wlist` file
- `hide_hyphen` - a boolean. Hide all hyphens in the text
- `notify_on_ellipses` - `[]` array of the name of the objects it will receive #using_ellipses when the text has '...'

Use of `notify_on_ellipses`. Mostly used with hardcoded texts.
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "label": {
    ...
    "notify_on_ellipses": [
      "my_button"
    ]
  },

  "my_button": {
    ...
    "bindings": [
      {
        "binding_type": "view",
        "source_property_name": "#using_ellipses",
        "target_property_name": "#visible"
      }
    ]
  }
}
```

### Image
`image` is a textured element. Its properties are:
- `texture` - required, a path string (e.g. `"textures/ui/title
- `tiled` - tiles the image. Can be a boolean or a string with possible values being `x` and `y` (which orientation it tiles)
- `tiled_scale` - sets the scale of the tiles (if tiled property is true)
- `bilinear` - a boolean. Applies bilinear filtering to the image
- `grayscale`- a boolean. Makes image black and white
- `fill` - boolean
- color - same as the `color` from `label` type. Only works if the texture is fully white or black 
- `$fit_to_width`- boolean
- `keep_ratio` - boolean. Keep the image ratio
- `clip_direction` - when `#clip_ratio` is used, tells in which direction will clip go (`down` will tell to clip from the top to the bottom), possible values are `"up"`,`"down"`,`"left"`,`"right"`.
- `uv` - `[x_offset, y_offset]`
- `uv_size` - `[width, height]`
- `nineslice_size` - a number, `[x, y]` or `[x1, y1, x2, y2]`
- `base_size` - `[base_width, base_height]`
- `zip_folder` - string. Used with hardcoded paths
- `texture_file_system` - string. Used with hardcoded paths
- `force_texture_reload` - boolean. Reload image when the texture path is changed

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
- `toggle_name` - string
- `toggle_default_state` - boolean
- `radio_toggle_group` - boolean.
- `toggle_group_forced_index` - number
- `toggle_group_default_selected` - index of the default toggle of the its group
- `toggle_grid_collection_name` - name of the collection the toggle belongs to
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
- `tts_toggle_on` - string
- `tts_toggle_off` - string

Specific property bag:
- `#toggle_state` - boolean

### Slider
`slider` is a slider.

Specific properties:
- `slider_name` - string
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
- `tts_value_changed` - string

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
- `virtual_keyboard_buffer_control` - string

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
- `dropdown_name` - string
- `dropdown_content_control` - name of the child that will have the dropdown content
- `dropdown_area` - string

### Factory
`factory`

Specific properties:
- `control_ids` - `{}`

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

## Properties
### Common Properties
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
- `offset`- how far in pixels or percentage from the position origin the element is (`[x_offset, y_offset]`). Possible values include `0`, `"0px"`, `"0%"`, `"0%c"`, `"100%cm"`, `"0%y"` and `"0%x`
- `clips_children` - boolean. Hides everything inside that is outside of the width and height of the element
- `allow_clipping` - boolean. Allows to `clips_children` to clip the element. if false `clips_children` won't affect the element
- `layer` - a number (positive or negative). the layer (like `z-index` in CSS) of the element relative to it's parent and so on. An element with a greater layer will be in front of an element with a lower layer.
- `visible` - a boolean. if false, element takes place, but isn't rendered (unlike ignored). It's by default true so you don't have to mention it every time you create a new element
- `ignored` - a boolean. Ignores element like if it isn't there (unlike not visible)
- `enabled` - a boolean. If false it will disable all input elements inside of it.
- `alpha` - number from 0.0 to 1.0. Opacity of the image or text. If it's defined in any other type it won't affect any image/text child inside of it. For that you need to enable `propagate_alpha`
- `locked_alpha` - same as `alpha`. It will be applied instead of `alpah` if the parent element is locked
- `propagate_alpha` - boolean. Propagate the alpha property to any image or text child.
- `disable_anim_fast_forward` - boolean
- `anims` - `[]`. Name of the animations that will apply to the element
- `animation_reset_name` - string
- `variables` - `[]` or `{}`. Have conditions that change the variables values.
- `property_bag` - `{}`. Change some special properties.
- `controls` - `[]`. To add children to the element
- `bindings` - `[]`. Bind and work with hardcoded values in the element

### Focus Properties
- `focus_identifier` - string
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
  - `other_focus_container_name` - name of the object that will receive focus when the focus of this container ends on `button.menu_up`
- `focus_container_custom_down`
- `focus_container_custom_left`
- `focus_container_custom_right`

For `focus_container_custom_*`
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
...
{
  "other_panel": {
    ...
    "focus_container": true,
    "controls": [
      ...
    ]
  }
},
{
  "input_panel": {
    ...
    "focus_container_custom_up": [
      {
        "other_focus_container_name": "other_panel"
      }
    ]
  }
}
...
```

### TTS Properties
- `tts_name` - string
- `tts_control_header` - string
- `tts_section_header` - string
- `tts_control_type_order_priority` - number
- `tts_index_priority` - number
- `tts_override_control_value` - string
- `tts_ignore_count` - boolean
- `tts_inherit_siblings` - boolean

### Bindings Property
Binding allows to bind hardcoded values/variables to an element property.

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

### Button Mappings Property
Button mappings can be applied to any kind of input elements (`button`, `toggle`, `slider` and `input_panel`).
- `"from_button_id"` - button (action) id that fires
- `"to_button_id"` - button (action) id that results
- `"handle_select` - boolean 
- `"handle_deselect` - boolean 
- `"mapping_type"`
  - `pressed` - mouse click
  - `double_pressed` - double mouse click
  - `focused` - element focused
  - `global`
- `"scope"`
  - `view`
  - `controller`
- `"input_mode_condition"`
  - `gamepad_and_not_gaze`
  - `not_gaze` 
- `"button_up_right_of_first_refusal"` - boolean 

### Variables Property
- `requires` - condition

If you only have one variable to use, you should just use `"variables": {}`
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "element": {
    ...
    "size": "$el_size",
    "$el_size|default": ["100%", 20],
    "variables": {
      "requires": "$var_condition",
      "$el_size": ["100%", 30]
    }
  }
}
```

If you have multiple variables use `"variables": [{}]`
{% include filepath.html path="RP/ui/example_file.json"%}
```jsonc
{
  "element": {
    ...
    "size": "$el_size",
    "offset": "$el_offset",
    "$el_offset|default": [0, 40],
    "$el_size|default": ["100%", 20],
    "variables": [
      {
        "requires": "$var_condition",
        "$el_size": ["100%", 30]
      },
      {
        "requires": "$other_var_condition",
        "$el_offset": [0, 15],
        "$el_size": ["90%", 35]
      }
    ]
  }
}
```

## Animations
`anim_type` and its possible values are `wait`, `size`, `offset`, `alpha` and `flipbook`.

- `initial_uv` - it's always `[0, 0]`
- `frame_count` - number
- `frame_steps` - number
- `reversible` - boolean
- `scale_from_starting_alpha` - boolean
- `fps` - number of frames per second
- `easing` - possible values are `linear`, `spring`, `in_sine`, `in_quart`, `in_quint`, `in_expo`, `out_expo`, `out_cubic` and `out_back` 
- `duration` - number. Duration of the animation in seconds
- `from` - number (`anim_type` alpha) or a `size`/`offset` array (`anim_type` size/offset)
- `to` - number (`anim_type` alpha) or a `size`/`offset` array (`anim_type` size/offset) 
- `destroy_at_end` - name of the object to destroy (stop rendering/ignored) when the animation ends. Doesn't require namespace
- `next` - name of the animation that will play after this ends
- `resettable` - boolean
- `play_event` - name of the event when the animation starts 
- `end_event` - name of the event when the animation ends

## Binding Property Names
- `#visible`
- `#enabled`
- `#toggle_state`
- `#text`
- `#texture`
- `#zip_folder`
- `#texture_file_system`
- `#clip_ratio`
- `#grayscale`
- `#alpha`
- `#propagateAlpha`
- `#focus_identifier`
- `#focus_change_up`
- `#focus_change_down`
- `#focus_change_left`
- `#focus_change_right`
- `#focus_enabled`
- `#default_focus_precedence`
- `#modal`
- `#maximum_grid_items`
- `#collection_length`
- `#button_navigation`
- `#item_id_aux`
- `#color`
- `#progress_bar_visible`
- `#progress_bar_total_amount`
- `#progress_bar_current_amount`

## Property Bag Property Names
- `#visible` - boolean
- `#hyperlink` - string
- `#tts_dialog_title` - string
- `#tts_dialog_body` - string
- `#property_field` - string
- `#flying_item_renderer` - boolean
- `#item_id_aux` - number
- `#collection_name` - string
- `#collection_index` - number
- `#playername` - string
- `#x_padding` - number
- `#hover_slice` - number
- `#common` - same as `color`
- `#uncommon` - same as `color`
- `#rare` - same as `color`
- `#epic` - same as `color`
- `#legendary` - same as `color`
- `#is_featured` - boolean
- `#anchored_offset_value_x` when using `use_anchored_offset` (boolean) property
- `#anchored_offset_value_y` when using `use_anchored_offset` (boolean) property
- `#timer_field_count_to_show` - number
- `#visible_after_x_ratings` - boolean
- `control_id` - string
- `#panel_title` - string
- `#should_host` - boolean

## Settings
### Sliders
| Name                            | Slider Name                    | Value Binding Name              | TTS Value (`tts_value_changed`) | Slider Text                                  | Enabled Binding Name                    |
|---------------------------------|--------------------------------|---------------------------------|---------------------------------|----------------------------------------------|-----------------------------------------|
| Brightness                      | `gamma`                        | `#gamma`                        | `#gamma_text_value`             | `#gamma_slider_label`                        | `#gamma_enabled`                        |
| Brightness (VR)                 | `vr_gamma`                     | `#vr_gamma`                     | `#vr_gamma_text_value`          | `#vr_gamma_slider_label`                     | `#vr_gamma_enabled`                     |
| HUD Opacity                     | `interface_opacity`            | `#interface_opacity`            | `#interface_opacity_text_value` | `#interface_opacity_slider_label`            | `#interface_opacity_enabled`            |
| HUD Opacity (Splitscreen)       | `splitscreen_interface_opacity`| `#splitscreen_interface_opacity`| `#interface_opacity_text_value` |`#splitscreen_interface_opacity_slider_label` | `#splitscreen_interface_opacity_enabled`|
| Field Of View                   | `field_of_view`                | `#field_of_view`                | `#field_of_view_text_value`     | `#field_of_view_slider_label`                | `#field_of_view_enabled`                |

### Toggles
| Name                                         | Toggle Name                          | State Binding Name                     | Enabled Binding Name                           |
|----------------------------------------------|--------------------------------------|----------------------------------------|------------------------------------------------|
| Fullscreen                                   | `full_screen`                        | `#full_screen`                         | `#full_screen_enabled`                         |
| Hide Hand                                    | `hide_hand`                          | `#hide_hand`                           | `#hide_hand_enabled`                           |
| Hide Hand (VR)                               | `vr_hide_hand`                       | `#vr_hide_hand`                        | `#vr_hide_hand_enabled`                        |
| Hide Paperdoll                               | `hide_paperdoll`                     | `#hide_paperdoll`                      | `#hide_paperdoll_enabled`                      |
| Hide HUD                                     | `hide_hud`                           | `#hide_hud`                            | `#hide_hud_enabled`                            |
| Hide HUD (VR)                                | `vr_hide_hud`                        | `#vr_hide_hud`                         | `#vr_hide_hud_enabled`                         |
| Screen Animations                            | `screen_animations`                  | `#screen_animations`                   | `#screen_animations_enabled`                   |
| Outline Selection                            | `classic_box_selection`              | `#classic_box_selection`               | `#classic_box_selection_enabled`               |
| Outline Selection (VR)                       | `vr_classic_box_selection`           | `#vr_classic_box_selection`            | `#vr_classic_box_selection_enabled`            |
| Show Players Names Ingame                    | `ingame_player_names`                | `#ingame_player_names`                 | `#ingame_player_names_enabled`                 |
| Show Players Names Ingame (Splitscreen)      | `splitscreen_ingame_player_names`    | `#splitscreen_ingame_player_names`     | `#splitscreen_ingame_player_names_enabled`     |
| View Bobbing                                 | `view_bobbing`                       | `#view_bobbing`                        | `#view_bobbing_enabled`                        |
| Camera Shake                                 | `camera_shake`                       | `#camera_shake`                        | `#camera_shake_enabled`                        |
| Fancy Leaves                                 | `transparent_leaves`                 | `#transparent_leaves`                  | `#transparent_leaves_enabled`                  |
| Fancy Leaves (VR)                            | `vr_transparent_leaves`              | `#vr_transparent_leaves`               | `#vr_transparent_leaves_enabled`               |

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

## Hardcoded Hyperlinks (`#hyperlink`)
`#hyperlink` doesn't allow custom urls. These are the ones that will work:
- `https://aka.ms/MCBanned`
- `https://education.minecraft.net/eula`
- `https://aka.ms/meeterms`
- `https://aka.ms/privacy`
- `https://itunes.apple.com/us/app/minecraft/id479516143?mt=8`
- `https://aka.ms/MCMultiplayerHelp`
- `https://aka.ms/mcedulogs`
- `https://aka.ms/minecraftfb`
- `https://aka.ms/minecraftfbbeta`
- `https://aka.ms/minecraftedusupport`
- `https://www.minecraft.net/attribution/?hideChrome`
- `https://aka.ms/switchattribution`
- `https://www.minecraft.net/licensed-content/?hideChrome`
- `https://aka.ms/switchcontent`
- `https://social.xbox.com/changegamertag`
- `https://account.xbox.com/Settings`

## Hardcoded Button IDs
Some of them only work in specific screens.

### Buttons IDs (`from_button_id`):
- `button.menu_exit`
- `button.menu_cancel` (`Escape` key or Controller `B`)
- `button.menu_inventory_cancel` (`Open Inventory` keybinding)
- `button.menu_ok` (`Enter` key)
- `button.menu_select` (Mouse click)
- `button.controller_select` (Controller `X`)
- `button.menu_secondary_select`
- `button.controller_secondary_select`
- `button.controller_secondary_select_left`
- `button.controller_secondary_select_right` (Controller `R3`)
- `button.controller_start`
- `button.menu_up` (`Arrow Up` key)
- `button.menu_down` (`Arrow Down` key)
- `button.menu_left` (`Arrow Left` key)
- `button.menu_right` (`Arrow Right` key)
- `button.menu_tab_left` (`Menu Tab Left` keybinding or Controller `Left Bumper`)
- `button.menu_tab_right` (`Menu Tab Right` keybinding or Controller `Right Bumper`)
- `button.menu_alternate_tab_left`
- `button.menu_alternate_tab_right`
- `button.menu_autocomplete` (Uses `Tab` key)
- `button.menu_autocomplete_back`
- `button.controller_autocomplete`
- `button.controller_autocomplete_back`
- `button.menu_textedit_up` (Uses `Arrow Up` key)
- `button.menu_textedit_down` (Uses `Arrow Down` key)
- `button.controller_textedit_up`
- `button.controller_textedit_down`
- `button.menu_auto_place`
- `button.menu_inventory_drop` (`Drop Item` keybinding)
- `button.menu_inventory_drop_all` (`Drop Item` + `Control` key)
- `button.menu_clear`
- `button.chat` (`Open Chat` keybinding)
- `button.mobeffects` (`Mob Effects` keybinding)
- `key.emote` (`Emote` keybinding)
- `button.slot1` (Emote Wheel) (`1` key)
- `button.slot2` (Emote Wheel) (`2` key)
- `button.slot3` (Emote Wheel) (`3` key)
- `button.slot4` (Emote Wheel) (`4` key)
- `button.slot5` (Emote Wheel) (`5` key)
- `button.slot6` (Emote Wheel) (`6` key)
- `button.inventory_right` (`Mouse Wheel Up`)
- `button.inventory_left` (`Mouse Wheel Down`)
- `button.scoreboard`
- `button.hide_gui` (`F1` key)
- `button.hide_tooltips`
- `button.hide_paperdoll` 
- `button.slot0`
- `button.slot1` (`1` key)
- `button.slot2` (`2` key)
- `button.slot3` (`3` key)
- `button.slot4` (`4` key)
- `button.slot5` (`5` key)
- `button.slot6` (`6` key)
- `button.slot7` (`7` key)
- `button.slot8` (`8` key)
- `button.slot9` (`9` key)
- `button.menu_vr_realign`
- `any` (literally the name of it)

### Specific Screen Button IDs:
#### Settings (`ui/settings_screen.json`)
- `button.open_content_log_history`
- `button.clear_content_log_files`
- `button.clear_msa_token_button`
- `button.terms_and_conditions_popup`
- `button.credits`
- `button.unlink_msa`
- `button.attribute_popup`
- `button.licensed_content`
- `button.font_license`
- `button.tos_hyperlink`
- `button.privpol_hyperlink`
- `button.tos_popup`
- `button.privpol_popup`
- `button.binding_button`
- `button.reset_binding`
- `button.reset_keyboard_bindings`
- `button.view_account_errors`

#### Book (`ui/book_screen.json`)
- `button.prev_page`
- `button.next_page`
- `button.book_exit`

#### Chat (`ui/chat_screen.json`)
- `button.send`
- `button.chat_autocomplete`
- `button.chat_autocomplete_back`
- `button.chat_previous_message`
- `button.chat_next_message`
- `button.chat_menu_cancel`

#### Command Block (`ui/command_block_screen.json`)
- `command_block.input_minimize`
- `button.chat_autocomplete`
- `button.chat_autocomplete_back`

#### Comment (`ui/comment_screen.json`)
- `button.comment_options_close`
- `button.comment_feed_options_close`
- `button.close_comments`
- `button.comment_next_button`
- `button.comment_prev_button`

#### Credits (`ui/credits_screen.json`)
- `button.show_skip`

#### Death Menu (`ui/death_screen.json`)
- `button.respawn_button`
- `button.main_menu_button`

#### Emote Wheel (`ui/emote_screen_wheel.json`)
- `button.rebind_mode`
- `button.dressing_room`
- `button.emote_selected`
- `button.select_emote_slot_0`
- `button.select_emote_slot_1`
- `button.select_emote_slot_2`
- `button.select_emote_slot_3`
- `button.select_emote_slot_4`
- `button.select_emote_slot_5`
- `button.iterate_selection_left`
- `button.iterate_selection_right`

#### Feed (`ui/feed_screen.json`)
- `button.feed_image`
- `button.newpost`
- `button.add_screenshot`
- `button.feed_comment`
- `button.feed_prev_button`
- `button.feed_next_button`
- `button.feed_new_post_close`
- `button.feed_options_close`
- `button.close_feed`

#### Game Menu (`ui/pause_screen.json`)
- `button.to_profile_or_skins_screen`
- `button.player_profile_card`
- `button.menu_continue`
- `button.menu_server_store`
- `button.screenshot`
- `button.menu_how_to_play`
- `button.menu_feedback`
- `button.menu_permission`
- `button.menu_invite_players`
- `button.menu_quit`
- `button.menu_feed`
- `button.pause_focus_filler`

#### In Bed (`ui/in_bed_screen.json`)
- `button.wake_up_button`

#### Invite (`ui/invite_screen.json`)
- `button.add_friend`
- `button.add_member`
- `button.send_invites`

#### Manage Feed (`ui/manage_feed_screen.json`)
- `button.manage_feed_prev_button`
- `button.manage_feed_next_button`
- `button.manage_feed_ignore`
- `button.manage_feed_delete`
- `button.close_manage_feed`

#### Anvil (`ui/anvil_screen.json`)
- `button.anvil_take_all_place_all`
- `button.anvil_coalesce_stack`

#### Cartography Table (`ui/cartography_screen.json`)
- `button.cartography_result_take_all_place_all`

#### Enchanting Table (`ui/enchanting_table_screen.json`)
- `button.enchant`

#### Grindstone (`ui/grindstone_screen.json`)
- `button.grindstone_take_all_place_all`
- `button.grindstone_coalesce_stack`

#### Loom (`ui/loom_screen.json`)
- `button.loom_result_take_all_place_all`
- `button.pattern_select`
 
### Others
- `button.try_menu_exit`
- `button.close_dialog`
- `button.menu_play`
- `$play_button_target` (**hardcoded**)
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
- `button.hotbar_inventory_button`
- `button.select_offer`
- `button.action_button`
- `button.create_realm`
- `button.switch_accounts`
- `button.hotbar_select`
- `button.hotbar_ok`
- `button.slot_pressed`
- `button.hotbar_inventory_left`
- `button.hotbar_inventory_right`
- `button.hide_gui_all`
- `button.hide_tooltips_hud`
- `button.hide_paperdoll_hud`
- `button.slot_1`
- `button.slot_2`
- `button.slot_3`
- `button.slot_4`
- `button.slot_5`
- `button.slot_6`
- `button.slot_7`
- `button.slot_8`
- `button.slot_9`
- `button.slot_0`
- `button.chat`
- `button.menu_continue`
- `user_confirm_dialog.escape`
- `user_confirm_dialog.left_button`
- `user_confirm_dialog.middle_button`
- `user_confirm_dialog.rightcancel_button`
- `button.view_skin`
- `button.delete_action`
- `button.exit_student`
- `button.play_video`
- `button.menu_store_error`
- `button.left_panel_tab_increment`
- `button.left_panel_tab_decrement`
- `button.right_panel_tab_increment`
- `button.right_panel_tab_decrement`
- `button.layout_increment`
- `button.layout_decrement`
- `button.is_hovered`
- `button.container_take_all_place_all`
- `button.container_take_half_place_one`
- `button.container_auto_place`
- `button.coalesce_stack`
- `button.shape_drawing`
- `button.destroy_selection`
- `button.clear_selected_recipe`
- `button.clear_hotbar_or_remove_one`
- `button.clear_hotbar_or_drop`
- `button.container_reset_held`
- `button.container_auto_place`
- `button.container_slot_hovered`
- `button.button_hovered`
- `button.shift_pane_focus`
- `button.focus_left`
- `button.focus_right`
- `button.filter_toggle_hovered`
- `button.drop_one`
- `button.cursor_drop_one`
- `button.drop_all`
- `button.cursor_drop_all`
- `button.search_bar_clear`
- `button.search_bar_selected`
- `button.search_bar_deselected`
- `button.menu_leave_screen`
- `button.turn_doll`
- `button.select_skin`
- `button.skin_hovered`
- `button.skin_unhovered`
- `button.leave`
- `button.leave_on_device`
- ...

## Hardcoded Collection Names
All of them only in specific screens.

### Screen specific:
#### Book (`ui/book_screen.json`)
- `book_pages`
- `pick_collection`

#### Bundle Purchase Warning (`ui/bundle_purchase_warning_screen.json`)
- `owned_list`
- `unowned_list`

#### Chat (`ui/chat_screen.json`)
- `auto_complete`
- `font_colors`
- `host_main_collection`
- `players_collection`
- `host_teleport_collection`
- `host_time_collection`
- `host_weather_collection`

#### Choose Realm (`ui/choose_realm_screen.json`)
- `realms_collection`

#### Coin Purchase (`ui/coin_purchase_screen.json`)
- `coin_purchase_grid`

#### Comment (`ui/comment_screen.json`)
- `comment_collection`

#### Content Log History (`ui/content_log_history_screen.json`)
- `content_log_message`

#### Create World Upsell (`ui/create_world_upsell_screen.json`)
- `world_list`
- `realm_list`

#### Custom Templates (`ui/custom_templates_screen.json`)
- `templates_collection`

#### Feed (`ui/feed_screen.json`)
- `feed_collection`

#### HUD (`ui/hud_screen.json`)
- `boss_bars`
- `chat_text_grid`
- `hotbar_items`
- `scoreboard_players`
- `scoreboard_scores`
- `left_helper_collection`
- `right_helper_collection`

#### Invite (`ui/invite_screen.json`)
- `online_platform_friends`
- `online_linked_account_friends`
- `online_xbox_live_friends`
- `offline_platform_friends`
- `offline_linked_account_friends`
- `offline_xbox_live_friends`

#### Manage Feed (`ui/manage_feed_screen.json`)
- `manage_feed_collection`

#### Manifest Validation (`manifest_validation_screen.json`)
- `pack_errors`

#### Mob Effects (`ui/mob_effects_screen.json`)
- `mob_effects_collection`

#### Game Menu (`ui/pause_screen.json`)
- `players_collection`

#### PDP (`ui/pdp_screen.json`)
- `factory_collection`
- `ratings_star_collection`

#### Permissions (`ui/permissions_screen.json`)
- `players_collection` - it's also used in `pause_screen.json`
- `permissions_collection`

#### Persona (`ui/persona_screen.json`)
- `color_collection`
- `skin_pack_in_grid_item`
- `persona_featured_skin_pack_collection`
- `body_size_collection`
- `arm_size_collection`
- `category_featured_collection`
- `main_featured_collection`
- `profile_featured_collection`
- `custom_section_collection`
- `featured_collection`
- `foobar_collection`
- `emote_collection`

#### Play (`ui/play_screen.json`)
- `friends_network_worlds`
- `cross_platform_friends_network_worlds`
- `lan_network_worlds`
- `personal_realms`
- `friends_realms`
- `servers_network_worlds`
- `third_party_server_network_worlds`
- `server_screenshot_collection`
- `server_games_collection`
- `local_worlds`
- `legacy_worlds`
- `beta_retail_local_worlds`
- `personal_realms`
- `loading_personal_realms`
- `friends_realms`
- `loading_friends_realms`

#### Portfolio (`ui/portfolio_screen.json`)
- `photos`

#### Progress (`ui/progress_screen.json`)
- `required_resourcepacks`
- `optional_resourcepacks`

#### Realms Pending Invitations (`ui/realms_pending_invitations_screen.json`)
- `pending_invites_collection`

#### Realms Settings (`ui/realms_settings_screen.json`)
- `additional_realms_subscriptions_collection`
- `realms_branch_collection`
- `realms_backup_collection`
- `members_collection`
- `invited_friends_collection`
- `uninvited_friends_collection`
- `blocked_players_collection`

#### Screenshot Picker (`ui/screenshot_picker_screen.json`)
- `screenshotpicker_collection`

#### Server Form (`ui/server_form.json`)
- `custom_form`
- `form_buttons`
- `custom_dropdown`

#### Settings (`ui/settings_screen.json`)
- `keyboard_standard_collection`
- `keyboard_full_collection`
- `gamepad_collection`
- `languages`
- `realms_plus_subscriptions_collection`
- `additional_realms_subscriptions_collection`
- `#selected_pack_items_global`
- `#available_pack_items_global`
- `#realms_pack_items_global`
- `#unowned_pack_items_global`
- `#invalid_pack_items_global`
- `#selected_pack_items_level`
- `#available_pack_items_level`
- `#realms_pack_items_level`
- `#unowned_pack_items_level`
- `#invalid_pack_items_level`
- `#selected_pack_items_addon`
- `#available_pack_items_addon`
- `#realms_pack_items_addon`
- `#unowned_pack_items_addon`
- `#invalid_pack_items_addon`
- `experimental_toggles`
- `world_panel`
- `world_template_panel`
- `resource_panel`
- `behavior_panel`
- `skin_panel`
- `cache_panel`
- `dependent_packs_panel`
- `dependency_panel`

#### Structure Block (`ui/structure_editor_screen.json`)
- `save_size_grid`
- `save_offset_grid`
- `load_offset_grid`
- `export_size_grid`
- `export_offset_grid`

#### Seed Picker (`ui/ugc_viewer_screen.json`)
- `ugc_items`

#### World Templates (`ui/world_templates_screen.json`)
- `world_templates`
- `realms_plus_templates`
- `custom_world_templates`
- `#suggested_offers_collection`

#### Anvil (`ui/anvil_screen.json`)
- `anvil_input_items`
- `anvil_material_items`
- `anvil_result_items`

#### Beacon (`ui/beacon_screen.json`)
- `beacon_payment_items`
- `speed`
- `haste`
- `resist`
- `jump`
- `strength`
- `regen`
- `extra`
- `confirm`
- `cancel`

#### Brewing Stand (`ui/brewing_stand_screen.json`)
- `brewing_fuel_item`
- `brewing_input_item`
- `brewing_result_items`

#### Cartography Table (`ui/cartography_screen.json`)
- `cartography_input_items`
- `cartography_additional_items`
- `cartography_result_items`

#### Enchanting Table (`ui/enchanting_table_screen.json`)
- `enchanting_input_items`
- `enchanting_lapis_items`
- `#enchant_buttons`

#### Furnace (`ui/furnace_screen.json`)
- `furnace_ingredient_items`
- `furnace_fuel_items`
- `furnace_output_items`

#### Gridstone (`ui/grindstone_screen.json`)
- `grindstone_input_items`
- `grindstone_additional_items`
- `grindstone_result_items`
  
#### Horse (`ui/horse_screen.json`)
- `horse_equip_items`

#### Inventory (`ui/inventory_screen.json` and `ui/inventory_screen_pocket.json`)
- `armor_items`
- `offhand_items`
- `crafting_input_items`
- `crafting_output_items`
- `recipe_book`

#### Loom (`ui/loom_screen.json`)
- `loom_input_items`
- `loom_dye_items`
- `loom_material_items`
- `loom_result_items`
- `patterns`

#### Smithing Table (`ui/smithing_table_screen.json`)
- `smithing_table_input_items`
- `smithing_table_material_items`
- `smithing_table_result_items`

#### Stonecutter (`ui/stonecutter_screen.json`)
- `stonecutter_input_items`
- `stonecutter_result_items`
- `stones`

#### Villager Trade2 (`ui/trade2_screen.json`)
- `trade2_ingredient1_item`
- `trade2_ingredient2_item`
- `trade2_result_item`
- `trade_item_1`
- `trade_item_2`
- `sell_item`
- `trades`
- `trade_tiers`

## Hardcoded Binding Names
Some of them only work in specific screens.

### Screen specific:
#### Account Transfer Error (`ui/account_transfer_error_screen.json`)
- `#error_title_text`
- `#error_number_label`
- `#error_number`
- `#correlation_id_label`
- `#correlation_id`

#### Add External Server (`ui/add_external_server_screen.json`)
- `#play_button_enabled`
- `#play_button_disabled`
- `#save_button_enabled`
- `#save_button_disabled`

#### Adhoc In Progress (`ui/adhoc_in_progress_screen.json`)
- `#adhoc_title`

#### Authentication (`ui/authentication_screen.json`)
- `#sign_in_visible`
- `#sign_in_ios_visible`
- `#sign_in_button_visible`
- `#sign_in_ios_buttons_visible`
- `#authentication_message`
- `#confirm_button_enabled`
- `#edu_store_visible`
- `#edu_store_purchase_info`
- `#asking_to_buy_visible`
- `#confirming_purchase_visible`
- `#demo_choice_visible`
- `#eula_visible`
- `#popup_text`
- `#popup_message_student_text`
- `#popup_message_student_visible`
- `#generic_popup_link_visible`
- `#trial_purchase_link_visible`
- `#show_popup_dismiss_button`

### Book (`ui/book_screen.json`)
- `#screenshot_path`
- `#is_photo_page`
- `#is_text_page`
- `#pick_grid_dimensions`
- `#page_number`
- `#title_text_box_item_name`
- `#author_editable`
- `#author_text_box_item_name`
- `#editable`
- `#viewing`
- `#signing`
- `#picking`
- `#exporting`
- `#page_visible`
- `#pick_item_visible`
- `#close_button_visible`
- `#edit_controls_active`
- `#finalize_button_enabled`

#### Braze (`ui/braze_screen.json`)
- `#image_texture`

#### Bundle Purchase Warning (`ui/bundle_purchase_warning_screen.json`)
- `#banner_visible`
- `#offer_title`
- `#keyart_path`
- `#keyart_texture_file_system`

#### Chat (`ui/chat_screen.json`)
- `#keyboard_being_use`
- `#keyboard_button_focus_override_up`
- `#keyboard_button_focus_override_down`
- `#keyboard_button_visible`
- `#send_button_visible`
- `#send_button_accessibility_text`
- `#chat_visible`
- `#message_text_box_content`
- `#text_edit_box_focus_override_up`
- `#text_edit_box_focus_override_down`
- `#auto_complete_item`
- `#auto_complete_text`
- `#get_grid_size`
- `#chat_title_text`
- `#chat_typeface_visible`

#### Choose Realm (`ui/choose_realm_screen.json`)
- `#realms_grid_dimension`
- `#world_button_focus_identifier`
- `#ten_player_button_visible`
- `#two_player_button_visible`
- `#realms_world_player_count`
- `#realms_game_online`
- `#realms_game_unavailable`
- `#realms_game_offline`

#### Coin Purchase (`ui/coin_purchase_screen.json`)
- `#bonus_coins`
- `#coins_without_bonus`
- `#coin_offer_texture_name`
- `#coin_offer_texture_file_system`
- `#bonus_coins_visible`
- `#price_text`
- `#coins_required_for_purchase`
- `#show_missing_coins`
- `#coin_offer_size`
- `#has_coin_offers`
- `#coin_loading_visible`

#### Command Block (`ui/command_block_screen.json`)
- `#maximized_input_visible`
- `#block_type_icon_texture`
- `#close_button_visible_binding_name`
- `#command_impulse_mode`
- `#command_chain_mode`
- `#command_repeat_mode`
- `#block_type_dropdown_toggle_label`
- `#block_type_dropdown_label_color_binding`
- `#block_type_dropdown_enabled`
- `#command_conditional_mode`
- `#command_unconditional_mode`
- `#condition_dropdown_toggle_label`
- `#condition_dropdown_enabled`
- `#command_always_on_mode`
- `#command_needs_redstone_mode`
- `#redstone_dropdown_enabled`
- `#command_hover_note`
- `#execute_on_first_tick_enabled`
- `#command_tick_delay`
- `#command_text_edit`
- `#command_output_text`
- `#previous_block_type_text`
- `#previous_block_type_text_color`
- `#previous_condition_mode_text`
- `#previous_redstone_mode_text`
- `#minimize_button_visible_binding_name`

#### Comment (`ui/comment_screen.json`)
- `#report_to_club_button_visible_feeditem`
- `#report_to_enforcement_button_visible_feeditem`
- `#delete_button_visible_feeditem`
- `#report_to_club_button_visible_comment`
- `#report_to_enforcement_button_visible_comment`
- `#delete_button_visible_comment`
- `#comment_buttons_visible`
- `#feed_comment_page_collection_length`
- `#comment_content`
- `#is_author_linked_account`
- `#content`
- `#text_visible`
- `#likes_and_comments`
- `#screenshot_texture`
- `#screenshot_texture_source`
- `#textpost_content`
- `#textpost_visible`
- `#comment_text_box`
- `#comment_platform_tag`
- `#comment_gamertag`
- `#likes_and_time_since_comment_post`
- `#author_gamertag`
- `#time_since_feed_post`
- `#author_platform_tag`
- `#author_gamertag`

#### Confirm MSA Unlink (`ui/confirm_msa_unlink_screen.json`)
- `#unlink_warning_text`
- `#unlink_consequences_acknowledged`
- `#confirm_0`
- `#confirm_0_enabled`
- `#confirm_1`
- `#confirm_1_enabled`
- `#confirm_2`
- `#confirm_2_enabled`
- `#confirm_3`
- `#confirm_3_enabled`

#### Content Log History (`ui/content_log_history_screen.json`)
- `#content_log_text`
- `#messages_size`

#### Create World Upsell (`ui/create_world_upsell.json`)
- `#realm_button_text`
- `#realm_trial_available`
- ...

...

#### Anvil (`ui/anvil_screen.json`)
- `#cost_text`
- `#cost_text_green`
- `#cost_text_red`

#### Beacon (`ui/beacon_screen.json`)
- `#supports_netherite`
- `#extra_image_selection`

#### Brewing Stand (`ui/brewing_stand_screen.json`)
- `#empty_bottle_image_visible`
- `#empty_fuel_image_visible`
- `#brewing_bubbles_ratio`
- `#brewing_fuel_ratio`
- `#brewing_arrow_ratio`

#### Cartography Table (`ui/cartography_screen.json`)
- `#is_none_mode`
- `#is_clone_mode`
- `#is_rename_mode`
- `#is_basic_map_mode`
- `#is_locator_map_mode`
- `#is_extend_mode`
- `#is_locked_mode`
- `#output_description`

#### Enchanting Table (`ui/enchanting_table_screen.json`)
- `#selectable_dust_is_visible`
- `#unselectable_dust_is_visible`
- `#runes`
- `#cost`
- `#unselectable_button_visibility`
- `#selectable_button_visibility`
- `#show_selected_button_highlight`
- `#active_enchant`
- `#inactive_enchant`
- `#input_item_id`
- `#output_item_id`
- `#enchant_hint`
- `#player_level_color`
- `#player_level_info`
- `#enchant_error`

#### Furnace (`ui/furnace_screen.json`)
- `#furnace_arrow_ratio`
- `#furnace_flame_ratio`
- `#output_name`

#### Horse (`ui/horse_screen.json`)
- `#entity_id`
- `#equip_grid_dimensions`
- `#inv_grid_dimensions`
- `#sadle_slot_centered`
- `#has_saddle_slot`
- `#has_armor_slot`
- `#has_only_armor_slot`
- `#has_only_carpet_slot`
- `#has_armor_and_saddle_slot`
- `#has_carpet_and_saddle_slot`
- `#is_chested`
- `#renderer_tab_toggle`
- `#chest_tab_toggle`

#### Loom (`ui/loom_screen.json`)
- `#pattern_cell_background_texture`
- `#container_cell_background_texture`
- `#empty_image_visible`
- `#banner_patterns`
- `#banner_colors`
- `#pattern_selector_total_items`
- `#result_patterns`
- `#result_colors`
- `#is_right_tab_loom`
- `#is_left_tab_patterns`

#### Stonecutter (`ui/stonecutter_screen.json`)
- `#stone_cell_background_texture`
- `#container_cell_background_texture`
- `#item_stack_count`
- `#stone_selector_total_items`
- `#has_input_item`
- `#is_right_tab_stonecutter`
- `#is_left_tab_stones`

#### Villager Trade2 (`ui/trade2_screen.json`)
- `#name_label`
- `#trade_cell_background_texture`
- `#trade_item_count`
- `#single_slash_visible`
- `#double_slash_visible`
- `#second_trade_item_count`
- `#trade_price_different`
- `#trade_cross_out_visible`
- `#padding_around_sell_item`
- `#trade_possible`
- `#trade_toggle_state`
- `#trade_toggle_enabled`
- `#trade_tier_total`
- `#tier_name`
- `#is_tier_unlocked`
- `#is_left_tab_trade`
- `#show_level`
- `#tier_visible`
- `#trade_selector_total`
- `#has_second_buy_item`
- `#exp_bar_visible`
- `#exp_progress`
- `#exp_possible_progress`
- `#trade_details_button_1_visible`
- `#trade_details_button_2_visible`
- `#enchantment_details_button_visible`
- `#item_valid`

### Value depends on the screen it is in:
- `#title_text`
- `#body_text`
- `#hover_text`
- `#cross_out_icon`
- `#is_left_tab_inventory`
- `#selected_hover_text`

### Others:
- `#tts_dialog_body`
- `#button_enabled`
- `#using_touch`
- `#close_button_visible`

## Item ID Aux (`#item_id_aux`)
| Name                         | ID       | Aux Values    |
|------------------------------|:--------:|:-------------:|
| diamond                      | 304      | 17301504      |
| emerald                      | 502      | 25427968      |
| gold_ingot                   | 306      | 17432576      |
| iron_ingot                   | 305      | 17367040      |
| netherite_ingot              | 592      | 48627712      |
| red_banner                   |          | 29229057      |
| saddle                       | 369      | 21561344      |
| cartography_table            | -200     | -13107200     |
| chest                        | 54       | 3538944       |
| crafting_table               | 58       | 3801088       |
| loom                         | -204     | -13369344     |
| stonecutter                  | -197     | -12910592     |

#### How to calculate block item aux value:
Aux = ID * 65536

ID = Aux / 65536
65536 = Aux / ID
