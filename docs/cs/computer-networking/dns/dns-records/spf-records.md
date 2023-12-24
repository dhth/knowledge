# SPF Records

An SPF record looks like this:

```
v=spf1 include:spf.mailjet.com ?all
```

v=spf1: This indicates that the SPF version being used is SPF version 1.

include:spf.mailjet.com: This mechanism includes the SPF record of
spf.mailjet.com. It allows the authorized mail servers listed in the SPF record
of spf.mailjet.com to send email on behalf of the domain that this SPF record
belongs to. In other words, it grants permission to Mailjet's mail servers to
send email on behalf of your domain.

?all: This is the result qualifier, specifying the action to take if the sending
server does not match any of the authorized servers. In this case, ?all
indicates a neutral result. It means that the SPF check is not decisive, and the
email server should determine the action to take. The email might be accepted or
rejected based on the policies of the receiving server.

To summarize, this SPF record includes the SPF record of spf.mailjet.com,
allowing Mailjet's authorized mail servers to send email on behalf of your
domain. The neutral result qualifier ?all suggests that the email server should
make the final decision on accepting or rejecting emails that do not match the
authorized servers.
