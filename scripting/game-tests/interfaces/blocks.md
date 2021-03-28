---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / Blocks

# Interface: Blocks

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Methods

Contains a method for every vanilla block. All blocks are in camelCase.

Example:

▸ **air**(): [*Block*](block)

___

## get

▸ **get**(`id`: *string*): [*Block*](block)

Fetches the requested block and returns it, if the block doesn't exist, this returns null

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`id` | *string* |  The identifier of the block to get    |

**Returns:** [*Block*](block)


