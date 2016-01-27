
# !/usr/bin/env python

import urllib
import urllib2
import StringIO
import re, sys, os
from lxml import etree

sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from main.models import State
#open
result = urllib.urlopen('http://www.50states.com/')
#read
html = result.read()

parser = etree.HTMLParser()

tree = etree.parse(StringIO.StringIO(html), parser)


href_xpath = '//*[@id="ar-full-homepage"]/div/ul/li/a/@href'

filtered_html = tree.xpath(href_xpath)

link_list = []

# for link in filtered_html:
#     if 'htm' in link:
#         link_list.append(link)

#print link_list
#print '-'*10

#Shorter version = list comprehension
links = [link for link in filtered_html if 'htm' in link]
#print links

for link in links:
    state_page = urllib.urlopen("http://www.50states.com/%s"% link)
    #print state_page.read()

    state_page_html = state_page.read()

    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_abbrev_xpath='//*[@id="content"]/div[1]/div[2]/div/div[1]/h1/text()'
    state_abbrev_xpath_list=tree.xpath(state_abbrev_xpath)
    #print state_abbrev_xpath_list

    state_abbrev_string = state_abbrev_xpath_list[0]
    state_abbrev = state_abbrev_string.split('(')[1].split(')')[0]
    state_name = state_abbrev_string.split('(')[0].replace(" ", "")


    state_nick_name_xpath= '//*[@id="collapseQuick-Facts"]/div/ul/li[5]/div/a/text()'
    state_nick_name=tree.xpath(state_nick_name_xpath)[0]

    try:
        state_bird_xpath='//*[@id="collapseFacts"]/div/ul/li[2]/div/text()'
        state_bird_xpath_list = tree.xpath(state_bird_xpath)
        state_bird = state_bird_xpath_list[0].replace(' |', '')
    except Exception, e:
        print e

    state_statehood_date_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/a/text()'
    state_statehood_date=tree.xpath(state_statehood_date_xpath)[0]
    print state_statehood_date
    state_statehood_num_xpath='//*[@id="collapseQuick-Facts"]/div/ul/li[1]/div/text()'
    state_statehood_num = tree.xpath(state_statehood_num_xpath)[0].replace(' (', '').replace(')', '')
    print state_statehood_num
    state_statehood = state_statehood_date + ' | ' + state_statehood_num
    print state_statehood

#HELP?
    state_flag_link_xpath = '//*[@id="content"]/div[1]/div[3]/div/a[2]/div/div/div[1]/img/@src'
    #finds

    try:

        state_flag_link = tree.xpath(state_flag_link_xpath)[0]
        print state_flag_link
        url = 'http://www.50states.com/%s'%state_flag_link
        image_response = urllib2.urlopen(url).read()

        img_temp = NamedTemporaryFile(delete = True)

        img_temp.write(image_response)
        try:
            state_object.flag.save('flag_image.gif', File(img_temp))
        except Exception, e:
            print e
        

    except Exception, e:
        print e


        

    print state_name
    #state_name_pattern = "(?<=\W).*(?=.htm)"
    #state_name_search= re.search(state_name_pattern, link)
    #state_name = '%s' % state_name_search.group()
    #use the xpath to the abbrevation
    #use a get instead of a filter to find the state object
    state_object= State.objects.get(abbrev=state_abbrev)

    state_population_xpath="//*[@id='collapseQuick-Facts']/div/ul/li[6]/div/text()"

    state_population_xpath_list=tree.xpath(state_population_xpath)
    # state_population_xpath_list
    try: 
        state_pop_string = (state_population_xpath_list)[0].replace(',', '').split(';')[0]
        #print state_pop_string
    except Exception, e:
        print e

    #no spaces in pattern
    #how can I clean up the string so regex is more simple?
    #['38,332,521; Rank: 1 of 50 | ', '\r\n']
    #look at strip and replace to clean up string
    # state_population_pattern = '\d+,\d+,\d+'
    # cleaned_pop_string = re.search(state_population_pattern, '%s' % state_population_string)

    #ALREADY CLEANED
    try:
        #print state_pop_string
        state_object.pop = state_pop_string
        state_object.nick_name = state_nick_name
        state_object.bird = state_bird
        state_object.statehood = state_statehood
        print state_object.bird
        state_object.save()
    except AttributeError, e:
        print e

    #open page, read page, parse page
    #get link
    #clean up
    state_map_link_xpath = '//*[@id="collapseGeography"]/div/ul/li[4]/div/a/@href'
    #finds

    try:

        state_map_link = tree.xpath(state_map_link_xpath)[0]
        #print state_map_link

        

    except Exception, e:
        print e

    state_map_page = urllib.urlopen(state_map_link)

    state_map_page_html = state_map_page.read()

    tree = etree.parse(StringIO.StringIO(state_map_page_html), parser)

    image_link_xpath = '//*[@id="innerPage"]/img/@src'

    state_map_image = tree.xpath(image_link_xpath)[0]


    url = 'http://quickfacts.census.gov/%s' % state_map_image

    image_response = urllib2.urlopen(url).read()

    img_temp = NamedTemporaryFile(delete = True)

    img_temp.write(image_response)
    try:
        state_object.state_map.save('map_image.gif', File(img_temp))
    except Exception, e:
        print e
