Docker Wiki
===

Get container ID from image name
---

```bash
docker ps -qf "name=CONTAINER_IMAGE_NAME" | awk '{print $1}'
```

Select columns in docker ps
---

```bash
docker ps --format "table {{ .ID }}\t{{.Names}}\t{{.Status}}"
# discussion here: https://github.com/moby/moby/issues/7477
```

Docker exec using fzf
---

```bash
function dex() {
  local selected_container
  selected_container=$(docker ps --format "table {{ .ID }}\t{{.Names}}\t{{.Status}}" --last=5 | fzf --height=6 --layout=reverse)

  if [ -n "$selected_container" ]; then
    echo "docker exec -it $(echo $selected_container | head -n1| awk '{print$1;}') /bin/bash"
    docker exec -it $(echo $selected_container | head -n1| awk '{print$1;}') /bin/bash
  fi
}
```

Docker build and run
---

```bash
docker build -f Dockerfile -t project-api:prod .
docker run --rm --name project-prod --env-file ./.current.env -p 5003:80 project-api:prod
docker rm project-prod -f
```

Keep container running
---

Mount a dummy file to the container. Set the entrypoint as:

```
entrypoint: tail -F /path/to/dummy/file.txt
```
