<<<<<<< HEAD
""""
This is master file for the Indeed web scraping project

"""

# TODO Andrey- list of URLs
# TODO AB- BS to scrape typical URL, using example https://www.indeed.com/viewjob?jk=76e4ebb16b02d47e&tk=1eb150gi42vt9000&from=serp&vjs=3

# below playing around with code to get it

from bs4 import BeautifulSoup
import requests, lxml
import pandas as pd
import time

list_of_urls1=['https://www.indeed.com/viewjob?jk=3821b20f5fe48ed7&tk=1eb3ago1d355l000&from=serp&vjs=3']

list_of_urls=['https://www.indeed.com/viewjob?jk=3821b20f5fe48ed7&tk=1eb3ago1d355l000&from=serp&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=cfaa5924b0627414&fccid=f5d2b93913542fa6&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=0b53b6007e1edb74&fccid=492d639d336fa9f3&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=0b7e5a4366f21e54&fccid=dc8fcc75cbbbd654&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=bbe0c267c12f93f4&fccid=9d58b2ccf32109ad&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=be33aa48ac4a387f&fccid=55a2bdb0a91b873d&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=4fbc59d736aac3c6&fccid=ae6e171391e978d5&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=dbd5f44b23485050&fccid=ae6e171391e978d5&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=4fbf696a56cacd4a&fccid=8765a4045377753a&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=9392d6c5172f2c55&fccid=6cfed7f3cd9dba94&vjs=3']


print(list_of_urls1)

def make_soup(single_url):
    base_url = requests.get(single_url)
    object_ = base_url.text
    soup_ = BeautifulSoup(object_, 'lxml') #storing into a variable
    return soup_

# def show_title_(soup_input):
#     title_ = soup_input.title.text
#     return title_
def show_text_(soup_input):
    text_ = soup_input.text
    return  text_

def find_title_(soup_):
    class__ = "icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"
    tag__ = 'h3'
    return soup_.find(tag__, class_= class__).text



def find_co(soup_):
    try:

        class__='icl-NavigableContainer-innerContainer'
        tag__='div'
        res= soup_.find(tag__, class_= class__).text
        res=res.strip('reviewsRead what people are saying about working here.')
        res = res.strip(num_reviews(page_soup)) # TODO clear up

        return res
    except:
        return None

def job_desc(soup_):
    try:
        text_ = soup_.find("div", attrs={"id": "jobDescriptionText", "class": "jobsearch-jobDescriptionText"}).text

        # class__='jobsearch - jobDescriptionText'
        # tab__='div'
        # res = soup_.find(tag__, class_=class__).text
        # return res
        return text_
    except:
        None

def num_reviews(soup_):
    try:
        class__='icl-Ratings-count'
        tag__='div'
        res= soup_.find(tag__, class_= class__).text.strip(' reviews')
        return res
    except:
        return None

def score(soup_):
    try:
        class__="icl-Ratings-starsCountWrapper"
        tag__='div'
        res = soup_.find(tag__, class_=class__)
        res=str(res)
        end_posn=res.find(' out of 5',0)
        res = res[17:end_posn] #Stripping out '<div aria-label="' leaving 3 spaces for score
        # res=res.strip(' ')
        return res # TODO convert to an integer- issues.

    except:
        return None

def locn(soup_):
    try:
        res=str(page_soup.title.text).strip(strip_from_locn).strip(' -  ').strip(' - Indeed.com')
    # TODO In absence of obvious clean way, manipulated page_soup.title.text
        return res
    except:
        return None



def employee_reviews_link(soup_):
    try:
        class__='icl - Ratings - link'
        tag__='href'
        res = soup_.find(tag__, class_=class__)
        res = str(res)

        return res
    except:
        none

def get_urls_in_page(soup_):
    res_=[]
    for link in soup_.find_all('a'):
        res= link.get('href')
        res_.append(res)
    return res_
number_urls=len(list_of_urls)-1

