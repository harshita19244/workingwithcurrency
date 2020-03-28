import datetime
import urllib.request
import datetime

def getLatestRates():
	""" Returns: a JSON string that is a response to a latest rates query.
	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	url=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
	data=url.read()

	return data
	



def changeBase(amount, currency, desiredCurrency, date):
	""" Outputs: a float value f.
	"""

	url=urllib.request.urlopen(str("https://api.exchangeratesapi.io/"+date))
	data=url.read()
	rate=str(data)

	f=rate.index("base")
	rate=rate[:f-3]
	rate=rate+","
	if(desiredCurrency=="EUR" and currency=="EUR"):
		return float(amount)
	elif(desiredCurrency=="EUR"):
		a=rate.index(currency)
		b=rate.index(",",a)
		currencyvalue=float(rate[a+5:b])
		return amount*currencyvalue
	elif(currency=="EUR"):
		a=rate.index(desiredCurrency)
		b=rate.index(",",a)
		desiredCurrencyvalue=float(rate[a+5:b])
		return amount/desiredCurrencyvalue
	else:
		a=rate.index(currency)
		b=rate.index(",",a)
		currencyvalue=float(rate[a+5:b])
		c=rate.index(desiredCurrency)
		d=rate.index(",",c)
		desiredCurrencyvalue=float(rate[c+5:d])
		required1=(desiredCurrencyvalue*amount)/(currencyvalue)
		return required1

def bubbleSort(a,b):
	n = len(a)
	for i in range(n):
		for j in range(0, n-i-1):
			if b[j] > b[j+1] :
				a[j], a[j+1] = a[j+1], a[j]
				b[j], b[j+1]= b[j+1], b[j]

	return (a,b)

def printAscending(json=getLatestRates()):
	""" Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
	D=eval(json)
	
	a=[]
	b=[]
	for num in D["rates"]:

		a.append(num)
		b.append(D["rates"][num])
	(a,b)=bubbleSort(a,b)
	for i in range(len(a)):
		print("1 Euro = "+ str(b[i])+" " + str(a[i]))
json=getLatestRates()
printAscending(json)

		

def extremeFridays(startDate, endDate, currency):
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.
		
	Parameters: 
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	"""
	url=urllib.request.urlopen(str("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate))
	data=url.read()
	D=eval(data)
	date=[]
	cur=[]
	for num in D["rates"]:

		a=int(num[:4])
		b=int(num[5:7])
		c=int(num[8:])
		date1=datetime.datetime(a,b,c)
		if (date1.weekday()==4):
			date.append(num)
			cur.append(D["rates"][num][currency])

	date,cur=bubbleSort(date,cur)
	x=len(date)
	if(x==0):
		print("No such Fridays exist")
	elif(x==1):
		print("Only on Friday exists which was on "+str(date[0])+ " so the currency has one value."+" 1 Euro was equal to "+str(cur[0])+" "+currency)
	else:
		print(currency+" was strongest on "+str(date[0])+". 1 Euro was equal to "+str(cur[0])+" "+currency)
		print(currency+" was weakest on "+str(date[-1])+". 1 Euro was equal to "+str(cur[-1])+" "+currency)


def findMissingDates(startDate, endDate):
	""" Output: the dates that are not present when you do a json query from startDate to endDate 
		You don't have to return anything.
		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd
	"""
	url=urllib.request.urlopen(str("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate))
	data=url.read()
	D=eval(data)
	datesinapi=[]
	datesinactual=[]
	for num in D["rates"]:
		datesinapi.append(str(num))
	datesinapi.sort()

	
	ty1=int(startDate[:4])
	tm1=int(startDate[5:7])
	td1=int(startDate[8:])
	ty2=int(endDate[:4])
	tm2=int(endDate[5:7])
	td2=int(endDate[8:])
	t1=datetime.date(year=ty1 , month= tm1 ,day= td1)
	t2=datetime.date( year=ty2 ,month= tm2 , day=td2)
	t3=(t2-t1).days
	print("The following dates were not present:")
	
	for i in range(0,t3+1):
		datesinactual.append(str(datetime.date(ty1,tm1,td1)+datetime.timedelta(i)))


	
	for i in range(0,len(datesinactual)):
		if datesinactual[i] not in datesinapi:
			print(datesinactual[i])