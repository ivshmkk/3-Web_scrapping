from pprint import pprint
from bs4 import BeautifulSoup
import requests


DATA_URL = 'https://habr.com/ru/articles/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
SOURCE = requests.get(DATA_URL).text


soup = BeautifulSoup(SOURCE, 'lxml')

articles_list = soup.findAll('article', class_='tm-articles-list__item')

parsed_data = []
for article in articles_list:
    link = f'https://habr.com{article.find("a", class_="tm-title__link")["href"]}'
    title = article.h2.a.span.text
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    time = article.find('time')['datetime']
    text_preview = soup.find('div', class_=('article-formatted-body_version-2', 'article-formatted-body')).text
    # print(text_preview.text)
    # parsed_data.append({
    #     'time': time,
    #     'title': title,
    #     'link': link
    # })

# pprint(parsed_data)


for search_word in KEYWORDS:
    if (search_word.lower() in title.lower()) or (search_word.lower() in text_preview.lower()):
        pprint(f'Дата: {time} - Заголовок: {title} - Ссылка: {link}')