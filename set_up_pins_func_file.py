import RPi.GPIO as GPIO #for GPIO 



def set_up_pins_func(pin1,pin2,pin3,pin4):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin1,GPIO.OUT)
	GPIO.setup(pin2,GPIO.OUT)
	GPIO.setup(pin3,GPIO.OUT)
	GPIO.setup(pin4,GPIO.OUT)
