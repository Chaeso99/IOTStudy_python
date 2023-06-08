# Btn_LED.py
import RPi.GPIO as GPIO
import time

button_pin = 15
led_pin = 4

# 불필요한 warning 제거
GPIO.setwarnings(False)
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

#GPIO 10번, 스위치 1번/GPIO 7번, 스위치 9번 (선 4개)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

light_on = False

def button_callback(channel):
	global light_on
	if light_on == False:
		GPIO.output(led_pin, 1)
		print('LED ON!')
	else:
		GPIO.output(led_pin, 0)
		print('LED OFF')
	light_on = not light_on
	
# Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다.
# 300ms 바운스타임을 설정하여 잘못된 신호를 방지합니다.	
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=300)

while 1:
	time.sleep(0.1)
