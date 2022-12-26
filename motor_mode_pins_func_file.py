import RPi.GPIO as GPIO #for GPIO 
import time  #for timing


def motor_mode_pins_func(i,pin1,pin2,pin3,pin4,sleep_time):
	if i==0:
		GPIO.output(pin1,GPIO.HIGH)
		GPIO.output(pin2,GPIO.LOW)
		GPIO.output(pin3,GPIO.LOW)
		GPIO.output(pin4,GPIO.LOW)
		time.sleep(sleep_time)
                  
	elif i==1:
		GPIO.output(pin1,GPIO.HIGH)
		GPIO.output(pin2,GPIO.HIGH)
		GPIO.output(pin3,GPIO.LOW)
		GPIO.output(pin4,GPIO.LOW)
		time.sleep(sleep_time)
                  
	elif i==2:  
		GPIO.output(pin1,GPIO.LOW)
		GPIO.output(pin2,GPIO.HIGH)
		GPIO.output(pin3,GPIO.LOW)
		GPIO.output(pin4,GPIO.LOW)
		time.sleep(sleep_time)
                  
	elif i==3:    
		GPIO.output(pin1,GPIO.LOW)
		GPIO.output(pin2,GPIO.HIGH)
		GPIO.output(pin3,GPIO.HIGH)
		GPIO.output(pin4,GPIO.LOW)
		time.sleep(sleep_time)
                  
	elif i==4:  
		GPIO.output(pin1,GPIO.LOW)
		GPIO.output(pin2,GPIO.LOW)
		GPIO.output(pin3,GPIO.HIGH)
		GPIO.output(pin4,GPIO.LOW)
		time.sleep(sleep_time)
                  
	elif i==5:
		GPIO.output(pin1,GPIO.LOW)
		GPIO.output(pin2,GPIO.LOW)
		GPIO.output(pin3,GPIO.HIGH)
		GPIO.output(pin4,GPIO.HIGH)
		time.sleep(sleep_time)
                  
	elif i==6:    
		GPIO.output(pin1,GPIO.LOW)
		GPIO.output(pin2,GPIO.LOW)
		GPIO.output(pin3,GPIO.LOW)
		GPIO.output(pin4,GPIO.HIGH)
		time.sleep(sleep_time)
                  
	elif i==7:    
		GPIO.output(pin1,GPIO.HIGH)
		GPIO.output(pin2,GPIO.LOW)
		GPIO.output(pin3,GPIO.LOW)
		GPIO.output(pin4,GPIO.HIGH)
		time.sleep(sleep_time)
