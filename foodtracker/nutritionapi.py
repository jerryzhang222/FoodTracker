import pycurl, json
import subprocess
import ast

def get_ndbno(food_name):
    proc = subprocess.Popen(["curl", "-H", "Content-Type: application/json", "-d", json.dumps({"q":food_name,"max":"1","offset":"0"}), "eFg7QhZRitIkCNrIfU0kDuFgfyXnkxlv4nQXAt2X@api.nal.usda.gov/ndb/search"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    ndbno = ast.literal_eval(out)["list"]["item"][0]["ndbno"]
    return ndbno

def get_nutrition_data(ndbno):
    proc = subprocess.Popen(["curl", "-H", "Content-Type: application/json", "-d", json.dumps({"ndbno":ndbno,"type":"f"}), "eFg7QhZRitIkCNrIfU0kDuFgfyXnkxlv4nQXAt2X@api.nal.usda.gov/ndb/reports"], stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    calories_dict = next((item for item in ast.literal_eval(out)["report"]["food"]["nutrients"] if item["unit"] == "kcal"), None)
    calories = calories_dict["measures"][0]["value"]
    nutrition_dict = {"calories" : calories}
    return nutrition_dict

get_nutrition_data("21350")

#curl -H "Content-Type: application/json" -d '{"q":"butter","max":"25","offset":"0"}' eFg7QhZRitIkCNrIfU0kDuFgfyXnkxlv4nQXAt2X@api.nal.usda.gov/ndb/search
#curl -H "Content-Type:application/json" -d '{"ndbno":"01009","type":"f"}' eFg7QhZRitIkCNrIfU0kDuFgfyXnkxlv4nQXAt2X@api.nal.usda.gov/ndb/reports