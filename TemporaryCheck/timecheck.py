import time
import pyttsx
import datetime
current_time = time.strftime('%H:%M:%S')
current_date = time.strftime('%x')
current_date = datetime.datetime.now()
full_date = str(current_date.day) +' '+time.strftime('%A') + ' ' + time.strftime('%B')

Engine = pyttsx.init()
Engine.say('Time is ' + current_time)
#Engine.say('Date is ' + current_date)
Engine.say('The Current is' + full_date)
Engine.runAndWait()