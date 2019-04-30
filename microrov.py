import time
import RPi.GPIO as GPIO
import keyboard
import pigpio
relay_pin = 23 # role pin
motor = 4 # motor pin 

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(relay_pin, GPIO.OUT) # GPIO Assign mode
pi = pigpio.pi() # Connect to local Pi.



durum = 3
while True:
    tus = input("")
    if tus == "1":
    	durum = 1
    elif tus == "2":
    	durum = 0
    if (durum == 1):
    	print("Aydinlatma Aktif")
    	GPIO.output(relay_pin, GPIO.LOW) # out
    elif(durum == 0):
    	print("Aydinlatma Deaktif")
    	GPIO.output(relay_pin, GPIO.HIGH) # on

    elif tus == "6":
    	pi.set_servo_pulsewidth(SERVO, 1600) # Maximum throttle.
    	print("ileri gidiliyor")
    	time.sleep(3)
    elif tus == "3":
    	pi.set_servo_pulsewidth(SERVO, 1400) # Maximum throttle.
    	print("geri gidiliyor")
    	time.sleep(3)


   