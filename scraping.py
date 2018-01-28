import requests
from bs4 import BeautifulSoup

print("Enter the date in (DD/MM/YYYY) format to view the headlines: ")
date = input()
dd = date[:2]
mm = date[3:5]
yy = date[8:10]

url="http://www.rediff.com/issues/" + dd + mm + yy + "hl.html"
r = requests.get(url)
soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "hdtab1"})
new_data = g_data[0].find_all("a", {"target": "_new"})
str = g_data[0].text

time = []

for i in range(len(str)):
	if str[i]=='I' and str[i+1]=='S' and str[i+2]=='T':
		time.append(str[i-6]+str[i-5]+str[i-4]+str[i-3]+str[i-2]+str[i-1]+str[i]+str[i+1]+str[i+2])

for i in range(1, len(new_data)):
	print("-", new_data[i].text, "-", time[i-1])