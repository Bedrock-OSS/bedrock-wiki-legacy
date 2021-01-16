---
layout: page
title: Resource Folder Schema
parent: Documentation
---

# Resource Pack Folder Schema

This shows the top-level folder/file structure for a resource pack. An additional folder nesting can be used as needed.

<!--
I also manually reordered, so files in the RP directory are at the top and the '...' "file" is at the bottom and looks like an image.

RP/manifest.json
RP/pack_icon.png
RP/sounds.json
RP/biomes_client.json
RP/animations/example.animation.json
RP/animation_controllers/example.animation_controller.json
RP/entity/example.entity.json
RP/models/entity/example.geo.json
RP/particles/example.particle.json
RP/items/example.item.json
RP/render_controllers/example.render_controller.json
RP/sounds/example.sound.ogg
RP/sounds/sound_definitions.json
RP/texts/languages.json
RP/textx/en_US.lang
RP/textures/item_texture.json
RP/textures/blocks/example.block.png
RP/textures/blocks/example.texture.variant.block/0.png
RP/textures/blocks/example.texture.variant.block/1.png
RP/textures/blocks/example.texture.variant.block/...
RP/textures/entity/example.entity.png
RP/textures/items/example.item.png
RP/textures/particle/example.particle.png
-->

<div markdown="0" class="folder-structure">
    <ul>
        <li><span class="folder">RP</span>
            <ul>
                <li><span class="file">biomes_client.json</span></li>
                <li><span class="file">manifest.json</span></li>
                <li><span class="image">pack_icon.png</span></li>
                <li><span class="file">sounds.json</span></li>
                <li><span class="folder">animation_controllers</span>
                    <ul>
                        <li><span class="file">example.animation_controller.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">animations</span>
                    <ul>
                        <li><span class="file">example.animation.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">entity</span>
                    <ul>
                        <li><span class="file">example.entity.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">example.item.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">models</span>
                    <ul>
                        <li><span class="folder">entity</span>
                            <ul>
                                <li><span class="file">example.geo.json</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><span class="folder">particles</span>
                    <ul>
                        <li><span class="file">example.particle.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">render_controllers</span>
                    <ul>
                        <li><span class="file">example.render_controller.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">sounds</span>
                    <ul>
                        <li><span class="file">example.sound.ogg</span></li>
                        <li><span class="file">sound_definitions.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">languages.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">textures</span>
                    <ul>
                        <li><span class="folder">blocks</span>
                            <ul>
                                <li><span class="image">example.block.png</span></li>
                                <li><span class="folder">example.texture.variant.block</span>
                                    <ul>
                                        <li><span class="image">0.png</span></li>
                                        <li><span class="image">1.png</span></li>
                                        <li><span class="image">...</span></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li><span class="folder">entity</span>
                            <ul>
                                <li><span class="image">example.entity.png</span></li>
                            </ul>
                        </li>
                        <li><span class="file">item_texture.json</span></li>
                        <li><span class="folder">items</span>
                            <ul>
                                <li><span class="image">example.item.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">particle</span>
                            <ul>
                                <li><span class="image">example.particle.png</span></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><span class="folder">textx</span>
                    <ul>
                        <li><span class="file">en_US.lang</span></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>