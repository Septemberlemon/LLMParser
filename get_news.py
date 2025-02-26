from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup as bs


count = 0


def download_all_news():
    url = "https://ict.gdqy.edu.cn/xwdt1.htm"
    while url:
        download_page(url)
        url = get_next_page_url(url)


def fetch_soup(url, encoding=None):
    response = requests.get(url)
    if encoding:
        response.encoding = encoding
    return bs(response.text, 'html.parser')


def download_page(url):
    soup = fetch_soup(url)
    news_list = soup.find("ul", id="list_1")
    for li in news_list.find_all("li"):
        download_news(urljoin(url, li.find("a")["href"]))


def download_news(url):
    print(url)
    soup = fetch_soup(url, "utf-8")
    global count
    count += 1
    with open(f"news/{count}.txt", "w", encoding="utf-8") as file:
        file.write(url + "\n")
        file.write(soup.find("div", class_="d-header text-left").find("h2", class_="title").string + "\n")
        file.write(soup.find("div", class_="v_news_content").get_text().strip())


def get_next_page_url(url):
    soup = fetch_soup(url, "utf-8")
    for a in soup.find_all("a"):
        if a.string == "下页":
            return urljoin(url, a["href"])
