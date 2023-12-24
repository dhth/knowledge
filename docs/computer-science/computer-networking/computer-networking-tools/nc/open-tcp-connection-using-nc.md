Open TCP connection using nc
===

Resources
---

- [The HTTP crash course nobody asked for][1]

<!-- Links -->
[1]: https://fasterthanli.me/articles/the-http-crash-course-nobody-asked-for

<!-- Links end -->


Make a simple request
---

```bash
printf 'HEAD / HTTP/1.1\r\nHost: neverssl.com\r\nConnection: close\r\n\r\n' | nc neverssl.com 80
```

Response:

```
HTTP/1.1 200 OK
Date: Sun, 11 Dec 2022 08:13:45 GMT
Server: Apache/2.4.54 ()
Upgrade: h2,h2c
Connection: Upgrade, close
Last-Modified: Wed, 29 Jun 2022 00:23:33 GMT
ETag: "f79-5e28b29d38e93"
Accept-Ranges: bytes
Content-Length: 3961
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
```

Make multiple requests over the same connection
---

```bash
printf 'HEAD / HTTP/1.1\r\nHost: example.org\r\n\r\nHEAD / HTTP/1.1\r\nHost: example.org\r\nConnection: close\r\n\r\n' | nc example.org 80
```
