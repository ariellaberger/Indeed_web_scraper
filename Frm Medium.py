import re
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen


FULL_TIME = 'full%20time&l=New%20York'
PART_TIME = 'part%20time&l=New%20York'
CONTRACT = 'contract&l=New%20York'
INTERNSHIP = 'internship&l=New%20York'
TEMPORARY = 'temporary&l=New%20York'
COMMISSION = 'commission&l=New%20York'


def get_clean_text(website):
    """
    this function scrape the page and cleans the required text
    :param webpage
    :return text
    """
    try:
        site = urlopen(website).read()
    except:
        return

    soup_obj = BeautifulSoup(site, features='html5lib')
    text = soup_obj.find("div", attrs={"id": "jobDescriptionText", "class": "jobsearch-jobDescriptionText"})

    if text:
        text = soup_obj.find("div",
                             attrs={"id": "jobDescriptionText", "class": "jobsearch-  jobDescriptionText"}).get_text()

        lines = (line.strip() for line in text.splitlines())
        text = " ".join(line for line in lines if line)
        text = text.lower().split()

        stop_words = set(stopwords.words("english"))
        text = [w for w in text if w not in stop_words]
        return " ".join(text)
    else:
        return


def get_jobs_by_type(job_type=None):
    """
    this function extracts the jobs from indeed page using param   job_type
    :param job_type
    :return jobs
    """
    final_site_list = ['http://www.indeed.com/jobs?q=', job_type]
    final_site = "".join(final_site_list)

    base_url = "http://www.indeed.com"

    try:
        # Open up the front page of our search first
        html = urlopen(final_site).read()
    except:
        "That city/state combination did not have any jobs. Exiting   . . ."
        return
    soup = BeautifulSoup(html, features="html5lib")

    # Find jobs count
    num_jobs_area = soup.find(id='searchCount').text

    job_numbers = re.findall(r'\d+', num_jobs_area)

    if len(job_numbers) >= 3:
        total_num_jobs = (int(job_numbers[1]) * 1000) + int(job_numbers[2])
    else:
        total_num_jobs = int(job_numbers[1])

    # Total jobs
    print("There were", total_num_jobs, "jobs found,")
    num_pages = int(total_num_jobs / 10)
    job_descriptions = []

    for i in range(1, num_pages + 1):
        print('Getting page', i)
        start_num = str(i * 10)
        current_page = ''.join([final_site, '&start=', start_num])

        html_page = urlopen(current_page).read()

        page_obj = BeautifulSoup(html_page, features="html5lib")
        job_link_area = page_obj.find(id='resultsCol')

        job_URLS = [base_url + link.get('href') for link in
                    job_link_area.find_all('a', href=True)]

        job_URLS = list(filter(lambda x: 'clk' in x, job_URLS))

        for j in range(0, len(job_URLS)):
            final_description = get_clean_text(job_URLS[j])
            if final_description:
                job_descriptions.append(final_description)
            sleep(3)

    print("There were", len(job_descriptions), "jobs successfully found.")

    return job_descriptions


ft = get_jobs_by_type(job_type=FULL_TIME)
ft_count = ["FULL_TIME"] * len(ft)
full_time = pd.DataFrame({"description": ft, "job_type": ft_count})
full_time.to_csv("full_time.csv", index=False)

pt = get_jobs_by_type(job_type=PART_TIME)
pt_count = ["PART_TIME"] * len(pt)
part_time = pd.DataFrame({"description": pt, "job_type": pt_count})
part_time.to_csv("part_time.csv", index=False)

cont = get_jobs_by_type(job_type=CONTRACT)
cont_count = ["CONTRACT"] * len(cont)
contract = pd.DataFrame({"description": cont, "job_type": cont_count})
contract.to_csv("contract.csv", index=False)

intern = get_jobs_by_type(job_type=INTERNSHIP)
intern_count = ["INTERN"] * len(intern)
internship = pd.DataFrame({"description": intern, "job_type": intern_count})
internship.to_csv("internship.csv", index=False)

temp = get_jobs_by_type(job_type=TEMPORARY)
temp_count = ["TEMPORARY"] * len(temp)
temporary = pd.DataFrame({"description": temp, "job_type": temp_count})
temporary.to_csv("temporary.csv", index=False)

comm = get_jobs_by_type(job_type=COMMISSION)
comm_count = ["COMMISSION"] * len(comm)
commission = pd.DataFrame({"description": comm, "job_type": comm_count})
commission.to_csv("commission.csv", index=False)

frames = [full_time, part_time, contract, internship, temporary, commission]
total = pd.concat(frames)

total.to_csv("indeed_jobs.csv", index=False)