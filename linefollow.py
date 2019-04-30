import cv2
import numpy as np
from pymavlink import mavutil


cam = cv2.VideoCapture(0)

master = mavutil.mavlink_connection('udpin:192.168.2.2:14550')

def set_rc_channel_pwm(id, pwm=1500):

    if id < 1:
        print("Channel does not exist.")
        return


    if id < 9:
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,                # target_system
            master.target_component,             # target_component
            *rc_channel_values)                  # RC channel list, in microseconds.

while True:
	ret, orig_frame = cam.read()
	if not ret:
		cam = cv2.VideoCapture(0)
		continue
	frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	low_red = np.array([171, 100, 60])
	up_red = np.array([255, 255, 255])
	mask = cv2.inRange(hsv, low_red, up_red)
	edges = cv2.Canny(mask, 75, 150)

	lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line[0]
			cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

			x = x2 -x1
			y = y2-y1
			if (x < y):
				if (280< x1 > 320):
					set_rc_channel_pwm(3, 1600)
				elif(280 < x1):
					set_rc_channel_pwm(4, 1600)
				elif(320<x1):
					set_rc_channel_pwm(4, 1400)
			elif (y < x):
				set_rc_channel_pwm(3, 1600)



	cv2.imshow('cizgi', frame)
	cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()