# coding=utf8

# importing BeautifulSoup

from bs4 import BeautifulSoup
import re

def parse():
	f = open('data.htm',"r")
	data = f.read()
	soup = BeautifulSoup(data)
	return soup



soup    = parse()
tables  = soup.find_all('table') 
req_tab = tables[len(tables)-3]
req_tr  = req_tab.find_all('tr')

req_map = {}

for tr in req_tr:
	tds = tr.find_all('td')
	req_map[re.sub(' +',' ',tds[0].get_text())] = re.sub(' +',' ',tds[1].get_text())


for key in req_map:
    print key, 'corresponds to', req_map[key]

