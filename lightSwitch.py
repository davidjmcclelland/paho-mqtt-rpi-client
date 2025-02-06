from time import sleep
import RPi.GPIO as GPIO
import lightStatus as lStatus

delay = 0.4
inPin = 40
outPin = 38
cachedStatus = -1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
try:
    while True:
        readVal = GPIO.input(inPin)
        print(f"readVal: `{readVal}`") #1
        status = 1-readVal
        print(f"cachedStatus: `{cachedStatus}` status: `{status}`")
        GPIO.output(outPin,status)
        if cachedStatus != status or cachedStatus == -1:
            lStatus.run(status)
            cachedStatus = status
        # update MQTT lightStatus
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO clean')