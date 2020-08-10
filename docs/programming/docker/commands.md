# Commands

## Get container ID from image name

```bash
docker ps -qf "name=CONTAINER_IMAGE_NAME" | awk '{print $1}'
```
