# HC_SR501.py
# 열 감지 센서(PIR센서(HC-SR501))
# PIR센서와 두개의 LED를 브레드보드에 연결 필요
# VCC(5V)는 2번, GND는 6번, GPIO 20은 38번 GPIO 21은 40번 GPIO 4는17번3.............

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin number
led_R = 20
led_Y = 21
sensor = 4

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_Y, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

print('PIR Ready...')
time.sleep(5)

try:
	while True:
		if GPIO.input(sensor)==1:
			GPIO.output(led_Y, 1) # yellow on
			GPIO.output(led_R, 0) # red off
			print('Motion Detected')
			time.sleep(0.2)
			
		if GPIO.input(sensor)==0:
			GPIO.output(led_R, 1) # red on
			GPIO.output(led_Y, 0) # yellow off
		
except KeyboardInterrupt:
	print:('Stopped by User')
	GPIO.cleanup()
