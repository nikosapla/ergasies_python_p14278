import calendar

try:
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	d, m, y = map(int, raw_input("Enter a date: ").split('/'))
	weekday = calendar.weekday(y, m, d)
	print days[weekday] 
	
except:
	print "error, the correct date is d/m/yyyy"
