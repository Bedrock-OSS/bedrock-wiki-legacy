---
layout: page
title: Components/Groups/Events
parent: Knowledge
---

# Component Groups Vs. Components Vs. Events

There are three main structures that make up the base of a behavior-pack entity file. This doc will explain what each of them means, and how to use them.

# Components

Components should be thought of as the logical building-blocks that make up minecraft-entities. All components are written by microsoft, and provided to us for use. Components can do all sorts of things, like set the size of an entity, or give it the ability to swim. The full list of components can be found [here](https://bedrock.dev/docs/1.16.0.0/1.16.0.66/Entities#minecraft:color2).

It is impossible to create your own components. The entire list of components is hard-coded, and provided by Microsoft. The `only` thing that should go intside the `components` object is components.

All components begin with `minecraft:`.

# Component groups

Component groups should be thought of as `folders` for components. They group components together, and can be added or removed using `events` to create custom game-play.

Here is an example:

```json
"minecraft:cat_persian": { //the name of the component group
    "minecraft:variant": { //A list of valid components. Add as many as you like.
        "value": 6
    },
    "minecraft:physics: {}
}
```

All component groups are custom-created. You cannot use component groups from other entities in your own entity. In the example above, `minecraft:cat_persian` is *not* a component. You cannot use it in your entity. If you want the `cat_persian` functionality in your entity, you must create your own group, or add the components directly into the your entities `components` object.

`Note:` All minecraft component groups are prefixed with `minecraft:`. When you create your own groups, you should *not* follow this design. Rather, use your own [namespace](https://wiki.bedrock.dev/knowledge/namespaces.html).s

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

Like component-groups, events are 100% custom created inside each entity. You cannot use events from other entities in your own. Do not be temted to use `"minecraft:ageable_grow_up"` in your own entity. If you want grow-up functionality, you need to define the component-groups and events yourself.

The only thing you can add/remove from an entity is `component groups`. As tempting as it is to try and add/remove components directly, this is not possible. 

# Triggering events

Many components can trigger events. Particularly, components like [environment sensor](https://wiki.bedrock.dev/vanilla_usage/components_1.14.html#minecraftenvironment_sensor) or [timer](https://wiki.bedrock.dev/vanilla_usage/components_1.14.html#minecrafttimer).

The flow is:
 - Add component to the entity
 - Component triggers event
 - Which adds component group
 - Which adds component
 - Which effects the entity in some form or another.

# Uses in vanilla

Component groups and events are the main tool that vanilla entities use to create custom and adaptable behavior. For a specific example, look at the zombie.

The zombie is programmed to turn into a `drowned` if it spends too long in the water. Look at the component-groups and events, and see if you can work out how this is done!


