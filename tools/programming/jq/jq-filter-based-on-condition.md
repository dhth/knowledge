jq Filter based on condition
===

Say you need to filter items in an array based on some condition. For example,
`https://api.github.com/repos/user/repo/pulls` might return (response shortened
for brevity):

```json
[
    {
        "html_url": "https://api.github.com/repos/user/repo/pulls/307",
        "title": "PR title",
        "user": {
            "login": "user1",
            "id": 123
            }
    },
    {
        "html_url": "https://api.github.com/repos/user/repo/pulls/423",
        "title": "Bump something to some version",
        "user": {
            "login": "dependabot[bot]",
            "id": 112
            }
    },
    {
        "html_url": "https://api.github.com/repos/user/repo/pulls/123",
        "title": "PR title 2",
        "user": {
            "login": "user2",
            "id": 311
            }
    }
]
```
And we want to filter out the second item in the array (from dependabot).

JQ filter for that would be:

```bash
jq '[.[] | select(.user.login != "dependabot[bot]")]'
```

This would result in:

```json
[
    {
        "html_url": "https://api.github.com/repos/user/repo/pulls/307",
        "title": "PR title",
        "user": {
            "login": "user1",
            "id": 123
            }
    },
    {
        "html_url": "https://api.github.com/repos/user/repo/pulls/123",
        "title": "PR title 2",
        "user": {
            "login": "user2",
            "id": 311
            }
    }
]
```
