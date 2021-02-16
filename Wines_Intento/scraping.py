from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_wines(path, time_slp, num_wines, Print):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.vivino.com/explore?e=eJzLLbI11jNVy83MszVQy02ssDU2NzBQS660dQxSSwYSwWoFtoZq6Wm2ZYlFmakliTlq-Um2RYklmXnpxfHJ-aV5JWr5timpxclAPcXRsbaJRQAoERtp'
    driver.get(url)

    wines = []
    while num_wines > len(wines):
        time.sleep(time_slp)
        wines_cards = driver.find_elements_by_xpath('//div[@class="explorerCard__explorerCard--3Q7_0 explorerPageResults__explorerCard--3q6Qe"]')
        for wine_card in wines_cards:
            if len(wines) >= num_wines:
                break
            time.sleep(time_slp)
            collected_successfully = False
            while not collected_successfully:
                try:
                    title = wine_card.find_element_by_xpath('.//span[@class="vintageTitle__winery--2YoIr"]').text
                    grape = wine_card.find_element_by_xpath('.//span[@class="vintageTitle__wine--U7t9G"]').text
                    location = wine_card.find_element_by_xpath('.//div[@class="vintageLocation__vintageLocation--1DF0p"]/a[3]').text
                    rating = wine_card.find_element_by_xpath('.//div[@class="vivinoRatingWide__averageValue--1zL_5"]').text
                    print (title)
                    collected_successfully = True
                except:
                    print ('No encontro')
                    time.sleep(6)

                try:
                    time.sleep(4)
                    wine_card.find_element_by_xpath('.//button[@class="button__button--247vZ button__themeFlat--WqIBc button__sizeDefault--3HuoB explorerCard__button--3HZ-g"]').click()
                    time.sleep(12)
                    price = driver.find_element_by_xpath('//a[@class="button__button--m8RH9 button__themePrimary--3H_zH button__sizeMedium--1-uHP shop__priceButton--33XSU button__link--h-Ho-"]/span').text
                    time.sleep(1)
                    driver.find_element_by_xpath('//*[name()="path" and @fill="#a8a5a3" and @fill-rule="evenodd"]/..').click()
                    print (price)
                except:
                    print ('No encontro precio')
                    time.sleep(6)

            if Print:
                print (f'Title: {title}')
                print (f'Grape: {grape}')
                print (f'Price: {price}' )
                print (f'Location: {location}')
                print (f'Rating: {rating}')

            
            wines.append({
                'Title': title,
                'Grape': grape,
                'Location': location,
                'Rating': rating,
                'Price': price
            })

    return pd.DataFrame(wines)

                











