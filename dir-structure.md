---
layout: default
title: Directory structure
nav_exclude: true
search_exclude: true
---

# Directory structure

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