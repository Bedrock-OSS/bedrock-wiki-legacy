---
layout: page
title: Text Localization
parent: Tutorials
---

# Text Localization Tips & Tricks

Beginner
{: .label .label-green }

## What is localization?

Language localization is the process of translating a game or software product for a specific country or region.

As an example let's take the `Gold Ingot` from Minecraft, in the code of the game, the developers refered to it as `item.gold_ingot.name`.
That's not a very nice way to call it all the time is it? So for each language that has a Minecraft translation, the developers created a translation(or Localization) file that asigns the proper name to that `item.gold_ingot.name`.

For example for US English they created a `en_US.lang` file and inside it you can find the line: `item.gold_ingot.name=Gold Ingot`
For Spanish we have the `es_ES.lang` file and inside that one you can find the line: `item.gold_ingot.name=Lingote de oro`
For French Canadian we have `fr_CA.lang` and the line: `item.gold_ingot.name=Lingot d'or`

You get the point! For more information about these localization files I recommend our [.lang](https://wiki.bedrock.dev/concepts/lang.html) section.

## A quick example

Ok, before we get too bored, let's do a fast example to peak your curiosity!
Go inside your Resource Pack and find the `texts` folder. Here you should already see a `en_US.lang` file. This is a simple text file that you can open with Notepad. If you can't find it, just create a new `.txt` file and rename it to `en_US.lang`.

Inside the file find the line with `item.gold_ingot.name=Gold Ingot`. If you can't find it just write it yourself.
Now change it to `item.gold_ingot.name=Shiny Yellow Ingot`.

Exit and re-enter your world and hover over a Gold Ingot, it should now say Shiny Yellow Ingot.






Intermediate
{: .label .label-yellow }

Death animation refers to the rotation of the entity as it dies. This is accompanied by a red coloring, and followed shortly after by the disappearance of the entity geometry, and the appearance of the death particles.

# Teleporting the Entity

A fairly common way to remove entities without causing death-effects, is to simply teleport them into the void. This can be done from animation controllers like:
`/teleport @s ~ ~-1000 ~`

Please note that this will remove all death-effects, including sound, particles, loot, and the visual death of the entity. 

# Cancelling the Animation

We can also cancel the rotational value of the entity, allowing the entity to die more conventionally (particles, red-coloring, loot) without the 90 degree spin. This could be useful for things like furniture, where the tipping over effect of entity-death is not desirable.

If you need more information about triggering animations from entity death, [see this document on death effects](/tutorials/death-effects).

Rotation needs to be applied to a bone parent to all other bones, with a pivot at [0,0,0], and the animation should only start when `!query.is_alive`.

Animation:
```json
"rotation" : [ 0, 0, "Math.min(Math.sqrt(Math.max(0, query.anim_time * 20 - 0.5) / 20 * 1.6), 1) * -90" ]

```

---
### Credits
Scai(of Scai Quest)