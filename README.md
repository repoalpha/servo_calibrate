# servo_calibrate
This is a quick and dirty tool to calibrate servo positioning for object tracking when using Open CV or Dlib libraries.
This tool is designed primarily for the raspberry pi. It assumes the use of python 3.4.2
The motivation behind this tool was to figure out how pwm servos could be positioned to track an object relative to the screen size and current position of that object. Rather than tackle this issue inside half built object tracker code it was easier to split this off as a side problem to be solved and then ported inside the object tracker once the issues are understood clearly. The problem was tackled using a zero offset from dead centre as marked on the screen. The motors are then started at a zero position of exactly facing front for the pan motor and exactly dead level for the tilt motor. Once we have this set we move the motors relative to the start postion as an offset as indicated by the numbers displayed. These numbers where derived by the servos maximum and minimum useful positions. Driving the motors to the extreme can cause issues and you could strip the gears so 'useful' means exactly that as the pan/tilt mount places limits on what can be achieved.

Since servos differ and the pan & tilt mounts vary, it can be hard to figure out where to start on this problem and just how to implement tracking of objects in realtime, driving pwm servos and using a camera feed. 
You will need to modify the code particularily the if-then statements variables controlling the postioning relaitve to your screen size and equipment.
Once you have the positioning where you want it, the calibrated if-then statements can be copied from the tool and added to your object tracker project.

# Dependencies
- open cv version 3.2
- imutils
- pigpiod

# A note about pigpiod
The pigpiod Daemon needs to be run first for a few seconds before starting the calibrate tool. This Daemon is used in place of the Rpi.gpio module normally used as the servo jitter is herendous. You can leave the pipiod Daemon running the same can't be said for the native pwm used by the pi. Pigpoid could be run from boot if required by modifying the init.d file, I do not since I may need resources for other projects at times so I keep it flexible. The camera I used is a USB logitech 920 not the raspberry pi type hence the bigger servos and mount. 

To start the pigpiod Daemon use:
> sudo pigpiod

To stop the Daemon:
> pkill pigpiod

# The hardware
I used the Hitech HS-645 servos and a SPT-100 pan & tilt mount with the matching HS-645 motor brackets to hold the pan motor to a base board.
