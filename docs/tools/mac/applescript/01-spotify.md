---
title: "Spotify"
summary:
---

Spotify
===

Commands
---

Play/Pause
---

```AppleScript
tell application "Spotify"
	playpause
end tell
```

Get ID of current track
---

```AppleScript
tell application "Spotify"
	get id of current track
end tell
```

Get url of current track
---

```AppleScript
tell application "Spotify"
	get artwork url of current track
end tell
```

Next/Previous Track
---

```AppleScript
tell application "Spotify"
	next track
end tell
```

`previous` for previous track.

Increase/Decrease Volume
---

```AppleScript
tell application "Spotify"
    set sound volume to sound volume + 5
end tell
```

!!! note "sound volume"
    sound volume property is read only
