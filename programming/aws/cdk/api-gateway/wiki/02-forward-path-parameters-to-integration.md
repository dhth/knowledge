Forward Path Parameters to Integration
===

Let's say we have the following endpoint in a web application (running on ECS),
which is fronted by API Gateway.

```
/details/1/1234?verbose=1
```

which needs two path parameters:

- `artist`
- `album`

Set up a VPC link to the NLB pointing to the ECS service. Then API Gateway's
endpoint URL (for the VPC Link integration) needs to be configured as follows:

```
/details/{artist}/{album}
```

And, the VPC Link integration needs to be configured with request parameters as
follows:

```python
# ... (setup)
integration = api_gateway.Integration(
    type=api_gateway.IntegrationType.HTTP_PROXY,
    integration_http_method="GET",
    options=api_gateway.IntegrationOptions(
        vpc_link=vpc_link,
        connection_type=api_gateway.ConnectionType.VPC_LINK,
        request_parameters={
            "integration.request.path.artist": "method.request.path.artist",
            "integration.request.path.album": "method.request.path.album",
        },
    ),
    uri=f"http://{nlb.load_balancer_dns_name}"+"/details/{artist}/{album}",
)
details_resource.add_method(
    http_method="GET",
    request_parameters={
        "method.request.path.artist": True,
        "method.request.path.album": True,
    },
    integration=integration,
)
```

Query parameters will be forwarded to the integration automatically (this will
work if they're named the same in the ECS implementation).
