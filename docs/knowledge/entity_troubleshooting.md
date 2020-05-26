---
layout: page
title: Entity Troubleshooting
parent: Knowledge
---

# Entity Troubleshooting

Adding entities into Minecraft is a fairly easy process *once you get a hang of it*. The first time is usually a difficult, bug-prone process. This document contains some tips and tricks for fixing those dastardly bugs, as well as best practice information.

## The Environment

The best way to prevent *invisible entity syndrome* and other nasty bugs is by setting yourself the correct environment. You should review [The Editor](https://wiki.bedrock.dev/docs/knowledge/the_editor.html) document for my editor recommendations. The most important part is getting a json-linter ([or using an online tool](https://jsonlint.com/)).

## Content Log

The next thing you should do is turn on your content log. This can be done like: `Settings > Profile > Enable Content Log GUI`. Then press `ctrl+h` in-game to see any errors our output that might pop-up. Errors in the content log will show up every time you open the world, and also during gameplay if more errors occur. 

`warning:` Errors are not cleared between runs, so it is possible the errors you see in the content log are *old* errors, from prior 

## Using Vanilla Resources

You should also download the vanilla resource and behavior pack. You can find these [here](https://www.minecraft.net/en-us/addons/). You can compare against the vanilla files if you have any issues.

## JSON-Schemas

A very valuable tool for validation entity files is by using a JSON-Schema, which you can learn more about [here](https://wiki.bedrock.dev/docs/knowledge/using_schema.html).