import RPi.GPIO as GPIO #for GPIO 
import time  #for timing

pin1 = 11 #GPIO 17
pin2 = 7 #GPIO 4
pin3 = 13 #GPIO 27
pin4 = 8 #GPIO 14

i=0
positive=0
negative=0
y=0
sleep_time=0.0005 #you have to adjust this for different size of step motors
limit=2000 # this limit the spinning angle

from set_up_pins_func_file import set_up_pins_func

set_up_pins_func(pin1,pin2,pin3,pin4)



print ("Enter negative integer for clock-wise turn. Positive integer for conter clock-wise turn.....")


from init_pins_func_file import init_pins_func
from motor_mode_pins_func_file import motor_mode_pins_func
try:
   while(1):
         
      init_pins_func(pin1,pin2,pin3,pin4) #initialize motor pins to all zero

      xi = input()
      x=int(xi)
      if x>0 and x<=limit:
          for y in range(x,0,-1): #range(start, stop, step)
              if negative==1:
                  if i==7:
                      i=0
                  else:
                      i=i+1
                  y=y+2
                  negative=0
              positive=1
              
              motor_mode_pins_func(i,pin1,pin2,pin3,pin4,sleep_time)
                  
              if i==7:
                  i=0
                  continue
              i=i+1
      
      
      elif x<0 and x>=-limit:
          x=x*-1
          for y in range(x,0,-1):
              if positive==1:
                  if i==0:
                      i=7
                  else:
                      i=i-1
                  y=y+3
                  positive=0
              negative=1
              
              motor_mode_pins_func(i,pin1,pin2,pin3,pin4,sleep_time)
              
              if i==0:
                  i=7
                  continue
              i=i-1 

              
except KeyboardInterrupt:
    GPIO.cleanup()
