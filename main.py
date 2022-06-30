import json
from settings import shops
from dateutil.parser import parse
from pars_yandex import get_data_from_yandex


def start_get_data_from_yandex():
    """ Загружает данные с яндекса и сохраняет их в json-файлах"""
    print("==== Start Parsing Yandex Maps ====")
    for shop in shops:
        get_data_from_yandex(shop["id_yandex"], shop["name"])
    print("==== End Parsing Yandex Maps ====")
    print()


def get_data_from_file(filename: str):
    """Получает и возвращает словарь из файла. Может вернуть None."""
    result = None
    with open(filename) as json_file:
        data = json.load(json_file)
        if data and data != "null":
            result = data["company_reviews"]
            result.pop(0)
    return result


def clear_reviews(shop: str, reviews: list, date_start, date_end):
    """Очищает список словарей с отзывами, приводит их в нормальный вид, фильтрует по периоду."""
    result = []
    for review in reviews:
        try:
            review_date = parse(review["review_date"]).date()
            if review_date >= date_start and review_date <= date_end:
                clear_review = {
                    "shop": shop,
                    "date": review_date,
                    "stars": review["star_count"],
                    "text": review["review_text"],
                    "from": "yandex",
                }
                result.append(clear_review)
        except Exception as e:
            # print("Error:", e)
            # print(shop)
            pass
    return result


def get_filtered_and_cleaned_reviews_from_files_yandex(date_start="2010-01-01", date_end="2010-01-01"):
    """Возвращает отфильрованные, очищенные и отсортированные отзывы из яндекс-файлов"""
    result = []
    date_start = parse(date_start).date()
    date_end = parse(date_end).date()
    for shop in shops:
        reviews_of_shop = get_data_from_file(shop["name"] + ".json")
        if reviews_of_shop:
            result.extend(clear_reviews(
                shop["name"], reviews_of_shop, date_start, date_end))
    return sorted(result, key=lambda x: x['date'])


def print_review(review: dict):
    print("------")
    print(review['date'], "(", review['from'], ")")
    print(review['shop'])
    print("Оценка:", review['stars'])
    print(review['text'])


def print_reviews(reviews: list):
    for review in reviews:
        print_review(review)



is_parsing = input("Запустить парсинг отзывов с яндекса? y/n ")
if is_parsing=="y" or is_parsing=="д":
    start_get_data_from_yandex()
    
date_start = "2022-06-01"
date_end = "2022-07-01"
reviews = get_filtered_and_cleaned_reviews_from_files_yandex(
    date_start, date_end)
print_reviews(reviews)
