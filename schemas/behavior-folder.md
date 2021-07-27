---
layout: page
title: Behavior Folder Schema
parent: Schemas
---

# Behavior Pack Folder Schema

This shows the top-level folder/file structure for a behavior pack.

If you need additional organization, you are encouraged to use *child folders*. Child folders are nested under the top-level folder, and can be anything you like. For example: `BP/entities/dragons/drake.entity.json`

<!--
BP/manifest.json
BP/pack_icon.png
BP/animations/example.animation.json
BP/animation_controllers/example.ac.json
BP/biomes/example.biome.json
BP/blocks/example.block.json
BP/entities/example.entity.json
BP/feature_rules/example.rule.json
BP/features/example.feature.json
BP/functions/example.mcfunction
BP/functions/tick.json
BP/items/example.item.json
BP/loot_tables/example.loot.json
BP/recipes/example.recipe.json
BP/texts/languages.json
BP/texts/en_US.lang
BP/trading/example.trade.json
BP/trading/economy_trades/example.trade.json
BP/scripts/client/example.js
BP/scripts/server/example.js
BP/spawn_rules/example.spawn.json
-->

<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">BP</span>
            <ul>
                <li><span class="folder">animation_controllers</span>
                    <ul>
                        <li><span class="file">example.ac.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">animations</span>
                    <ul>
                        <li><span class="file">example.animation.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">biomes</span>
                    <ul>
                        <li><span class="file">example.biome.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">blocks</span>
                    <ul>
                        <li><span class="file">example.block.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">entities</span>
                    <ul>
                        <li><span class="file">example.entity.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">feature_rules</span>
                    <ul>
                        <li><span class="file">example.feature.json</span></li>
                        <li><span class="file">example.rule.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">features</span>
                    <ul>
                        <li><span class="file">example.feature.json</span></li>
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
                <li><span class="file">manifest.json</span></li>
                <li><span class="image">pack_icon.png</span></li>
                <li><span class="folder">recipes</span>
                    <ul>
                        <li><span class="file">example.recipe.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">scripts</span>
                    <ul>
                        <li><span class="folder">client</span>
                            <ul>
                                <li><span class="file">example.js</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">server</span>
                            <ul>
                                <li><span class="file">example.js</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><span class="folder">spawn_rules</span>
                    <ul>
                        <li><span class="file">example.spawn.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">structures</span>
                    <ul>
                        <li><span class="file">example.mcstructure</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">en_US.lang</span></li>
                        <li><span class="file">languages.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">trading</span>
                    <ul>
                        <li><span class="folder">economy_trades</span>
                            <ul>
                                <li><span class="file">example.trade.json</span></li>
                            </ul>
                        </li>
                        <li><span class="file">example.trade.json</span></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>
