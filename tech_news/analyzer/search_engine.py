from tech_news.database import search_news


def search_by_title(title):
    tupled_results = []
    insensitive_title = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(insensitive_title)
    for result in results:
        tupled_results.append((result["title"], result["url"]))
    return tupled_results


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
