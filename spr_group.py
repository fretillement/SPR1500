import csv 


f = "N:/Research/_Long Term Storage/Shruthi Venkatesh/Market Caps/"


# Initialize empty dict with all company names
industry = {}
indgroup = {}
sector = {}
namesfile = f+'industrynames.csv'
names = csv.DictReader(open(namesfile, 'r'))
for x in names: 
	industry[(x['Industry_Ticker'], x['Industry_Name'], x['Industry_Category'])] = {}
	indgroup[(x['Indgroup_Ticker'], x['Indgroup_Name'], x['Indgroup_Category'])] = {}
	sector[(x['Sector_Ticker'], x['Sector_Name'], x['Sector_Category'])] = {}


# For each grouping, read in files and append rows 
groupnames = ['Industry', 'Industry Group', 'Sector']
files = ['1_19', '20_49', '50_79', '80_109', '110_139', '140_169', 
		'170_199', '200_229', '230_260', '261_290']

for group in groupnames:
	for x in files: 
		fname = f + group + '/' + x + '.csv'
		handle = csv.DictReader(open(fname, 'r'), dialect = 'excel')
		for line in handle: 
			if group == 'Industry': industry[(line['Ticker'], line['Name'], line['Category'])].update(line)			
			if group == 'Industry Group': indgroup[(line['Ticker'], line['Name'], line['Category'])].update(line) 
			if group == 'Sector': sector[(line['Ticker'], line['Name'], line['Category'])].update(line) 


# Output to csv 
grheader = ['Name', 'Category', 'Ticker'] + industry[('PCP UN Equity', 'Precision Castparts Corp', 'Aerospace & Defense (29 members)')].keys()
industry_output = csv.DictWriter(open(f+'Industry/allyears.csv', 'w'), fieldnames = grheader, lineterminator = '\n')
indgroup_output = csv.DictWriter(open(f+'Industry Group/allyears.csv', 'w'), fieldnames = grheader, lineterminator = '\n')
sector_output = csv.DictWriter(open(f+'Sector/allyears.csv', 'w'), fieldnames = grheader, lineterminator = '\n')

industry_output.writerow(dict(zip(grheader, grheader)))
indgroup_output.writerow(dict(zip(grheader, grheader)))
sector_output.writerow(dict(zip(grheader, grheader)))

for x in industry: 
	industry_output.writerow(industry[x])
for x in indgroup: 
	indgroup_output.writerow(indgroup[x])
for x in sector: 
	sector_output.writerow(sector[x])