# servo_calibrate
This is a quick and dirty tool to calibrate servo positioning for object tracking when using Open CV or Dlib libraries.
This tool is designed primarily for the raspberry pi. It assumes the use of python 3.4.2
The driver behind this tool is to locate the servos at a zero offset position mid screen.
Since servos differ and the pan & tilt mounts vary, it can be hard to figure out just how to implement tracking
of objects in realtime, driving servos and using a camera feed. This tool may help. 
You will need to modify the code particularily the if-then statements variables section controlling the postioning relaitve to your screen size and equipment.
Once you have the positioning where you want it, the calibrated if-then statements can be copied from the tool and added to your object tracker project.

# Dependecies
- open cv version 3.2
- imutils
- pigpiod

# A note about pigpiod
The pigpiod Daemon needs to be run first for a few seconds before starting the tracker tool. It could be run from boot if required by modifying the init.d file, I do not since I may need resources for other projects at times so I keep it flexible. The camera I used is a USB logitech 920 not the raspberry pi type hence the bigger servos and mount. 

To start the pigpiod Daemon use:
sudo pigpiod
to stop the Daemon:
pkill pigpiod

