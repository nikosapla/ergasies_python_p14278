import pyowm       #Python wrapper around the OpenWeatherMap API
try:
	lat= float(input("enter latitude:"))
	lon= float(input("enter longitude:"))
	owm = pyowm.OWM('d2710aa7f537a5ca496c34a6e365c8ea') # API-key
	observation = owm.weather_at_coords(lat, lon)
	l = observation.get_location().get_name()
	w = observation.get_weather()
	s = w.get_status()
	t = w.get_temperature('celsius').get('temp')
	print 'the location is ' + l + ', the status is ' + s+ ' and the temprature is ', t

	if t >20:
		print 'nice....'
	elif t<5:
		print 'brrrrrr'

	if s == 'Rain':
		print "I'm singing in the rain!"

except:
	print "error, enter the correct latitude, longitude"
