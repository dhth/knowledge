Debugging Celery
===

Debugging dockerized celery services is not as straightforward as debugging
simple python services. One issue is that the normal `breakpoint()` doesn't work
for celery. The other issue is that celery doesn't come with a `auto-reload`
feature, the same way frameworks like `flask` do.

So, we need to do a couple of things to make debugging celery docker services
easier:

- use celery's own remote debugger.
- open up the ports the debugger generally listens to
- use an external hot reloading tool

Changes to docker-compose.yml
---

```yaml
stdin_open: true
tty: true
ports:
	- 6900-7000:6900-7000
environment:
	- CELERY_RDB_HOST=0.0.0.0. # to be able to telnet from outside the container
	- PYTHONUNBUFFERED=1       # any non-empty string will do
```

Hot reloading celery
---

```
pip install watchdog
```

Instead of running celery directly like `celery worker --app=...`, run it
indirectly using `watchmedo`:

```bash
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery \
worker --app=...
```

More [:fontawesome-solid-link:
here](https://www.distributedpython.com/2019/04/23/celery-reload/).

Add breakpoints in code
---
Add a breakpoint using:

```python
from celery.contrib import rdb

# SOME PYTHON CODE
rdb.set_trace()
# SOME MORE PYTHON CODE
```

More [:fontawesome-solid-link:
here](https://docs.celeryproject.org/en/stable/reference/celery.contrib.rdb.html).

Running containers
---

Unfortunately, celery's `rdb` doesn't work with `docker-compose up`. There seems
to be an issue with the way service ports are exposed via `up`. More on that
[:fontawesome-solid-link: here](https://github.com/docker/compose/issues/4677).

Run the service using `docker-compose run`.

```bash
docker-compose run --service-ports celery
```

Using the debugger
---

Invoke breakpoint. On invocation, remote debugger will take over: `Remote
debugger:<PORT>: Ready to connect: telnet 0.0.0.0 <PORT>`. It's important that
the debugger is listening on `0.0.0.0` as it will enable us to connect to it
from outside the container.

```bash
telnet localhost <PORT>
```
