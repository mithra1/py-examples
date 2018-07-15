from datetime import datetime
 

name = raw_input("Please Enter your name -> ")  
date = raw_input("Please enter your date of brith as mm/dd/yyy -> ")

year = datetime.strptime(date,'%m/%d/%Y').year

print '\n'

print 'So you  born in %i' % year
answer = raw_input('* %s *, Would you like to know about your generation cohort ? Please enter Y or N ->' % name)

if answer.upper() == 'N':
	print 'ok - Good Bye'
	exit()


result = ''

if year in range(1966,1976):
	result = 'X'
if year in range(1977,1994):
	result = 'Y'
if year in range(1995,2012):
	result = 'Z'

print '\n \n'

print '*****************  \n'
print 'Your name is :' + name
print 'Your DOB is :' + date
print 'You belong to Generartion:' + result
print '\n *****************  \n'

