Accidently pushed local only files
===

Let's say you have some local files that in a repo that are not meant to be
pushed to a remote, but, accidently, have been.

Let's say the sha of the commit is `ACCIDENTAL_COMMIT_SHA`, and the
branch of this commit is `FEATURE_BRANCH`.

To retrieve the local only files, and keep them in an untracked status:

- Revert the commit, or bring the remote to the intended state via any method
    (ie, the only difference between the branch and the faulty commit is the
    local only files)
- Check out to another branch locally
- Run git diff to see the files that that are different in the branch and the
    accidental commit
    ```
    git diff --name-only ACCIDENTAL_COMMIT_SHA origin/FEATURE_BRANCH
    ```
- Checkout those files into the current branch.
    ```bash
    git checkout ACCIDENTAL_COMMIT_SHA \
    $(git diff --name-only ACCIDENTAL_COMMIT_SHA origin/FEATURE_BRANCH | xargs)
    ```
- Finally, remove these files from the staging area.

Breathe a sigh of relief!
