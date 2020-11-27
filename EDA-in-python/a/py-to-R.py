#!/usr/bin/python3
import json
import pickle
l2 = json.load(open("Modeling.ipynb", "r"))
replace = pickle.load(open("modefication_json.pkl", "rb"))
l2['metadata'] = replace
json.dump(l2, open("Modeling.ipynb", "w"))
