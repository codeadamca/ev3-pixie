#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.parameters import Color

# Import the Pixy2 library
from pixycamev3.pixy2 import Pixy2

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Connec the Pixy2 to port 1
pixy2 = Pixy2(port=1, i2c_address=0x54)

wait(2000)

# Get version
version = pixy2.get_version()
print('Hardware: ', version.hardware)
print('Firmware: ', version.firmware)

# Get frame resolution
resolution = pixy2.get_resolution()
print('Frame width:  ', resolution.width)
print('Frame height: ', resolution.height)

# Turn upper leds on for 2 seconds, then turn off
pixy2.set_lamp(1, 0)
wait(1000)
pixy2.set_lamp(0, 0)

# Track blocks with signature 1, request just 1 block
while True:

    nr_blocks, blocks = pixy2.get_blocks(1, 1)

    # Extract data of first (and only) block
    if nr_blocks >= 1:

        sig = blocks[0].sig
        x = blocks[0].x_center
        y = blocks[0].y_center
        w = blocks[0].width
        y = blocks[0].height

        print(x,',',y)

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        ev3.light.off()
        break

    wait(500)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
