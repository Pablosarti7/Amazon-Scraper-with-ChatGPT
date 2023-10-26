from bs4 import BeautifulSoup
import requests


class Scraper:
    
    def __init__(self) -> None:
        self.soup = None

    def request(self):
        http_headers = {
            "Accept-Language": 'en-US,en;q=0.9',
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }
        response = requests.get(
            'https://www.amazon.com/Best-Sellers-Books-Business-Money/zgbs/books/3/ref=zg_bs_nav_books_1', headers=http_headers)

        self.soup = BeautifulSoup(response.text, "html.parser")
    

    def parse_html(self):

        titles = self.soup.find_all('span')
        authors = self.soup.find_all(class_='a-size-small a-link-child')
        asins = self.soup.find_all('div', class_='p13n-sc-uncoverable-faceout')

        titles_list = []
        authors_list = []
        asins_list = []

        for title in titles:
            _title = title.find(
                'div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
            if _title:
                titles_list.append(_title.text)

        for author in authors:
            _author = author.find(
                'div', class_='_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y')
            if _author:
                authors_list.append(_author.text)

        for asin in asins:
            _asin = asin.get('id')
            if _asin:
                asins_list.append(_asin)

        return titles_list, authors_list, asins_list
    