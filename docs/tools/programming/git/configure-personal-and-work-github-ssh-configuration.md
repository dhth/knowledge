# Configure Personal and Work Github SSH configuration

Resources
---

- [git - GitHub Error: Key already in use][1]

<!-- Links -->
[1]: https://stackoverflow.com/questions/21160774/github-error-key-already-in-use

<!-- Links end -->


Setup
---

```ssh-config
# ~/.ssh/config

# github_work
Host github-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
  IdentitiesOnly yes

# github_personal
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_personal
  IdentitiesOnly yes
```

Then, in the work repo, make the following change in the `.git/config` file:

```
[remote "origin"]
	url = git@github-work:<username>/<repo>.git
```

And, while cloning, use `git@github-work:<username>/<repo>.git` as well.
