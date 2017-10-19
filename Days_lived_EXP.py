def nextDay(year, month, day):
	
	if day <30:
		return year, month, day + 1
	else:
		if month < 12:
			return year, month +1, 1
		else:
			return year + 1, 1, 1


def dateIsBefore(year1,month1,day1,year2,month2,day2):
	if year1 < year2:
		return True
	elif year1 <= year2 and month1 < month2:
		return True
	if year1 <= year2 and month1 <= month2 and day1 < day2:
		return True
	else:
		return False
"""
def dateIsBefore(year1,month1,day1,year2,month2,day2):
	if year1 < year2:
		return True
	if year1==year2:
		if month1<month2:
			return True
		if month1 == month2:
			return day1 < day2
	return False
"""	

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    assert not dateIsBefore(year2,month2,day2,year1,month1,day1)
    days=0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1=nextDay(year1,month1,day1)
        days+=1
    return days
    


print daysBetweenDates(2015,12,3,2017,12,3)


