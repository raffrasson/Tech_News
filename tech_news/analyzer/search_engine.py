from tech_news.database import search_news
import datetime


def search_by_title(title):
    tupled_results = []
    insensitive_title = {"title": {"$regex": title, "$options": "i"}}
    results = search_news(insensitive_title)
    for result in results:
        tupled_results.append((result["title"], result["url"]))
    return tupled_results


# Requisito 7
def search_by_date(date):
    # referencias:
    # https://theprogrammingexpert.com/python-remove-time-from-datetime/
    # https://stackoverflow.com/questions/969285/how-do-i-translate-an-iso-8601-datetime-string-into-a-python-datetime-object
    try:
        converted_date = datetime.datetime.fromisoformat(date).strftime(
            "%d/%m/%Y"
        )
        tupled_results = []
        results = search_news(
            {"timestamp": {"$regex": converted_date, "$options": "i"}}
        )
        for result in results:
            tupled_results.append((result["title"], result["url"]))
        return tupled_results

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
