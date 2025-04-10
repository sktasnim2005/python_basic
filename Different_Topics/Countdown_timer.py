import time # Importing the time module

total_time = int(input("Enter the time in seconds: "))

for x in range(total_time,0,-1): # The range function will start from total_time and end at 0 and will decrement by 1
    seconds = x % 60
    minutes = int((x /60) % 60)
    hours = int(minutes / 3600)
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)
    
print("TIME'S UP!")

