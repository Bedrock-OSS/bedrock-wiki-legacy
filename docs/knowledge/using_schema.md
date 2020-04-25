---
layout: page
title: Using Schemas
parent: Documentation
---

# What's a Schema?

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.

Using this Minecraft Bedrock Add-On Schema will help you make files by providing auto-completions, descriptions, and file validation.

# Adding Schema to File

To use this tool in VS code, simply add this line to your root object.

`"$schema": "https://aexer0e.github.io/bedrock-schema/"`

It should look like something like this:
```json
"format_version": "1.14.0",
"$schema": "https://aexer0e.github.io/bedrock-schema/"
```

# Adding Schema to Workspaces

If you want to utilize this schema to work with all of your files inside your Workspace, you can add it to your VS Code Workspace's settings.

To do that, make sure you're in your workspace, then, press `Ctrl+Shift+P` and type and select `>Preferences: Open Workspace Settings (JSON)`. After that, simply add this to the root object
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

---

### **Note:** This tool is still in early development, meaning it will probably have some bugs. If you spot one, please send me a DM on Discord at `assassin#1634`, or on Twitter [here](https://twitter.com/aexer0e).