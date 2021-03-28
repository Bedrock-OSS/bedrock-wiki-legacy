---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / Test

# Interface: Test

## Table of contents

### Methods

- [assertBlockNotPresent](test#assertblocknotpresent)
- [assertBlockPresent](test#assertblockpresent)
- [assertBlockState](test#assertblockstate)
- [assertContainerContains](test#assertcontainercontains)
- [assertContainerEmpty](test#assertcontainerempty)
- [assertEntityHasArmor](test#assertentityhasarmor)
- [assertEntityHasComponent](test#assertentityhascomponent)
- [assertEntityInstancePresent](test#assertentityinstancepresent)
- [assertEntityNotPresent](test#assertentitynotpresent)
- [assertEntityPresent](test#assertentitypresent)
- [assertEntityPresentInArea](test#assertentitypresentinarea)
- [assertItemEntityPresent](test#assertitementitypresent)
- [failIf](test#failif)
- [killAllEntities](test#killallentities)
- [pressButton](test#pressbutton)
- [print](test#print)
- [pullLever](test#pulllever)
- [runAfterDelay](test#runafterdelay)
- [setBlock](test#setblock)
- [spawn](test#spawn)
- [startSequence](test#startsequence)
- [succeed](test#succeed)
- [succeedOnTick](test#succeedontick)
- [succeedOnTickWhen](test#succeedontickwhen)
- [succeedWhen](test#succeedwhen)
- [succeedWhenBlockPresent](test#succeedwhenblockpresent)
- [succeedWhenEntityPresent](test#succeedwhenentitypresent)

## Methods

### assertBlockNotPresent

▸ **assertBlockNotPresent**(`id`: [*Block*](block), `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified block is not found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | [*Block*](block) |  The block to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the block    |

**Returns:** *void*



___

### assertBlockPresent

▸ **assertBlockPresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified block is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The block to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the block    |

**Returns:** *void*



___

### assertBlockState

▸ **assertBlockState**(`state`: *string*, `data`: *string* \| *number*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified block at the specified coordinates has the block state

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`state` | *string* |  The block state to test for   |
`data` | *string* \| *number* |  The value of the state to test for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the block    |

**Returns:** *void*



___

### assertContainerContains

▸ **assertContainerContains**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error if there is a container with the specified item at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The item to test for in the container   |
`position` | [*BlockPos*](blockpos) |  The relative position of the container to check    |

**Returns:** *void*



___

### assertContainerEmpty

▸ **assertContainerEmpty**(`position`: [*BlockPos*](blockpos)): *void*

Asserts an error if there is an empty container at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`position` | [*BlockPos*](blockpos) |  The relative position of the container to check    |

**Returns:** *void*



___

### assertEntityHasArmor

▸ **assertEntityHasArmor**(`id`: *string*, `slot`: *number*, `item`: *string*, `data`: *number*, `position`: [*BlockPos*](blockpos), `bool`: *boolean*): *void*

Asserts an error when the armor is found on the entity at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to check for the armor on   |
`slot` | *number* |  The slot of the entity to test for the item   |
`item` | *string* |  The item to test for in the specified slot   |
`data` | *number* |  The data value of the item   |
`position` | [*BlockPos*](blockpos) |  The position of the entity to test for the armor   |
`bool` | *boolean* |  Unknown function of parameter...    |

**Returns:** *void*



___

### assertEntityHasComponent

▸ **assertEntityHasComponent**(`id`: *string*, `component`: *string*, `position`: [*BlockPos*](blockpos), `bool`: *boolean*): *void*

Asserts an error when the specified entity has the component

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to test   |
`component` | *string* |  The name of the component to test for   |
`position` | [*BlockPos*](blockpos) |  The position of the entity to test   |
`bool` | *boolean* |  Unknown function of parameter...    |

**Returns:** *void*



___

### assertEntityInstancePresent

▸ **assertEntityInstancePresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified entity is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the actor    |

**Returns:** *void*



___

### assertEntityNotPresent

▸ **assertEntityNotPresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified entity is not found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the actor    |

**Returns:** *void*



___

### assertEntityPresent

▸ **assertEntityPresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Asserts an error when the specified entity is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the actor    |

**Returns:** *void*



___

### assertEntityPresentInArea

▸ **assertEntityPresentInArea**(`id`: *string*): *void*

Throws an Error if an entity matching the given identifier does not exist in the test region

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifer of the entity to test for    |

**Returns:** *void*



___

### assertItemEntityPresent

▸ **assertItemEntityPresent**(`itemStack`: [*ItemStack*](itemstack), `position`: [*BlockPos*](blockpos), `amount`: *number*): *void*

Asserts an error when the specified item stack is not found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`itemStack` | [*ItemStack*](itemstack) |  The item stack to test for   |
`position` | [*BlockPos*](blockpos) |  The position to test for the item stack   |
`amount` | *number* |  The amount of items that should be in the stack    |

**Returns:** *void*



___

### failIf

▸ **failIf**(`func`: () => *void*): *void*

When the `func` parameter calls an assert function the GameTest will fail

#### Parameters:

Name | Type |
:------ | :------ |
`func` | () => *void* |

**Returns:** *void*



___

### killAllEntities

▸ **killAllEntities**(): *void*

Kills all entities in the test

**Returns:** *void*



___

### pressButton

▸ **pressButton**(`position`: [*BlockPos*](blockpos)): *void*

Presses a button at the specified coordinates if there is one there

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`position` | [*BlockPos*](blockpos) |  The relative position to press the button    |

**Returns:** *void*



___

### print

▸ **print**(`text`: *string*): *void*

Prints the given text to the chat

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`text` | *string* |  The text to print out    |

**Returns:** *void*



___

### pullLever

▸ **pullLever**(`position`: [*BlockPos*](blockpos)): *void*

Pulls a lever at the specified coordinates if there is one there

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`position` | [*BlockPos*](blockpos) |  The relative position to pull the lever    |

**Returns:** *void*



___

### runAfterDelay

▸ **runAfterDelay**(`ticks`: *number*, `func`: (`test`: [*Test*](test)) => *void*): *void*

Runs the a function after the set delay

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`ticks` | *number* |  The amount of ticks that should pass until the function is run   |
`func` | (`test`: [*Test*](test)) => *void* |  The function that will be run when the delay has passed    |

**Returns:** *void*



___

### setBlock

▸ **setBlock**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

Places the specified block at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The block to place   |
`position` | [*BlockPos*](blockpos) |  The relative position to place the block    |

**Returns:** *void*



___

### spawn

▸ **spawn**(`id`: *string*, `position`: [*BlockPos*](blockpos)): [*Entity*](entity)

Spawns the specified entity at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to spawn   |
`position` | [*BlockPos*](blockpos) |  The relative position to spawn the entity    |

**Returns:** [*Entity*](entity)



___

### startSequence

▸ **startSequence**(): [*Sequence*](sequence)

Allows finer control over advanced test sequences

**Returns:** [*Sequence*](sequence)



___

### succeed

▸ **succeed**(): *void*

When this is called, the GameTest succeeds

**Returns:** *void*



___

### succeedOnTick

▸ **succeedOnTick**(`tick`: *number*): *void*

The GameTest will succeed when the specified amount of ticks has passed

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`tick` | *number* |  The tick to succed the test after    |

**Returns:** *void*



___

### succeedOnTickWhen

▸ **succeedOnTickWhen**(`tick`: *number*, `func`: () => *void*): *void*

The GameTest will succeed when the specified amount of ticks has passed and the `func` parameter calls an assert function

#### Parameters:

Name | Type |
:------ | :------ |
`tick` | *number* |
`func` | () => *void* |

**Returns:** *void*



___

### succeedWhen

▸ **succeedWhen**(`func`: () => *void*): *void*

When the `func` paramater calls an assert function the GameTest will succeed

#### Parameters:

Name | Type |
:------ | :------ |
`func` | () => *void* |

**Returns:** *void*



___

### succeedWhenBlockPresent

▸ **succeedWhenBlockPresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

The GameTest will succeed when the specified block is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The block to check for   |
`position` | [*BlockPos*](blockpos) | - |

**Returns:** *void*



▸ **succeedWhenBlockPresent**(`id`: [*Block*](block), `position`: [*BlockPos*](blockpos)): *void*

The GameTest will succeed when the specified block is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | [*Block*](block) |  The block to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the block    |

**Returns:** *void*



___

### succeedWhenEntityPresent

▸ **succeedWhenEntityPresent**(`id`: *string*, `position`: [*BlockPos*](blockpos)): *void*

The GameTest will succeed when the specified entity is found at the specified coordinates

#### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the entity to check for   |
`position` | [*BlockPos*](blockpos) |  The relative position to test for the actor    |

**Returns:** *void*


