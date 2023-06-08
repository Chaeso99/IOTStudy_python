# HC_SR40.py
# 2, 16, 18, 6또는 20번

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
print('거 리 측 정 중')

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print('센서 안정화 대기 중')
time.sleep(2)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
			
		while GPIO.input(ECHO)==0:
			start = time.time()
		while GPIO.input(ECHO)==1:
			stop = time.time()
				
		check_time = stop-start
		distance = check_time * 34300 / 2
		print('거리 : %.1f cm' % distance)
		time.sleep(0.4) #0.4초 간격으로 센서 측정
except:
	print('측 정 종 료')
	GPIO.cleanup()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
 
