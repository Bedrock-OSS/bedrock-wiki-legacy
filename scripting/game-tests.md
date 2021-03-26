---
layout: page
title: Game Tests
parent: Scripting
badge: BETA
badge_color: red
---

# Game Tests


<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>


{% include notice.html 
    contents='The GameTest framework requires you to activate **"Enable GameTest Framework"** in your world settings and you must be using **Minecraft 1.16.210.60 beta or above**'
%}

GameTests are a new feature which allow developers to create unit tests to make it easier to test if game mechanics work. They are created with javascript files in the behavior pack folder and each file can register multiple GameTests. Each GameTest must also have an .mcstructure file in the `BP/structures` folder.

It is recommended that your GameTests go in the `BP/scripts/gametests` directory.

## Manifest

In the behavior pack manifest you need to add a `plugin` module where you set an `entry` point for your GameTests.

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

## Modules
### "GameTest"

`import * as GameTest from "GameTest";`

**Methods:**

- `register(namespace, identifier, callback(gameTest))`
Registers a GameTest into Minecraft. The namespace + identifier should match the identifier of the GameTest's structure. The callback should run the test.

Example:
```js
GameTest.register("MyTest", "five_seconds_past", (test) => {
  // Succeed after 100 ticks (5 seconds)
  test.runAfterDelay(100, (test) => {
    test.succeed();
  });
});
```

- `maxTicks(ticks)`
Sets the maximum amount of time the GameTest must complete until it fails. If this isn't set, it will default to 100 ticks.

Example:
```js
GameTest.register("MyTest", "actor_is_present", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:zombie", new BlockLocation(3, 2, 4));
    });
}).maxTicks(500); // Test must complete before 500 ticks pass.
```

- `batch(time)`
The time argument states the time of day the GameTest must take place in. Sets the time of day when the GameTest is run.
Valid arguments: "night" and "day"

Example:
```js
GameTest.register("MyTest", "zombie_is_present_at_night", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:zombie", new BlockLocation(3, 2, 4));
    });
}).batch("night"); // Test must complete at night.
```

- `setupTicks(ticks)`
Sets the ticks at which the GameTest begins

Example:
```js
GameTest.register("MyTest", "actor_is_present", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:cow", new BlockLocation(0, 3, 0));
    });
}).setupTicks(20);
```

- `tag(tag)`
Sets a tag for the GameTest to be referenced in the "/gametest runall" command

Example:
```js
GameTest.register("MyTest", "actor_is_present", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:cow", new BlockLocation(0, 3, 0));
    });
}).tag(GameTest.Tags.suiteDefault);
```

- `padding(time)`
Sets the padding between GameTests being run

Example:
```js
GameTest.register("MyTest", "actor_is_present", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:cow", new BlockLocation(0, 3, 0));
    });
}).padding(40);
```

- `structureName(name)`
Sets the structure name linked with this GameTest

Example:
```js
GameTest.register("MyTest", "actor_is_present", (test) => {
    test.succeedWhen(() => {
        test.assertEntityPresent("minecraft:cow", new BlockLocation(0, 3, 0));
    });
}).structureName("mystructure:actor_is_present");
```

**`gameTest` methods:** 

_All relative coordinates are from the structure block position._

- `startSequence()`
Begins a sequence for finer control over advanced sequences.

Example:
```js
startSequence()
// Sequence methods
startSequence().thenIdle(100).thenSucceed()
```

- `spawn(identifier, position)`
Spawns the specified entity at the coordinates relative to where the GameTest was run.

Example:
```js
spawn("minecraft:pig", new BlockLocation(0, 3, 0));
```
- `setBlock(block, position)`
Sets the specified block at the coordinates relative to where the GameTest was run.

Example:
```js
setBlock(Minecraft.Blocks.dirt(), new BlockLocation(2, 0, 5));
```

- `pullLever(position)`
Pulls a lever at the specified coordinates if there is one there.

Example:
```js
pullLever(new BlockLocation(4, 4, 6))
```

- `pressButton(position)`
Presses a button at the specified coordinates if there is one there.

Example:
```js  
pressButton(new BlockLocation(2, 1, 0));
```

- `killAllEntities()`
Kills all entities in the GameTest area.

Example:
```js
killAllEntities();
```

- `failIf(callback())`
If the callback asserts, the GameTest will fail.

Example:
```js
failIf(() => {
    test.assertEntityPresent("minecraft:cow", new BlockLocation(1, 2, 0));
});
```
- `runAfterDelay(delay, callback())`
Runs the callback after the set delay (in ticks).

Example:
```js
runAfterDelay(20, () => {
    test.succeed();
});
```
- `succeedWhen(callback())`
If the callback asserts, the GameTest will succeed.

