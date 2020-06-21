
from bs4 import BeautifulSoup
import requests, lxml
import pandas as pd
import time


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

def make_soup(single_url):
    base_url = requests.get(single_url)
    object_ = base_url.text
    soup_ = BeautifulSoup(object_, features='html5lib')#'lxml') #storing into a variable
    return soup_

for index in range(3):
    try:
        page_soup = make_soup(list_of_urls[index]) #  parsed html on page, set to a variable
        print (page_soup.prettify())
        text = page_soup.find("h3", attrs={"class":"jobSectionHeader"}).text
        job_loc=page_soup.find_all()
        # "id": "jobDescriptionText", "class": "jobsearch-  jobDescriptionText",
        job_title = page_soup.find('h3',attrs={'class':'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title'}).text
        # script_ = page_soup.find("script", attrs={"body class": "miniRefresh"})
        co =page_soup.find('div', attrs={'class':"icl-u-lg-mr--sm icl-u-xs-mr--xs"}).text
        location=page_soup.find('div',{'class':"icl-u-lg-mr--sm icl-u-xs-mr--xs"})
        num_reviews=page_soup.find('div', attrs={"class":"icl-Ratings icl-Ratings--gold icl-Ratings--md"}).text[:-55]
        score=page_soup.find('div',attrs={"class":"icl-Ratings icl-Ratings--gold icl-Ratings--sm"} )
        score=str(score.contents)
        score=(score[16:19].strip()) #returns a strng
        when_posted= page_soup.find('div', attrs={"class":"jobsearch-JobMetadataFooter"}).text


        # print(text)
        print('Title',job_title)
        print('Company',co)
        print('location',location)
        print('Number reviews',num_reviews)
        print('Score out of 5', score)
        print('type', type(score), 'len', len(score))
        print('when_posted',when_posted)

    except:
        None