# Hammerspoon Reload Config

```lua
hs.hotkey.bind({"ctrl", "shift", "alt"}, "r", function()
  hs.reload()
end)
hs.alert.show("Config loaded")
```
