from bs4 import BeautifulSoup
import requests as req


def getWeather():
	url = "https://weather.yahoo.co.jp/weather/jp/13/4410/13209.html"
	r = req.get(url)

	soup = BeautifulSoup(r.text, "html.parser")

	weather_table = soup.select("table.yjw_table2")[0]

	col = len(weather_table.find_all("tr")[0].find_all("td"))
	weathercols = [[]*1 for i in range(9)]

	for tr in weather_table.find_all("tr")[0:3]:
		for i,td in enumerate(tr.find_all("td")):
			td = td.text.replace("\n", "")
			weathercols[i].append(td)

	result = ""
	for weather in weathercols:
		result += str(weather)+"\n"

	return result
