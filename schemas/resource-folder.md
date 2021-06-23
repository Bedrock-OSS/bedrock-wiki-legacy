---
layout: page
title: Resource Folder Schema
parent: Schemas
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
                <li><span class="image">pack_icon.png</span></li>
                <li><span class="image">bug_pack_icon.png</span></li>
                <li><span class="file">biomes_client.json</span></li>
                <li><span class="file">blocks.json</span></li>
                <li><span class="file">contents.json</span></li>
                <li><span class="file">items_offsets_client.json</span></li>
                <li><span class="file">loading_messages.json</span></li>
                <li><span class="file">manifest.json</span></li>
                <li><span class="file">sounds.json</span></li>
                <li><span class="file">splashes.json</span></li>
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
                <li><span class="folder">font</span></li>
                <li><span class="folder">items</span>
                    <ul>
                        <li><span class="file">example.item.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">materials</span>
                    <ul>
                        <li><span class="file">example.material</span></li>
                        <li><span class="file">example.json</span></li>
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
                        <li><span class="file">example.ogg</span></li>
                        <li><span class="file">music_definitions.json</span></li>
                        <li><span class="file">sound_definitions.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">texts</span>
                    <ul>
                        <li><span class="file">languages.json</span></li>
                        <li><span class="file">language_names.json</span></li>
                        <li><span class="file">...</span></li>
                    </ul>
                </li>
                <li><span class="folder">textures</span>
                    <ul>
                        <li><span class="folder">blocks</span>
                            <ul>
                                <li><span class="image">example.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">colormap</span>
                            <ul>
                                <li><span class="image">birch.png</span></li>
                                <li><span class="image">evergreen.png</span></li>
                                <li><span class="image">...</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">entity</span>
                            <ul>
                                <li><span class="image">example.entity.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">environment</span>
                            <ul>
				<li><span class="folder">overworld_cubemap</span>
				<ul>
				<li><span class="image">cubemap_0.png</span></li>
				<li><span class="image">cubemap_1.png</span></li>
				<li><span class="image">cubemap_2.png</span></li>
				<li><span class="image">cubemap_3.png</span></li>
				<li><span class="image">cubemap_4.png</span></li>
				<li><span class="image">cubemap_5.png</span></li>
				</ul></li>
                                <li><span class="image">clouds.png</span></li>
                                <li><span class="image">destroy_stage_0.png</span></li>
                                <li><span class="image">...</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">gui</span>
                            <ul>
                                <li><span class="folder">achievements</span></li>
                                <li><span class="folder">newgui</span></li>
                                <li><span class="image">...</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">items</span>
                            <ul>
                                <li><span class="image">example.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">map</span>
                            <ul>
                                <li><span class="image">map_background.png</span></li>
                                <li><span class="image">map_icons.png</span></li>
                                <li><span class="image">player_icon_background.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">misc</span>
                            <ul>
                                <li><span class="image">enchanted_item_glint.png</span></li>
                                <li><span class="image">missing_texture.png</span></li>
                                <li><span class="image">pumpkinblur.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">models</span>
                            <ul>
                                <li><span class="folder">armor</span>
                                    <ul>
                                        <li><span class="image">chain_1.png</span></li>
                                        <li><span class="image">chain_2.png</span></li>
                                        <li><span class="image">...</span></li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li><span class="folder">painting</span>
                            <ul>
                                <li><span class="image">kz.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">particle</span>
                            <ul>
                                <li><span class="image">campfire_smoke.png</span></li>
                                <li><span class="image">particles.png</span></li>
                                <li><span class="image">example.png</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">persona_thumbnails</span>
                            <ul>
                                <li><span class="image">alex_hair_thumbnail_0.png</span></li>
                                <li><span class="image">alex_pants_thumbnail_0.png</span></li>
                                <li><span class="image">...</span></li>
                            </ul>
                        </li>
                        <li><span class="folder">ui</span>
                            <ul>
                                <li><span class="folder">subcategory_icons</span></li>
                                <li><span class="image">5stars_empty.png</span></li>
                                <li><span class="image">...</span></li>
                            </ul>
                        </li>
                        <li><span class="image">flame_atlas.png</span></li>
                        <li><span class="image">forcefield.png</span></li>
                        <li><span class="file">flipbook_textures.json</span></li>
                        <li><span class="file">item_texture.json</span></li>
                        <li><span class="file">terrain_texture.json</span></li>
                        <li><span class="file">textures_list.json</span></li>
                    </ul>
                </li>
                <li><span class="folder">ui</span>
                    <ul>
                        <li><span class="folder">realmsPlus_sections</span></li>
                        <li><span class="folder">settings_sections</span></li>
                        <li><span class="image">...</span></li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
</div>
