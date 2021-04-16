---
title: "Tmux Wiki"
summary: 
---

Tmux Wiki
===

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
