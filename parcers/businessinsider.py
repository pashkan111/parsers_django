import requests
from bs4 import BeautifulSoup


keywords = ['bitcoin', 'btc', 'crypto', 'cryptocurrency']
URL = 'https://www.insider.com/latest'
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Content-Type": 'text/html; charset=utf-8'
    }
HOST = 'https://www.insider.com'


class Main:
    def get_html(self, url, headers):
        req = requests.get(url=url, headers=headers)
        return req

    def get_text(self, html):
        text = html.text.encode()
        return text

    def get_list_of_links(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        a = soup.find_all('section', class_='river-item featured-post')
        links = []
        for i in a:
            links.append(i.find('a', class_='tout-title-link').get('href'))
        return links

    def check_key_words(self, article):
        for word in keywords:
            if word in article.lower():
                return article
        return False

    def get_article_attributes(self, text, link):
        soup = BeautifulSoup(text, 'lxml')
        article = soup.find('div', class_='content-lock-content')
        title = soup.find('h1', class_='post-headline').text
        if not article:
            article = soup.find('section', class_='video-content-post')
        article = article.find_all('p')
        text = ''
        for i in article:
            text += i.text
        text = self.check_key_words(text)
        if not text:
            return False
        return {
            'text': text,
            'href': link,
            'title': title,
            'source_name': 'insider',
            # 'wrote_at': 
            "source_href": 'https://www.insider.com/latest'
            }
        
        
def main_businessinsider():
    a = Main()
    html_main_page = a.get_html(url = URL, headers=HEADERS)
    text_main_page = a.get_text(html_main_page)
    links = a.get_list_of_links(text=text_main_page)
    obj = []
    for link in links:
        link = HOST+link
        html_article_page = a.get_html(url=link, headers=HEADERS)
        text_article_page = a.get_text(html_article_page)
        lst = a.get_article_attributes(text=text_article_page, link=link)
        if not lst:
            continue
        obj.append(lst)
    return obj

