import RPi.GPIO as GPIO          
import time
import Encoder

in1 = 24
in2 = 23
in3 = 22
in4 = 27
enA = 12
enB = 17

leftMotorEncoderA = 13
leftMotorEncoderB = 19
rightMoterencoderA = 5
rightMoterencoderA = 6

servo = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.setup(servo, GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


pwmEna = GPIO.PWM(enA,1000)
pwmEnb = GPIO.PWM(enB,1000)

pwmServo = GPIO.PWM(servo, 50)

pwmEna.start(50)
pwmEnb.start(50)

pwmServo.start(0)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

def changeSpeed(speed):

    pwmEna.ChangeDutyCycle(speed)
    pwmEnb.ChangeDutyCycle(speed)

def forward(joystickValue):
   
    print("forward")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    x='z'
    speed = map(joystickValue, -2768, -129, 100, 0)
    
    changeSpeed(speed)

    print(speed)

def back():
   
    print("backward")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

    speed = map(joystickValue, 32767, -129, 100, 0)

    changeSpeed(speed)

    print(speed)

    x='z'
   
def right():

    print("right")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    x='z'

def left():

    print("left")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    x='z'

def stop():
   
    print("stop")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    x ='z'
   
def lowspeed():

    print("lowspeed")
    pwmEna.ChangeDutyCycle(50)
    pwmEnb.ChangeDutyCycle(50)
    x='z'

def meduimspeed():
   
    print("meduimspeed")
    pwmEna.ChangeDutyCycle(75)
    pwmEnb.ChangeDutyCycle(75)
    x='z'
   
def highspeed():
   
    print("highsped")
    pwmEna.ChangeDutyCycle(100)
    pwmEnb.ChangeDutyCycle(100)
    x='z'
   
def moveServo(percent):
    print("moving servo clockwise")
    pwmServo.ChangeDutyCycle(percent)
   

while(1):

    x = input()
   
    if x =='s':
        stop()
    elif x=='f':
        forward()
    elif x=='b':
        back()
    elif x=='r':
        right()
    elif x=='l':
        left()
    elif x == 'servo':
        moveServo(12)
    elif x == 'e':
        GPIO.cleanup()
        break
   
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")