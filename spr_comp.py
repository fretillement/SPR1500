import csv


#Insheet data 
comp = csv.reader(open('M:/SPR_cap/spr_composite2.csv', 'r'))

#Create empty dict of ticker 
#print comp.fieldnames
info = {}

#Create dict of dates
def processLine(line):  
	line = filter(None, line)
	if "Date" in line: 
		line.remove('Date')
		line = map(str, line)
	if "CUR_MKT_CAP" in line: line.remove('CUR_MKT_CAP') 
	return line 

def processEntry(entry, line):
	entry.append(processLine(line))

#Organize entries by company name, date, and caps in dict of dicts
entry = []
capinfo = {}
for line in comp: 
	if len(entry) <= 2: 
		processEntry(entry, line)
	else: 
		capinfo[''.join(entry[0])] = dict(zip(entry[1], entry[2]))
		entry = []

#Get full list of dates in data
dates = []
for k in capinfo: 
	dates = dates + capinfo[k].keys()
finaldates = list(set(dates))

#Output to a csv file 
header = ['Company'] + finaldates
output = csv.DictWriter(open('M:/SPR_cap/SPR_comp_cleaned.csv', 'w'), fieldnames= header,  lineterminator = '\n')
output.writeheader()
for company in capinfo: 
	tempinfo = {"Company": company}
	caps = capinfo[company]
	for h in header: 
		if h in caps: 
			tempinfo[h] = caps[h]
	output.writerow(tempinfo)	

# Sort dates in excel