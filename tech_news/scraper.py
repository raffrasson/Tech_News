import requests
import time
from tech_news.database import create_news
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
    return news_dict


# Requisito 5
def get_tech_news(amount):
    page = "https://blog.betrybe.com/"
    arcticles = []
    while len(arcticles) < amount:
        page_data = fetch(page)
        links = scrape_novidades(page_data)
        for link in links:
            if len(arcticles) < amount:
                page_data = fetch(link)
                noticia = scrape_noticia(page_data)
                arcticles.append(noticia)
        page = scrape_next_page_link(fetch(page))
    create_news(arcticles)
    return arcticles
