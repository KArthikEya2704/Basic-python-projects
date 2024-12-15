import time
import datetime
import winsound  

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("Wake up! It's time!")
            
            for _ in range(5):  
                winsound.Beep(440, 1000)  
            break
        time.sleep(1)  
alarm_time = input("Enter the alarm time in HH:MM:SS format (24-hour): ")

try:
    datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    set_alarm(alarm_time)
except ValueError:
    print("Invalid time format. Please use HH:MM:SS format.")
