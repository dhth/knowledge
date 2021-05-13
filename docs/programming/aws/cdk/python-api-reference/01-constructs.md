---
title: "Constructs"
summary:
---

Constructs
===

Intro
---

A CDK stack looks like this:

```python
class BaseResources(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, 'vpc', max_azs=2, nat_gateways=1)
```

The class constructors of both `BaseResources` and `ec2.Vpc` (and many
other classes in the CDK) have the signature `(scope, id, **kwargs)`. This is
because all of these classes are constructs. Constructs are the basic building
block of CDK apps. They represent abstract components which can be composed
together into higher level abstractions via scopes. Scopes can include
constructs, which in turn can include other constructs, etc.

Constructs are always created in the scope of another construct and must always
have an identifier which must be unique within the scope it's created.
Therefore, construct initializers (constructors) will always have the following
signature:

- **scope**: the first argument is always the scope in which this construct is
created. In almost all cases, you'll be defining constructs within the scope of
current construct, which means you'll usually just want to pass self for the
first argument.

- **id**: the second argument is the local identity of the construct. It's an ID 
that has to be unique amongst construct within the same scope. The CDK uses this
identity to calculate the CloudFormation Logical ID for each resource defined
within this scope.

- **kwargs**: the last (sometimes optional) arguments is always a set of
initialization arguments. Those are specific to each construct. For example, the
lambda. Function construct accepts arguments like runtime, code and handler.
