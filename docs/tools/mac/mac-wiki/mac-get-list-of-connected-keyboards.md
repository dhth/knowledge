# Mac Get List of Connected Keyboards

```bash
ioreg -p IOUSB -w0 | sed 's/[^o]*o //; s/@.*$//' | grep -v '^Root.*'
```

This will return a list like

```
AppleT8103USBXHCI
USB2.0 HUB
USB2.0 HUB
IOUSBHostDevice
Das Keyboard
USB Storage
AppleT8103USBXHCI
```

Usage in a KM macro
---

```
KEYBOARDS=$(ioreg -p IOUSB -w0 | sed 's/[^o]*o //; s/@.*$//' | grep -v '^Root.*')
if [[ $KEYBOARDS == *"Das Keyboard"* ]]; then
    exit 0
else
    exit 1
fi
```

Exit code of 1 can be used to cancel a macro.
