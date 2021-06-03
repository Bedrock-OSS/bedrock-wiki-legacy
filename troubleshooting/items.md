---
layout: page
title: Item Troubleshooting
parent: Troubleshooting
---

# Step-by-step Item Debugging

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---
<a name="0.0.0"></a>
## 0.0.0 - Trouble

I followed a tutorial or tried to make my own item and something's wrong! Calm down. This page will help debug common issues.

[Continue](#1.0.0){: .btn .btn-blue }

---
<a name="1.0.0"></a>
## 1.0.0 - 1.10 vs 1.16 Items?

First things first, determine whether you used 1.10 or 1.16 format.
Items are VERY DIFFERENT in 1.16. The main change you need to focus on is that there are longer two files (BP + RP), but rather a single BP file. This means that components like the following need to go into the BP -not the non-existent RP file.

{% include filepath.html path="BP/blocks/your_block.json"%}
```jsonc
"minecraft:icon": {
    "texture": "copper_ingot"
}
```
Make sure it matches the one from your item_texture.json
Learn about the new 1.16 items here: https://wiki.bedrock.dev/concepts/items

## Result
I'm using 1.10 format [Go](#2.0.0){: .btn .btn-blue }

I'm using 1.16 format [Go](#3.0.0){: .btn .btn-blue }

---
<a name="2.0.0"></a>
## 2.0.0 - 1.10 Items

---
<a name="2.1.0"></a>
