import os, sys, django
sys.path.append('/home/jerryzhang/bankfood')
os.environ['PYTHONPATH']= '/home/jerryzhang/bankfood/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'bankfood_proj.settings'
django.setup()
from nutritionapi import get_ndbno, get_nutrition_data
from yelpscraper import getRestaurantTopFoods
from yelpapi import query_api
from mint import getTransactionsCSV
from foodtracker.models import Restaurant, Transaction, Food

#food_list = getRestaurantTopFoods("test")

#transactions = getTransactionsCSV("transactions.csv", ["restaurants", "coffee shops", "fast food"])

r1 = Restaurant.objects.create_restaurant(name="McDonald's", location="Toronto, ON")
r1.save()
r1.add_foods(r1)

print r1.yelpurl
food_list = Food.objects.filter(restaurants__name="McDonald's")
for food in food_list:
    print food.name
    print food.calories
    print food.ndbno

#r1 = Restaurant(name="McDonald's", location="Toronto, ON", yelpurl = "http://www.yelp.com/biz/mcdonalds-toronto-82")
#r1.save()
#t1 = Transaction(date="2014-07-08", restaurant=r1, amount=1.46, category="fast food")
#t1.save()
#print t1.restaurant
def delModelInstance(model, the_id):
    model.objects.filter(id=the_id).delete()

