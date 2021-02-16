import scraping_with_price as sc
import pandas as pd

PATH = "/Users/ramiro/Desktop/python-ml-course-master/Practica/chromedriver"
df = sc.get_wines(PATH, 7, 30, False)

#Guardamos los datos en un csv
df.to_csv('wines_vivino.csv', index=False)