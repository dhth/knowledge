# Github Repo Search

Resources
---

- [Repositories - GitHub Docs][1]

<!-- Links -->
[1]:
https://docs.github.com/en/rest/reference/repos#list-repositories-for-the-authenticated-user


Setup
---

```bash
curl --location --request GET 'https://api.github.com/user/repos?sort=updated&per_page=15' \
--header "Authorization: token $GH_ACCESS_TOKEN" \
--header 'Accept: application/vnd.github.v3+json' | $HOMEBREW_DIR/jq '. | map({uid: .name, title: .name, subtitle: .owner.login, arg: .html_url }) | { items: . }'
```
