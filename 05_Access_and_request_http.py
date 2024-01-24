import requests
import os
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r = requests.get(url)

print(r.status_code)
print(r.request.headers)
print("request body:",r.request.body)
header = r.headers
print(header)
dateValue = header['date']
print(dateValue)
print(header['content-type'])
print(r.encoding)
print(r.text[0:100])

#url of an image
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r = requests.get(url)

print(r.headers)
print(r.headers['Content-Type'])
path = os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)


#Downloading a file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(),'example.txt')
r= requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

#Get Request with URL params
url_get = 'http://httpbin.org/get'
payload = {'name':'Shreyas','ID':'123'}

r=requests.get(url_get, params=payload)
print(r.url)
print(r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['content-type'])
print(r.json)
print(r.json()['args'])

#POST requests with URL 
url_post = 'http://httpbin.org/post'
r_post = requests.post(url_post,data=payload)
print("POST request URL:",r_post.url)
print("POST request body:",r_post.request.body)
print(r_post.json()['form'])

#end of python Access and Requests

