# Set Imports
from splinter import Browser
from selenium import webdriver
import time
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import re
import httplib2
import csv

# User enters a web site address.
site_to_visit = input("Please enter your fully qualified domain name: ") 

# driver location
executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
# create a browser instance
browser = Browser('chrome', **executable_path, headless=True)

# add 'https://' to the front if the link doesn't start with 'http'
if not site_to_visit.startswith("http"):
    site_to_visit = "https://" + site_to_visit

# stick the user input into the visit function
print('Hold please, we\'re checking....' + site_to_visit)
browser.visit(site_to_visit)

print('Here are the links I found: ')

# html_page = urllib.request.urlopen(site_to_visit).read()
# soup = BeautifulSoup(html_page)
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     print(link.get('href'))

# ! ha! finding all the bleacher report links
# html_page = urllib.request.urlopen(site_to_visit).read()
# soup = BeautifulSoup(html_page)
# for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])
    
parser = 'html.parser' 
# you can also use lxml or html5lib
resp = urllib.request.urlopen(site_to_visit)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])
#     with open("Found Links",'w') as csvfile:
#         write = csv.writer(csvfile, delimiter = ' ')
#         write.writerows(link)

# can i stick these into an excel sheet
# https://stackoverflow.com/questions/59509411/python-selenium-csv-how-to-open-links-from-list-in-csv-file-loop-code-ap

#  with open('Found Links', 'w', newline='') as csvfile:
#     write = csv.writer(csvfile)
#     write.writerows(link)


# End test and quit browser    
print('Ending test')
browser.quit()
