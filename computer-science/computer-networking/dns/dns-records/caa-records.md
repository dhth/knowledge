CAA Records
===

Resources
---

- [DNS CAA record tester][1]

<!-- Links -->
[1]: https://caatest.co.uk/

<!-- Links end -->


A CAA record looks like this:

```
example.com. CAA 0 issue "letsencrypt.org"
```

example.com.: This is the domain name for which the CAA record is being
set. It ends with a dot to signify the root of the domain.

CAA: This is the type of DNS record, indicating that it is a Certificate
Authority Authorization record.

0: This value specifies the "flag" field, which is currently unused. It
is set to 0.

issue: This is the "tag" field, specifying the policy type. In this case,
it indicates that the CAA record is specifying the certificate authority (CA)
that is authorized to issue certificates for the domain.

"letsencrypt.org": This is the "value" field, which contains the value
associated with the policy type. In this example, it specifies that Let's
Encrypt (letsencrypt.org) is the authorized CA to issue certificates for the
domain.

This CAA record essentially states that Let's Encrypt is authorized to issue
certificates for the domain "example.com". Other CAs would not be allowed to
issue certificates for this domain based on this CAA record.
