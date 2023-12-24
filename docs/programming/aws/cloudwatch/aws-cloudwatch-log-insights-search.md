# AWS Cloudwatch Log Insights Search

Sample query
---

```
filter @logStream = '<LOGSTREAM_ID'
 | filter @message like /search_string/
 | fields @timestamp, @message
```
