Hasura Run on Another Machine
===

Use case: Run hasura on a machine, and then access the web console via the
browser using the IP of the machine. (Reason: hasura doesn't work well at the
moment on M1 machines)

Find IP using `ifconfig`. Say it's `192.168.178.50`

Run graphql engine on the machine locally.

```bash
hasura console \
    --address 192.168.178.50 \
    --console-port 9695 \
    --endpoint "http://192.168.178.50:8080"
```

Open `http://192.168.178.50:9695/console` on another machine connected to the
same local network.
