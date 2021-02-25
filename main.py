from bs4 import BeautifulSoup
# import requests
import pandas as pd
from selenium import webdriver

url = 'https://finder.bupa.co.uk/Consultant/search/?first=1&qk=&ql=&qn=&giottoFormFlag_consultant=1#start'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.151 Safari/537.36'}

#Selenium:
driver = webdriver.Chrome()
driver.get(url)

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

names=[] #List to store name of the consultant
l_user_html=[]

# driver.find_element_by_xpath('//*[@id="list"]/article[3]/div/a').click()

# html_text = requests.get(url, headers=headers).text

# soup = BeautifulSoup(html_text, 'lxml')
consultants = soup.find_all('article', class_ = 'listing male')+soup.find_all('article', class_ = 'listing female')+soup.find_all('article', class_ = 'listing company')

for consultant in consultants:
    name = consultant.find('span', attrs={'class':'copy-me'}).text
    user_html = consultant.div.a['href']

    # names.append(name.text)
    print(f"Name: {name}")
    print(f"Link: {user_html}")

    print('')