import requests
from bs4 import BeautifulSoup


keywords = ['bitcoin', 'btc', 'crypto', 'cryptocurrency']
URL = 'https://www.coindesk.com/wp-json/v1/home/more?page=1&per_page=15'
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
HOST = 'https://www.coindesk.com/'

class Main:
    def get_json(self, url, headers):
        req = requests.get(url=url, headers=headers)
        return req.json()

    def get_data(self, json_data):
        posts = json_data['posts']
        list_of_posts = list(map(lambda a: {'title': a['title'], 'slug': a['slug'], 'date': a["date"] }, posts))
        return list_of_posts

    def request_article_info(self, url):
        req = requests.get(url=url, headers=HEADERS)
        return req

    def get_text(self, html):
        text = html.text.encode()
        return text

    def check_key_words(self, article):
        for word in keywords:
            if word in article.lower():
                return article
        return False

    def get_article_attributes(self, text, post):
        soup = BeautifulSoup(text, 'html.parser')
        try:
            article = soup.find('section', class_='article-body has-media news default-article').text
        except AttributeError:
            return False
        return article

def main_coindesk():
    a = Main()
    json_main_page = a.get_json(url=URL, headers=HEADERS)
    list_of_posts = a.get_data(json_main_page)
    obj = []
    for post in list_of_posts:
        link = HOST+post['slug']
        title = post['title']
        wrote_at = post['date']
        html = a.request_article_info(url=link)
        text = a.get_text(html)
        article = a.get_article_attributes(text, post)
        if not article or a.check_key_words(article) == False:
            continue
        obj.append({
            'title': title,
            'href': link,
            # 'wrote_at': wrote_at,
            'text': article,
            'source_name': 'coindesk',
            'source_href': HOST
        })
    return obj
