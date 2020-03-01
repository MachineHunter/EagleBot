from bs4 import BeautifulSoup
import requests as req
import datetime



def getWeather():
	url = "https://weather.yahoo.co.jp/weather/jp/13/4410/13209.html"
	r = req.get(url)

	soup = BeautifulSoup(r.text, "html.parser")

	weather_table = soup.select("table.yjw_table2")[0]


	current_time = str(datetime.datetime.now()).split(" ")[1]
	current_time = current_time.split(":")[0]+":"+current_time.split(":")[1]
	result = current_time+"\n"


	col = len(weather_table.find_all("tr")[0].find_all("td"))
	weathercols = [[]*1 for i in range(9)]

	for tr in weather_table.find_all("tr")[0:3]:
		for i,td in enumerate(tr.find_all("td")):
			td = td.text.replace("\n", "")
			weathercols[i].append(td)

	for i,weather in enumerate(weathercols):
		if(i==0): continue
		result += str(weather)+"\n"

	return result
