# Using flask with celery

Using `url_for` within celery
---

Celery can be configured to use flask app's application_context.

More [here](https://flask.palletsprojects.com/en/1.1.x/patterns/celery/).

However, since `url_for` typically needs a `request_context` (which is always
available in functions that define flask routes), it is not able to build a url
without it.

Flask lets us generate urls in the absence of a request if a `SERVER_NAME`
is configured for the app.

The default url scheme for generating urls in the absence of a request context
is `http`. This can be set to `https` either on a case by case basis by passing
`_scheme='https'` to `url_for`, or by setting the config variable
`PREFERRED_URL_SCHEME` to `https`. More
[here](https://flask.palletsprojects.com/en/1.1.x/config/).

More on the application context [here](https://flask-doc.readthedocs.io/en/latest/appcontext.html#app-context).

More on the request context [here](https://flask-doc.readthedocs.io/en/latest/reqcontext.html).
