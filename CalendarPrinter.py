#Referebce Date is used to calculate Day on specific date
#Reference Date has Monday on starting of the year
referenceDate = [1,1,1979]
DayName = {1:"Mon",2:"Tue",3:"Wed",4:"Thu",5:"Fri",6:"Sat",7:"Sun"}

#Check Leap year
def isLeapYear(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

#Calculates total days in a month of specific year
def daysInMonth(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return -1
def daysInYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365

#Calculates date differece in days
def totalDays(date):
    total = 0
    date_year = int(date[2])
    date_month = int(date[1])
    date_day = int(date[0])
    for i in range(referenceDate[2],date_year):
        total += daysInYear(i)
    for i in range(referenceDate[1],date_month):
        total += daysInMonth(i,date_year)
    total += date_day - 1
    return total
def dayOnDate(date):
    d = totalDays(date) % 7 + 1
    if d > 7:
        return d - 7
    else:
        return d
        
#Print given month of a given year
def printMonth(month,year):
    date = [1,month,year]
    day = dayOnDate(date)
    
    if day >= 1 and day <= 7:
        diff = day - 1
        str = " M   T   W   T   F   S   S\n"
        str += "    "*diff
        i = 1
        while i <= daysInMonth(month,year):
            dt = [i,month,year]
            str += f"{i:2d}  "
            if dayOnDate(dt) == 7:
                str += "\n"
            i += 1
        print((str))
        
#Print Calendar of the given year      
def printCalander(year):
    print(f"-----------{year:4d}-----------")
    i = 1
    while i <= 12:
        print(f"------------{i:02d}------------")
        printMonth(i,year)
        i += 1
        
        
#Input For Year        
year = int(input("Enter Year: "))
printCalander(year)