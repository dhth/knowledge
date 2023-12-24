# JIRA API

Search Issues
---

```bash
curl --location --request POST "https://${domain}.atlassian.net/rest/api/3/search" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic <TOKEN>' \
--data-raw '{
    "jql": "project = SEL AND Sprint in (19, 20) AND text ~ \"'"$QUERY"'\" AND assignee in (currentUser()) order by updated DESC",
    "fieldsByKeys": false,
    "fields": [
        "summary",
        "status",
        "assignee",
	    "issuetype"
    ],
    "startAt": 0
}
```
