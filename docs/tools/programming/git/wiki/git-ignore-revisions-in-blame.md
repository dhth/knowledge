Git Ignore Revisions in Blame
===

Add a `.git-blame-ignore-revs` file to the repo.

```
# ran black for the first time
31f90834066ad6acf112

# changed line length to 79
33da33ad33ce3d29142a
```

Run the following to configure git to use this file locally.
```
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

Now, the commits specified in the `.git-blame-ignore-revs` file won't show up in `git blame`.