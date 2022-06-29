import json
from settings import shops
from dateutil.parser import parse
from pars_yandex import get_data_from_yandex

def start_get_data_from_yandex():    
    print ("==== Start Parsing Yandex Maps ====")
    for shop in shops:
        get_data_from_yandex(shop["id"], shop["name"])
    print("==== End Parsing Yandex Maps ====")
    print()
        

def analyze_yandex_files(date_start="2010-01-01", date_end="2010-01-01"):
    date_start = parse(date_start).date()
    date_end = parse(date_end).date()
    for shop in shops:
        name_file = shop["name"] + ".json"
        with open(name_file) as json_file:
            data = json.load(json_file)
            if data and data != "null":
                reviews = data["company_reviews"]
                reviews.pop(0)
                sorted_reviews = sorted(reviews, key=lambda x: x['review_date'])
                for review in sorted_reviews:
                    count_views = 0
                    try:
                        review_date = parse(review["review_date"])
                        if review_date.date() >= date_start and review_date.date() <= date_end:                            
                            if count_views == 0:
                                print(shop['name'])
                            print (review_date.date())
                            print("Оценка: ", review["star_count"])
                            print(review["review_text"])
                           
                            print ('----------')
                            count_views += 1
                    except:
                        pass    
   
                        
                    # print (review["review_date"])
                    # print (review["review_text"])
                    # print("----------------")
                    # print(type(review["review_date"]))
                    # if review["review_date"]:
                    #     date_time_obj = parse(review["review_date"])
                    #     print(date_time_obj.date())

# start_get_data_from_yandex()
date_start="2022-03-01"
date_end="2022-07-01"
analyze_yandex_files(date_start, date_end)
