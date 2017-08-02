import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#servo pin
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)

#turn the lock first!
p.start(2.5)

#button pin
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#led pin
GPIO.setup(15, GPIO.OUT)


try:
	while True:
		input_state = GPIO.input(13)
    		if input_state == False:
        		print('Button Pressed')
			#LED on
			GPIO.output(15,GPIO.HIGH)        		
			time.sleep(0.2)

			p.ChangeDutyCycle(7.5)
			time.sleep(1)
			p.ChangeDutyCycle(2.5)
			time.sleep(3)
			#p.ChangeDutyCycle(12.5)
			#time.sleep(1)

			#LED off
			GPIO.output(15, GPIO.LOW)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
