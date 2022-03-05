from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

bs.find_all(lambda tag: len(tag.attrs) == 2)
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
bs.find_all('', text='Or maybe he\'s only resting?')
