---
layout: page
title: Game Tests
parent: Documentation
badge: BETA
badge_color: red
---

# Game Tests

GameTests are a new feature in the 1.16.210.60 beta which allow developers to create unit tests to make it easier to test if game mechanics work. They require the "Enable GameTest Framework" toggle to be activated in the world settings. They are created with javascript files in the `BP/gametests` folder and each file can register multiple GameTests. Each GameTest must also have an .mcstructure file in the `BP/structures` folder.

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
    test.succeedWhen((test) => {
        test.assertActorPresent("minecraft:zombie", 3, 2, 4);
    });
}).maxTicks(500); // Test must complete before 500 ticks pass.
```

- `batch(time)`
The time argument states the time of day the GameTest must take place in. Sets the time of day when the GameTest is run.
Valid arguments: "night" and "day"

Example:
```js
GameTest.register("MyTest", "block_is_present_at_night", (test) => {
    test.succeedWhen((test) => {
        test.assertActorPresent("minecraft:zombie", 3, 2, 4);
    });
}).batch("night"); // Test must complete at night.
```

**`gameTest` methods:** 

_All relative coordinates are from the structure block position._

- `spawn(identifier, x, y, z)`
Spawns the specified entity at the coordinates relative to where the GameTest was run.

Example:
```js
spawn("minecraft:pig", 0, 3, 0);
```
- `setBlock(block, x, y, z)`
Sets the specified block at the coordinates relative to where the GameTest was run.

Example:
```js
setBlock(Minecraft.Blocks.dirt(), 2, 0, 5);
```
- `pressButton(x, y, z)`
Presses the button at the corridnates relative to where the GameTest was run.

Example:
```js  
pressButton(2, 1, 0);
```
- `failIf(callback(gameTest))`
If the callback asserts, the GameTest will fail.

Example:
```js
failIf((test) => {
    test.assertActorPresent("minecraft:cow", 1, 2, 0);
});
```
- `runAfterDelay(delay, callback(gameTest))`
Runs the callback after the set delay (in ticks).

Example:
```js
test.runAfterDelay(20, (test) => {
    test.succeed();
});
```
- `succeedWhen(callback(gameTest))`
If the callback asserts, the GameTest will succeed.

Example:
```js
succeedWhen((test) => {
    test.assertActorNotPresent("minecraft:sheep", 1, 2, 0);
})
```
- `succeedWhenActorPresent(identifier, x, y, z)`
If the specified actor is present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenActorPresent("minecraft:villager", 2, 1, 10);
```
- `succeedWhenActorNotPresent(identifier, x, y, z)`
If the specified actor is not present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenActorNotPresent("minecraft:villager", 2, 1, 9);
```
- `succeedWhenBlockPresent(block, x, y, z)`
If the specified block is present at the coordinates relative to where the GameTest was run, the test will succeed.

Example:
```js
succeedWhenBlockPresent(Minecraft.Blocks.stone(), 5, 0, 1);
```

- `assertActorPresent(identifier, x, y, z)`
Asserts an error if the specified actor is present at the coordinates relative to where the GameTest was run.

Example:
```js
assertActorPresent("minecraft:skeleton", 2, 1, 9);
```
- `assertActorNotPresent(identifier, x, y, z)`
Asserts an error if the specified actor is not present at the coordinates relative to where the GameTest was run.

Example:
```js
assertActorNotPresent("minecraft:spider", 0, 6, 8);
```
- `assertBlockPresent(block, x, y, z)`
Asserts an error if the specified block is present at the coordinates relative to where the GameTest was run.

Example:
```js
assertBlockPresent(Minecraft.Blocks.bedrock(), 0, 0, 1);
```

- `succeed()`
When this is called, the GameTest will succeed.

Example:
```js
succeed();
```

### "Minecraft"

`import * as Minecraft from "Minecraft";`

_Needs more information_

**Objects:**

`Blocks`

**Methods:**

The `Blocks` object contains a method for every block to reference it in GameTests. These methods should be used when referencing a block in GameTests.

Examples:

- `concrete()`

- `concretePowder()`

- `sand()`

- `air()`

## Complete examples

```js
// Structure Path: BP/structures/MinecartTests/turn.mcstructure

import * as GameTest from "GameTest";

GameTest.register("MinecartTests", "turn", (test) => {
  const minecartActorType = "minecart";

  test.assertActorPresent(minecartActorType, 1, 2, 0);
  test.assertActorNotPresent(minecartActorType, 1, 2, 2);

  test.pressButton(0, 3, 0);

  test.succeedWhenActorPresent(minecartActorType, 1, 2, 2);
});
```

```js
// Structure Path: BP/structures/DoorTests/four_villagers_one_door.mcstructure

import * as GameTest from "GameTest";

GameTest.register("DoorTests", "four_villagers_one_door", (test) => {
  const villagerActorType = "minecraft:villager_v2";
  const villagerActorSpawnType =
    "minecraft:villager_v2<minecraft:spawn_farmer>";

  test.spawn(villagerActorSpawnType, 5, 2, 4);
  test.spawn(villagerActorSpawnType, 4, 2, 5);
  test.spawn(villagerActorSpawnType, 2, 2, 5);
  test.spawn(villagerActorSpawnType, 1, 2, 4);

  test.succeedWhen((test) => {
    test.assertActorPresent(villagerActorType, 5, 2, 2);
    test.assertActorPresent(villagerActorType, 5, 2, 1);
    test.assertActorPresent(villagerActorType, 1, 2, 2);
    test.assertActorPresent(villagerActorType, 1, 2, 1);
  });
}).batch("night")
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

- `/gametest runAll [tagTag: GameTestTag] [rotationSteps: int]`

Creates and runs all GameTests with the specified GameTestTag.

- `/gametest create <testName: string> [width: int] [height: int] [depth: int]`

Creates a blank GameTest area with the specified dimensions.