---
layout: page
title: Game Tests
parent: Scripting
badge: BETA
badge_color: red
---

# Game Tests

{% include notice.html 
    contents='The GameTest framework requires you to activate **"Enable GameTest Framework"** in your world settings and you must be using **Minecraft 1.16.210.60 beta or above**'
%}

GameTests are a new feature which allow developers to create unit tests to make it easier to test if game mechanics work. They are created with javascript files in the behavior pack folder and each file can register multiple GameTests. Each GameTest must also have an .mcstructure file in the `BP/structures` folder.

It is recommended that your GameTests go in the `BP/scripts/gametests` directory.

(Type declaration files for the GameTest API)[https://github.com/bridge-core/editor/tree/dev/data/types/gameTest]

## Using GameTests

In the behavior pack manifest you need to add a `plugin` module where you set an `entry` point for your GameTests. The etry point should contain imports 

{% include filepath.html path="BP/manifest.json"%}
```json
{
    "format_version": 2,
    "header": {
        "name": "Pack Name",
        "description": "Pack descripton",
        "min_engine_version": [
            1,
            16,
            210
        ],
        "uuid": "604420b9-f4c3-4df2-9f09-4364486f1195",
        "version": [
            1,
            0,
            0
        ]
    },
    "modules": [
        {
            "description": "",
            "type": "data",
            "uuid": "42651ba5-6619-4547-9d48-84a5a37cf2a3",
            "version": [
                1,
                0,
                0
            ]
        },
        {
            "description": "",
            "uuid": "239c134f-67bf-4738-9bcc-8c69d31b1f72",
            "version": [
                1,
                0,
                0
            ],
            "type": "plugin",
            "entry": "scripts/gametests/Main.js"
        }
    ]
}
```

The entry point should link to a file containing imports to your GameTest files

{% include filepath.html path="BP/scripts/gametests/Main.js"%}
```js
import "scripts/gametests/MyGameTest.js";
import "scripts/gametests/OtherGameTest.js"
```


GameTests can be used with the /gametest command.

- `/gametest runthis`

Runs the nearest GameTest in range.

- `/gametest runthese`

Runs all GameTests in range.

- `/gametest pos`

Tells you the relative coordinates of the nearest GameTest.

- `/gametest clearall [radius: int]`

Removes all GameTests in the specified radius.

- `/gametest run <testName: GameTestName> [rotationSteps: int]`

Creates and runs the specified GameTest.

- `/gametest runset [tagTag: GameTestTag] [rotationSteps: int]`

Creates and runs all GameTests with the specified tag.

- `/gametest create <testName: string> [width: int] [height: int] [depth: int]`

Creates a blank GameTest area with the specified dimensions.

## Table of contents

### Namespaces

- [GameTest](/scripting/game-tests/modules/gametest)
- [Minecraft](/scripting/game-tests/modules/minecraft)

### Interfaces

- [**Test**](/scripting/game-tests/interfaces/test)

- [Block](/scripting/game-tests/interfaces/block)
- [BlockPos](/scripting/game-tests/interfaces/blockpos)
- [BlockPositionClass](/scripting/game-tests/interfaces/blockpositionclass)
- [BlockStates](/scripting/game-tests/interfaces/blockstates)
- [Blocks](/scripting/game-tests/interfaces/blocks)
- [Dimension](/scripting/game-tests/interfaces/dimension)
- [Entity](/scripting/game-tests/interfaces/entity)
- [EntityComponent](/scripting/game-tests/interfaces/entitycomponent)
- [Item](/scripting/game-tests/interfaces/item)
- [ItemStack](/scripting/game-tests/interfaces/itemstack)
- [ItemStackClass](/scripting/game-tests/interfaces/itemstackclass)
- [Sequence](/scripting/game-tests/interfaces/sequence)
- [State](/scripting/game-tests/interfaces/state)
- [TestRunner](/scripting/game-tests/interfaces/testrunner)
- [World](/scripting/game-tests/interfaces/world)

### Type aliases

- [WorldEvent](/scripting/game-tests/modules#worldevent)

## Type aliases

### WorldEvent

Ƭ **WorldEvent**: `*onEntityCreated*` \| `*onEntityDefinitionTriggered*`


## Complete examples
```js
// Structure Path: BP/structures/MinecartTests/turn.mcstructure

import * as GameTest from "GameTest";
import { BlockLocation } from "Minecraft";

GameTest.register("MinecartTests", "turn", (test) => {
  const minecartActorType = "minecart";

  const endPos = new BlockLocation(1, 2, 2);
  const startPos = new BlockLocation(1, 2, 0);

  test.assertEntityPresent(minecartActorType, startPos);
  test.assertEntityNotPresent(minecartActorType, endPos);

  test.pressButton(new BlockLocation(0, 3, 0));

  test.succeedWhenEntityPresent(minecartActorType, endPos);
}).tag(GameTest.Tags.suiteDefault);
```
```js
// Structure Path: BP/structures/DoorTests/four_villagers_one_door.mcstructure

import * as GameTest from "GameTest";
import { BlockLocation } from "Minecraft";

GameTest.register("DoorTests", "four_villagers_one_door", (test) => {
  const villagerActorType = "minecraft:villager_v2";
  const villagerActorSpawnType =
    "minecraft:villager_v2<minecraft:spawn_farmer>"; // Attempt to spawn the villagers as farmers

  test.spawn(villagerActorSpawnType, new BlockLocation(5, 2, 4));
  test.spawn(villagerActorSpawnType, new BlockLocation(4, 2, 5));
  test.spawn(villagerActorSpawnType, new BlockLocation(2, 2, 5));
  test.spawn(villagerActorSpawnType, new BlockLocation(1, 2, 4));

  test.succeedWhen(() => {
    test.assertEntityPresent(villagerActorType, new BlockLocation(5, 2, 2));
    test.assertEntityPresent(villagerActorType, new BlockLocation(5, 2, 1));
    test.assertEntityPresent(villagerActorType, new BlockLocation(1, 2, 2));
    test.assertEntityPresent(villagerActorType, new BlockLocation(1, 2, 1));
  });
})
  .tag(GameTest.Tags.suiteDefault)
  .padding(50) // Space out villager tests to stop them from confusing each other
  .batch("night") // This should be a constant at some point
  .maxTicks(600);
```