#!/usr/bin/env python

# # import urllib
# import urllib2

# from lxml import etree
# import StringIO
# import re, sys, os

# sys.path.append('..')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

# from django.core.files import File
# from django.core.files.temp import NamedTemporaryFile

# from main.models import State

# result = urllib.urlopen('http://www.50states.com/')

# html = result.read()

# parser = etree.HTMLParser()

# tree = etree.parse(StringIO.StringIO(html), parser)

# href_xpath = "//*[@id='ar-full-homepage']/div/ul/li/a/@href"

# filtered_html = tree.xpath(href_xpath)

# links = [link for link in filtered_html if 'htm' in link]

# for link in links:
#     # print "loop"
#     state_name_pattern = "(?<=\W).*(?=.htm)"
#     state_name_search = re.search(state_name_pattern, link)
#     state_name = "%s" % state_name_search.group()
#     # use the xpath to the abbreviation to get the abbreviation
#     # use a get instead of a filter to find the state object
#     state_object = State.objects.filter(name__icontains=state_name.strip('new').strip('nc').strip('wv')).first()

#     state_page = urllib.urlopen("http://www.50states.com/%s" % link)

#     state_page_html = state_page.read()

#     tree = etree.parse(StringIO.StringIO(state_page_html), parser)

#     state_population_xpath = "//*[@id='collapseQuick-Facts']/div/ul/li[6]/div/text()"

#     state_population_string = tree.xpath(state_population_xpath)
    
#     cleaned_string = ''
    
#     for letter in state_population_string:
#         if letter == '':
#             cleaned_string = cleaned_string + letter
        
        

# # return int(value)
# # ValueError: invalid literal for int() with base 10: "['4,833,722; Rank: 23 of 50 | ']"

#     # how can I clean up this string so the regex is more simple?
#     # ['735,132; Rank: 47 of 50 | ', '\r\n\r\n']
#     # look at strip and replace to clean up this string
#     # print state_population_string
#     state_population_pattern = "(.+)"
#     cleaned_pop_string = re.search(state_population_pattern, '%s' % state_population_string)

#     try:
#         # print cleaned_pop_string.group()
#         state_object.pop = cleaned_pop_string.group()
#         state_object.save()

#     except AttributeError, e:
#         pass

#     state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'
#     # my_list = [1,2,3]
#     # my_list[0]

#     try:
#         state_map_link = tree.xpath(state_map_link_xpath)[0]
#     except Exception, e:
#         print e

#     state_map_page = urllib.urlopen(state_map_link)

#     state_map_page_html = state_map_page.read()

#     tree = etree.parse(StringIO.StringIO(state_map_page_html), parser)

#     image_link_xpath = '//*[@id="innerPage"]/img/@src'

#     state_map_image = tree.xpath(image_link_xpath)[0]

#     url = 'http://quickfacts.census.gov/%s' % state_map_image

#     image_response = urllib2.urlopen(url).read()
#     img_temp = NamedTemporaryFile(delete=True)
#     img_temp.write(image_response)

#     try:
#         state_object.state_map.save('map_img.gif', File(img_temp))
#     except Exception, e:
#         print e





#         