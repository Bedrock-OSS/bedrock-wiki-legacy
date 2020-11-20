---
layout: page
title: Block Texture Variation
parent: Tutorials
---

# Block Texture Variation

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

Beginner
{: .label .label-green }

Block texture variation is when a single block can have multiple textures.  This is useful for blocks such as dirt or grass where some blocks may have slight variations such as small rocks and others don't.

To enable texture variations you create a folder with the block name in the textures / blocks resource pack folder.  You then store your texture variations as numbered png images, starting at 0.

## Example Dirt Texture Variation

This is an example on how to create texture variations for the dirt block with three images:
- Create a `textures/blocks/dirt` folder in the resource pack
- Create or modify three dirt textures, name them `0.png`, `1.png`, and `2.png`
- Copy the `0.png`, `1.png`, and `2.png` to the `textures/blocks/dirt` folder
- Remove `textures/blocks/dirt.png` if it exists