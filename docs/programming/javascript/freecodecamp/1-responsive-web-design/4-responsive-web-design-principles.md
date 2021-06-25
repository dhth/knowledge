
Media Queries consist of a media type, and if that media type matches the type of device the document is displayed on, the styles are applied. You can have as many selectors and styles inside your media query as you want.

Here's an example of a media query that returns the content when the device's width is less than or equal to 100px:

`@media (max-width: 100px) { /* CSS Rules */ }`

and the following media query returns the content when the device's height is more than or equal to 350px:

`@media (min-height: 350px) { /* CSS Rules */ }`

Remember, the CSS inside the media query is applied only if the media type matches that of the device being used.

## Make images responsive

Making images responsive with CSS is actually very simple. Instead of applying an absolute width to an element:

`img { width: 720px; }`

You can use:

```css
img {
  max-width: 100%;
  display: block;
  height: auto;
}
```

The `max-width` property of 100% scales the image to fit the width of its container, but the image won't stretch wider than its original width. Setting the `display`property to block changes the image from an inline element (its default), to a block element on its own line. The `height` property of auto keeps the original aspect ratio of the image.

## Responsive Typography

Instead of using `em` or `px` to size text, you can use viewport units for responsive typography. Viewport units, like percentages, are relative units, but they are based off different items. Viewport units are relative to the viewport dimensions (width or height) of a device, and percentages are relative to the size of the parent container element.

The four different viewport units are:

- `vw` (viewport width): `10vw` would be 10% of the viewport's width.
- `vh` (viewport height): `3vh` would be 3% of the viewport's height.
- `vmin` (viewport minimum): `70vmin` would be 70% of the viewport's smaller dimension (height or width).
- `vmax` (viewport maximum): `100vmax` would be 100% of the viewport's bigger dimension (height or width).
