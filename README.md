# gpioconfig

This project is a small Python library that allows to check whether a pair of GPIO pins
on the Raspberry Pi are shorted.

It can be used in combination with jumpers to change the configuration of the Pi on boot.

I use it because I use my Pi in different locations that require different network
configurations, for instance sometimes I want it to act as a WiFi access point, and
sometimes as a client, sometimes I want it to connect to my VPN and redirect all traffic
through it, sometimes not, and so on. This library allows me to control this behaviour
simply by putting a few jumpers on the GPIO pins, without having to log into the Pi
(which requires a serial cable if it has no network connection...)

### Usage

This module requires the `RPi.GPIO`module to be installed (it is present by default in
Raspbian). As all programs interacting with GPIO pins, python must be run as root when
using this module.

Then use the `get_status` function to get the state of a pair:
```python
import gpioconfig as gc
shorted = gc.get_status(pair_number)
```

`pair_number` must be one of the following:
+ `1` for pins number (39, 40) (the closest to the USB ports)
+ `2` for pins number (37, 38)
+ `3` for pins number (35, 36)
+ `4` for pins number (33, 34)
+ `5` for pins number (31, 32)
+ `6` for pins number (29, 30)

You can have a look at the `example.py` script, that runs a command if a given pair is
connected, and a different one otherwise. Example run:
```shell
$ sudo python example.py 1 'echo "Pair 1 is connected!"' 'echo "Pair 1 is not connected"'
Pair 1 is connected!
```

