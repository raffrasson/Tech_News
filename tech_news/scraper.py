import requests
import time
from parsel import Selector


def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    link_list = selector.css("h2 a::attr(href)").getall()
    return link_list


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_list = selector.css("a.next.page-numbers::attr(href)").get()
    return link_list


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
