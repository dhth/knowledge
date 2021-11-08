Mac Battery Helpers
===

Check if charging or discharging
---

```bash
ioreg -r -n AppleSmartBattery | grep IsCharging | cut -c22-
# Yes or No
```

Check charge percentage
---

```bash
pmset -g batt |xargs | sed 's/.*) \([^ ]*\)%.*/\1%/'
# 80%
```
