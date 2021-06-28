Use Existing Rest API
===

Fetch rest api ID, and root resource ID via:

```bash
aws apigateway get-rest-apis --region=eu-central-1
aws apigateway get-resources --rest-api-id XXXX --region=eu-central-1
```

```python
rest_api = api_gateway.RestApi.from_rest_api_attributes(
    self,
    "rest-api",
    rest_api_id="XXXX",
    root_resource_id="YYYY",
)
```
