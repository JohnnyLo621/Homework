import requests
import bs4
import csv

def check_expected_result(src, html_section, content):
    root = bs4.BeautifulSoup(requests.get(src).text, 'html.parser')
    head = root.find(html_section.split('.')[0])
    title = head.find_next(html_section.split('.')[1])
    if content in title.text:
        print('The expected result is right.')
    else:
        print('The expected result is incorrect.')

with open('data/data.csv', newline='', encoding='UTF-8-sig') as csvfile:
    rows = csv.DictReader(csvfile)
    for cell in rows:
        src = cell['url']
        htmlSection = cell['html_section']
        content = cell['expected_content']
        check_expected_result(src, htmlSection, content)


