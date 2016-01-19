from django.db import models

from nutritionapi import get_ndbno, get_nutrition_data
from yelpscraper import getRestaurantTopFoods
from yelpapi import query_api
from mint import getTransactionsCSV

# Create your models here.

class FoodManager(models.Manager):
    @classmethod
    def getNutrition(cls, food):
        try:
            ndbno = get_ndbno(food)
            nutrition = get_nutrition_data(ndbno)
            return ndbno, nutrition
        except:
            return
    def delete_everything(self):
        Food.objects.all().delete()
    def create_food(self, name):
        ndbno, nutrition = FoodManager.getNutrition(name)
        food = self.create(name=name, calories=nutrition['calories'], ndbno=ndbno)
        return food

class Food(models.Model):
    name = models.CharField(max_length=300)
    calories = models.FloatField(blank = True)
    ndbno = models.IntegerField(blank = True)
    
    objects = FoodManager()
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class RestaurantManager(models.Manager):
    def create_restaurant(self, name, location):
        yelpurl = query_api(name, location)
        restaurant = self.create(name=name, location=location, yelpurl=yelpurl)
    
        return restaurant
    def delete_everything(self):
        Food.objects.all().delete()

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    yelpurl = models.CharField(max_length=200)
    foods = models.ManyToManyField(Food, related_name="restaurants", blank=True)
    
    objects = RestaurantManager()
    
    @classmethod
    def add_foods(self, restaurant):
        #foods = getRestaurantTopFoods(self.yelpurl) real version
        foods_list = ['Big Mac', 'Fries', 'Cola'] # test version
        for this_food in foods_list:
            food = Food.objects.create_food(this_food)
            food.save()
            restaurant.foods.add(food)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Transaction(models.Model):
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    amount = models.FloatField()
    category = models.CharField(max_length=120, default ='fast food')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.amount
    
        

    