API Gateway Mapping Template
===

Resources
---

- [Apache Velocity Engine VTL Reference][1]
- [Velocity Reference][2]

<!-- Links -->
[1]: https://velocity.apache.org/engine/devel/vtl-reference.html#variables
[2]: https://cwiki.apache.org/confluence/display/velocity/CheckingForNull

Conditionals
---

Let's say the payload looks like this:

```json
{
  "event": {
    "op": "INSERT",
    "data": {
      "old": "something",
      "new": "something else"
    }
  }
}
```

Mapping template to set the `MessageGroupId` based on `op` would be:

```
#if($util.parseJson($input.body).event.op == "DELETE")
#set ($MessageGroupId = $util.parseJson($input.body).event.data.old)
#else
#set ($MessageGroupId = $util.parseJson($input.body).event.data.new)
#end
Action=SendMessage&MessageGroupId=$MessageGroupId&MessageBody=$util.urlEncode($input.body)
```

Set SQS Message Attributes
---

```
#set ($MessageGroupId = $util.parseJson($input.body).data.some_id)
Action=SendMessage&MessageGroupId=$MessageGroupId&MessageBody=$util.urlEncode($input.body)&MessageAttribute.1.Name=someattributename&MessageAttribute.1.Value.DataType=String&MessageAttribute.1.Value.StringValue=somevalue
```
