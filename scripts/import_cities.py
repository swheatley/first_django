#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


from main.models import State, StateCapital, City

print os.path.abspath(__file__)

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv") 

csv_file_path = open(cities_csv, 'r')

reader = csv.DictReader(csv_file_path)

for row in reader:
   


    new_city, created = City.objects.get_or_create(name=row['city'])

    new_city.county = row['county']
    new_city.latitude = row['latitude']
    new_city.zip_code = row['zip_code'] 
    new_city.longitude = row['longitude'] 
    try:
        state = State.objects.get(abbrev=row['state'])
        new_city.state = state
    except Exception, e:
        print e

    try:
        new_city.save()
    except Exception, e:
        print e

    