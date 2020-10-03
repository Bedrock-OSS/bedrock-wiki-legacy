# Table of contents

## Basic usage

To include new dynamic TOC in a page, add this snippet under the page title.

```html
<details id="toc" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>
```

## CSS classes

There are some CSS classes, which can be added to the details tag.

### top-level

Using the class will leave only the top-level links in TOC.

Usage:

```html
<details id="toc" class="top-level" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>
```

### numbered

Using the class will number all links in TOC, while respecting the levels.

Usage:

```html
<details id="toc" class="numbered" open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>
```