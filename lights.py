import datetime
import time
import RPi.GPIO as GPIO

runnning = 1
hours = [23, 18, 15, 14]
mins = [4, 17, 27, 22, 10, 9]
secs = [11, 5, 6, 13, 19, 26]


def setuppins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BOARD)
    for x in hours:
        GPIO.setup(x, GPIO.OUT)
        print('Enabling GPIO PIN: ' + str(x))

    for y in mins:
	GPIO.setup(y, GPIO.OUT)
        print('Enabling GPIO PIN: ' + str(y))

    for z in secs:
        GPIO.setup(z, GPIO.OUT)
        print('Enabling GPIO PIN: ' + str(z))
        

def updatetime(types):
    currentTime = datetime.datetime.now().time()
    currentTime = currentTime.strftime(types)
    timeOutput = int(currentTime)
    #print(timeOutput)
    return timeOutput


def inbinary(type):
    currenttime = updatetime(type)
    if type == '%I':
	binary = [0,0,0,0]
    else:
	binary = [0,0,0,0,0,0]
    counter = 0
    while currenttime:
        remainder = currenttime % 2
        currenttime = int(currenttime / 2)
        binary[counter] = remainder
        counter += 1
    return binary[::-1]


def updatesecs():
    i = 0
    binarytime = inbinary('%S')
    for i in range(-1, 5):
        GPIO.output(secs[i], binarytime[i])
        i += 1
    #print(binarytime)

def updatemins():
    i = 0
    binarytime = inbinary('%M')
    for i in range(-1, 5):
        GPIO.output(mins[i], binarytime[i])
        i += 1
    #print(binarytime)

def updatehours():
    i = 0
    binarytime = inbinary('%I')
    for i in range(-1, 3):
	GPIO.output(hours[i], binarytime[i])
	i += 1

def updateclock():

    updatesecs()
    updatemins()
    updatehours()

setuppins()

while runnning:
    updateclock()
#    time.sleep(1)
