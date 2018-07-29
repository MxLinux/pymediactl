# pymediactl
It's like mediactrl, but with Python
Requires `python-pyalsa`

Currently sends spotify commands with Popen(), because Python's dbus is giving me issues, namely:
`"dbus.exceptions.DBusException: org.freedesktop.DBus.Error.ServiceUnknown: The name org.mpris.MediaPlayer2.spotify was not provided by any .service files"`
