CNAME records
===

Resources
---

- [What is a DNS CNAME record? | Cloudflare][1]
- [CNAME Lookup][2]

<!-- Links -->
[1]: https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-cname-record/
[2]: https://dnschecker.org/cname-lookup.php

<!-- Links end -->


A CNAME record looks like this:

```
subdomain.example.com. IN CNAME targetdomain.com.
```

subdomain.example.com.: This is the source domain or subdomain for which the
CNAME record is being set. It ends with a dot to signify the root of the domain.

IN: This indicates the class of the record, typically "IN" for Internet.

CNAME: This is the type of DNS record, indicating that it is a Canonical Name
record.

targetdomain.com.: This is the target domain or the canonical name to which the
source domain is being aliased. It also ends with a dot.

This CNAME record essentially creates an alias for the subdomain
subdomain.example.com, pointing it to the target domain targetdomain.com. When
someone tries to access subdomain.example.com, the DNS resolution will follow
the CNAME record and direct the request to the target domain.
