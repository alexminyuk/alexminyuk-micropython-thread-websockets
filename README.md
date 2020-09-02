# ESP32 micropython websockets and read analog values using _threads

The idea is to connect a led strip to the esp32 board and manually read 3 potentiometers to change the color of the leds or to be able to change them by websockets.

## How send the program to the board with rshell:

* rshell --port com4 (windows)
* rshell -p /dev/ttyUSB0 (linux)
* rsync . /pyboard

by @dhylands -
https://github.com/dhylands/rshell

# Library uwebsockets:
by @danni -
https://github.com/danni/uwebsockets

Board: ESP32-WROVER-B

![alt text](https://m.media-amazon.com/images/I/71dik06NObL._AC_UL320_.jpg)
