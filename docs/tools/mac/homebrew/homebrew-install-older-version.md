# Homebrew Install Older Version

Resources
---

- [Homebrew - how to install older versions][1]

<!-- Links -->
[1]: https://stackoverflow.com/questions/39187812/homebrew-how-to-install-older-versions

<!-- Links end -->


Steps
---

Based on [this][1] post.

```bash
# say you want to pin tmux
cd "$(brew --repo homebrew/core)"
# find the commit you want to revert to either from git log or
# on github

git checkout <COMMIT_ID>
brew unlink tmux
HOMEBREW_NO_AUTO_UPDATE=1 brew install tmux

# revert homebrew's local installation
git checkout master

# if needed
brew pin tmux
```
