# servo_calibrate
This is a quick and dirty tool to calibrate servo positioning for object tracking when using Open CV or Dlib libraries.
This tool is designed primarily for the raspberry pi. It assumes the use of python 3.4.2
The motivation behind this tool was to figure out how the servos could be positioned to track an object relative to the screen size and current position of that object. Rather than tackle this issue inside half built object tracker code it was easier to split this off as a side problem to be solved and then ported inside the object tracker once the issues are understood clearly.
Since servos differ and the pan & tilt mounts vary, it can be hard to figure out where to start on this problem and just how to implement tracking of objects in realtime, driving servos and using a camera feed. 
You will need to modify the code particularily the if-then statements variables controlling the postioning relaitve to your screen size and equipment.
Once you have the positioning where you want it, the calibrated if-then statements can be copied from the tool and added to your object tracker project.

# Dependecies
- open cv version 3.2
- imutils
- pigpiod

# A note about pigpiod
The pigpiod Daemon needs to be run first for a few seconds before starting the tracker tool. It could be run from boot if required by modifying the init.d file, I do not since I may need resources for other projects at times so I keep it flexible. The camera I used is a USB logitech 920 not the raspberry pi type hence the bigger servos and mount. 

To start the pigpiod Daemon use:
"> sudo pigpiod"
to stop the Daemon:
"> pkill pigpiod"

