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

