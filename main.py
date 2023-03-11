#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait
from pybricks.parameters import Color

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        ev3.light.off()
        break

    ev3.light.on(Color.RED)

    wait(500)

    ev3.light.on(Color.GREEN)

    wait(500)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
