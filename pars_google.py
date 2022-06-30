import re
from parsel import Selector
from selenium import webdriver
from bs4 import BeautifulSoup

# используйте путь к драйверу, который вы скачали на предыдущих шагах
chromedrive_path = './chromedriver'
# driver = webdriver.Chrome(chromedrive_path)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chromedrive_path, options=options)

url = 'https://www.google.com/maps/place/Республика+игр/@55.7058266,37.5918679,10z/data=!3m1!5s0x414ab6f43a1d07a5:0x64dca85301e5d81c!4m5!3m4!1s0x414ab6f5ba5bbfd7:0x1216ae5deed2aad!8m2!3d55.6575829!4d37.8455413'
driver.get(url)

page_content = driver.page_source

# print (page_content)
# response = Selector(page_content)
soup = BeautifulSoup(page_content)
strings = soup.find_all(string=re.compile('wiI7pd'))
for txt in strings:
    print(" ".join(txt.split()))



results = []
# print(response)
# for el in response.xpath('//div/div[@data-review-id]/div[contains(@class, "content")]'):
#     results.append({
#         'title': el.xpath('.//div[contains(@class, "title")]/span/text()').extract_first(''),
#         'rating': el.xpath('.//span[contains(@aria-label, "stars")]/@aria-label').extract_first('').replace('stars', '').strip(),
#         'body': el.xpath('.//span[contains(@class, "wiI7pd")]/text()').extract_first(''),
#     })

# print(results)

driver.quit()
