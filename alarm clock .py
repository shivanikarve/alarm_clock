import datetime
from signal import alarm
from playsound import playsound
alarmhour=int(input("enter hour"))
alarmmin=int(input("enter min"))
alarmAm=input("am/pm:-")
if alarmAm=="pm":
    alarmhour+=12
elif alarmAm=="am":
    alarmhour-=12
while True:
    if alarmhour==datetime.datetime.now().hour and alarmmin==datetime.datetime.now().minute:
        print("playing sound using  playsound")
        print("playing....")
        playsound('/home/shivani/Downloads/ringtone')
        break
