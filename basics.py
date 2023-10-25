# Web Scraping

from bs4 import BeautifulSoup

with open('sample.html', 'r') as html_file:
    content = html_file.read()

    # Display the contents of the html file.
    # print(content)

    soup = BeautifulSoup(content, 'lxml')

    # Display the content using parser method 'lxml' & prettify the text
    # print(soup.prettify())

    # To fetch the desired part of code from the file (Scraping):-

    # 1. To get the first value from the desired file:
    # courses_list = soup.find('h5')

    # 2. To get all the values containing the specified keyword:
    courses_list = soup.find_all('h5')
    print(courses_list)

    # Obtaining required information

    for courses in courses_list:
        print(courses.text)
