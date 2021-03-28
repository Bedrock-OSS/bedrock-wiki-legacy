---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / GameTest

# Namespace: "GameTest"

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Functions

## register

▸ **register**(`namespace`: *string*, `identifier`: *string*, `func`: (`test`: [*Test*](/scripting/game-tests/interfaces/test)) => *void*): [*TestRunner*](/scripting/game-tests/interfaces/testrunner)

Registers a GameTest into Minecraft

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`namespace` | *string* |  Namespace of the GameTest. Should match the namespace of the mcstructure file   |
`identifier` | *string* |  Identifier of the GameTest. Should match the identifier of the mcstructure file    |
`func` | (`test`: [*Test*](/scripting/game-tests/interfaces/test)) => *void* | - |

**Returns:** [*TestRunner*](/scripting/game-tests/interfaces/testrunner)


