from bs4 import BeautifulSoup
import requests as req
import datetime


url = "https://weather.yahoo.co.jp/weather/jp/13/4410/13209.html"
r = req.get(url)

soup = BeautifulSoup(r.text, "html.parser")

weather_table = soup.select("table.yjw_table2")[0]
current_time = str(datetime.datetime.now()).split(" ")[1]
current_hour = current_time.split(":")[0]
print(current_hour)

for tr in weather_table.find_all("tr"):
	for td in tr.find_all("td"):
		td = td.text.replace("\n", "")
		td = td.replace(' ', '')
		td = td.ljust(15)
		print("|"+td+"|", end="")
	print()
