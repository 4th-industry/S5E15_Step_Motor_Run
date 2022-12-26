import RPi.GPIO as GPIO #for GPIO 



def init_pins_func(pin1,pin2,pin3,pin4):
	GPIO.output(pin1,GPIO.LOW)
	GPIO.output(pin2,GPIO.LOW)
	GPIO.output(pin3,GPIO.LOW)
	GPIO.output(pin4,GPIO.LOW)
