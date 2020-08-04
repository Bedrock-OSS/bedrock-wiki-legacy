---
layout: page
title: Shaders
parent: Knowledge
---

# Shaders

## Overview

Shaders are divided into 2 folders: glsl and hlsl. For shaders to work on every device, 
you need to code shaders in both languages. For testing on Windows, hlsl is enough. 
When rewriting shaders from one language to another, there are few things to change, 
like HLSL `float3` is `vec3` in GLSL. [Mapping between those languages can be found here](https://anteru.net/blog/2016/mapping-between-HLSL-and-GLSL/)

## Troubleshooting

### Shader doesn’t change

Every time there is a change in the shader, you need to completely restart Minecraft to recompile the shader.

### Compilation error

When there is a shader compilation error, usually there is a line number specified, where the error occurred. You need to check few lines above the one specified in error, because before compilation, Minecraft adds `#define` directives

### Couldn’t find constant buffer named: $Globals

I couldn’t accurately find the actual cause of this error, but it seems to be somehow connected to global variables. Removing them (initializing them in `main` function or changing them to `#define` directives) seems to fix the problem.

## Tips and tricks

### Passing variables to shader

You can pass variables to the shader from a particle, or an entity by changing entity color.
Input color is clamped to `<0.0, 1.0>`. To pass bigger values, you need to divide by max value (or at least by some big number).

### Using time in shader

`TIME` variable is number of seconds as `float` and is global for all shaders. For time based on particle lifetime, you need to pass this:

```json
"minecraft:particle_appearance_tinting": {
    "color": ["variable.particle_age/variable.particle_lifetime", 0, 0, 1]
}
```

Then in shader, use `PSInput.color.r` as time, where `0.0` is particle birth and `1.0` is particle death.

### Camera direction towards the entity

For entity shaders, you can make the shader dependent on camera direction towards the entity.

* Add to `PS_Input` in vertex and fragment shader new field
```
float3 viewDir: POSITION;
```
* After that, add to vertex shader this line
```
PSInput.viewDir = normalize((mul(WORLD, mul(BONES[VSInput.boneId], float4(VSInput.position, 1)))).xyz);
```
* In fragment shader use `PSInput.viewDir` to make changes depending on camera rotation

### Debugging values

The easiest way to debug a value is to turn it into color and render it like this

```
PSOutput.color = float4(PSInput.uv, 0., 1.);
```

This should create a red-green gradient, showing that the values of `uv` are between `<0, 0>` and `<1, 1>`.

For more advanced debugging, you can use the debug shader I wrote [based on this shader](http://mew.cx/drawtext/drawtext.html).
Right now this shader will display values of the color passed to the shader. To display another value, change line 70 in hlsl shader to
```
int ascii = getFloatCharacter( cellIndex, <float4 vector here> );
```
GLSL version of debug shader may crash Minecraft, use only for debugging.

[Download debug shader](http://files.stirante.com/debugShader.zip)