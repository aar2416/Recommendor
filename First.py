import csv
import re
import datetime
d={}
count=[]
csvFile = csv.reader(open("sales_data.csv", "r"))
i=0
brand=[]
product_line=[]
for row in csvFile:
		if i==0:
			i=i+1
			continue
		d[int(row[0])]={}
		d[int(row[0])]['sku']=row[1].lower()
		d[int(row[0])]['product_line'] = row[2].lower()
		d[int(row[0])]['brand'] = row[3].lower()
		d[int(row[0])]['sales'] = int(row[4].lower())
		d[int(row[0])]['price'] = float(row[5].lower())
		brand.append(d[int(row[0])]['brand'])
		product_line.append(d[int(row[0])]['product_line'])
brand=set(brand)
print brand
product_line=set(product_line)
while(1):
	flag=1
	input_p=raw_input("What you wanna search ")
	wordList = re.sub("[^\w]", " ",  input_p).lower().strip().split()
	if input_p is not(""):                       #check if input in not empty
		with open('user_logs.txt','a') as logfile:  #storing inputs in log file
			logfile.write('\n%s \t'%input_p + " " +str(datetime.datetime.now()))
	else:
		input_p=raw_input("What you wanna search ")
		if input_p is (""):
			break
		else:
			with open('user_logs.txt','a') as logfile:  #storing inputs in log file
				logfile.write('\n%s \t'%input_p + " " +str(datetime.datetime.now()))
	word=list(wordList)
	i=0
	bran='na'
	prod='na'
	j=0
	count=0
	results={}
	for i in wordList:
		if (next((s for s in brand if i == s),'na') != 'na'):
			bran=next((s for s in brand if i == s),'na')
		if(next((s for s in product_line if i in s),'na') != 'na'):
			prod=next((s for s in product_line if i in s),'na')
	print bran, prod
	for x,y in filter( lambda (x,y):(y['brand']==bran or bran=='na') and (y['product_line']==prod or prod=='na'),d.iteritems()):
		count=0
		for i in wordList:
			if i in d[int(x)]['sku']:
				count+=1
			if count>=len(wordList)-1:
				results[x]=y
	hp=sorted(results.values(), key=lambda y: (y['price']),reverse=True)[:3]
	print "---------------------Highest Price---------------------"
	for i in hp:
		print i
	hp=sorted(results.values(), key=lambda y: (y['price']))[:3]
	print "---------------------lowest Price---------------------"
	for i in hp:
		print i
	hp=sorted(results.values(), key=lambda y: (y['sales']),reverse=True)[:3]
	print "---------------------Highest Sales---------------------"
	for i in hp:
		print i