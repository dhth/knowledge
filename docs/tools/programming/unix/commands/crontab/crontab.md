# crontab

Stands for cron table.

Format
---

```bash
* * * * * cd some_dir && python somefile.py
```

Create a new crontab
---

```bash
crontab -e
```

Remove current crontab
---

```bash
crontab -r
```

Schedules
---

Every minute

```bash
* * * * *
```

Every 5 minutes

```bash
*/5 * * * *
```

