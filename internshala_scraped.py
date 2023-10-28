from bs4 import BeautifulSoup

import requests

url = 'https://internshala.com/internships/machine-learning-internship/'

info= requests.get(url).text

soup = BeautifulSoup(info,'lxml')

jobs = soup.find_all('div', class_ = 'internship_meta')

for count,job in enumerate(jobs):
    company = job.find('h4',class_ = 'heading_6 company_name').text
    role = job.find('h3', class_ = 'heading_4_5 profile').text

    print(f'{count}.')
    print(f"Company_Name -> {company.strip()}")
    print(f"Job_Role -> {role.strip()}")

    print('')