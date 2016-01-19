from bs4 import BeautifulSoup
from mechanize import Browser
import re

def getRestaurantTopFoods(url):
    #mech = Browser()
    #mech.set_handle_robots(False)
    #page = mech.open(url)
    
    #html = page.read()
    
    text_file = open("sample_yelp_html.txt", "r")
    html = text_file.read()
    text_file.close()
    
    soup = BeautifulSoup(html, "html5lib")
    foods = soup.find_all(class_="ngram")
    
    food_list = []
    for food in foods:
        food_list.append(food.get_text().split()) # this is a terrible way to get foods
    return food_list