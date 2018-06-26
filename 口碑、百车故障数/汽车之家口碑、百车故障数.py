import re
import requests
from bs4 import BeautifulSoup

def get_liveid():
	ids=set()
	response=requests.get('https://www.autohome.com.cn/a00/1_1-0.0_0.0-0-0-0-0-0-0-0-0/')
	soup=BeautifulSoup(response.text,'html.parser')
	for link in soup.find_all('h4'):
		for links in link.find_all('a'):
			href=links.attrs['href']
			ids.add(href)
	return ids


def get_carid(liveid):
	car_url='https:{}'.format(href)
	response=requests.get(car_url)
	soup=BeautifulSoup(response.text,'html.parser')
	
	car_name=soup.title.get_text()
	car_koubei=soup.select('a[class="font-score"]')
	car_bad=soup.select('a[class="fn-left font-fault"]')
	print(car_name,car_koubei,car_bad,',')


			
if __name__ == '__main__':
        ids=(get_liveid())
        for href in ids:
        	get_carid(href)
      
