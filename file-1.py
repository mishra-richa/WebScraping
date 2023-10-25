# Finding Machine Learning Internships on Internshala:

from bs4 import BeautifulSoup

import requests

html_text = requests.get('https://internshala.com/internships/machine-learning-internship/').text
# print(html_text)

soup = BeautifulSoup(html_text,'lxml')
# print(soup.prettify())

role =soup.find('a', class_ = 'view_detail_button').text.replace(' ','')
# print(role)

company = soup.find('a','link_display_like_text view_detail_button').text.replace(' ','')
# print(company)

print(f"The following internship postings are listed for Machine Learning at Internshala: {role} at {company}")