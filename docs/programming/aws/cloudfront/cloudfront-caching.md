# Cloudfront Caching

Resources
---

- [Troubleshoot issues with CloudFront custom object caching][1]
- [Managing how long content stays in the cache (expiration) - Amazon CloudFront][2]

<!-- Links -->
[1]: https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-custom-object-caching/
[2]: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html

<!-- Links end -->


X-Cache-Header
---

If the X-Cache header is "Hit from cloudfront" or "RefreshHit from cloudfront," then the request was served from the cache of the edge location.

If the X-Cache header is "Miss from cloudfront," then the request was retrieved
from the origin and wasn't served by the cache.
