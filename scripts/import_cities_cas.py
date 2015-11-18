#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import City, State, CityCas

from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster

City.objects.all().delete()

states = State.objects.all()
# states = State.objects.all()

# for state in states:
# print state.name

print os.path.abspath(__file__)

# print os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cities.csv"

# print "%s/%s" % (dir_name, file_name)

# print os.path.join(dir_name, file_name)

cities_csv = os.path.join(dir_name, file_name)

csv_file = open(cities_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:

    city = unidecode(row['name'])

    print city

    city = unidecode(row['name'])
    session = cluster.connect() 
    city2 = CityCas(name=city)
    city2.save()

    cluster.shutdown()



    # #try:
    #     state_obj = State.objects.get(abbrev=row['state'])
    # except:
    #     print row['state']


    # new_city, created = City.objects.get_or_create(name=row['city'], state=state_obj)
    
    # new_city.zip_code = row['zip_code']
    # new_city.lat = row['latitude']
    # new_city.lon = row['longitude']
    # new_city.county = row['county']
    # new_city.save()

    # try:
    #     new_city.save()
    # except Exception, e:
    #     print e
    #     print new_city.county
    #     print new_city.latitude
    #     print new_city.longitude

    # print new_city.name
    # print created
    # # new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    # # new_capital.lat = row['latitude']
    # # new_capital.lon = row['longitude']
    # # new_capital.coun = row['county']

    # # new_city.state = new_city
    # try:
    #     new_city.save()
    # except Exception, e:
    #     print "major fail"    