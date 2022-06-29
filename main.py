import json
from settings import shops
from dateutil.parser import parse
from pars_yandex import get_data_from_yandex

def start_get_data_from_yandex():  
    """ Загружает данные с яндекса и сохраняет их в json-файлах"""  
    print ("==== Start Parsing Yandex Maps ====")
    for shop in shops:
        get_data_from_yandex(shop["id_yandex"], shop["name"])
    print("==== End Parsing Yandex Maps ====")
    print()

        

def analyze_yandex_files(date_start="2010-01-01", date_end="2010-01-01"):
    all_reviews = []
    date_start = parse(date_start).date()
    date_end = parse(date_end).date()
    for shop in shops:
        name_file = shop["name"] + ".json"
        with open(name_file) as json_file:
            data = json.load(json_file)
            if data and data != "null":
                reviews = data["company_reviews"]
                reviews.pop(0)
                for review in reviews:
                    try:
                        review_date = parse(review["review_date"]).date()
                        if review_date >= date_start and review_date <= date_end:                  
                            cur_review = {
                                "shop" : shop["name"],
                                "date" : review_date,
                                "stars": review["star_count"],
                                "text" : review["review_text"],
                            }
                            all_reviews.append(cur_review)                            
                    except Exception as e:
                        print ("Error:", e)
                        print(shop["name"])
                        
    sorted_reviews = sorted(all_reviews, key=lambda x: x['date'])
    for review in sorted_reviews:
        print ("------")
        print(review['date'])
        print(review['shop'])
        print("Оценка:", review['stars'])
        print(review['text'])
    return sorted_reviews

# start_get_data_from_yandex()
date_start="2022-06-01"
date_end="2022-07-01"
analyze_yandex_files(date_start, date_end)
