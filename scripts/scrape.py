#!/usr/bin/env python
import urllib
import urllib2
from lxml import etree
import StringIO
import re, sys, os
# import request
from PIL import Image



sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_states.settings")

from main.models import State, StateCapital
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
#result = urllib.urlopen("http://164.100.47.132/LssNew/Members/Alphabaticallist.aspx")

result = urllib.urlopen("http://www.50states.com/")

html = result.read()

parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(html), parser)

# xpath = "//table[@id='ctl00_ContPlaceHolderMain_Alphabaticallist1_dg1']/tr/td/img/@src"  #/child::text()

# xpath1 = "//table[@id='Table2']/tr/td/a/child::text()"

# xpath2 = "////table[@id='Table2']/tr/td/a/@href"

xpath3 = "//*[@id='ar-full-homepage']/div/ul/li/a/@href"


filtered_html3 = tree.xpath(xpath3)


links = [html for html in filtered_html3 if 'htm' in html]

print links

for link in links:
    state_name_pattern = "(?<=\W)[^.]*(?=.htm)"

    state_name_search = re.search(state_name_pattern, link)

    state_name = "%s" % state_name_search.group()


    print "#### %s #####" % state_name.strip('new')


    try:
        state_object, created = State.objects.get_or_create(name__icontains=state_name.strip('new'))
    except:
        state_object = State.objects.filter(name__icontains=state_name.strip('new')).first()

    print created

    #print "http://www.50states.com/%s" % link
    state_page = urllib.urlopen("http://www.50states.com%s" % link)

    state_page_html = state_page.read()

    tree   = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_population_xpath = '//*[@id="collapseQuick-Facts"]/div/ul/li[6]/div/text()'

    state_population_string = tree.xpath(state_population_xpath)
    state_population_pattern = "([\d]+),([\d]+),([\d]+)"
    cleaned_pop_string = re.search(state_population_pattern, "%s" % state_population_string)

    try:
        print cleaned_pop_string.group()
        state_object.population = "%s" % cleaned_pop_string.group()
        try:
            state_object.save()
        except:
            print state_object.name
    except AttributeError:
        print "no groups"

    state_map_link_xpath = '//*[@id="collapseGovernment"]/div/ul/li[2]/div/a/@href'
    state_map_link = tree.xpath(state_map_link_xpath)


    state_page = urllib.urlopen(state_map_link[0])

    state_page_html = state_page.read()

    tree = etree.parse(StringIO.StringIO(state_page_html), parser)

    state_map_image_link = '/html/body/img/@src'

    state_map_image = tree.xpath(state_map_image_link)


    print "STATE MAP IMAGE LINK %s" % 'http://quickfacts.census.gov%s' % state_map_image[0]

    url = 'http://quickfacts.census.gov%s' % state_map_image[0]
    image_response = urllib2.urlopen(url).read()

    img_temp = NamedTemporaryFile(delete=True)

    img_temp.write(image_response)

    state_object.state_map.save('tmpimage.gif', File(img_temp))

        # img = StringIO.StringIO(image_response)
        #img = Image.open(StringIO.StringIO(image_response.content))

        # image_file = open('temp.gif', 'wb')

        # for block in image_response.iter_content(1024):
        #   image_file.write(block)



    # image = urllib.URLopener()
    
    #   f = open(StringIO.StringIO(), 'wb')
    #     f.write(chunk)
    
    #    = f
    #   state_object.save()

# ([\d{0,2}])(,\d{0,3})

# ^([0-9]+,)*[0-9]+$



# state_page_result = state_page.read()
# for html in filtered_html3:
#   # if '.html' in html:
#   print html


# print filtered_html3
# !/usr/bin/env python

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