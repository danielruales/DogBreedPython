from bs4 import BeautifulSoup as bs
import requests as req
import re

# Use web scrapping techniques to gather data
# on project associated with random_int aka display_num
# Return data to output to html
def displayData(display_num):

	url = 'https://unity.com/madewith'
	results = req.get(url)
	soup = bs(results.text, "lxml")
	titles = [x.text for x in soup.find_all('div', attrs={'class': 'section-home-stories--item-title'})]
	studio = [x.text for x in soup.find_all('div', attrs={'class': 'section-home-stories--item-studio'})]
	image_temp = soup.find_all('div',attrs={'class':'section-home-stories--item-image','style':True})
	image_url = []
	for num,x in enumerate(image_temp):
		if x is not None:
			url_temp = (re.findall("\('(/sites/.*)'\)",image_temp[num]['style']))
			image_url.append("https://unity.com"+url_temp[0])
	projects = soup.find_all('article')
	project_url = []
	for x in projects:
			project_url.append("https://unity.com" + x.find('a').attrs['href'])
	project_results = req.get(project_url[display_num])
	soup = bs(project_results.text, "lxml")
	main_texts = [x.text for x in soup.find_all('div', attrs={'class': 'section-article-text'})]
	project_text = main_texts[2]
	studio_text = main_texts[0]
	reveal_text = main_texts[3]

	unity_data = [
		{
			'title': titles[display_num],
			'studio' : studio[display_num],
			'url' : project_url[display_num],
			'studiotext' : studio_text,
			'projecttext' : project_text,
			'revealtext' : reveal_text,
			'image' : image_url[display_num]
		}
	]
	return unity_data