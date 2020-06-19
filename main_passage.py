from bs4 import BeautifulSoup
import requests
import urllib
from urllib.parse import urljoin
import random
from time import sleep
import pandas as pd


def parse_positions_from_page(input_url):
    html = requests.get(input_url)
    soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
    df = pd.DataFrame(columns=["Title", "Location", "Company", "Salary", "Synopsis", "URL"])

    for each in soup.find_all(class_="result"):
        try:
            title = each.find(class_='jobtitle').text.replace('\n', '')
        except:
            title = 'None'

        try:
            location = each.find('span', {'class': "location"}).text.replace('\n', '')
        except:
            location = 'None'

        try:
            company = each.find(class_='company').text.replace('\n', '')
        except:
            company = 'None'

        try:
            salary = each.find('span', {'class': 'no-wrap'}).text.replace('\n', '')
        except:
            salary = 'None'

        try:
            synopsis = each.find('span', {'class': 'summary'}).text.replace('\n', '')
        except:
            synopsis = 'None'

        try:
            link = each.find('a', attrs={'class': 'turnstileLink'})
            url = "https://www.indeed.com" + link.attrs['href']
        except:
            url = 'None'

        df = df.append(
            {'Title': title, 'Location': location, 'Company': company, 'Salary': salary, 'Synopsis': synopsis,
             'URL': url}, ignore_index=True)
    return df


def parse_pages(base_url):

    START_PAGE = 10
    FINISH_PAGE = 50
    STEP = 10

    df_result = pd.DataFrame(columns=["Title","Location","Company","Salary", "Synopsis", "URL"])

    for suffix in range(START_PAGE, FINISH_PAGE, STEP):
        df_curr = parse_positions_from_page(base_url + str(suffix))
        df_result = pd.concat([df_result, df_curr], ignore_index=True)
        sleep(random.uniform(1, 3))

    return df_result


base_url = "https://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l=New+York&start="
df_res = parse_pages(base_url)


# df_res.info()
# df_res.head()


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