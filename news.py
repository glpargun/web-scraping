from asyncore import write
import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.butenunbinnen.de/'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_='teaser')

with open('dailynews.csv', 'w', encoding='utf-8', newline='') as d:
    thewriter = writer(d)
    #header row creating:
    header = ['Title', 'News Texts', 'Addional Label']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('span', class_='teaser-title').text

        try:
            text = list.find('p', class_='teaser-text').text
            document_label = list.find('span', class_='teaser-documentlabel').text.replace('\n', '')
        except Exception as e:
            text = None
            document_label = None

        info = [title, text, document_label]

        thewriter.writerow(info)