# Btn_Polling.py
# Tact 스위치 15번에 연결, 3.3V 핀 연결

import RPi.GPIO as GPIO
import time

button_pin = 15

# 불필요한 warning 제거
GPIO.setwarnings(False)
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정, PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1: #무한반복
	if GPIO.input(button_pin) == GPIO.HIGH:
		print('Button pushed!')
	time.sleep(0.5)
	
