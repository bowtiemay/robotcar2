import RPi.GPIO as GPIO          
import time
import Encoder
from evdev import InputDevice, categorize, ecodes, KeyEvent, InputEvent

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
   

for event in game_pad.read_loop():
        key_event = categorize(event)
        if event.type == ecodes.EV_KEY:
            #print key_event
            if key_event.keystate == KeyEvent.key_down:
                scan_code = key_event.scancode
                if scan_code == 304:  # A
                    print("A")
                elif scan_code == 308:  # Y
                    print ("Y")
                elif scan_code == 305:  # B
                    print ("B")
                elif scan_code == 307:  # X
                    print ("X")
                elif scan_code == 311:  # R1
                    print ("R1")
                elif scan_code == 310:  # L1
                    print ("L1")
                elif scan_code == 314:  # Back
                    print ("Back")
                elif scan_code == 315:  # Start
                    print ("Start")

        if event.type == ecodes.EV_ABS:
            event_code = key_event.event.code
            absevent = categorize(event)
            
            if event_code == 2:
                print ("ABS_Z L2")
            elif event_code == 5:
                print ("ABS_RZ R2")
            elif event_code == 0:
                print ("ABS_X left/right")
            elif event_code == 1:
                if absevent.event.value > -129:
                    print("back")
                elif absevent.event.value < -129:
                    print("forward")
                else:
                    print("stop")
                print(absevent.event.value)
            elif event_code == 3:
                print ("ABS_RX left/right")
            elif event_code == 4:
                print ("ABS_RX up/down")
            elif event_code == 16:
                print ("ABS_HAT0X left/right")
            elif event_code == 17:
                print ("ABS_HAT0Y up/down")






def joystickDriving():
    
    game_pad = InputDevice('/dev/input/event2')

    for event in game_pad.read_loop():
        key_event = categorize(event)
    
        if event.type == ecodes.EV_ABS:
            event_code = key_event.event.code
            absevent = categorize(event)

            if event_code == 4:
                if absevent.event.value > -129:
                    Drive.back(absevent.event.value)
                elif absevent.event.value < -129:
                    Drive.forward(absevent.event.value)
                else:
                    Drive.stop()

            if event_code == 0:
                if absevent.event.value > 128:             
                    Drive.turnRight(absevent.event.value)
                elif absevent.event.value < 128:
                    Drive.turnLeft(absevent.event.value)
                else:
                    Drive.stopServo()

while(1):

    joystickDriving()

    #x = input()
   
    #if x =='s':
        #stop()
    #elif x=='f':
        #forward()
    #elif x=='b':
        #back()
    #elif x=='r':
        #right()
    #elif x=='l':
        #left()
    #elif x == 'servo':
        #moveServo(12)
    #elif x == 'e':
        #GPIO.cleanup()
        #break
   
    #else:
        #print("<<<  wrong data  >>>")
        #print("please enter the defined data to continue.....")