# ch05/PWM_LED.py

import RPi.GPIO as GPIO
import time

# 불필요한 warning 제거
GPIO.setwarnings(False)
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) #6, 12번에 꼽아야됨
# PWM 인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정, 주파수 = 50hz
p = GPIO.PWM(18, 50)
p. start(0)

try:
	while 1:
		for dc in range(0, 101, 5): # dc의 값은 0에서 100까지 5만큼 증가
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
			
			for dc in range(100, -1, -5): # dc의 값은 100에서 0까지 5만큼 감소
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
except KeyboardInterrupt:
	pass
	
p.stop()
GPIO.cleanup()
