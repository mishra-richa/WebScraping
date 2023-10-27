# Finding Machine Learning Internships on Internshala:

from bs4 import BeautifulSoup

import requests

html_text = requests.get('https://internshala.com/internships/machine-learning-internship/').text
# print(html_text)

soup = BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

role = soup.find('h3', class_ = 'heading_4_5 profile').text.strip()

company = soup.find('div','company_and_premium').text.strip()


for count, postings in enumerate(role, start=1):
    print(f'''The following openings are available on Internshala: 
    {count}. Role: {role} 
    Company: {company}''')
    break


