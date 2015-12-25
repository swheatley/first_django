#!/usr/bin/env python

import csv
import sys
import os


sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import State, StateCapital

#state = State.objects.all().order_by('-pop')
#for state in states:
#   print state.name

#states = States.objects.all().exclude(name__contains='N')
#states = States.objects.all().exclude(name__istartswith='N')
#for state in states
#    print state.name

#states = State.objects.all().values('name', 'pop')

#for state in states:
#    print states


#states = State.objects.all().values_list('name','abbrev')


#for state in states:
#   print " State Name: %s, State Abbreviation %s" % (state[0], state[1])

#states = State.objects.all().values_list("name", "abbrev", "pop")

#for name, abbrev, pop in states:
#    print "Name: {0}, Abbrev: {1}".format(abbrev, name)
    
#states=State.objects.all().exclude(name__startswith='N').filter(pop__gte=100000).order_by('-pop').values_list('name','pop')
#
#for state in states:
    #print "%s %s" %(state.name, state.pop)
    #for list in list:
    #   print "%s %s" % (state[0], state[1])

 #   states_list = ['Texas', 'California', 'Nevada']
 #  states = State.objects.filter(name__in=states_list)
 #  print states


#state = State.objects.get(name='Alabama')

#print state.name

state = State.objects.get(pk=153)
cap = StateCapital.objects.get(pk=1)

print state.name
print cap.name

state.statecapital_set.add(cap)
cap.state.add(state)

print state.capital_set.all()

try:
        state_obj = State.objects.get(abbreviation=row['state'])
except:
    print row['state']

    new_city, created = City.objects.get_or_create(name=row['city'], state=state_obj)
    new_city.county = row['county']
    new_city.latitude = row['latitude']
    new_city.longitude = row['longitude']

    try:
        new_city.save()
    except Exception, e:
        print e
        print new_city.county
        print new_city.latitude
        print new_city.longitude



