AWS Lambda Docker Image Function
===

Setup
---

Get up and running with a lambda function running a docker image.

Directory structure:

```
.
├── __init__.py
├── app.py
├── cdk.json
├── cdk_code
│   ├── __init__.py
│   └── lambda_service.py
├── project
│   ├── Dockerfile.dev
│   ├── Dockerfile.prod
│   ├── docker-compose.yml
│   └── project
│       ├── __init__.py
│       ├── app
│       │   ├── __init__.py
│       │   ├── process_file.py
│       └── requirements.txt
├── pyproject.toml
├── requirements-cdk.txt
├── requirements-dev.txt
└── tox.ini
```

Lambda handler
---

`process_file.py`

```python
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "event": event,
            }
        ),
    }
```
Using docker run
---

`Dockerfile.prod`

```
# syntax = docker/dockerfile:1.2
FROM public.ecr.aws/lambda/python:3.8

RUN pip install --upgrade pip
COPY ./project/requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

COPY ./project/* ${LAMBDA_TASK_ROOT}/

```

Might need to be authorized to be able to pull the base image. (the region has
to be `us-east-1`)

```bash
aws ecr-public get-login-password \
    --region us-east-1 | \
    docker login --username AWS \
    --password-stdin public.ecr.aws
```

Docker build:

```bash
docker build -t lambda-function:dev -f Dockerfile .
```

Docker run:

```bash
docker run \
    --env AWS_ACCESS_KEY_ID="$(aws configure get default.aws_access_key_id)" \
    --env AWS_SECRET_ACCESS_KEY="$(aws configure get default.aws_secret_access_key)" \
    --env AWS_SESSION_TOKEN="$(aws configure get default.aws_session_token)" \
    --env AWS_REGION="$(aws configure get default.region)" --env AWS_DEFAULT_REGION="$(aws configure get default.region)" \
    -p 9080:8080 \
lambda-function:dev process_file.lambda_handler
```

Using docker-compose (easier)
---

`Dockerfile.dev`

```
# syntax = docker/dockerfile:1.2
FROM public.ecr.aws/lambda/python:3.8

RUN pip install --upgrade pip
COPY ./project/requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt
```

`docker-compose.yml`

```yaml
version: '3.8'

services:
  momentum-etl:
    build:
      context: .
      dockerfile: Dockerfile.dev
    command: 'process_file.lambda_handler'
    env_file: .env
    image: lambda-docker:dev
    volumes:
      - ~/.pdbrc.py:/root/.pdbrc.py
      - ~/.pdbrc:/root/.pdbrc
      - ./project/app/:/var/task/app/
      - ./tmp/:/tmp/
    ports:
      - 9080:8080
    stdin_open: true
    tty: true
```

Use `docker-compose up -d` and `docker-compose restart` will work fine.

Invoke container
---

```bash
curl -s "http://localhost:9080/2015-03-31/functions/function/invocations" -d '{"some_key":"some_value"}' | jq
```

Response:

```json
{
  "statusCode": 200,
  "body": "{\"event\": {\"some_key\": \"some_value\"}}"
}
```

CDK
---

CDK code to create a lambda function running a docker image:

```python
process_file_function = _lambda.DockerImageFunction(
    self,
    construct_id,
    code=_lambda.DockerImageCode.from_image_asset(
        path.join(this_dir, "../project"),
        cmd=["process_file.lambda_handler"],
        entrypoint=["/lambda-entrypoint.sh"],
        file="Dockerfile.prod",
    ),
    description="Description",
    memory_size=256,
    timeout=cdk.Duration.seconds(300),
    environment={
        "KEY": "value",
    },
)
```
