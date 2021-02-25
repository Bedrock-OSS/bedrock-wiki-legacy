---
layout: page
title: Biomes
parent: Concepts
---

# Biomes

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

*Last updated for 1.16.201*

> Biome generation has been bugged since version 1.16.100. Biome layout remains consistent on the first generation when a pack is applied to a world, but breaks on subsequent loads, causing new chunks to be loaded using the vanilla generation. The only workaround for now is removing and reapplying all behavior packs containing biome definitions to a world between loads.

>  Biome customization is *experimental*. An experimental gameplay toggle must be enabled for each world that uses behavior packs containing biome definitions. What is currently available works well if declared correctly; however, incorrectly declared components and properties may result in crashing as opposed to just logged errors. Furthermore, in light of the [inheritance model](#inheritance), the schema used for custom biomes is not well constructed.

Behavior packs allow for the customization of biomes. Behavior packs can either override vanilla biomes or create entirely new ones (with some limitations to each). Biomes hook into critical gameplay features, such as mob spawning, data-driven gameplay, and presentation of custom blocks. Biomes also enable a powerful system for adding decorations like flowers and trees, or even structures like towers and houses; these decorations and structures are together known as [features](/concepts/features), which are (generally) separate in scope and construction from biomes.

While both vanilla overrides and custom biomes offer the same power, custom biomes are the recommended means for creating entirely new gameplay experiences. Vanilla overrides should only be reserved for:

- Mild surface, heightmap, or climate adjustments
- Redistribution of biome rarities across a dimension
- Addition of new features or mobs, but only if these are intended to be used globally across a dimension

Custom biomes should be used when *any* unique gameplay experience is desired or if an adjustment to a vanilla biome would fundamentally change its nature. Examples of situations where custom biomes shine include:

- A new or radical terrain is required to achieve an aesthetic.
- Custom features, like a new tree type, need somewhere to generate.
- An alternate or more challenging gaming experience is desired, potentially using new mobs and structures.

> There are some exceptions to these recommendation due to oversights in the biomes schema. For example, it might make sense only to use vanilla overrides when attempting to force a vanilla Overworld biome to generate in additional locations, but this may be impossible because of how biomes register themselves to be generated.

## Biome definitions
Biomes are declared in a file of the form <code>*biome_name*.json</code> or <code>*biome_name*.biome.json</code> in the top-level `biomes` directory of a behavior pack. Subdirectories may not be used within the `biomes` directory to group biome definitions; all definitions within sub-directories of `biomes` will be ignored.

[Because identifiers must match the filename](#description), namespace collisions may occur with other biome-declaring packs. One strategy to avoid collisions is to use a reverse-domain name scheme. *biome_name* may contain periods for grouping biomes in nested order, like `biomes/fancycraft.fantasy_realms.magical_springs.hills.mutated.json`. Here, `fancycraft` is the developer, `fantasy_realms` is the behavior pack, `magical_springs` is the [top-level biome](#heirarchy) name, `hills` and `mutated` are the [sub-biome](#types) types, and `json` is the required file extension (the optional `.biome` extension being omitted in this example).

> Invalid JSON files declared in the top-level `biomes` directory are more likely to log errors, but they may cause crashes. Non-JSON files directly placed inside this directory are ignored. If a file exists directly inside `biomes` that begins with a `.`, the game currently always crashes. This can cause problems with overlooked configuration files in build environments or the infamous [.DS_Store file](https://en.wikipedia.org/wiki/.DS_Store) on macOS.

### Format
Like all constructed assets in a behavior pack, biome definitions are written in JSON, such as:

```
{
  "format_version": "1.13.0",

  "minecraft:biome": {
    "description": {
      "identifier": "pumpkin_pastures"
    },

    "components": {
      "minecraft:climate": {
        "temperature": 0.25,
        "downfall": 0.25,
        "snow_accumulation": [0.0, 0.25]
      },

      "minecraft:surface_parameters": {
        "sea_floor_depth": 4,

        "foundation_material": "minecraft:stone",

        "top_material": "minecraft:grass",
        "mid_material": "minecraft:dirt",

        "sea_material": "minecraft:water",
        "sea_floor_material": "minecraft:sand"
      },
      "minecraft:overworld_height": {
        "noise_params": [0.125, 0.0625]
      },

      "minecraft:overworld_generation_rules": {
        "generate_for_climates": [
          ["cold", 1]
        ],

        "hills_transformation": "pumpkin_pastures_hills",
        "shore_transformation": "pumpkin_pastures"
      },

      "overworld": {},
      "pumpkin_pastures": {},

      "animal": {},
      "monster": {}
    }
  }
}
```

#### Format Version
```
"format_version": "1.13.0"
```

The top-level property `format_version` describes the version specification to which the proceeding schema conforms. The latest issued `format_version` for biomes is `1.13.0`.

> A previous version for 1.12 existed but has been deprecated and is unusable in newer versions. In it, the biome identifier acted as the key for a top-level object property, which itself contained the format version, components, and tags directly. This document exclusively uses the `1.13.0` format, but the deprecated one may be seen elsewhere.

The version must be of the form <code>*major*.*minor*.*patch*</code>, where `patch` or both `minor` and `patch` are optional. All 3 identifiers must be integers, but the completed version numbers do not have to represent a real version of Minecraft. Currently, any version number greater than or equal to `1.13.0` may be used and will refer to the `1.13.0` specification, but it is recommended to only use the value `1.13.0` or the version targeted during development: future versions may alter the expectations of the versioning system.

#### Biome Specification
```
"minecraft:biome": {  
  …
}
```

The other top-level property is `minecraft:biome`, which establishes the schema for the biome file.

##### Description
```
"description": {
  "identifier": "pumpkin_pastures"
}
```

The `description` property of the `minecraft:biome` property is used as the metadata for the biome. It currently contains only one property, `identifier`, which is used to uniquely identify a biome. The value here must match the file name, sans the `.json` or `.biome.json` extensions. For example, if the identifier is `prairie`, the filename must be either `prairie.json` or `prairie.biome.json`. This identifier is also used for referencing from other biome files.

> Unlike other aspects of add-ons, biomes do not accept a filename-ignored namespace prefix in their identifier. Such a prefix may be provided, but the file would have to contain the prefix, including the colon; such a filename is invalid on many Minecraft-supporting file systems, so this traditional namespace system should not be used.

##### Components
```
"components": {
  …
}
```

The `minecraft:biome` property also holds the `components` property, which is the meat of a biome definition. The components declared here place, shape, and style biomes. Components are always object properties, even those that should seemingly act as booleans.

> Component details are scattered throughout the rest of this document; they cannot be as neatly described or organized as these wrapper properties due to intricacies in their interactions.

###### Tags
```
"components": {
  …
  
  "overworld": {},
  "pumpkin_pastures": {},
  
  "animal": {},
  "monster": {}
}
```

In addition to the components that work to create a biome, the `components` property also allows for the addition of arbitrary tags. Tags appear like empty components, e.g., `"animal": {}`. Tag names must conform to the regular expression `[a-z0-9_.:]+`, that is: lowercase Latin letters, Arabic numerals, underscores, periods, and colons.

> For future-proofing, it is not recommended to create a tag with the prefix `minecraft:` to ensure a tag does not clash with a future Mojang-defined component. Furthermore, it is suggested to use a pack-specific namespace with these tags to minimize collisions with other behavior packs, such as `betterbiomes:arboreal`.

### Inheritance
Biome files can act as initial definitions or overrides depending on behavior pack ordering. The earliest appearance of a biome definition in a behavior pack stack is the **initial definition**; Subsequent definitions of the same biome in the behavior pack stack can modify or override earlier definitions through inheritance.

Only components and tags in the `components` property are inherited. Properties within an individual component are also usually inherited. Unfortunately, some components or component property objects require complete redeclaration of all their properties to work, meaning it is often better to redeclare an entire component when overriding. Inheritance always occurs unless a new component would interfere with a previously existing component, as is typically the case with [surface builders](#surface-builders).

There is no way to indicate a property should be removed from earlier definitions. This can especially be troublesome with tags due to their usage in signifying biome placement and how they power other gameplay elements like mob spawning. If conflicts arise due to inheritance issues, it is recommended to extract the desired elements of a biome into a new custom biome and attempt to remove the old biome from world generation.

Biome files may uselessly be empty if overriding a previously declared biome. If a biome definition, initial or override, contains any contents, it must contain the top-level `format_version` property and down to the `identifier` property. Initial definitions of a biome must contain at least one component or tag; the required declaration is small because defaults for almost every biome aspect are available for fallback.

## Generation
The rules for how a biome is selected for placement depend on 3 things:

1. The dimension for which the biome registers itself
2. The weight for a biome to generate within a slot of a dimension, relative to any other biomes also in that slot *across all behavior packs applied to a world at the time a chunk is loaded*
3. The immutable random noise surface used in that slot derived from the seed of the world

*Biome layout is not randomized per world, only per seed.* This means that if the same add-ons containing custom biome definitions are applied to two new worlds with the same seed, each dimension in both worlds will contain the exact same biome layout. This is obvious for vanilla generation, as the same seed will always generate the same vanilla biomes in the same places.

> The concept of biome slots does not exist in the actual documentation or schemas. This term is used here to represent a dedicated region within a dimension either for which a biome can be selected from a pool or where a collection of biomes are independently connected for a singular purpose. Slots are fixed per seed; that is: they cannot be moved or changed in any way using behavior packs.

Biome weights work like any other weight in behavior packs, so if for a given dimension rule:  
A fictional Biome X has a weight of 5. All the biomes placed in this target slot, including Biome X, have a combined weight of 20. Therefore, Biome X will have a 5 in 20, or 25%, chance of generating.

Biomes are not filled into valid slots in entirety by weight; instead, the available space in a slot appears divided by the weights. A more radical discrepancy between numerator (the target biome’s weight) and denominator (the sum of all relevant biomes’ weights) will result in *smaller* biomes as opposed to *rarer* biomes.

Minecraft currently has no way of creating new dimensions. The End does not allow for biome alterations, new or overridden, leaving only Overworld and Nether implementations.

> A `"minecraft:legacy_world_generation_rules"` component is noted in the documentation to affect legacy limited worlds, but no schema is provided for this component and no vanilla biome definition uses it, rendering the component useless.

### Overworld
```
"minecraft:overworld_generation_rules": {
  "generate_for_climates": [
    ["cold", 1]
  ],

  "hills_transformation": "pumpkin_pastures_hills",
  "shore_transformation": "pumpkin_pastures"
}
```

The Overworld uses concepts of **regions**, **climates**, and **heirarchy** to determine how to place biomes. Biomes are slotted directly into the Overworld as **base biomes**, while **sub-biomes** can be declared in these base biomes for finer tuning.

Biomes interact with Overworld generation using the `minecraft:overworld_generation_rules` component. Here, they can register themselves as base biomes or declare sub-biomes. Biomes do not necessarily need to be base biomes to have sub-biomes. Sub-biomes — in some circumstances — may have their own sub-biomes.

#### Regions
The Overworld is composed of many regions, which act as slots for the Overworld dimension. Obviously split by land and oceans, the dedicated slots relate in a complicated fashion.

> The nature of a biome (its aesthetic and gameplay), do not have to conform to the intention of the slot in which they are placed. The “land” and “ocean” region names used here are therefore slightly misleading: land biomes can be aquatic and ocean biomes can represent land. These are only named as such here in reference to vanilla generation. This is additionally true for all other slot names: river-like biomes do not have to generate along designated stretches for rivers, etc.

Biomes are placed into the Overworld using the `generate_for_climates` property in the `minecraft:overworld_generation_rules` component, but the values given here only affect [climates](#climates). Configuring a biome to generate in a particular slot is unintuitive and expounded upon below.

Vanilla biomes can effectively be removed by setting the weights for their `generate_for_climates` property to `0` across the applicable climates, but Minecraft actually has an aggressive fallback system in place to prevent generation failures.

> Biomes can additionally be **de-slotted** in the Overworld, forcing them to generate elsewhere or not at all. This change is irreversible by later listed behavior packs, as it relies on the tagging inheritance model. Due to the aggressiveness of the fallback system, de-slotting is in some circumstances the only means of removing an unwanted biome.

##### Land
Unlike the real world, land makes up the majority of the Overworld. Land technically contains several odd sub-slots because of a mix of interactions and restrictions with oceans. As noted above, land biomes do not actually have to represent land: this is only the designation for the slot; they can be aquatic or contain ocean sub-biomes.

There are a total of 56 vanilla land biomes, many of which are mutated or hilly forms of base biomes. By default, all custom biomes are land unless marked otherwise.

###### Common Land
```
"generate_for_climates": [
  ["cold", 1]
]
```

Common land is the largest slot in the game, making up the vast majority of land. The majority of biomes in Minecraft are slotted here, such as Deserts, Dark Forests, Plains, and Swamps. Custom biomes generate here when using the ``generate_for_climates` property unless otherwise indicated using the tag system.

<blockquote>
  When all common land biomes are instructed not to generate by setting their climate weights to `0`, Minecraft fills this slot using biomes from the [rare land](#rare-land) slot: Eroded Badlands and Giant Tree Taigas. If these biomes are then de-slotted and also set not to generate, the game descends down a fallback list for which biome will generate across the entirety of land in the Overworld:
- Jungle variants
- The remaining Giant Tree Taiga variants
- Mushroom Fields
- Birch Forest variants
- The remaining Badlands variants
- Desert variants
- Custom biomes and their variants
- Forest variants
- Ocean variants

The variants selected for this list may even act as sub-biomes in vanilla generation. Ocean biomes are the final fallback for land because of tag inheritance: there is no way to de-slot ocean biomes into the ocean slot, as they already have the `ocean` tag in their vanilla definitions. Rare biomes will continue to be slotted in rare land slots until they are de-slotted into oceans.

Minecraft only allows the player’s first load in a select few biomes:
- Plains
- Forest
- Taiga
- Dark Forest
- Savanna
- Jungle

If none of these biomes are present due to setting their weights  for generation to `0` (and in the case of the Plains and Forest biomes, additionally being unlisted as sub-biomes of Deep Oceans), the player cannot load in to the world. The game will search for a valid spawn location endlessly.
</blockquote>

###### Rare Land
```
"minecraft:overworld_generation_rules": {
  "generate_for_climates": [
    ["medium", 1]
  ]
},

"rare": {}
```

Rare land slots are somewhat large but very uncommon regions of the Overworld set aside for biomes. Biomes are slotted here when the `rare` tag is applied to them. Examples of rare biomes in vanilla generation include Jungles, Mesas, and Giant Tree Taigas.

> Rare land biomes can be de-slotted by applying the `ocean` tag to the declaration. This is because the `ocean` tag takes precedence over the `rare` tag. If no `rare`-tagged biome is available for an instance of rare land in a given climate, the game will fall back to compatible common land biomes.

##### Oceans
The rest of the Overworld is covered in oceans. Oceans are a misnomer as they do not fully connect through the world; in Minecraft, the land region instead behaves like this to give the player more room, causing oceans to behave more as seas or lakes. Biomes are slotted into the ocean region by using the `ocean` tag.

The oceans are prevalently split by normal and deep depths with about equal weight. Scattered islands can generate inside the ocean region. By default, there are twelve ocean biomes in total: ten aquatic biomes, one for each combination of the five temperatures and two depths, and two for the Mushroom Fields, base and shore. Ocean biomes do not have to actually generate as aquatic biomes; they can be land. Furthermore, oceans can contain land sub-biomes. Plains, Forests, and Beaches, for example, are not exclusive to oceans but can generate as a part of ocean islands, themselves contained within the ocean region.

> Ocean weighting behaves differently from other distributions. Seemingly, oceans weren’t intended to compete for space: vanilla biomes have exclusively one ocean biome for each depth-climate combination. Competing oceans of similar weights are separated on a very small scale: approximately several blocks across each instance. A greater difference in weights does more cleanly separate competing biomes, but the lesser-weighted biome will still only generate in very small clumps. Generally, it is wiser to use [surface adjusments](#surface-adjustments) or features to transform oceans.

> If all oceans are set not to generate by changing their `generate_for_climates` weights to 0, the game falls back to Frozen Ocean and Deep Frozen Ocean.

###### Basic Oceans
```
"minecraft:overworld_generation_rules": {
  "generate_for_climates": [
    ["lukewarm", 1]
  ]
},

"ocean": {}
```

The basic oceans make up about half of the ocean region. This region is intended to be used by aquatic biomes with a relatively shallow depth.

> [Despite how deep ocean slotting occurs](#deep-oceans), a basic ocean biome cannot be de-slotted using the `deep` tag. It will continue to generate unless the weight for its designated climate is set to `0`.

###### Deep Oceans
```
"minecraft:overworld_generation_rules": {
  "generate_for_climates": [
    ["frozen", 1]
  ]
},

"ocean": {},
"deep": {}
```

Biomes slotted into the deep ocean region use the `deep` tag in addition to the `ocean` tag. Deep oceans make up most of the space remaining in oceans. This slot is typically used with oceans extending deeper than others, often halfway to bedrock from the surface.

> The `deep` tag on its own has no effect.

###### Islands
{% include filepath.html path="biomes/ocean.json" %}

```
"minecraft:overworld_generation_rules": {
  "hills_transformation": "tropical_island"
},
```

Conceptually, islands are no different from sub-biomes in the land region. The islands that generate in vanilla are actually just “hills” in oceans!

> While these islands do not technically form a slot and are instead sub-biomes, due to what is either a bug or an oversight, they are noted as a slot due to how they must be declared. Islands are never declared for a custom ocean biome and can only be separately grouped by ocean depth. Islands are declared using either the `hills_transformation` or `mutate_transformation` properties in the `minecraft:overworld_generation_rules` component *only* in override definitions for the `ocean` and `deep_ocean` biomes; they can also be declared as [mutated hills](#mutated-hills). Islands in vanilla only generate using hills sub-biomes and only in Deep Oceans; vanilla islands can therefore entirely be disabled by pointing the `hills_transformation` in an override for Deep Oceans to the Deep Ocean biome itself:

{% include filepath.html path="biomes/deep_ocean.json" %}

```
"minecraft:overworld_generation_rules": {
  "hills_transformation": "deep_ocean"
},
```

Because of [how shores are prioritized when generating land](#shores), islands in the ocean may form entirely as shores. This can, however, be overridden, as described in [Rivers & Shores](#rivers-shores). Islands may additionally have their own river sub-biome; the vanilla islands use Rivers.

###### Mushroom Fields
Very rarely, Mushroom Fields generate within ocean regions. The Mushroom Fields biomes cannot be disabled and are generated at fixed locations determined by the seed; these are the only biomes in the Overworld that are fixed.

#### Climates
```
"generate_for_climates": [
  ["frozen", 2],
  ["cold", 1]
]
```

Base biomes must be declared in a temperature category to generate. All of a base biome’s sub-biomes will exist within the bounds of the base biome and therefore lie within its associated climate.

> These climate temperature types are different from the float property `temperature` in the `minecraft:climate` component. Traditionally, however, they correlate for gameplay purposes. Because of how sub-biomes are placed as noted above, it is possible to force a snowy sub-biome to appear within a warm biome, but this is not recommended.

The 5 climates are, by increasing temperature:

- Frozen: `frozen`
- Cold: `cold`
- Medium: `medium`
- Lukewarm: `lukewarm`
- Warm: `warm`

To promote a biome to a base biome that will generate in the Overworld, the biome’s definition must have the `generate_for_climates` array property within the `minecraft:overworld_generation_rules` component. This array contains array values of the form <code>[*climate_type*, *weight*]</code>, where <code>*climate_type*</code> is one of the listed climate strings and <code>*weight*</code> is a float value reflecting the biome’s chance to generate. Biomes are generated by weight within each declared climate category *in the relevant region*, generating sub-biomes within their bounds.

The temperature map is entirely separate from the designated slot locations described above. Climate temperature regions are fixed per seed. A biome with a given climate and region slot can therefore only generate in the fixed intersections of the climate and region slot maps for a seed.

Unlike region slots, biomes can be registered for multiple climates. This can, for example, be used to spread a biome across different climates if it would be appropriate, like the Plains biome. If the same biome generates in two adjacent climates and these separate biome instances are next to each other, the biome will seem to combine into one with no indication of the boundaries of a climate region.

> If all biomes for a climate are set not to generate, Minecraft will use biomes from other climates to fill that climate’s designated space.

#### Hierarchy
```
"minecraft:overworld_generation_rules": {
  …
  
  "hills_transformation": [
    ["overgrown_forest_hills_short", 4],
    ["overgrown_forest_hills_tall", 1]
  ],
  "shore_transformation": "rocky_shore"
}
```

Overworld biomes may directly or indirectly be placed by the world generator.

If declaring a target climate temperature in the `generate_for_climates` property, a biome will behave as a base biome. Biomes placed directly are generally large and may declare their own sub-biomes of these categories:

- Hills: `hills_transformation`
- Mutated: `mutate_transformation`
- River: `river_transformation`
- Shore: `shore_transformation`

These sub-biomes are therefore indirectly placed, not declaring their own generation in the Overworld but instead relying on a base biome’s generation. Biomes may be referenced without limitation: they may appear as a base biome and simultaneously be a sub-biome somewhere else.

In light of regions and climates, sub-biomes may be perceived as optional further limitations on biome placement. Hills and mutations are fixed, scattered, bounded regions within which sub-biomes may be placed; they can even overlap, forming mutated hills. Rivers run as lines through the world, and their shape cannot be influenced at all. The placement of shores, meanwhile, is indirectly determined by other biomes.

##### Types
###### Hills
```
"hills_transformation": "pumpkin_pastures_hills"
```

Hills sub-biomes are small, common subsets of a biome generally used for elevation shifts. Despite their name, they do not have to be used to generate hilly terrain. Their chance to generate within a base biome is common enough that they can reliably be used to form large, natural generations such as lakes, craters, woods in an otherwise tree-less biome, and more. Hills sub-biomes are used in the vanilla Deep Ocean biome to generate islands. They can be used anywhere in the Overworld but will never be selected if used in a river or shore sub-biome. Not declaring a hills sub-biome will have no effect on the base biome, leading to normal generation.

###### Mutations
```
"mutate_transformation": "mushroom_forest_dense"
```

Mutated sub-biomes are large, rare subsets of a base biome that are typically used for odd variations. One vanilla example is Sunflower Plains; another is Ice Spikes. Unlike the other dependently generated biome categories, mutated sub-biomes do not generate reliably. They should not be used with an expectation that they will generate within an instance of a base biome. Like hills sub-biomes, declaring mutations as a sub-biome to a river or shore sub-biome won’t do anything. If no mutated sub-biome is declared, no transformation will occur.

###### Mutated Hills
{% include filepath.html path="biomes/mangrove_forest.json" %}

```
"hills_transformation": "mangrove_forest_hills"
```

{% include filepath.html path="biomes/mangrove_forest_hills.json" %}

```
"mutate_transformation": "mangrove_forest_hills_mutated"
```


Hills sub-biomes may declare their own mutated sub-biomes, effectively creating a mutated hills sub-biome. This very rare sub-biome generation allows all the same interactions as hills or mutated sub-biomes including having its own river and shore. Mutated hills won’t generate if a hills sub-biome is declared as part of a mutated sub-biome.

###### Rivers
```
"river_transformation": "riverbed_dry"
```

Rivers exist in dedicated spaces fixed to the seed of a world and are unchangeable via behavior packs. While the shape of rivers technically run everywhere in the Overworld, they only generate when intersecting with a land biome. The intersecting land biome declaration can specify a river sub-biome to apply to stretches allocated for river generation. While the widths of rivers are not configurable, rivers may appear wider with lower heightmap configurations.

By default, Minecraft uses the River biome if the `river_transformation` property is not declared as part of the `minecraft:overworld_generation_rules` component or if this component is not declared at all. To effectively remove rivers from a biome, the `river_transformation` property can point to the declaring biome itself via its identifier; this retains the biome’s surface builder and its specified blocks, heightmap, climate, etc., along the river’s route, generating the declaring biome smoothly without interruption. Rivers declared in a biome with the `ocean` tag have no effect on world generation. Slotting tags added to a river biome are ignored.

###### Shores
```
"shore_transformation": "cliffs_steep"
```

Shores are special stretches of land designated to generate between a land biome and ocean biomes: biomes without the `ocean` tag and those with it. Because these locations vary under customized biome definitions, shores are the only sub-biome whose location can be influenced. This is not merely restricted to the major land and ocean regions of the Overworld but can also be used between conflicting sub-biomes. Alternations such as these could be used to generate large, shallow lakes with shores or even a transition biome between what appears to be two land biomes.

Like rivers, shores are declared as part of a land biome, this time using `shore_transformation`. The shores that generate between land and ocean biomes are *always* selected from the land biome; adding shores to oceans has no effect on generation. Slotting tag additions have no effect on shores. Shores default to Beaches and can again be effectively removed by referencing the declaring biome. If removed, the base biome will ease into the ocean at a slightly steeper angle, ignoring sandy shores in favor of the blocks used by the base biome’s surface builder.

Shores are always prioritized against their referencing biome when space is small. If an area of the Overworld surface designated for a land biome would be sufficiently small, the resultant generation may just be shore, with no hint of the referencing biome in sight.

##### Interactions
Nesting sub-biomes has no effect. Hills cannot have further hills. The same goes for all sub-biome types. Hills, mutations, and mutated hills may all declare their own river and shore sub-biomes allowing for finely tuned changes on a sub-biome scale. Rivers and shores do not generate any sub-biomes. 

##### Weighting
```
"mutate_transformation": [
  ["crater", 2],
  ["lava_pit", 1]
]
```

Multiple sub-biomes may be declared for each type of sub-biome. They may be given float-valued weights when declared in a base biome to vary their occurrences. For example, the hills sub-biome is really just a small, common subregion of a base biome, so it can be used to form many different scenes. A single base biome may have, for example, both hill and lake “hills” sub-biomes.

The base biome may be referenced from its own weighted sub-biome declarations. Like with climate biome weights, this has the effect of decreasing the available space afforded to actual sub-biomes, making them smaller in surface area as opposed to making them rarer by count. For a hilly base biome using hills sub-biomes, this could be used to make small, rare mountain peaks. For a dry, warm base biome using river sub-biomes, rivers could appear dried up every now and again without having to depend on hills or mutated sub-biomes.

##### Exceptions
Mushroom Fields cannot have river or shore sub-biomes; the shore that generates along its coast is fixed. Mushroom Fields do not generate separate shores even if it has hills, mutations, or mutated hills sub-biomes marked as oceans via tags. The mutations Mushroom Fields does allow can have their own river and shore sub-biomes, but this is not recommended.

Mushroom Fields Shore cannot have any sub-biomes.

### The Nether
```
"minecraft:nether_generation_rules": {
  "target_temperature": 0.5,
  "target_humidity": 0.75,
  "target_altitude": -0.25,
  "target_weirdness": 0,
  "weight": 0.1
}
```

Nether generation is far more pure and allows for more control than the Overworld, but this comes at the cost of significantly increased complexity. [Arbitrary systems](#strategies-considerations) should be constructed on top of [the powerful provided mathematical system](#principles) for a functioning Nether layout system to work.

#### Principles
Unlike the Overworld, which defines fixed regions for placing biomes by random chance, the Nether uses a 4-dimensional “multi-noise” biome layout system. No sub-biomes exist in this dimension: the Nether exclusively places biomes directly.

> As described in [Aspects & Targets](#aspects-targets), a biome may completely encapsulate another biome if both biomes are configured for this to happen.

> Despite its appearance, Nether biomes only generate depending on the `x` and `z` coordinates with all `y` values at those coordinates belonging to the same biome; it is not currently possible to place a biome vertically adjacent to another biome in the Nether.

##### Aspects
In the Nether’s multi-noise system, 4 independent values are assigned to every `x`-`z` location in the Nether based on the world seed using Perlin noise curves, values on the closed interval [-1, 1]. These values remain constant across worlds of the same seed if the Nether-declaring biomes across all applied behavior packs remain constant — they will not change per world otherwise. For convenience, these independent values will be described here as **aspects**; the documentation does not use this vocabulary. These four aspects are assigned arbitrary names for usage in behavior packs and “targeted” by a biome definition with the following properties:

- Temperature: `"target_temperature"`
- Humidity: `"target_humidity"`
- Altitude: `"target_altitude"`
- Weirdness: `"target_weirdness"`

> The names have no correlation to the properties of a biome, i.e., setting a larger `target_temperature` will not result in a warmer climate for that biome. These names are merely a way to refer to the independent aspects. The names can be disregarded or reinterpreted as desired.

###### Aspect Properties
Values generated by Perlin noise exist on the interval `[-1, 1]`, but the distribution between the extremes is not even. Perlin noise on such an interval tends to distribute similarly to a bell curve with a standard deviation of about 0.4, leading to a couple of obvious conclusions:

- Values closer to `0` are more likely to generate; values closer and closer to the extremes become *much* less likely.
- The distribution is effectively symmetrical around `0`, yielding 2 even “paths” of rarity.

Because Perlin noise is an interpolated process, each aspect will be smoothly generated. This means that a generated noise curve for the Nether based on the `x` and `z` coordinates conforms to the [Intermediate Value Theorem](https://en.wikipedia.org/wiki/Intermediate_value_theorem): values for that dimension must smoothly transition between local maxima and minima.

> Currently, the way coordinates are mapped as inputs to the Perlin noise generators cannot be changed. This means that the distance along the horizontal plane (the `x` and `z` coordinates in the Nether) between local extrema is fixed; conveniently setting all biomes to be larger or smaller is impossible. Biomes may, however, appear sufficiently large with a small number of Nether-registered biomes and vice-versa.

As an example of these properties, consider a scenario where only the 5 vanilla Nether biomes generate. [Isolating a single dimension](#ignoring-aspects) for the example, temperature, all other aspect targets will be set to `0`. The vanilla biomes will be mapped to temperatures as such:

| Biome | Temperature
|:--|--:|
| Soulsand Valley | -1 |
| Warped Forest | -0.5 |
| Nether Wastes | 0 |
| Crimson Forest | 0.5 |
| Basalt Deltas | 1 |

This means that Soulsand Valleys and Basalt Deltas act as extremes; they will be isolated and uncommon and form simple, often convex shapes. In the middle, Nether Wastes will often wind seemingly endlessly in a loose, wavy shape. The two forests will form large rings between the mean and extremes. In other words, because of interpolation, a player would have to move through the Warped Forest, Nether Wastes, and Crimson Forest biomes in that order to reach a Basalt Delta from a Soulsand Valley.

Unfortunately, actual generation is much less convenient to understand. With 4 dimensions, configurability of target matching, and virtually no limit on biome count, it can be much more challenging to create a compelling Nether layout. However, by [understanding targeting](#targeting) and [constraining and isolating target values and fine-tuning the weightings](#strategies), an interesting layout can be achieved with minimal trial and error.

##### Targeting
With particular values set for each aspect at a spot in the Nether, Minecraft then uses biome definitions to determine which biome will be selected for generation. Unlike the Overworld, the same biomes will always generate for the same values; there is no hidden randomness here. This is because the game uses a formula to determine the biome whose aspect targets most closely match the values at a given position. The declared targets never change in a game session, so that biome would always be selected for those values.

> The exact formula used to determine the closest matching biome to a set of values is unknown. It can be expected to be either a simple sum of absolute value differences or a 4-dimensional distance formula.

It can therefore be understood that every Nether biome shares a portion of the 4-dimensional space that is formed from the intersections of valid aspect values. The divides between these forms are derived from the aspect targets of “adjacent” and therefore competing biomes.

Again [considering a single dimension](#ignoring-aspects) (Aspect 1) for the sake of simplicity, imagine attempting to distribute 3 biomes: Biome A, Biome B, and Biome C. Because of how targeting finds a closest match, success intervals are formed based on the targeted values, which is what will ultimately decide where a biome generates.

As one specific example, imagine targeting the most extreme values on the range:

| Biome | Aspect 1 Target | Success Interval |
|:--|--:|--:|
| Biome A | -1 | [-1, -0.5] |
| Biome B | 0 | [-0.5, 0.5] |
| Biome C | 1 | [0.5, 1] |

In this case, even though the targeted values are evenly spread along the range, the intervals derived from these values are not the same size. This is because the targets are pushed to the limits of the range, with midpoints between the targets of means and extremes existing at -0.5 and 0.5; it is these 2 values that ultimately divide the resultant intervals. In this scenario, Biome B will be very prevalent across the Nether, while Biomes A and C will be noticeably less common.

Attempting to evenly distribute the intervals by approaching the problem in reverse reveals that the full noise range can be divided into thirds via [-1, -1/3], [-1/3, 1/3], [1/3, 1]. The targets must then be evenly spaced around the breakpoints, resulting in:

| Biome | Targeted Value | Success Interval |
|:--|--:|--:|
| Biome A | -0.667 | [-1, -0.333] |
| Biome B | 0 | [-0.333, 0.333] |
| Biome C | 0.667 | [0.333, 1] |

The space (in this case just intervals on a line segment) is now evenly divided, showing how the spatial boundaries are formed between targets.

> *However, even with the intervals being evenly spaced, noise distribution will still ensure the biomes don’t evenly take up 1/3 of the Nether!* Biome B here will still be the most common, but Biomes B and C will appear more frequently than the first example. To truly evenly distribute biomes such that each would have about a 1 in 3 chance of generating, both the success interval and the noise distribution must be taken into consideration. In this example, intervals of [-1, -0.25], [-0.25, 0.25], and [0.25, 1] would approximately evenly distribute the three biomes across the Nether.

###### Targeting Adjustment
Biomes can also declare a fifth property in the `"minecraft:nether_generation_rules"` component to affect biome matching, `"weight"`, which can require the aspect values to more closely align with the biome’s aspect targets for the biome to generate. Weight is designed to behave on the interval [0, 1], where 0 causes the matching to behave as normal, and 1 will require an *exact* match for the biome to generate.

> Because exact matches are exceptionally rare and take up only an infinitesimal space on the map, a value of `1` will effectively disable a biome from generating unless all other biomes have radical weights, too. Using values outside the intended interval will result in further extreme situations, with only one biome of a set of radically weighted biomes being able to generate. It is therefore not recommended to set this property outside its intended range.

Weight adjustments can therefore only decrease a biome’s size. These adjustments are helpful when using a biome to transition between two other biomes. While a biome may be made smaller by adjusting its aspect targets, this can cause a chain reaction of constantly having to revise targets in other biomes because of how they all influence each others’ generation. Using `"weight"` is a simple, singular action.

> Constantly using weight adjustments can make the system even more complicated to understand, as an additional property will have to be taken into consideration everywhere it is used. For this reason, weight adjustments should be used sparingly. A general rule is to never use it in “successive” biomes: biomes that target more or less the same aspect values.

If multiple Nether biomes have the same exact aspect targets, only one of them will generate. If a targeting adjustment is given with the `"weight"` property, the biome whose `"weight"` is closest to `0` will be selected, and the other biomes will never generate. If multiple biomes are equally distant from `0`, a fixed order is used to determine the single biome that will always generate for those targets.

> The system used for prioritizing a biome for generation under equal targets and effective weights is unknown. The biome selected does not change with each instance of a world or even a seed, so presumably it is based on the filename or biome identifier, perhaps taking behavior pack ordering into consideration, too.

#### Strategies & Considerations
In a vague mathematical system of unseeable values, it can be difficult to decide how to lay out the Nether. When going further and reinterpreting the aspects, there is no set direction, which can lead to an endless cycle of property readjustments. It is therefore paramount to establish strategies before beginning.

> Due to the arbitrary nature of meaning used in the Nether, any custom system only works when all Nether-declaring biome definitions are “on the same page”. Such a system fails when biome definitions from other behavior packs follow their own agenda. Interpretations must be conservative when Nether-altering behavior packs may compete.

##### Separation of Concerns
Because the aspects are completely independent and their given names are meaningless, the aspects can be reinterpreted as any system of independent properties. In a grimmer Nether, these aspects could be something like:

- Corruption
- Living/dead ratio
- Soul affinity
- Spitefulness

In a Nether reinterpreted as an extension of the bottom of the Overworld, the aspects could be:

- Temperature
- Darkness
- Richness
- Dangerousness

So long as the arbitrary meanings always match the property names, any custom system can be used. Only after establishing the meaning of the aspects can the actual assignments of aspect targets commence.

> Due to the arbitrary nature of meaning used in the Nether, any custom system only works when all Nether-declaring biome definitions are “on the same page”. Such a system fails when biome definitions from other behavior packs follow their own agenda. Interpretations must be conservative when Nether-altering behavior packs may compete.

###### Ignoring Aspects
Aspects can effectively be ignored for the sake of generation. By setting all aspect targets to the same value, such as `0`, that aspect will not play a role in determining biome layout. This can be the right option for several use cases:

- A total of four independent parameters are not required to achieve an effect.
- Only a small number of biomes need to be considered.
- [Simple, dependable biome transitions](#containment-transitions) are desired.

If any of these conditions are true, some aspects should be ignored to ease development.

> Vanilla generation itself ignores 2 of the 4 aspects, altitude and weirdness.

###### Arbitrary Aspect Types
It can be challenging to ensure all biomes can generate [due to uniqueness requirements in biome generation under a multi-noise layout system](#targeting-adjustment). Values can be arbitrarily adjusted per-aspect, but it is cleaner and easier to impose uniqueness expectations onto each aspect, creating non-unique and unique aspects.

Non-unique aspects may have values that are not guaranteed to help uniquely place a biome. One usage of this is [tiered aspects](#tiering). Unique aspects, meanwhile, can be used to find a distinct set of conditions in the Nether for a biome to generate.

When using such a methodology, at least one unique aspect must be used. Beyond the guaranteed one unique aspect, any of the other aspects may be unique or non-unique, but this system affords the most potential when only one aspect is expected to contain unique values.

##### Rarity
There are two primary means of establishing the rarity of Nether biomes: per-aspect rarity and the designation of one of the aspects to represent rarity itself. The latter method enables complete control over biome weighting, not too dissimilar to [Overworld layout](#overworld).

###### Per-Aspect Rarity
Per-aspect rarity refers to how each aspect, no matter its functional use case or arbitrary interpretation, is [independently distributed](#aspect-properties). This distribution must be taken into consideration when targeting aspect values. With 2 symmetrical distributions of rarity with Perlin noise generations, competition for available space on an interval is typically a non-issue; the negative values can be targeted if the positive values become too cluttered. A [tiering](#tiering) plan for rarity can further ease pains caused by constrained space.

###### Independent Rarity Aspect (Weighting)
[Usage of a unique aspect](#arbitrary-aspect-types) works especially well for setting weights for Nether biomes like how the Overworld generation works. In this system, one aspect, such as weirdness, is re-designated to represent weight. Assuming the other 3 aspects are non-unique and used to represent standalone properties of a biome, this weighting can be used to pick a particular biome dependent upon the [distribution of Perlin noise](#aspect-properties) for that re-imagined aspect.

Generally, a meaningful selection of the other aspects shouldn’t necessitate great complexity within the weight aspect, but if there are a large number of possibilities desired for a given combination, the uniqueness of values and computed target intervals must also be considered. Essentially, every weight for a given combination of the other aspects must be unique [due to uniqueness requirements](#targeting). With this uniqueness in mind, the intervals derived from these targets need to be carefully spread to get the desired weightings exactly right. [Targeting adjustments](#targeting-adjustments) are useful here, but the weights may need to be adjusted across all biomes targeting the same combination when a new biome is added to the set.

When no weights are needed for a combination of the non-unique aspects because only one biome matches the conditions, target a value of `0`. This gives the maximum berth possible for that biome to generate, helping to avoid interference from unwanted biomes.

> Because masking of aspects does not exist in the Nether, this weighting system is susceptible to some minor failures caused by [the function that calculates distance in the 4-dimensional map of aspect target spaces](#targeting). For a given set of values for a point in the Nether, if a target weight is far enough from the actual value of that aspect at that point when the other 3 aspects are well-targeted, the discrepancy may cause the system to pick an undesired biome. In other words, usage of a weighting aspect is not rigid or guaranteed. However, the biome selected by the system will still be well-targeted and appropriate for the values, and the intended biome may very well show up with a smaller surface area nearby, so this system’s failures are mild.

##### Tiering
Tiering can be used to assign descriptive, qualified meaning to quantifiable values. Tiering further helps Nether biome development by imposing a sort of “schema” to which all targeting values for an aspect should conform.

Using the Overworld climates as an example, one could assign numbers to temperature meanings, like the following:

| Climate | Temperature |
|:--|--:|
| Frozen | `-0.6` |
| Cold | `-0.25` |
| Normal | `0` |
| Lukewarm | `0.25` |
| Warm | `0.6` |

In this system, all values of this aspect across all Nether-declaring biomes should be expected to use these values. Such a system would both ensure “colder” biomes won’t generate near “warmer” biomes while also conveniently allowing for [clustering](#clustering-avoidance) of similar biomes without worrying about uniqueness. At any given time, this “schema” may be extended with additional meanings, like a “flaming hot” definition with a value of `0.8`.

##### Transitions
As described in [Aspect Properties](#aspect-properties), transitions are guaranteed to occur across a single aspect when all other aspects are [ignored](#ignoring-aspects). This can lead to long transitions or “shorelines” between biomes, depending upon the sizing of the intervals and the targeting adjustment. Achieving this effect becomes non-trivial when only adding one more aspect to consider and almost always unmanageable when using more than 2 aspects.

Regardless of implementation difficulty, the behaviors at play are simple to understand. Because the aspects are independent and each follows the Intermediate Value Theorem, transitions across the surface of the Nether are independently smooth *across every aspect*. When using multiple aspects in Nether generation, the transition between a point and another nearby point may result in changes across any of the aspects from one to another. [Because biomes always generate under the same conditions in the Nether](#targeting), every single aspect leading into to a target biome would have to be considered for a transition to occur to that target.

As an example, if a biome had the following Nether generation rules:

```
"minecraft:nether_generation_rules": {
  "target_temperature": 0.2,
  "target_humidity": -0.6,
  "target_altitude": 0.4,
  "target_weirdness": 0,
  "weight": 0
}
```

Assuming the weirdness aspect was ignored, a transition biome would have to occur for every combination before and after each of the other 3 target aspects. Because a single biome definition cannot target multiple spots in the Nether, 8 different definitions would have to be created and well adjusted to act as transitions into this target biome. Furthermore, if any of the aspect targets in this biome changed, all transition biome definitions would have to be updated to accommodate the change.

There are, however, two different scenarios where transition biomes can be used with minimal effort or complications.

###### Corner Transitions
Corner transitions can occur when the biome to be transition to exists at the absolute extremes of the used aspects. An example is if the target biome targeted values of +/-1 for every used aspect. In this case, a transition biome could be created by placing values “right in front of” the target biome, like at +/- 0.8 for the same aspects.

As an example, if at target biome had the following targets:

```
"target_temperature": 1,
"target_humidity": -1
```

A transition biome could be established using:

```
"target_temperature": 0.8,
"target_humidity": -0.8
```

###### Tiering Transitions
Tiering transitions can be used in a [tiering system](#tiering) to separate otherwise strongly opposing tiers. Unlike corner transitions, tiering transitions are fallible due to the nature of biome selection in the Nether and how available space is delegated for aspect targeting.

If a tiered aspect had the following schema:

| Life force | Value |
|:--|--:|
| Undead | -0.8 |
| Virile | 0.8 |

A transition mixing these two extremes would help the change between the two be less jarring. To achieve this, simply add a new transition tier, such as “Void” with a value of `0`.

In the case that this transition could be represented by more than one biome, the set of space dedicated to these transition biomes could end up being sufficiently large for the transition to always occur between the two extremes. If only one biome should act as this transition, however, the biome may need to be duplicated for combinations of other used aspects to reserve enough of the targeting space for the transition to always occur.

##### Arrangements
Because strict boundaries aren’t a given in the Nether’s multi-noise system, biomes are never absolutely arranged; the concept of [slotting](#regions) doesn’t exist in the Nether. However, biomes in this system can still be arranged relative to one another, so long as all targeted values across all Nether-declaring biomes are considered.

###### Clustering
Biome clustering is rather straightforward and becomes more obvious as the count of biomes registered for the Nether increases. Biome clustering occurs when a group of related biomes have sufficiently close values. To cluster biomes together, simply assign targets to every biome that are only mildly offset from one another. Ensure the every biome has its own unique values to avoid conflicts.

Due to the nature of the multi-noise system, there is no guarantee that all the biomes in an intended cluster will generate together, but more than likely at least some of them will.

For biomes targeting values farther away from the averages for each aspect in the cluster, a small [target adjustment](#target-adjustment) may need to be provided to ensure the “outermost” biomes in the cluster don’t bleed too far into space that would typically be designated for biomes outside the cluster.

###### Isolation
Biomes may be isolated at the extremes of the values of an aspect. Setting a biome to target a value near the extremes (`-1` or `1`) of any aspect can help ensure the rarity of that biome. With a sufficiently large number of biomes per [used aspects](#ignoring-aspects), these isolated biomes will typically be smaller and form simple, discrete shapes due to Perlin noise interpolation. Such isolated biomes become increasingly smaller and rarer for each aspect targeted with an extreme value.

###### Avoidance
The dual nature of the range of Perlin noise for aspects can be used to force biomes away from one another. If the biome count for the Nether is small, [transitions](#tiering-transitions) can be established to separate biomes. For larger biome counts, biomes can avoid each other by setting their targets *for a single aspect* to opposing extremes, such as `-1` and `1`. This will effectively [isolate](#isolation) both biomes and prevent them from ever directly touching.

> Setting the values for more than one aspect target in opposing biomes to extremes is fruitless for the actual sake of avoidance. This would only work to further isolate each biome by constraining the conditions under which each could generate due to the independence of the aspects. At the same time, the minimum distance between two instances of these biomes would not decrease but would only serve to minimize the count of “close calls” due to the now compounded rarity of the biomes.

### Dimension Interactions
Dimension-specific tags used for slotting have no effect across dimensions; for example, the `ocean` or `rare` tags have no effect in the Nether or on The End biome.

Biomes may generate in multiple dimensions; they need only to register themselves for each desired place (currently only the Overworld and Nether).

## Shape & Style
The actual look of a biome depends on its shape and its aesthetic. These concepts exist entirely separately from how a biome is placed, meaning that a single aesthetic can be reused in multiple places in the Overworld; as an example, Forests can exist: independently as a base biome, as a sub-biome to Plains, or as an island in the ocean.

Biome aesthetic is controlled by the blocks comprising the biome and the climate features the biome declares. Blocks comprising a biome are predominantly declared using surface builders, but eligible surface builders allow for noise-controlled adjustments.

Biome shape depends on the surface builder it declares and the biome’s heightmap settings. A biome’s shape will fluctuate per-block; these fluctuations are fixed per dimension per seed, meaning that the same shape settings for a biome at the same location in a dimension will then only vary per seed.

### Block Types
Blocks are declared using the simple notation or the stateful notation. The **simple notation** references the identifier for a block as a string, such as `"minecraft:grass"`. If no namespace is provided, the game attempts to find a registered block with that name across all declared namespaces.

> It is strongly advised to always use the complete name of a block, including the namespace, to avoid unexpected issues.

The **stateful notation** indicates block states for selecting a particular variant of a block.

> Unfortunately, block states for vanilla blocks do not currently cover every possible true state for every block; for example, not all directionally placeable blocks have a state for their orientation, like walls.

Stateful notations are objects with a `name` string property referring to the block identifier (like the basic notation) and a `states` object property providing state declarations. An example of a stateful declaration would be:

```
{
  "name": "minecraft:concrete",
  
  "states": {
    "color": "red"
  }
}
```

### Heightmap
```
"minecraft:overworld_height": {
  "noise_type": "lowlands"
}
```

**The heightmap for a biome can only be customized for the Overworld.** The Nether sets its biomes’ heightmaps to give the dimension a consistent feel.

Heightmaps are customized by affecting the noise a seed gives its terrain. The Overworld heightmap is adjusted using the `minecraft:overworld_height` component. Noises declared here can be customized using either numeric parameters passed to the noise generator or named presets of these parameters used in vanilla generation.

> If a preset is used anywhere in the inheritance chain for a biome, this preset will unconditionally override declarations of numeric parameters. This can occur if both described properties are declared in a biome definition’s `minecraft:overworld_height` component or when attempting to override a biome initially declared earlier in a behavior pack stack. Unfortunately, most vanilla biomes use presets, restricting heightmap adjustments in these biomes only to the provided presets.

The world generator will smoothly transition between heightmaps of adjacent biomes. Gradual descents and diagonal changes in elevation are not reliably possible using heightmap adjustments. In other words, world painter-like biomes are not currently possible.

#### Noise Parameters
```
"noise_params": [0.5, 0.125]
```

Noise parameters are declared as a 2-valued array using the `noise_params` property.

The first value represents the average height of a biome. Interestingly, this parameter does not directly use block height (the `y` coordinate) and is scaled to where a ∆ of 1 in the value represents a ∆ of 16 blocks in the average height of a biome. Furthermore, this value is zero-set to a `y`-height of about 67, several blocks above sea level. This means that to set this value with a particular average `y`-height in mind, use the formula:

*f*(*y*) = (*y* - 67) / 16

Therefore, setting this value to `1` will result in an average `y`-height of about 83, similar to the lesser hills in the Mountains biome. Setting this value to `-2` will result in a surface like that of a Deep Ocean, well under sea level.

> The maximum average height of a biome only works up to a `y`-height of 128: the first value of the `"noise_params"` array, therefore, has no effect above about `3.8125`.

The second value of the array determines height variation. Negative values behave erratically and should generally not be used; in many cases, no terrain is formed other than the bedrock foundation. A value of `0` will make terrain variance small but not make the biome completely flat. Values up to about `0.125` will generate particularly smooth terrain; values greater than this begin to form cliffs, coves, and hollows. Extreme overhangs form beginning at `0.25`. By `0.5`, massive floating islands can dominate the landscape at the cost of player mobility. The terrain becomes more radical with larger values and should generally not be used to avoid player annoyance.

> If a perfectly flat surface is desired within a biome, the second value given to `"noise_params"` should be set to `0` to minimize height variation. The first value should then be set to `4`, above the value of maximum effect, to guarantee unconditional height variations do not dip below the average height upper bound. Despite how flat these values will cause the biome interior to generate, the biome surface will still smoothly transition to lower adjacent biomes as needed, causing massive rises and falls unless the entirety of the Overworld is rewritten to sit at this `y`-height of 128.

#### Noise Presets
```
"noise_type": "ocean"
```

Noise presets provide a convenient way to emulate vanilla biome generation. It is not possible to create custom presets. While the exact values of these presets are hard to gauge, their names are descriptive enough to get an idea of what kind of heightmap a biome will have.

The built-in noise presets include:

- Default: `default`
- Mutated default: `default_mutated`
- Lowlands: `lowlands`
- Highlands: `highlands`
- Mountains: `mountains`
- Extreme: `extreme`
- Less extreme: `less_extreme`
- Taiga: `taiga`
- Swamp: `swamp`
- Mushroom: `mushroom`
- Ocean: `ocean`
- Deep ocean: `deep_ocean`
- River: `river`
- Beach: `beach`
- Stone beach: `stone_beach`

### Surface Builders
Surface builders allow for more stylized terrain. Surface builders allow for biome terrain features that would otherwise be impossible using only heightmap adjustments or biome features. These terrain features are either intricately shaped or large in size. Unfortunately, there is no way to create a surface builder; surface builders exist solely to represent complex vanilla biome surfaces.

Surface builders // inheritance and restrictions;

> Decorations created by surface builders are unfortunately fixed and not relative to the declared heightmap. This means that if the heightmap at the location of a given surface builder-created decoration is high or low enough, the decoration will not appear to exist, consumed by the land or the water.

#### Surfaces for the Overworld


##### Default


##### Swamp


##### Mesa


##### Frozen Ocean


#### Surfaces for Other Dimensions
The surface in The End cannot be changed in any way.

##### Nether


##### Capped


##### The End


### Surface Adjustments
```
"minecraft:surface_material_adjustments": {
  "adjustments": [
    {
      "materials": {
        "top_material": "minecraft:podzol"
      }
      
      "noise_range": [0, 0.5],
      "noise_frequency_scale": 0.0625,
      "height_range": [72, 255]
    }
  ]
}
```

Surface adjustments allow for fine-tuning a biome's surface blocks. Despite being called "surface" adjustments, these adjustments can actually affect all blocks from the heightmap down to the origin (bedrock layer); they cannot be used to alter bedrock or air in caves, above the heightmap, or between shelves of land. Surface adjustment conditions are checked against random noise specific to the world seed.

Surface adjustment declarations can affect the intervals for noise intersection and relative sizing of the noise surface as mapped to the biome surface. Restrictions can also be applied to the heights at which surface adjustments will be applied, either independently or coordinated with noise intersections. Therefore, for an adjustment to be applied to a location, every restriction must succeed; it any fail, the condition fails, and the game will fall back to the surface builder’s declared block for that location.

> Currently, only the default and swamp surface builders support adjustments.

#### Noise Intersections
A noise curve that is dependent upon the seed of a world can be used to limit the `x` and `z` components of an adjustment. The origin of the adjustments noise curve is centered on the world origin and can then be scaled to map onto the horizontal plane of a dimension. The noise curve can therefore only work on this horizontal plane and not on the `y` coordinate; for that, use height restrictions.

The exact value generated from the noise curve at a particular location is inconsequential to the resultant surface adjustment. The only consideration is whether the value at that location falls within the provided closed interval.

##### Intervals
```
"noise_range": [0.5, 1]
```

The noise curve used for surface adjustments generates values lying on the closed interval `[-1, 1]`. The negative values behave symmetrically with the positives; that is: an intersecting sub-interval to this curve `[-0.8, -0.6]` would theoretically have approximately the same shape and represent approximately the same ratio of the full range as the sub-interval `[0.6, 0.8]`. Intervals closer to `0` tend to form continually winding striations in the surface, while those further away tend to form small, discrete, well spread shapes. Intervals closer to `0` also intersect a larger range of the noise curve than intervals of equal length further from `0`; this means that if discrete shapes are desired, like those that are formed at the extremes of the noise curve’s range, a larger relative interval may be required than one targeting the winding paths close to `0`.

##### Sizing
```
"noise_frequency_scale": 0.25
```

The surface adjustment noise curve uses a default mapping relative to the dimension coordinates that would form extremely small transformations. The noise intersections are actually made larger by setting the sizing value to be smaller. Smaller values, such as `0.125`, are key to forming large patches of transformations, such as podzol or coarse dirt clusters. Larger values of this property are typically used to create a messier feel to the terrain. Values greater than the default `1` are not recommended unless something akin to a checkerboard pattern is desired.

#### Height Restrictions
```
"height_range": [
  "math.random_integer(30, 40)",
  "math.random_integer(60, 70)"
]
```

Height restrictions can be provided to limit the valid transformation region. These restrictions are independent of limitations using the noise curve and much simpler, too. Height restrictions are provided as an interval and simply target a range of `y`-heights to transform a region. Layer will be created that are either bound to the entire target biome or to the specific `x` and `z` intersections determined by the adjustments noise curve if it was used. The first value of the `"height_range"` array must be less than the second value or else the adjustment will fail.

Unlike the properties establishing checks against the noise curve, the `"height_range"` property accepts MoLang expressions for its elements. Using math functions, intervals can be created that are randomly spread for higher quality adjustments. Unfortunately, queries cannot be used in these expressions, so adjustments cannot be made relative to the heightmap.

### Climate
```
"minecraft:climate": {
  "temperature": 1,
  "downfall": 0.25,
  "snow_accumulation": [0.0, 0.125],
  "ash": 1
}
```

Climate adjustments work everywhere in Minecraft, even The End.

#### Temperature
```
"minecraft:climate": {
  "temperature": 0.5
  …
}
```

The temperature of a biome affects various gameplay features like precipitation type, the formation of ice and snow layers, and the survivability of snow golems. It is implemented as the float property `"temperature"` and may be set without limitation: all possible float values may be used. Lower values represent colder temperatures. Freezing temperatures, such as where snow falls, occur below `0.15`.

> The `"temperature"` property is unrelated to the climate temperatures given in the `"generate_for_climates"` property in the `"minecraft:overworld_generation_rules"` component, affecting gameplay rather than biome placement.

The temperature established with this property is not the fixed temperature of a biome, only the basis; the actual temperature at a location also depends on the `y`-height. The temperature at or below sea level is fixed to this basis. The temperature decreases by `1 / 600` every block above sea level. The formula, therefore, of the temperature, *T*, at a given `y`-height, *y*, from a declared temperature basis, *t*, for `y`-heights above sea level is given by:

*T*(*y*) = *t* - ((*y* - 63) / 600)

The constant 63 represents the `y`-height of the Overworld sea level. To establish a `y`-height at which a biome will freeze, use the formula:

*t*(*y*) = 0.15 + ((*y* - 63) / 600)

The constant 0.15 here represents the freezing temperature. Data-driven gameplay can use the temperature at the position of an entity to perform actions upon that entity using the `"is_temperature_value"` damage condition filter in an entity definition.

Vanilla biomes only use temperature values ranging from `-0.5` to `2`. Biomes to be completely covered in snow should use values less than `0.15`; `0` is the recommended value for this case. Warm biomes, such as those that would damage snow golems, should use values greater than `1`. Deserts and Nether biomes use `2`. For biomes that should only be capped with snow layers, a value between about `0.2` and about `0.4` should be used due to [how snow layer generation is affected by temperature](#snow-cover).

#### Precipitation
```
"minecraft:climate": {
  "downfall": 0.5
  …
}
```

The float property `"downfall"` controls the extent of precipitation within a biome. Currently, the property only behaves on the closed interval `[0, 1]`; values outside this interval are clamped to the nearest valid value. At `0` or less, this property disables all precipitation effects within a biome. At `1` or greater, precipitation effects will be maximized. Values between `0` and `1` scale accordingly.

> Adjustments to precipitation are *never* reflected visually in the particles that fall when raining or snowing. Precipitation particles are never visible in Desert variants, Savanna variants, or Mesa variants, no matter their overrides; particles are *always* visible in any other biome, including custom ones. Despite this, *most* gameplay affected by precipitation will behave accordingly.

Examples of precipitation effects in vanilla gameplay include the addition of snow layers when snowing, the filling of exposed cauldrons in rain, and the time required for a fish to spawn when fishing. Some gameplay aspects that should consider this value will instead ignore it, such as entities with the `"in_water_or_rain"` damage filter. Lesser values of `"downfall"` will slow precipitation effects accordingly, i.e., snow layers will form a tenth asC fast at a value of `0.1` as they would at `1`.

The type of precipitation occurring at a location depends on its `y`-coordinate. If the value is [freezing or below](#temperature), snow will fall at that location; otherwise, rain will fall.

#### Snow Cover
```
"minecraft:climate": {
  "snow_accumulation": [1, 0.5],
  …
}
```

#### Particle Decorations
```
"minecraft:climate": {
  …
  
  "white_ash": 0.5
}
```

**Particle decorations** are storms of ambient particles visible within a biome. These properties are solely decorative; unlike other aspects of a biome’s climate, particle decorations have no effect on gameplay. Custom particles currently may not be used. 4 different particle decorations from vanilla biomes are available to use anywhere:
- Ash: `ash`
- White ash: `white_ash`
- Red spores: `red_spores`
- Blue spores: `blue_spores`

These decorations will be a constant presence within a biome. If a player is within the bounds of a biome, these particles will be visible, even if underground or within water or lava. If undeclared, no particles will be used in a biome.

As they are represented as float properties in the `minecraft:climate` component, their intensities are adjustable. The float value works for any number greater than `0`. The larger the value, the more particles will be used simultaneously; negative values or `0` will disable the effect.

> It is not recommended to set this value too large, as the particle count may cause crashes to occur. By a value of `16`, the screen will be inundated with particles, but the biome will still be visible through the storm.

## Gameplay


### Features
```
"minecraft:forced_features": {
  "surface_pass": {
    "identifier": "pioneercraft:grasslands_caravan_feature",
    "feature_reference": "pioneercraft"caravan_feature",
    
    "scatter_chance": "100 * math.pow(2, -4)",
    
    "x": {
      "distribution": "uniform",
      "extent": [0, 16]
    },
    "z": {
      "distribution": "uniform",
      "extent": [0, 16]
    },
    "y": "query.heightmap(variable.worldx, variable.worldz)"
  }
},
"minecraft:ignore_automatic_features": {}
```

If a collection of blocks generating in a world aren’t created by a surface builder, they are created from a feature. Features are fundamental to gameplay in Minecraft: vanilla features range from trees to villages to boulders. The features in a biome may handily determine that biome’s worth to a player.

Features are mostly outside the scope of biomes, but the two components within a biome’s schema should be noted.

#### Forced Features
The `minecraft:forced_features` component can be used to force a feature to generate within a biome without using [feature rules](/concepts/features/#feature-rules). The schema here is similar to feature rules and further detailed in that documentation.

#### Ignoring Feature Rules
The empty `minecraft:ignore_automatic_features` component is intended to indicate that a declaring biome will ignore all feature rules attached to it, but this component currently does not work, whether for overrides or initial definitions.

### Tagging
```
"components": {
 …
 
 "urban": {},
 "city": {},
 "metro": {},
 
 "rare": {}
}
```

Tags power much of what brings a biome to life in Minecraft, including entity spawns, feature attachment, and data-driven gameplay. [Because some tags are additionally used (by poor design) to determine where a biome may generate](#regions), issues may arise when attempting to separate placement from form and function. See the [tags section](#tags) for implementation details.

#### Key Vanilla Tags
Custom usages of tags are outside the scope of this document, but a few important vanilla tags should be noted for most behavior packs.

##### Regions & Slotting


##### Mob Spawning


##### Decorations
