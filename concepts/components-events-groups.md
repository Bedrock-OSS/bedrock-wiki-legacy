---
layout: page
title: Components/Groups/Events
parent: Concepts
---

# Component Groups Vs. Components Vs. Events

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Three main structures make up the base of a behavior-pack entity file. This doc will explain what each of them means, and how to use them.

# Components

Components should be thought of as the logical building blocks that make up Minecraft-entities. All components are written by Mojang, and provided to us for use. Components can do all sorts of things, like set the size of an entity, or give it the ability to swim. The [full list of components can be found here](https://bedrock.dev/docs/stable/Entities).

It is impossible to create your own components. The entire list of components is hard-coded and provided by Microsoft. The `only` thing that should go inside the `components` object is components.

All components begin with `minecraft:`.

# Component groups

Component groups should be thought of as `folders` for components. They group components together, and can be added or removed using `events` to create custom game-play.

Here is an example:

```json
"minecraft:cat_persian": { //the name of the component group
    "minecraft:variant": { //A list of valid components. Add as many as you like.
        "value": 6
    },
    "minecraft:physics": {}
}
```

All component groups are custom-created. You cannot use component groups from other entities in your entity. In the example above, `minecraft:cat_persian` is *not* a component. You cannot use it in your entity. If you want the `cat_persian` functionality in your entity, you must create your group, or add the components directly into your entities  `components` object.

`Note:` All Minecraft component groups are prefixed with `minecraft:`. When you create your groups, you should *not* follow this design. Rather, use your own. [Here's more info on namespaces](/knowledge/namespaces).

# Events

Events are a special syntax for adding and removing component-groups. 

An example:
```json
"minecraft:ageable_grow_up": { //Name of the event
    "remove": { //list of component groups to remove
        "component_groups": [
            "minecraft:cat_baby"
        ]
    },
    "add": {
        "component_groups": [
            "minecraft:cat_adult" //list of component groups to add.
        ]
    }
},
```

Like component-groups, events are 100% custom created inside each entity. You cannot use events from other entities on your own. Do not be tempted to use `"minecraft:ageable_grow_up"` in your own entity. If you want grow-up functionality, you need to define the component-groups and events yourself.

The only thing you can add/remove from an entity is `component groups`. As tempting as it is to try and add/remove components directly, this is not possible. 

# Advanced Usage
Advanced Usage {: .label .label-yellow }

Conditional events are events using "filters" to return a component group depending on your filter see the below example.
We are testing if a tag exists and if it doesn't return the "prefix:is_false" component but if it does exist return "prefix:is_true".

An example:
```json
      "prefix:event_name": {//Name of the event
        "sequence": [//Sequence 1 >>> 2 >>> 3 this follows top to bottom order.
          {
            "filters": {//filter this checks if the filter conditions are false.
              "test": "has_tag",
              "subject": "self",
              "operator": "not",
              "value": "tag_name"
            },
            "add": {//list of component groups to remove.
              "component_groups": [
                "prefix:is_false"
              ]
            },
            "remove": {//list of component groups to add.
              "component_groups": [
                "prefix:is_true"
              ]
            }
          },
          {
            "filters": {//filter this checks if the filter conditions are true.
              "test": "has_tag",
              "subject": "self",
              "operator": "equals",
              "value": "tag_name"
            },
            "add": {//list of component groups to add.
              "component_groups": [
                "prefix:is_true"
              ]
            },
            "remove": {//list of component groups to remove.
              "component_groups": [
                "prefix:is_false"
              ]
            }
          }
        ]
      }
```

# Triggering events

Many components can trigger events. Particularly, components like the [environment sensor](/vanilla-usage/components.html#minecraftenvironment_sensor) or [timer](/vanilla-usage/components.html#minecrafttimer).

`Note:` You can also use the /event <target> <prefix:event_name> to trigger an event directly off an entity. In the below example we run the "minecraft:become_charged" event to turn all creepers in loaded chunks into charged creepers.

An example.
```json
        //Command usage to send an event to all creepers.
        /event @e[type=creeper] minecraft:become_charged
```

The flow is:
 - Add the component to the entity
 - Component triggers event or /event triggers event
 - Which adds component group
 - Which adds the component
 - Which affects the entity in some form or another.

# Uses in vanilla

Component groups and events are the main tools that vanilla entities use to create custom and adaptable behavior. For a specific example, look at the zombie.

The zombie is programmed to turn into a `drowned` if it spends too long in the water. Look at the component-groups and events, and see if you can work out how this is done!


