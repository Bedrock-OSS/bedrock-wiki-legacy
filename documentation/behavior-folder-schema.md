---
layout: page
title: Behavior Folder Schema
parent: Documentation
---

# Behavior Pack Folder Schema

This shows the top-level folder/file structure for a behavior pack. An additional folder nesting can be used as needed.

<!--
I also manually reordered, so files in the BP directory are at the top.

BP/manifest.json
BP/pack_icon.png
BP/animations/example.animation.json
BP/animation_controllers/example.animation.controller.json
BP/entities/example.entity.json
BP/functions/example.mcfunction
BP/functions/tick.json
BP/items/example.item.json
BP/loot_tables/example.loot.json
BP/recipes/example.recipe.json
BP/texts/languages.json
BP/textx/en_US.lang
BP/trading/example.trade.json
-->

<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">BP</span>
            <ul>
                <li><span class="file">manifest.json</span></li>
                <li><span class="image">pack_icon.png</span></li>
                <li><span class="folder">animation_controllers</span>
                    <ul>
                        <li><span class="file">example.animation.controller.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">animations</span>
                    <ul>
                        <li><span class="file">example.animation.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">entities</span>
                    <ul>
                        <li><span class="file">example.entity.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">functions</span>
                    <ul>
                        <li><span class="file">example.mcfunction</span></li>
                        <li><span class="file">tick.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">example.item.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">loot_tables</span>
                    <ul>
                        <li><span class="file">example.loot.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">recipes</span>
                    <ul>
                        <li><span class="file">example.recipe.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">languages.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">textx</span>
                    <ul>
                        <li><span class="file">en_US.lang</span></li>
                    </ul>
                </li>
                <li><span class="folder">trading</span>
                    <ul>
                        <li><span class="file">example.trade.json</span></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>
