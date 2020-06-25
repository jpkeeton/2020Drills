# import the libraries
import requests
from bs4 import BeautifulSoup
import logging
logging.warning('this is a warning!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

# create a variable for the site
url = 'http://quotes.toscrape.com'

# create the request
response = requests.get(url)


# 'response.text' returns the content of the response
    # basically response just returns the content
# we'll include the lxml parser
soup = BeautifulSoup(response.text, 'lxml')




# let's see if it worked correctly by printing soup
# soup
# or
print(soup)
