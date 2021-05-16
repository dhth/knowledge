---
title: "Use secrets from secrets manager"
summary:
---

Use secrets from secrets manager
===

Resources
---

- [:fontawesome-brands-aws: Ec2TaskDefinition][1]
- [:fontawesome-solid-link: I tell you a secret: Provide Database credentials to
    an ECS Fargate task in AWS CDK][2]

<!-- Links -->
[1]:
https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ecs/Ec2TaskDefinition.html#aws_cdk.aws_ecs.Ec2TaskDefinition.add_container
[2]:
https://dev.to/michaelfecher/i-tell-you-a-secret-provide-database-credentials-to-an-ecs-fargate-task-in-aws-cdk-5f4

Code
---

Secrets from secrets manager can be passed to the container instead of regular
environment variables. The benefit of that is that these don't show up as
plain text on the AWS dashboard.

```python
secret = sm.Secret.from_secret_name_v2(
self, id="secret-1", secret_name="super-secret-secret"
)

worker_definition.add_container(
"worker-container",
image=ecs.ContainerImage.from_asset(directory="./api/project"),
cpu=256,
memory_limit_mib=512,
port_mappings=[
ecs.PortMapping(
    container_port=80, host_port=80, protocol=ecs.Protocol.TCP
)
],
secrets={
'SECRET_FROM_SM': ecs.Secret.from_secrets_manager(secret),
},
environment={
"ENV_VAR_ONE": "this will show up on the dashboard",
},
logging=ecs.AwsLogDriver(stream_prefix="worker"),
)
```

To use these secrets as regular environment variables, we'd have to call their
`.secret_value.to_string()` method. They still won't show up in the
cloudformation template, but will on the dashboard.

```python
environment={
    "ENV_VAR_ONE": "env var unprotected",
    "ENV_VAR_TWO": secret.secret_value.to_string(),
}
```