Example:
```js
succeedWhen(() => {
    test.assertEntityNotPresent("minecraft:sheep", new BlockLocation(1, 2, 0));
})
```
- `succeedWhenEntityPresent(identifier, position)`
If the specified actor is present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenEntityPresent("minecraft:villager", new BlockLocation(2, 1, 10));
```
- `succeedWhenEntityNotPresent(identifier, position)`
If the specified actor is not present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenEntityNotPresent("minecraft:villager", new BlockLocation(2, 1, 9));
```
- `succeedWhenBlockPresent(block, position)`
If the specified block is present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenBlockPresent(Minecraft.Blocks.stone(), new BlockLocation(5, 0, 1));
```

- `succeedOnTick(tick)`
The GameTest will succeed when the specified amount of time has passed.

Example:
```js
succeedOnTick(40);
```

- `succeedOnTickWhen(tick, callback())`
The GameTest will succeed when the specified amount of time has passed and the callback calls an assert.

Example:
```js
succeedOnTickWhen(40, () => {
    test.assertEntityPresent("minecraft:cow", new BlockLocation(2, 1, 9);
});
```

- `assertEntityPresentInArea(identifier)`
Asserts an error if the specified entity is present in the GameTest area.

Example:
```js
assertEntityPresentInArea("minecraft:skeleton");
```

- `assertEntityPresent(identifier, position)`
Asserts an error if the specified actor is present at the coordinates relative to where the GameTest was run.

Example:
```js
assertEntityPresent("minecraft:skeleton", new BlockLocation(2, 1, 9));
```

- `assertEntityNotPresent(identifier, position)`
Asserts an error if the specified actor is not present at the coordinates relative to where the GameTest was run.

Example:
```js
assertEntityNotPresent("minecraft:spider", new BlockLocation(0, 6, 8));
```
- `assertBlockPresent(block, position)`
Asserts an error if the specified block is present at the coordinates relative to where the GameTest was run.

Example:
```js
assertBlockPresent(Minecraft.Blocks.bedrock(), new BlockLocation(0, 0, 1));
```

- `assertBlockNotPresent(block, position)`
Asserts an error if the specified block is not present at the coordinates relative to where the GameTest was run.

Example:
```js
assertBlockNotPresent(Minecraft.Blocks.bedrock(), new BlockLocation(0, 0, 1));
```

- `assertBlockState(state, data, position)`
Asserts an error when the specified block at the specified coordinates has the block state.

Example:
```js
assertBlockState("respawn_anchor_charge", 0, new BlockLocation(0, 3, 0));
```

- `assertContainerEmpty(position)`
Asserts an error if there is an empty container at the specified coordinates.

Example:
```js
assertContainerEmpty(new BlockLocation(5, 2, 1));
```

- `assertContainerContains(identifier, position)`
Asserts an error if there is a container with the specified item at the specified coordinates.

Example:
```js
assertContainerContains("minecraft:glowstone", new BlockLocation(5, 2, 1));
```

- `assertEntityHasArmor(identifier, slot, item, data, position, bool)`
Asserts an error when the armor is found on the entity at the specified coordinates.

Example:
```js
assertEntityHasArmor(
    "minecraft:horse", 
    1, 
    "", 
    0, 
    new BlockLocation(5, 2, 1), 
    false // Last parameter function unknown
); 
```

- `assertEntityHasComponent(identifier, component, position, bool)`
Asserts an error when the specified entity has the component.

Example:
```js
assertEntityHasComponent(
    "minecraft:sheep",
    "minecraft:is_sheared",
    new BlockLocation(5, 2, 1),
    false // Last parameter function unknown
);
```

- `assertItemEntityPresent(block, position, amount)`
Asserts an error when the specified item stack is not found at the specified coordinates

Example:
```js
assertItemEntityPresent(new ItemStack(Blocks.redSandstone()), new BlockLocation(0, 2, 0), 2.0)
```

- `succeed()`
When this is called, the GameTest will succeed.

Example:
```js
succeed();
```

- `print(text: string)`
Prints the given text to the chat

Example:
```js
print('Hello World!');
```

### "Minecraft"

`import * as Minecraft from "Minecraft";`

_Needs more information_

**Objects:**

#### `Blocks`

**Methods:**

- `get(identifier)`
Returns the block from the specified identifier to be referenced in GameTests.

Example:
```js
const block = Blocks.get("minecraft:dirt");
```

The `Blocks` object also contains a method for every block to reference it in GameTests. These methods should be used when referencing a block in GameTests.

Examples:

- `concrete()`

- `concretePowder()`

- `sand()`

- `air()`

#### `BlockStates`

**Methods:**

The `BlockStates` objects contains a method for every block state which can be used in the `setState` method of the block object

#### `World`

**Methods:**

- `addEventListener(event, callback())`

Valid events: `"onEntityCreated"`, `"onEntityDefinitionTriggered"`

- `getDimension()`

**Classes:**

#### `ItemStack(item)`

`new ItemStack(Minecraft.Blocks.sand())`

#### `BlockLocation(x, y, z)`

`new BlockLocation(1, 6, 0)`

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

## Using GameTests

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