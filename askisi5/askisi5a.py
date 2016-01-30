try:	
	d= int(input("enter day:"))
	m= int(input("enter month:"))
	y= int(input("enter year:"))
	if 1<=d<=31 and 1<=m<=12 and 1900<=y<=2099:	
		if m<3:
			m=m+12
			y=y-12
		a=(2*m)+(6*(m+1)/10)
		b=y+(y/4)+(y/400)-(y/100)
		c=d+a+b+1
		f=c%7
		if f==0:
			print "sunday"
		elif f==1:
			print "monday"
		elif f==2:
			print "tuesday"
		elif f==3:
			print "wednesday"
		elif f==4:
			print "thursday"
		elif f==5:
			print "friday"
		else:
			print "saturday"
	else:
		print "wrong input"
except:
	print "error..... not number"
