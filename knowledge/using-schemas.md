---
layout: page
title: Using Schemas
parent: Knowledge
---

# What's a Schema?

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.

Using this Minecraft Bedrock Add-On Schema will help you make files by providing auto-completions, descriptions, and file validation.

# Adding Schema to File

To use this schema inside your JSON file in VS code, simply add this line to your root object.

`"$schema": "https://aexer0e.github.io/bedrock-schema/"`

It should look like something like this:
```json
"format_version": "1.14.0",
"$schema": "https://aexer0e.github.io/bedrock-schema/"
```

# Adding Schema to Workspaces

If you want to utilize this schema to work with all of your files inside your Workspace, you can add it to your VS Code Workspace's settings.

To do this, make sure you're in your workspace, then, press `Ctrl+Shift+P` and type and select `>Preferences: Open Workspace Settings (JSON)`. After that, add this to the root object
```json
"settings": {
	"json.schemas": [
		{
			"fileMatch": [
				"*.json"
			],
			"url": "https://aexer0e.github.io/bedrock-schema/"
		}
	]
}
```

To test if it works, create a `.json` file, open an object, and see if you get the auto-completion options. (You can also press `Ctrl+Space` to force it into showing the available options.)

# Other Schemas

There are a plethora of schemas for Bedrock with varying degrees of support. Here is a list of more schemas:

- BlueFrog130's Add-On Schema: https://github.com/BlueFrog130/minecraft-add-on-schemas/
- Tschrock's Bedrock JSON Schema: https://github.com/bedrock-studio/bedrock-json-schemas/
- stirante's Bedrock Shader Schema: https://github.com/stirante/bedrock-shader-schema/
- Blockception's Bedrock Development VSCode Extension: https://marketplace.visualstudio.com/items?itemName=BlockceptionLtd.blockceptionvscodeminecraftbedrockdevelopmentextension

