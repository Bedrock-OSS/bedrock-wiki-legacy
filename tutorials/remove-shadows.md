---
layout: page
title: Remove Entity Shadows
parent: Tutorials
---

# Remove Entity Shadows

Change these lines in the `shadow.material` file under the Resource Pack / materials folder. 

**NOTE:** This folder is NOT included in the vanilla RP Pack examples and must be exported from a APK files or added by hand.

**NOTE:** This has not been tested for blocks and has only been verified for entities. If you find it works on blocks too please let us know so we can add that in.

## Working shadow code: Shadows for ALL entities:
```json
"shadow_overlay": {
      "+states": [
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
      ],

      "vertexShader": "shaders/color.vertex",
      "vrGeometryShader": "shaders/color.geometry",
      "fragmentShader": "shaders/shadow_stencil_overlay.fragment",

      "blendSrc": "DestColor",
      "blendDst": "Zero",

      "frontFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      },
```

## Disabled shadow code: No Shadows for ALL entities: 
```json
 "shadow_overlay": {
      "+states": [
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
      ],

      "vertexShader": "",
      "vrGeometryShader": "",
      "fragmentShader": "",

      "blendSrc": "DestColor",
      "blendDst": "Zero",

      "frontFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      }
}
```

## Vanilla shadow.material file with working shadows

```json
{
  "materials": {
    "version": "1.0.0",

    "shadow_front": {
      "+states": [
        "StencilWrite",
        "DisableColorWrite",
        "DisableDepthWrite",
        "EnableStencilTest"
      ],

      "vertexShader": "shaders/position.vertex",
      "vrGeometryShader": "shaders/position.geometry",
      "fragmentShader": "shaders/flat_white.fragment",

      "frontFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "backFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "stencilRef": 0,
      "stencilReadMask": 255,
      "stencilWriteMask": 1,
      "vertexFields": [
        { "field": "Position" }
      ],
      "msaaSupport": "Both"

    },

    "shadow_back": {
      "+states": [
        "StencilWrite",
        "DisableColorWrite",
        "DisableDepthWrite",
        "InvertCulling",
        "EnableStencilTest"
      ],

      "vertexShader": "shaders/position.vertex",
      "vrGeometryShader": "shaders/position.geometry",
      "fragmentShader": "shaders/flat_white.fragment",

      "frontFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "backFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "stencilRef": 1,
      "stencilReadMask": 255,
      "stencilWriteMask": 1,

      "vertexFields": [
        { "field": "Position" }
      ],
      "msaaSupport": "Both"

    },

    "shadow_overlay": {
      "+states": [
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
      ],

      "vertexShader": "shaders/color.vertex",
      "vrGeometryShader": "shaders/color.geometry",
      "fragmentShader": "shaders/shadow_stencil_overlay.fragment",

      "blendSrc": "DestColor",
      "blendDst": "Zero",

      "frontFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      },

      "backFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      },

      "stencilRef": 1,
      "stencilReadMask": 255,
      "stencilWriteMask": 0,

      "vertexFields": [
        { "field": "Position" },
        { "field": "Color" }
      ],
      "msaaSupport": "Both"

    },

    "water_hole": {
      "+states": [
        "DisableColorWrite"
      ],
      "vertexFields": [
        { "field": "Position" },
        { "field": "Color" },
        { "field": "UV0" }
      ],

      "vertexShader": "shaders/position.vertex",
      "vrGeometryShader": "shaders/position.geometry",
      "fragmentShader": "shaders/flat_white.fragment",

      "msaaSupport": "Both"
    }
  }
}
```

## shadow.material with NO Shadows

```json
{
  "materials": {
    "version": "1.0.0",

    "shadow_front": {
      "+states": [
        "StencilWrite",
        "DisableColorWrite",
        "DisableDepthWrite",
        "EnableStencilTest"
      ],

      "vertexShader": "",
      "vrGeometryShader": "",
      "fragmentShader": "",

      "frontFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "backFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "stencilRef": 0,
      "stencilReadMask": 255,
      "stencilWriteMask": 1,
      "vertexFields": [
        { "field": "Position" }
      ],
      "msaaSupport": "Both"

    },

    "shadow_back": {
      "+states": [
        "StencilWrite",
        "DisableColorWrite",
        "DisableDepthWrite",
        "InvertCulling",
        "EnableStencilTest"
      ],

      "vertexShader": "",
      "vrGeometryShader": "",
      "fragmentShader": "",

      "frontFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "backFace": {
        "stencilFunc": "Always",
        "stencilFailOp": "Keep",
        "stencilDepthFailOp": "Keep",
        "stencilPassOp": "Replace"
      },

      "stencilRef": 1,
      "stencilReadMask": 255,
      "stencilWriteMask": 1,

      "vertexFields": [
        { "field": "Position" }
      ],
      "msaaSupport": "Both"

    },

    "shadow_overlay": {
      "+states": [
        "DisableDepthTest",
        "DisableCulling",
        "Blending",
        "EnableStencilTest"
      ],

      "vertexShader": "",
      "vrGeometryShader": "",
      "fragmentShader": "",

      "blendSrc": "DestColor",
      "blendDst": "Zero",

      "frontFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      },

      "backFace": {
        "stencilFunc": "Equal",
        "stencilPass": "Replace"
      },

      "stencilRef": 1,
      "stencilReadMask": 255,
      "stencilWriteMask": 0,

      "vertexFields": [
        { "field": "Position" },
        { "field": "Color" }
      ],
      "msaaSupport": "Both"

    },

    "water_hole": {
      "+states": [
        "DisableColorWrite"
      ],
      "vertexFields": [
        { "field": "Position" },
        { "field": "Color" },
        { "field": "UV0" }
      ],

      "vertexShader": "shaders/position.vertex",
      "vrGeometryShader": "shaders/position.geometry",
      "fragmentShader": "shaders/flat_white.fragment",

      "msaaSupport": "Both"
    }
  }
}
```
I hope this helps, if you find other ways to disable shadow please let us know so we can add them.

---

**Credit:** by Outlandishly Crafted updated by Jeremy Benisek AKA CyberAxe
06212020