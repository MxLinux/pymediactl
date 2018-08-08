# pymediactl
It's like mediactrl, but with Python

Requires [`pyalsaaudio`](https://github.com/larsimmisch/pyalsaaudio)

Assign this script, with arguments, to a keybinding for quick control of audio levels/spotify.

# Usage
Call the script using `python /path/to/pymediactrl/main.py [options]`

Available options:
```
    -h, --help              Display this help
    -t, --toggle-play       Toggle play/pause
    -p, --previous-track    Previous track
    -s, --skip-track        Skip track
    -m, --toggle-mute       Toggle mute/unmute
    -vu, --volume-up        Increase volume by 5%
    -vd, --volume-down      Decrease volume by 5%
```

It is possible to use multiple flags, space separated.
Whether or not that's practical is a question for another time.
