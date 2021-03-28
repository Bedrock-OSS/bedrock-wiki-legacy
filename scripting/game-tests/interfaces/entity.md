---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / Entity

# Interface: Entity

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Methods

## getComponent

▸ **getComponent**(`component`: *string*): [*EntityComponent*](entitycomponent)

Returns the component matching the given identifier

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`component` | *string* |  The component identifier to get    |

**Returns:** [*EntityComponent*](entitycomponent)



___

## getComponents

▸ **getComponents**(): [*EntityComponent*](entitycomponent)[]

Returns an array of supported components

**Returns:** [*EntityComponent*](entitycomponent)[]



___

## getName

▸ **getName**(): *string*

Returns the name of the entity (e.g. "Horse")

**Returns:** *string*



___

## hasComponent

▸ **hasComponent**(`component`: *string*): *boolean*

Returns true if the given component exists on the entity and is supported

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`component` | *string* |  The component identifier to check for    |

**Returns:** *boolean*



___

## kill

▸ **kill**(): *void*

Kills the entity

**Returns:** *void*


