from bs4 import BeautifulSoup
import pandas as pd
import requests

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html,'html5lib')
print(soup.prettify())

title_object = soup.title

print("title object:",title_object)
print('title object type',type(title_object))

tag_object = soup.h3
print(tag_object)

tag_child = tag_object.b
print(tag_child)

parent_tag = tag_object.parent
print(parent_tag)

sibling1 = tag_object.next_sibling
print(sibling1)

sibling2 = sibling1.next_sibling
print(sibling2)

# printing stephan currys salary
sibling3 = sibling2.next_sibling
print(sibling3)

tag_child['id']
tag_child.attrs

tag_string = tag_child.string
print(tag_string)
type(tag_string)

# Another method to get string from object
unicode_string = str(tag_string)
print(unicode_string)

# Downloading and Scraping Contents of a Web Page
url = "http://www.ibn.com"
data = requests.get(url).text

soup = BeautifulSoup(data,"html5lib")

for link in soup.find_all('a',href=True):
    print(link.get('href'))

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

#scraping using pandas

website = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
tables = pd.read_html(website)
print(tables)
print(tables[0])







