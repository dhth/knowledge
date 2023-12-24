# Tmux Wiki

Resources
---

- [Tmux display popup][1]: Use tmux display popups

<!-- Links -->
[1]: https://qmacro.org/autodidactics/2021/08/06/tmux-output-formatting/

<!-- Links end -->


Session
---

### New session

```
tmux new -s basic
```

### Create session in background

```
tmux new -s second_session -d
```

### Rename Session

```
Prefix $
```

### Attach to session

```
tmux attach -t second_session
```

### Move between sessions

```
Prefix )
Prefix (
Prefix s # see all sessions
```

Windows
---

### Create windows

```
tmux new -s windows -n shell
# this will create a session with name windows and a window with name shell
```

```
Prefix c  # create window from within tmux
```

### Rename windows

```
Prefix + ,
```

### Move between windows

```
Prefix + n   #next window
Prefix + p   #previous window
Prefix + 1   #window at index 1
```

### Open new window in current directory

```
bind c new-window -c "#{pane_current_path}"
```

### Reorder windows

```
:swap-window -t -1
//moves current window to the left

:swap-window -s 3 -t 1
//swaps window indexed at 3 with that indexed at 1
```

### List windows

```bash
tmux list-windows -a -F '#S:#W'
# will return windows in all sessions for a server.
# the format will be session_name:window_name
```


Panes
---

### Splits

```
Prefix + %   # split vertically
Prefix + "   # split horizontally
```

### Resizing panes

```
Prefix + space  #cycle through built-in layouts
```

### Kill pane

```
exit
#or
Prefix + x
```

### Show pane numbers

```
Prefix q
```

### Pane → Window

```
# Prefix !
# will convert a pane into a window
```

Command mode
---

```
# get into command mode
Prefix + :
```

Scrolling
---

```
# Prefix [ -> puts in copy mode
```

```
#enable vim mode with
setw -g mode-keys vi

#then use ctrl-b/ctrl-f to move up/down one page.
```

Searching
---

```
# ? to search backwards
# / to search forwards
# just like vim
```

Copying
---

```
# In copy mode
# press Space to start selecting, end with Enter

# paste with Prefix ]
```

Make pane border invisible
---

Just set `pane-border-style`, and `pane-active-border-style` to be the same
color as the background.

```
set-option -g pane-active-border-style fg=colour0 #fg2
set-option -g pane-border-style fg=colour0 #bg1
```
