import requests as req
from bs4 import BeautifulSoup
import sys


def getMeaning(word):
	url = "https://ejje.weblio.jp/content"+str(word)
	r = req.get(url)

	soup = BeautifulSoup(r.text, "html.parser")

	meaning = soup.select("#summary > div.summaryM.descriptionWrp > table > tbody > tr > td.content-explanation.ej")

	if(len(meaning) > 0):
		return "("+word+") >>> "+meaning[0].text
	else:
		return "meaning not found."
