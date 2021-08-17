def add_time(start, duration, day = None):

    #Find out if optional arg is default
    if day is add_time.__defaults__[0]:
        default = True
        day = "Sunday"
    else: default = False

    #Convert optional day to lowercase, set up array, get start day as integer
    day = day.lower()
    daysArr = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    dayInt = daysArr.index(day)
    
    #store start time as 3 different vars
    hourStart = start.split(" ")[0].split(":")[0]
    minuteStart = start.split(" ")[0].split(":")[1]
    ampm = start.split(" ")[1]
    
    #Convert hourStart to 24-hour format
    if ampm == "PM" and hourStart != "12":
        hourStart = int(hourStart) + 12
    elif ampm == "AM" and hourStart == "12":
        hourStart = int(hourStart) - 12
    
    #store duration as 2 different vars
    hourDur = duration.split(":")[0]
    minuteDur = duration.split(":")[1]

    #Add duration to start time
    hourEnd = int(hourStart) + int(hourDur)
    minuteEnd = int(minuteStart) + int(minuteDur)

    #Check if minuteEnd is >60
    if minuteEnd >= 60:
        hourEnd += 1
        minuteEnd -= 60

    #Find num numDays later, final day index, hour and minute of day
    numDays = hourEnd // 24
    dayInt += numDays
    dayInt = dayInt % 7
    weekday = daysArr[dayInt]
    hour24Final = hourEnd % 24

    #Convert back to 12-hour time
    if hour24Final < 12:
        ampmFinal = "AM"
    else: ampmFinal = "PM"

    if hour24Final == 0:
        hour12Final = 12
    elif hour24Final > 12:
        hour12Final = hour24Final - 12
    else: hour12Final = hour24Final

    if numDays == 1:
        dayText = " (next day)"
    elif numDays > 1:
        dayText = " (" + str(numDays) + " days later)"
    else: dayText = ""
    
    #zfill learned from https://www.kite.com/python/answers/how-to-add-leading-zeros-to-a-number-in-python | Takes number of digits as argument and fills with leading zeros
    #If optional argument is defaulted, suppress weekday text in output
    if default:
        #print(str(hour12Final) + ":" + str(minuteEnd) + " " + ampmFinal + dayText)
        return str(hour12Final) + ":" + str(minuteEnd).zfill(2) + " " + ampmFinal + dayText
    else: 
        #print(str(hour12Final) + ":" + str(minuteEnd) + " " + ampmFinal + ", " + weekday.capitalize() + dayText)
        return str(hour12Final) + ":" + str(minuteEnd).zfill(2) + " " + ampmFinal + ", " + weekday.capitalize() + dayText

add_time("8:16 PM", "466:02")