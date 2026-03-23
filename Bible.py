from bs4 import BeautifulSoup
import requests


website = 'https://www.bible.com/bible/107/GEN.1.NET'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content,'lxml')

box = soup.find("div", class_="ChapterContent-module__cat7xG__reader")
title = box.find('h1').get_text()
subtitle  = box.find("div", class_="ChapterContent-module__cat7xG__s1").get_text(strip=True, separator='\n')
transcript  = '\n'.join([span.get_text(strip=True) for span in box.find_all("span", class_="ChapterContent-module__cat7xG__content")])

with open(f'{title}.txt','w') as file:
    file.write(subtitle)
    file.write(transcript)
    

print("End of the program")