# run a loop in titles and text
# for index in range(number_urls):
for index in range(10):
    page_soup = make_soup(list_of_urls[index]) #  parsed html on page, set to a variable
    # print (page_soup.prettify())
    title_again = find_title_(page_soup)
    strip_from_locn= str(title_again)
    loc=locn(page_soup)
    co= find_co (page_soup)
    num_reviews_=num_reviews(page_soup)
    score_=score(page_soup)
    employ_reviews_link =employee_reviews_link(page_soup)
    urls_in_page=get_urls_in_page(page_soup)
    job_desc_=job_desc(page_soup)

    # loc=locn(page_soup)
    print('find_title_:', title_again)
    print(' find_co: ',co)
    print(' num_reviews: ', num_reviews_)
    print(' score_: ',score_)
    print(' locn: ',loc)
    print('employ reviews link', employ_reviews_link)
    print('urls_in_page',urls_in_page)
    print('\n')
    print('job_desc_',job_desc_)
    print('\n')

=======
""""
This is master file for the Indeed web scraping project

"""

# TODO Andrey- list of URLs
# TODO AB- BS to scrape typical URL, using example https://www.indeed.com/viewjob?jk=76e4ebb16b02d47e&tk=1eb150gi42vt9000&from=serp&vjs=3

from bs4 import BeautifulSoup
import requests, lxml

# import html5lib


list_of_urls=['https://www.indeed.com/viewjob?jk=3821b20f5fe48ed7&tk=1eb3ago1d355l000&from=serp&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=cfaa5924b0627414&fccid=f5d2b93913542fa6&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=0b53b6007e1edb74&fccid=492d639d336fa9f3&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=0b7e5a4366f21e54&fccid=dc8fcc75cbbbd654&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=bbe0c267c12f93f4&fccid=9d58b2ccf32109ad&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=be33aa48ac4a387f&fccid=55a2bdb0a91b873d&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=4fbc59d736aac3c6&fccid=ae6e171391e978d5&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=dbd5f44b23485050&fccid=ae6e171391e978d5&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=4fbf696a56cacd4a&fccid=8765a4045377753a&vjs=3',\
              'https://www.indeed.com/rc/clk?jk=9392d6c5172f2c55&fccid=6cfed7f3cd9dba94&vjs=3']


print(list_of_urls)

def make_soup(single_url):
    base_url = requests.get(single_url)
    object_ = base_url.text
    soup = BeautifulSoup(object_, 'lxml')
    return soup

def show_title_(soup_input):
    title_ = soup_input.title.text
    return title_
def show_text_(soup_input):
    text_ = soup_input.text
    return  text_

number_urls=len(list_of_urls)-1

# run a loop in titles and text
for index in range(number_urls):
    soup__=make_soup(list_of_urls[index])
    title__=show_title_(soup__)
    text__= show_text_(soup__)
    print(title__, '\n', text__, '___________________________________')


"""base_url3=requests.get('https://www.indeed.com/jobs?q=data%20scientist&l=united%20States&vjk=3821b20f5fe48ed7')
base_url2 = requests.get('https://www.indeed.com/jobs?q=data%20scientist&l=united%20States&vjk=0b53b6007e1edb74')
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
# print(match1)
print(match2)
# print(match3)


def extract_title_district_state_zip(text_):
    list1_=[]
    list2_ = []
    list1_=(text_.split(",")[0])
    title_=((list1_.split("-")[0])).strip()
    district_=((list1_.split("-")[1])).strip()

    list3_ = ("list3",text_.split(",")[0])
    list4_ = (text_.rsplit(","))
    US_state=list4_[1][1:3]
    zip_code = list4_[1][4:10]

    print("list4",list4_)
    print("list1_",list1_)
    print("text_", text_)
    print("title",title_)
    print("district",district_)
    print('US_state',US_state)
    print('zip_code',zip_code)

extract_title_district_state_zip(match2)"""
>>>>>>> f4bfeada34cf2244310beb9e3734f3e64e7cbf5b
