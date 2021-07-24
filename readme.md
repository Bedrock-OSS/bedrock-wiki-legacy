<h1>This is the old wiki it is not maintained anymore changes will not be merged direct yourself to https://github.com/Bedrock-OSS/bedrock-wiki </h1>

<p align="center">
    <h1 align="center">Bedrock Wiki</h1>
    <p align="center">The Bedrock Wiki is a knowledge-sharing website for Technical Bedrock, containing documentation, tutorials, and general how-to information.<br>Here, you can contribute to this amazing, open-source resource!</p>
    <p align="center"><strong><a href="https://old-wiki.bedrock.dev/">Visit the website!</a>             <a href="https://discord.gg/XjV87YN">Join the discord!</a></strong></p>
    <br>
</p>

# Contributing

## Discord

Please join the [discord](https://discord.gg/XjV87YN), which is where all wiki-communication takes place. While small changes and new articles do not need permission, large-scale changes should go through community review.

## Using GitHub

It is beyond the scope of this readme to teach the proper use of Git and GitHub, but you can always reach out personally for help. Some steps to get you started though (google steps if unsure):
 - `make github account`
 - `fork the repository`
 - `make changes, commit changes, push changes`
 - `create pull requests`

## Commits and Pulls

Please provide proper commit messages when contributing, this will make it much easier to approve pull requests. Don't change anything in the config unless you really need to.

## Contributing without GitHub

Want to submit an article, but can't be bothered to learn Git, or GitHub? You can send me markdown articles directly, and I will add them manually.

## Running Locally
You can locally test the website by [installing Jekyll](https://jekyllrb.com/docs/installation/#guides) and then running  `bundle install` and `bundle exec jekyll serve`.

Assuming the Ruby dependencies installed correctly, the local server will run and you should see `http://127.0.0.1:4000`
printed out.

You can now make changes to any of the markdown files and you'll see the changes reflected at that URL in your browser! Note the site can take several seconds to rebuild, so have an eye on your terminal window

# Formatting tools

Various formatting options (such as buttons and labels) come from out up-line theme: [just the docs](https://pmarsceill.github.io/just-the-docs/). Go there to learn about these tools. 

## Codeblock Filepaths

You can annotate your code-blocks with filepath information, using the following format:

```
{% include filepath.html path="RP/textures/item_texture.json" %}
```jsonc
{
	"resource_pack_name": "tut",
	"texture_name": "atlas.items",
	"texture_data": {
		"meal": {
			"textures": "textures/items/meal"
		},
		"gem": {
			"textures": "textures/items/gem"
		}
	}
}
\```
```

You can also add a local path:

`{% include filepath.html path="example.json" local_path="minecraft:entity/description%}`

## File Tree Viewer

There is a number of CSS classes, which help build the directory structure. 

Example:
```html
<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">BP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">gem.item.json</span></li>
                        <li><span class="file">meal.item.json</span></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><span class="folder">RP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">gem.item.json</span></li>
                        <li><span class="file">meal.item.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">en_US.lang</span></li>
                    </ul>
                </li>
                <li><span class="folder">textures</span>
                    <ul>
                        <li><span class="file">item_texture.json</span></li>
                        <li><span class="folder">items</span>
                            <ul>
                                <li><span class="image">gem.png</span></li>
                                <li><span class="image">meal.png</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>
```

Result:
<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">BP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">gem.item.json</span></li>
                        <li><span class="file">meal.item.json</span></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><span class="folder">RP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">gem.item.json</span></li>
                        <li><span class="file">meal.item.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">en_US.lang</span></li>
                    </ul>
                </li>
                <li><span class="folder">textures</span>
                    <ul>
                        <li><span class="file">item_texture.json</span></li>
                        <li><span class="folder">items</span>
                            <ul>
                                <li><span class="image">gem.png</span></li>
                                <li><span class="image">meal.png</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>

## CSS classes

### folder-structure

Changes unordered list style, so it resembles directory tree.

### folder

Adds folder emoji before element. 

### file

Adds text file emoji before element. 

### image

Adds image emoji before element. 

## Structure generator

There is also automatic structure generator at [https://stirante.com/dir-converter/converter.html](https://stirante.com/dir-converter/converter.html).

The text area on the left accepts a list of paths delimited by new line. After clicking the convert button, the HTML should be generated in text area on the right side.

To generate the output in the first example, use this input:
```
RP/texts/en_US.lang
RP/textures/item_texture.json
RP/items/meal.item.json
BP/items/meal.item.json
BP/items/gem.item.json
RP/items/gem.item.json
RP/textures/items/gem.png
RP/textures/items/meal.png
```

### File links

To link file inside directory structure to an element, add `#<id>` after file path like this:

```
RP/texts/en_US.lang
RP/textures/item_texture.json
RP/items/meal.item.json#rp_meal_item
BP/items/meal.item.json#bp_meal_item
BP/items/gem.item.json#bp_gem_item
RP/items/gem.item.json#rp_gem_item
RP/textures/items/gem.png
RP/textures/items/meal.png
```

This will result in this output:
```html
<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">BP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><a href="#bp_gem_item" class="file">gem.item.json</>
                        </li>
                        <li><a href="#bp_meal_item" class="file">meal.item.json</>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><span class="folder">RP</span>
            <ul>
                <li><span class="folder">items</span>
                    <ul>
                        <li><a href="#rp_gem_item" class="file">gem.item.json</>
                        </li>
                        <li><a href="#rp_meal_item" class="file">meal.item.json</>
                        </li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">en_US.lang</>
                        </li>
                    </ul>
                </li>
                <li><span class="folder">textures</span>
                    <ul>
                        <li><span class="file">item_texture.json</>
                        </li>
                        <li><span class="folder">items</span>
                            <ul>
                                <li><span class="image">gem.png</>
                                </li>
                                <li><span class="image">meal.png</>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>
```

# Icons

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Using Panels

There are three kinds: Info, Warning, and Error

Use like this:

```
{% include warning.html
  contents='Animation Controllers "reset" when an entity reloads (player join/leave, chunk reload, etc). This means that it will "jump" back to the default state. You should always have logic in your default state that can handle restarting any critical animations.'
%}
```

Or like this:
```

```
<p class="panel-warning" markdown="1">
  Remember! Render controllers work based on short-names. If you want to use the cow render controller, you need to provide the short-names it is using. In this case, you will need to provide:<br>
    - `default` geometry<br>
    - `default` texture<br>
    - `default` material
</p>
```
