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
    next = selector.css("a.next.page-numbers::attr(href)").get()
    return next


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    news_dict = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1[class=entry-title]::text").get().strip(),
        "timestamp": selector.css("li[class=meta-date]::text").get(),
        "writer": selector.css("a.url.fn.n::text").get(),
        "comments_count": len(selector.css("ol.comment-list.li").getall()),
        "summary": "".join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip(),
        # refs:
        # https://www.simplilearn.com/
        # tutorials/python-tutorial/list-to-string-in-python e o método strip
        # encontrado na lista:
        # https://www.w3schools.com/python/python_strings_methods.asp
        "tags": selector.css("a[rel=tag]::text").getall(),
        "category": selector.css(
            ".entry-details .meta-category .category-style span.label::text"
        ).get(),
    }

    print(news_dict)
    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
