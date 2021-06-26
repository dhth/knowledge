Vimium
===

Bindings worth remembering
---

```
W:    Detach tab into new window
```

Custom CSS
---

[:fontawesome-brands-github: Source](https://github.com/Foldex/vimium-dark-themes/blob/master/vimium-dark.css)

```css
:root {
  --font-size: 20;
  --font-weight: normal;
  --padding: 2px;
  --shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);


  /* ---------- Gruvbox Dark ---------- */
  --fg: #ebdbb2;
  --bg: #282828;
  --border: #3c3836;
  --main-fg: #83a598;
  --accent-fg: #b8bb26;

  /* Unused Alternate Colors */
  /*--bg-dark: #1d2021;*/
  /*--cyan: #076678;*/
  /*--purple: #8f3f71;*/
  /*--red: #fb4934;*/
  /*--yellow: #fabd2f;*/

}

/*****************************************************************************/
/*                                    CSS                                    */
/*****************************************************************************/

/* -------- HINTS -------- */
#vimiumHintMarkerContainer div.internalVimiumHintMarker, #vimiumHintMarkerContainer div.vimiumHintMarker {
  background: var(--bg);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  padding: 3px 4px;
}

#vimiumHintMarkerContainer div span {
  color: var(--main-fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
  text-shadow: none;
}

#vimiumHintMarkerContainer div > .matchingCharacter {
  opacity: 0.3;
}

#vimiumHintMarkerContainer div > .matchingCharacter ~ span {
  color: var(--main-fg);
}

/* -------- VOMNIBAR -------- */
#vomnibar {
  animation: show 200ms cubic-bezier(0, 0, 0.2, 1) forwards;
  background: var(--bg);
  border: none;
  box-shadow: var(--shadow);
}

/* Animate Slide in */
@keyframes show {
  0% {
    opacity: 0;
    transform: translateY(50px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

#vomnibar .vomnibarSearchArea,
#vomnibar input {
  background: transparent;
  border: none;
  box-shadow: none;
  color: var(--fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

#vomnibar .vomnibarSearchArea {
  padding: var(--padding) 30px;
}

#vomnibar input {
  padding: var(--padding)}

#vomnibar ul {
  background: var(--bg);
  border-top: 1px solid var(--border);
  margin: 0;
  padding: var(--padding);
}

#vomnibar li {
  border-bottom: 1px solid var(--border);
  padding: var(--padding);
}

#vomnibar li .vomnibarTopHalf,
#vomnibar li .vomnibarBottomHalf {
  padding: var(--padding) 0;
}

#vomnibar li .vomnibarSource {
  color: var(--main-fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

#vomnibar li em,
#vomnibar li .vomnibarTitle {
  color: var(--main-fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

#vomnibar li .vomnibarUrl {
  color: var(--fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

#vomnibar li .vomnibarMatch {
  color: var(--accent-fg);
  font-weight: normal;
}

#vomnibar li .vomnibarTitle .vomnibarMatch {
  color: var(--main-fg);
}

#vomnibar li.vomnibarSelected {
  background-color: var(--border);
}

/* -------- HUD -------- */
div.vimiumHUD {
  background: var(--bg);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
}

div.vimiumHUD span#hud-find-input,
div.vimiumHUD .vimiumHUDSearchAreaInner {
  color: var(--fg);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

div.vimiumHUD .hud-find {
  background-color: transparent;
  border: none;
}

div.vimiumHUD .vimiumHUDSearchArea {
  background-color: transparent;
}
```
