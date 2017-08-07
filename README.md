# servo_calibrate
This is a quick and dirty tool to calibrate servo positioning for object tracking when using Open CV or Dlib libraries.
The driver behind this tool is to locate the servos at a zero offset position mid screen.
Since servos differ and the pan & tilt mounts vary and it can be hard to figure out just how to implement tracking
of objects in realtime driving servos using a camera feed. This tool may help. 
You will need to modify the code particularily the if-then statements section controlling the postioning relaitve to your screen size and equipment.
Once you have the positioning where you want it, the calibrated if-then statements can be copied from the tool and added to your object tracker project.
