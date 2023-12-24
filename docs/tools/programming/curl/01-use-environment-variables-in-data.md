# Use Environment Variables in Data

```bash
curl -s -X POST https://api.airtable.com/v0/$POMODORO_AIRTABLE_BASE_ID/tasks \
  -H "Authorization: Bearer $POMODORO_AIRTABLE_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Task Name": "'"$task_name"'"
      }
    }
  ]
}'
```
