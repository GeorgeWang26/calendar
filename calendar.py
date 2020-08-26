monthLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthTitle = ['January', 'February', 'March', 'April', 'May', 'June', 'Jully', 'August', 'September', 'October', 'November', 'December']
weekDayTitle = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

year = 0
firstDay = 0

def isLeap():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True

            return False

        return True

    return False


def getFirstDay():
    oriYear = 0
    oriJanFirst = 4

    diff = year - oriYear
    diffMinusOne = diff - 1
    fourYears = int(diffMinusOne / 4)
    hundredYears = int(diffMinusOne / 100) - 17
    fourHundredYears = int(diffMinusOne / 400) - 4

    diffDays = diff + fourYears + 1
    
    if year > 1752:
        diffDays = diffDays - hundredYears + fourHundredYears - 11
    
    day = (oriJanFirst + diffDays) % 7
    return day


def printCalendar():
    global firstDay

    print('             ', year, '\n')

    for month in range(12):
        print('            ', monthTitle[month])
        
        for weekDay in weekDayTitle:
            print(weekDay, end = '  ')
        print()

        for i in range(firstDay):
            print('     ', end = '')

        day = 1
        while day <= monthLen[month]:
            print('{:2d}'.format(day), end = '   ')

            firstDay += 1
            if firstDay == 7:
                firstDay = 0
                print()

            if year == 1752 and month == 8 and day == 2:
                day += 11
                
            day += 1
        print('\n')


if __name__ == '__main__':
    year = int(input('which year\'s calendar do you want to get: '))
    print('\n\n')
    firstDay = getFirstDay()

    if isLeap():
        monthLen[1] = 29

    printCalendar()
