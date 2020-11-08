---
layout: page
title: Filters
parent: Concepts
---

# Understanding Filters

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## General Overview

Filters are used inside of various components to _filter_ actions, events, transitions, etc. The general format is like this:

### Single filter
`"filters": { "test": "in_lava", "subject": "self", "operator": "==", "value": true }`

### List of filters

`filters": [{ "test": "in_lava", "subject": "self", "operator": "==", "value": true }]`

