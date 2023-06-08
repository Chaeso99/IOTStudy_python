# ch05/PWM_Buzzer.py

import RPi.GPIO as GPIO
import time

# 불필요한 warning 제거
GPIO.setwarnings(False)
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) #1,6(또는14), 12번에 꼽아야됨
# PWM 인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정, 주파수 = 50hz
p = GPIO.PWM(18, 100)

# 반짝반짝 작은별
Frq = [262, 262, 392, 392, 440, 440, 392, 349, 349, 330, 330, 294, 294, 262, 392, 392
, 349, 349, 330, 330, 294, 392, 392, 349, 349, 330, 330, 293]
speed = 0.5

p. start(10)

try:
	while 1:
		for fr in Frq:
			p.ChangeFrequency(fr)
			time.sleep(speed)
except KeyboardInterrupt:
	pass
	
p.stop()
GPIO.cleanup()
