---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / EntityComponent

# Interface: EntityComponent

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Methods

## getName

▸ **getName**(): *string*

Returns the name of the component

**Returns:** *string*



___

## leash

▸ **leash**(`entity`: [*Entity*](entity)): *void*

Leashes this entity to another specified entity. This must be used on the "minecraft:leashable" component

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`entity` | [*Entity*](entity) |  The entity to leash this entity to    |

**Returns:** *void*



___

## setColor

▸ **setColor**(`color`: *number*): *void*

Sets the entities color value. This must be used on the "minecraft:color" component

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`color` | *number* |  The color value to set    |

**Returns:** *void*



___

## setTamed

▸ **setTamed**(`particles`: *boolean*): *void*

Sets the entity as tamed

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`particles` | *boolean* |  Whether to display taming particles    |

**Returns:** *void*



___

## unleash

▸ **unleash**(): *void*

Causes this entity to detach leashes. This must be used on the "minecraft:leashable" component

**Returns:** *void*


