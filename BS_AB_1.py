from bs4 import BeautifulSoup
import requests, lxml

# import html5lib

base_url = requests.get('https://www.indeed.com/viewjob?jk=76e4ebb16b02d47e&tk=1eb150gi42vt9000&from=serp&vjs=3')
object_ = base_url.text
soup = BeautifulSoup(object_, 'lxml')
#print(soup.prettify())
# looking at the webpage formatted with heirarchy
match1 = soup.text
match2 = soup.title.text
# match3 = soup.p.text
# adding .title extracts text with <title> at begining and end of text
# adding .text extracts the text and loses the title
print(match1)
print(match2)
# print(match3)

# taking the title, Note format.. [JOB TITLE} - [[District]', ',[US STATE]' - ', 'Indeed.com']
# presumably indeed.com is the orignal advertiser?


def job__title():
    # extract from title
    return
    pass


def workplace():
    # extract from title
    return
    pass


def district():
    # extract from title
    return
    pass


def state():
    # extract from title
    return
    pass


def zip_code():
    # extract from title
    return
    pass


def reviews():
    return
    pass


def number_of_reviews():
    return
    pass


def apply_co_website():
    return
    pass


def how_long_poste():
    return
    pass


def url_to_pay_per_location():
    return
    pass


def main_text():
    return
    pass


def parse(full_url):
    """begin by defining a function named “parse” requiring one argument
     which will be the actual URL of the page we are attempting to parse/scrape.
      Next, we’ll use the BeautifulSoup class creator to parse the content (HTML code)
      of the provided website. We’ll use the “lxml” parser just in case the HTML
      is not perfectly formed."""

    pass


"""with open('simple.html') as html_file:
    # For the time being i saved an html file that is typical of the Indeed.com
    # website into the same folder as this python file.
    # Saved it as simple.html. URL below:
    # https://www.indeed.com/viewjob?jk=76e4ebb16b02d47e&tk=1eb150gi42vt9000&from=serp&vjs=3
    soup=BeautifulSoup(html_file, 'lxml')
    # passing in the html file for parsing,specifying in 2nd arg the parser



print(soup)
# print to see what we have
"""
