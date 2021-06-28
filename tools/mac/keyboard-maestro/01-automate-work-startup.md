Automate Work Startup
===

Open Chrome with urls
---

Create a file containing the urls (eg. at ~/.WORK_STARTUP_URLS)

```
https://someurl.com
https://someotherurl.com
https://someotherurl.com
```

Create a shell script to open chrome. (Mine is in my                                                                   [dotfiles](https://github.com/dhth/dotfiles/tree/master/keyboard_maestro),
symlinked to `$HOME`.

```bash
open -n -a "Google Chrome" --args \
    --profile-directory="Profile 4" $(cat $HOME/.WORK_STARTUP_URLS | xargs)
```

The chrome profile can be found from `~/Library/Application\
Support/Google/Chrome/<Profile Name>`. The default profile is probably named
`Default`, with the others named something like `Profile 4`.

Create a Keyboard Maestro macro that just runs the script.
