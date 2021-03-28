---
layout: page
---

[Game Tests](/scripting/game-tests) / Exports / TestRunner

# Interface: TestRunner

<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

# Methods

## batch

▸ **batch**(`time`: *night* \| *day*): [*TestRunner*](testrunner)

Sets the time of day when the GameTest is run. The time will be changed to the time set here when the GameTest is run

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`time` | *night* \| *day* |  The time that the GameTest must take place in    |

**Returns:** [*TestRunner*](testrunner)



___

## maxTicks

▸ **maxTicks**(`ticks`: *number*): [*TestRunner*](testrunner)

Sets the maximum amount of ticks the GameTest must complete until it fails

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`ticks` | *number* |  The maximum amount of ticks    |

**Returns:** [*TestRunner*](testrunner)



___

## padding

▸ **padding**(`time`: *number*): [*TestRunner*](testrunner)

Sets the padding between GameTests being run

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`time` | *number* |  The duration of the padding    |

**Returns:** [*TestRunner*](testrunner)



___

## setupTicks

▸ **setupTicks**(`ticks`: *number*): [*TestRunner*](testrunner)

Sets the ticks at which the GameTest begins

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`ticks` | *number* |  The tick starting point    |

**Returns:** [*TestRunner*](testrunner)



___

## structureName

▸ **structureName**(`name`: *string*): [*TestRunner*](testrunner)

Sets the structure name linked with this GameTest

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`name` | *string* |  Name of the structure    |

**Returns:** [*TestRunner*](testrunner)



___

## tag

▸ **tag**(`tag`: *any*): [*TestRunner*](testrunner)

Sets a tag for the GameTest to be referenced in the "/gametest runall" command

### Parameters:

Name | Type | Description |
:------ | :------ | :------ |
`tag` | *any* |  The tag of the GameTest    |

**Returns:** [*TestRunner*](testrunner)


