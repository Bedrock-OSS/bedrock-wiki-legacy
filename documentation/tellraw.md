---
layout: page
title: Tellraw
parent: Documentation
---

# What is tellraw

tellraw sends a JSON message to selected or all players being usefull for sending plain messages to players ingame

**The titleraw command follows the same theme**

![](/assets/images/Documentation/tellrawshow.png)

# Format

this is how the tell raw command is formated

```
tellraw <target: target> <raw json message: json>
```

- ` <target: target>`: The target is expressed as a playername or player groups such as `@a` `@r` `@s` `@p`
- `<raw json message: json>`: This is a json schema that tells how the message is structured or constructured. expressed with for example:
  `{"rawtext":[{"text":""}]}`

# Examples

This sends the words in the last set of quotes

```json
/tellraw @a {"rawtext":[{"text":"Hello"}]}
```

To use quotations in a tellraw message place a backslash to the left side of the quotation mark.

```json
/tellraw @a {"rawtext":[{"text":"Quote me: \"I am here\"."}]}
```

## Line breaks

To insert a line break use `\n`

```json
/tellraw @a { "rawtext": [ { "text":"I am line one\nI am line two" } ] }
```

## Displaying entities / player

You can use the following to use selector to display names.

```json
/tellraw @a {"rawtext": [{"text": "§6The winner is: §a"}, {"selector": "@a[r=5,c=1]"}]}
```

## Displaying scores

You can use the following to use selector to display names.

```json
/tellraw @a {"rawtext": [{"text": "§6The winner is: §a"}, {"selector": "@a[r=5,c=1]"}, {"text": "§6With a score of: "}, {"score":{"name": "@s","objective": "value"}}]}
```

## Translate text

To have a language changing text you can use the translate component. please note you will need to edit each languages files for this to work. In the
`resource pack / texts / all languages files`:

```lang
example.line.1=I am line 1
```

The command:

```json
tellraw @a { "rawtext": [ { "translate": "example.line.1" } ] }
```

## Translate text with selectors/scores

language files:

```lang
example.ine.1=The winner is: %%s. With a score of %%s
```

```json
/tellraw @a {"translate": [{"text": "example.ine.1", "with": {"rawtext": [{"selector": "@a[r=5,c=1]"}, {"text": "§6With a score of: "}, {"score":{"name": "@s","objective": "value"}}]}}]}
```
