# for Raspberry Pi3 using python 3.4
# make sure pigpiod daemon is started with sudo pigpiod
# This tool is used to calibrate opencv and camera to servo motors
# The servo's used are Hitech HS-645 MG using SPT-100 pan tilt assembly
import cv2  # import opencv - in this case version 3.2
import imutils  # image utilities
import pigpio  # library that uses DMA to generate timed pulse train

pigpio.exceptions = False
pi = pigpio.pi()
pi.set_PWM_frequency(17, 100)  # pin 12 'Pan' on Pi-3 set Freq to 100hz
pi.set_PWM_frequency(18, 100)  # pin 18 'Tilt' on Pi-3 set Freq to 100hz


def nothing(x):  # blank argument needed by cv2.createTrackbar
    pass


tilt_min = 900  # minimum tilt servo pulse
tilt_max = 2300  # maximum pan servo pulse
pan_min = 500  # minimum anticlockwise - pan left
pan_max = 2500  # maximum clockwise - pan right
tilt_level = 1306  # set camera level
pan_front = 1616  # set camera to front
# what is 'front'? the 'HS-645 part sticker on bottom pan servo is facing you!

cv2.namedWindow('image')
cv2.createTrackbar('Tilt', 'image', tilt_min, tilt_max, nothing)
cv2.createTrackbar('Pan', 'image', pan_min, pan_max, nothing)
cv2.setTrackbarPos('Tilt', 'image', tilt_level)  # start at level position
cv2.setTrackbarPos('Pan', 'image', pan_front)  # start at front position
camera = cv2.VideoCapture(0)

#  If Camera Device is not opened, exit the program
if not camera.isOpened():
    print("Video device or file couldn't be opened")
    exit()


while True:
    # grab the current frame
    (grabbed, frame) = camera.read()
    frame = imutils.resize(frame, width=640)  # set display width
    XFrameCenter = int(float(camera.get(cv2.CAP_PROP_FRAME_WIDTH)) / 2.0)
    YFrameCenter = int(float(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) / 2.0)
    cv2.rectangle(frame, (int(XFrameCenter+100), int(YFrameCenter-75)),
                  (int(XFrameCenter-100), int(YFrameCenter+75)),
                  (255, 0, 0), 2)  # draw box
    cv2.circle(frame, (int(XFrameCenter), int(YFrameCenter)), 3,
               (0, 255, 255), -1)  # put a dot in the centre of the screen
    tilt = cv2.getTrackbarPos('Tilt', 'image')
    pan = cv2.getTrackbarPos('Pan', 'image')

    if tilt >= 900:  # furtherest facing up it will go

        pi.set_servo_pulsewidth(18, tilt)
    if tilt > 900 and tilt <= 1306:  # At value 1306 tilt is dead level
        y = 1306 - tilt
        Y = str(-y)
        cv2.putText(frame, Y, (XFrameCenter, YFrameCenter-50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
    if tilt > 1306 and tilt <= 2300:  # At value 1306 tilt is dead level
        y = tilt - 1306
        Y = str(y)
        cv2.putText(frame, Y, (XFrameCenter, YFrameCenter-50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
    if pan > 500:
        pi.set_servo_pulsewidth(17, pan)
    if pan > 500 and pan <= 1616:  # At value 1306 tilt is dead level
        x = 1616 - pan
        X = str(-x)
        cv2.putText(frame, X, (XFrameCenter, YFrameCenter+50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
    if pan > 1616 and pan <= 2500:  # At value 1306 tilt is dead level
        x = pan - 1616
        X = str(x)
        cv2.putText(frame, X, (XFrameCenter, YFrameCenter+50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

    # show the frame to our screen
    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
print("cleaning up")
camera.release()
cv2.destroyAllWindows()
pi.stop
