---
layout: page
title: Runtime Identifiers
parent: Tutorials
---

# Runtime Identifiers

`Runtime identifiers` are used by Minecraft to give custom, hard-coded behaviors to entities. In other words, runtime identifiers give us access to powerful behaviors which can't be created using components. This is achieved by "pretending to be" a vanilla mob. 

If you ever asked yourself: 

"I can't seem to figure out this mechanic. I wish my entity would act more like a ___."

 Then you might consider using runtime identifiers. 

 # Adding Runtime Identifiers to your entity:

Add the "runtime_identifier" key into the description, with a valid runtime identifier.
 ```json
 "description": {
    "runtime_identifier": "minecraft:boat",
    "is_spawnable": false,
    "is_summonable": true,
    "is_experimental": false
}
```

# What do the runtime identifiers do?

This is a stub. If you want to contribute, I am looking for specific information about what certain runtime identifiers change!

| runtime_identifier | action |
|--------------------|--------|
| minecraft:boat     | ???    |
| minecraft:         | ???    |