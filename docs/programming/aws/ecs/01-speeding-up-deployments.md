---
title: "Speeding Up Deployments"
summary:
---

Speeding Up Deployments
===

Resources
---

- [:fontawesome-solid-link: Speeding up Amazon ECS container deployments Nathan Peck][1]

<!-- Links -->
[1]: https://nathanpeck.com/speeding-up-amazon-ecs-container-deployments/

Health Checks
---

CDK code:

```python
api_health_check = elb.HealthCheck(
    enabled=True,
    path="/ping",
    protocol=elb.Protocol.HTTP,
    healthy_http_codes="200-399",
    healthy_threshold_count=2,
    unhealthy_threshold_count=2,
    timeout=core.Duration.seconds(6),
    interval=core.Duration.seconds(5),
)
```

Deregistration Delay
---

CDK code:

```python
listener.add_targets(
    "target-group",
    port=fargate_service_container_port,
    deregistration_delay=core.Duration.seconds(5),
    health_check=metaflow_api_health_check,
    protocol=elb.Protocol.TCP,
    targets=[fargate_service],
)
```
