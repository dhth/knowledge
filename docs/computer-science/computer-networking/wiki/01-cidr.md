---
title: "CIDR"
summary:
---

CIDR
===

Resources
---

- [:fontawesome-brands-aws: Understanding CIDR Notation][1]
- [:fontawesome-solid-play-circle: IPv4, CIDR, and VPC Subnets Made Simple!][2]

<!-- Links -->
[1]: https://www.aws.training/Details/Video?id=16480
[2]: https://www.youtube.com/watch?v=z07HTSzzp3o&t=745s

Basics
---

CIDR: Classless Inter Domain Routing

An IPv4 IP address is made up of 32 bits:

![ip-address-32-bits](assets/ip-address-32-bits.png)

If we want a representation of all IPs starting with `10.10`, we can use the
CIDR representation as:

![cidr](assets/cidr.png)

!!! note "number of hosts"
    `10.10.0.0/16` will give us a total of `256*256` hosts. Similarly,
    `10.10.0.0/24` will give us a total of `256` hosts.

!!! note "single IPv4 address"
    A single IPv4 address in CIDR notation is: `10.10.101.5/32`.

All Wildcards
---

If we want to represent the entire set of possible IPv4 addresses:

![all-wildcards](assets/all-wildcards.png)
