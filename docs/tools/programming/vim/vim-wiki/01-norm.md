---
title: Norm
summary:
---

Norm
===

Resources
---
- [:fontawesome-solid-play-circle: A Vid in which Vim Saves Me Hours & Hundreds of Clicks](https://www.youtube.com/watch?v=hraHAZ1-RaM)

Use norm with visual mode
---

Let's say I want to prepend the text "prepend" and append the text "append" to a
bunch of lines.

- Highlight lines
- `:'<,'>norm! 0iprepend<C-v><Esc>Aappend` (Literally type `<C-v>` and `Esc`,
    which will be entered as `^` and `[` respectively in the command line)

More [:fontawesome-solid-link: here](https://www.reddit.com/r/vim/comments/4ofv82/the_normal_command_is_really_cool/).
