Cloudfront Caching
===

Resources
---

- [Troubleshoot issues with CloudFront custom object caching][1]

<!-- Links -->
[1]: https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-custom-object-caching/

<!-- Links end -->


X-Cache-Header
---

If the X-Cache header is "Hit from cloudfront" or "RefreshHit from cloudfront," then the request was served from the cache of the edge location.

If the X-Cache header is "Miss from cloudfront," then the request was retrieved
from the origin and wasn't served by the cache.
