Cloudformation CLI multiple values for a parameter
===

Say you have a parameter in a cloudformation stack that accepts a list of
values, eg.

```yaml
LoadBalancerSubnets:
  Type: List<AWS::EC2::Subnet::Id>
  Description: The subnets associated to the load balancer
```

These can be passed to the `cloudformation create-stack` command as:

```bash
aws cloudformation create-stack \
    --stack-name some-stack \
    --template-body path/to/stack.yml \
    --profile aws-profile \
    --region eu-central-1 \
    --parameters ParameterKey=Environment,ParameterValue=qa ParameterKey=LoadBalancerSubnets,ParameterValue="subnet-id-1\,subnet-id-2"
```
