import sys
class clockTime:
    def __init__(self):
        self.hours = 0
        self.min = 0
        self.sec = 0

    def __setHours(self, hours):
        print("Setting hour to: " + str(hours))
        self.hours = hours

    def __setMinutes(self, minutes):
        print("Setting minutes to: " + str(minutes))
        self.min = minutes

    def __setSeconds(self, seconds):
        print("Setting seconds to: " + str(seconds))
        self.sec = seconds

    def setTime(self, hours,minutes,seconds):
        self.__setHours(hours)
        self.__setMinutes(minutes)
        self.__setSeconds(seconds)

    def clear(self):
        print("Resetting clock...")
        self.hours = 0
        self.min = 0
        self.sec = 0

    def showTime(self):
        print(f"{self.hours:02d}:{self.min:02d}:{self.sec:02d}")
hours = -1
mins = -1
secs = -1

while hours not in range(24):
    try:
        hours = int(input("Enter Hours: "))
        if hours not in range(24):
            print("ERROR: Invalid hour")
    except:
        print("Invalid input")
        sys.exit("Exiting...")
    
while mins not in range(60):
    try:
        mins = int(input("Enter Minutes: "))
        if mins not in range(60):
            print("ERROR: Invalid minutes")
    except:
        print("Invalid input")
        sys.exit("Exiting...")
    
while secs not in range(60):
    try:
        secs = int(input("Enter Seconds: "))
        if secs not in range(60):
            print("ERROR: Invalid seconds")
    except:
        print("Invalid input")
        sys.exit("Exiting...")
        
test = clockTime()
test.setTime(hours,mins,secs)
test.showTime()
test.clear()
test.showTime()
