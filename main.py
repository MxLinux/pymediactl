import alsaaudio
import dbus
import sys

mixer = alsaaudio.Mixer()
volumelist = mixer.getvolume()
volume = volumelist[0]

bus = dbus.SessionBus()
spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
interface = dbus.Interface(spotify, dbus_interface="org.mpris.MediaPlayer2.Player")

def help():
    print("""Usage:
                -h, --help              Display this help
                -t, --toggle-play       Toggle play/pause
                -p, --previous-track    Previous track
                -s, --skip-track        Skip track
                -m, --toggle-mute       Toggle mute/unmute
                -vu, --volume-up        Increase volume by 5%
                -vd, --volume-down      Decrease volume by 5%""")

def toggle_play():
    interface.PlayPause()

def previous_track():
    interface.Previous()

def skip_track():
    interface.Next()

def toggle_mute():
    mutes = mixer.getmute()
    for i in range(len(mutes)):
        if mutes[i] == 0:
            mixer.setmute(1, i)
        else:
            mixer.setmute(0, i)


def volume_up():
    volume = volumelist[0]
    volume += 5
    if volume < 100:
        mixer.setvolume(volume, 0)
        mixer.setvolume(volume, 1)
    else:
        pass

def volume_down():
    volume = volumelist[0]
    volume -= 5
    if volume > 0:
        mixer.setvolume(volume, 0)
        mixer.setvolume(volume, 1)
    else:
        pass

if len(sys.argv) == 1:
    print("Argument(s) required\n")
    help()
elif len(sys.argv) == 2:
    focusArg = sys.argv[1]
    if focusArg == "-h" or focusArg == "--help":
        help()
    elif focusArg == "-t" or focusArg == "--toggle-play":
        toggle_play()
    elif focusArg == "-p" or focusArg == "--previous-track":
        previous_track()
    elif focusArg == "-s" or focusArg == "--skip-track":
        skip_track()
    elif focusArg == "-m" or focusArg == "--toggle-mute":
        toggle_mute()
    elif focusArg == "-vu" or focusArg == "--volume-up":
        volume_up()
    elif focusArg == "-vd" or focusArg == "--volume-down":
        volume_down()
    else:
        print("Command not supported: " + str(sys.argv[1]) + "\n")
        help()
else: 
    print("Script currently only supports one argument\n")
    help()
