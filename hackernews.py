from bs4 import BeautifulSoup
import requests
from pprint import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_link = links + links2
mega_subtext = subtext+subtext2

def arrange_hn(l):
	return sorted(l, key = lambda k: k['votes'])

def custom_hn(links, subtext):
	hn =[]
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		votes = subtext[idx].select('.score')
		if len(votes):
			points = int(votes[0].getText().replace(' points', ''))
			if points >= 100:
				hn.append({'title':title, 'href':href, 'votes': points})
	return arrange_hn(hn)
	
pprint(custom_hn(mega_link,mega_subtext))
