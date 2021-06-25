
<img src="../assets/1-basic-css/Untitled.png" alt="information-vs-knowledge" class="responsive">

An element's `padding` controls the amount of space between the element's content and its `border`.

Here, we can see that the blue box and the red box are nested within the yellow box. Note that the red box has more `padding` than the blue box.

## Margin

An element's `margin` controls the amount of space between an element's `border` and surrounding elements.

<img src="../assets/1-basic-css/Untitled1.png" alt="information-vs-knowledge" class="responsive">

Here, we can see that the blue box and the red box are nested within the yellow box. Note that the red box has a bigger `margin` than the blue box, making it appear smaller.

## Clockwise Notation

Specify padding and margins in one line: `top, right, bottom, left`

```css
.blue-box {
    padding: 40px 20px 20px 40px;
  }
```

## Hex Codes

`#RRGGBB`  (~16 million options) or `#RGB` (~4000 options)

Hex code `#FF0000` can be shortened to `#F00`. This shortened form gives one digit for red, one digit for green, and one digit for blue.

This reduces the total number of possible colors to around 4,000. But browsers will interpret `#FF0000` and `#F00` as exactly the same color.

## CSS Variables

```css
.penguin {
    --penguin-skin: gray;
    --penguin-belly: white;
    --penguin-beak: orange;
}
.penguin-top {
    top: 10%;
    left: 25%;
    background: var(--penguin-skin, gray);
    width: 50%;
    height: 45%;
    border-radius: 70% 70% 60% 60%;
  }
```

### Improve Compatibility with Browser Fallbacks

When your browser parses the CSS of a webpage, it ignores any properties that it doesn't recognize or support. For example, if you use a CSS variable to assign a background color on a site, Internet Explorer will ignore the background color because it does not support CSS variables. In that case, the browser will use whatever value it has for that property. If it can't find any other value set for that property, it will revert to the default value, which is typically not ideal.

This means that if you do want to provide a browser fallback, it's as easy as providing another more widely supported value immediately before your declaration. That way an older browser will have something to fall back on, while a newer browser will just interpret whatever declaration comes later in the cascade.

```css
:root {
    --red-color: red;
  }
  .red-box {
    background: red;  //fallback for older browser
    background: var(--red-color);
    height: 200px;
    width:200px;
  } 
```

`:root` is a pseudo-class selector that matches the root element of the document, usually the html element. By creating your variables in `:root`, they will be available globally and can be accessed from any other selector in the style sheet.

### Override CSS Variables

```css
:root {
    --penguin-skin: gray;
    --penguin-belly: pink;
    --penguin-beak: orange;
  }

  body {
    background: var(--penguin-belly, #c6faf1);
  }

  .penguin {

    --penguin-belly: white;

    position: relative;
    margin: auto;
    display: block;
    margin-top: 5%;
    width: 300px;
    height: 300px;
  }
```
