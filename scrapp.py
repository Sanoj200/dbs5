#imports
from bs4 import BeautifulSoup
from collections import Counter
import requests
import csv

def getPage(url):
	r = requests.get(url)
	data = r.text
	spobj = BeautifulSoup(data, "lxml")
	return spobj
	
def main():
	urls = ["https://www.heise.de/thema/https", "https://www.heise.de/thema/https?seite=1", "https://www.heise.de/thema/https?seite=2", "https://www.heise.de/thema/https?seite=3"]
	
	
	words = []
	
	for url in urls:
		bereich = getPage(url).find("div", {"class" : "keywordliste"}) #sucht Bereich Keywordliste in Quellcodedatei der Seite
		opsidian = bereich.findAll("header") #und findet die Überschriften
		splitline = []
		for op in opsidian: 
			splitline = op.get_text().split() # spaltet die Überschriften in Wörter
			for line in splitline:		#hier werden die wörter in words eingefügt		
				words.append(line);  
	
	
	word_counter = {}                       # wöter werden gezählt
	for word in words:
		if word in word_counter:
			word_counter[word] += 1
		else:
			word_counter[word] = 1
			
	pop_words = sorted(word_counter, key = word_counter.get, reverse = True) #gibt die häufigsten drei Wörter
	
	print(pop_words[:3])
	
	
		
	
if __name__ == '__main__':
	main()
