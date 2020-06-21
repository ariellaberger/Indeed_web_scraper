import pandas as pd
import requests
from bs4 import BeautifulSoup

def parse_position_page(single_url):
    HEADERS = {
             'User-Agent': 'My User Agent 1.0',
              'From': 'youremail@domain.com'
              }
    html = requests.get(single_url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    try:
        job_descriptoin = soup.find(name="div", attrs={"id": "jobDescriptionText"}).text
    except:
        job_descriptoin = 'None'
    print(job_descriptoin)
    try:
        starturl = soup.find("a", string = "original job").attrs['href']
        req = urllib.request.Request(starturl, None, HEADERS)
        res = urllib.request.urlopen(req)
        url = res.geturl()
    except:
        url = 'None'
    print(url)
url = 'https://www.indeed.com/rc/clk?jk=cfaa5924b0627414&fccid=f5d2b93913542fa6&vjs=3'
parse_position_page(url)