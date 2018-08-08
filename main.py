import alsaaudio
import dbus
import sys

mixer = alsaaudio.Mixer()
volumelist = mixer.getvolume()
volume = volumelist[0]

bus = dbus.SessionBus()
spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
interface = dbus.Interface(spotify, dbus_interface="org.mpris.MediaPlayer2.Player")

short_list = ["-h", "-t", "-p", "-s", "-m", "-vu", "-vd"]
long_list = ["--help", "--toggle-play", "--previous-track", "--skip-track", "--toggle-mute", "--volume-up", "--volume-down"]

def get_help():
    print("""Usage:
    -h, --help              Display this help
    -t, --toggle-play       Toggle play/pause
    -p, --previous-track    Previous track
    -s, --skip-track        Skip track
    -m, --toggle-mute       Toggle mute/unmute
    -vu, --volume-up        Increase volume by 5%
    -vd, --volume-down      Decrease volume by 5%

It is possible to use multiple flags, space separated.""")

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

def action(argv_item):
    if argv_item == short_list[0] or argv_item == long_list[0]:
        get_help()
    elif argv_item == short_list[1] or argv_item == long_list[1]:
        toggle_play()
    elif argv_item == short_list[2] or argv_item == long_list[2]:
        previous_track()
    elif argv_item == short_list[3] or argv_item == long_list[3]:
        skip_track()
    elif argv_item == short_list[4] or argv_item == long_list[4]:
        toggle_mute()
    elif argv_item == short_list[5] or argv_item == long_list[5]:
        volume_up()
    elif argv_item == short_list[6] or argv_item == long_list[6]:
        volume_down()
    else:
        print("Invalid argument: " + argv_item + "\n")
        get_help()

if len(sys.argv) == 1:
    print("Argument(s) required\n")
    get_help()
elif len(sys.argv) == 2:
    action(sys.argv[1])
else:
    for x in range(len(sys.argv)):
        current_arg = sys.argv[x]
        if current_arg in short_list or current_arg in long_list:
            print("Do " + current_arg)
            action(current_arg)

        else:
            print("Invalid option", str(sys.argv[x]))