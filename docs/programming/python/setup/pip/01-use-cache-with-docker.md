Use cache with docker
===

Setup
---

```Dockerfile
# syntax = docker/dockerfile:1.2
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY projects/api/requirements.txt .
COPY projects/api/requirements-dev.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements-dev.txt -r requirements.txt
```
