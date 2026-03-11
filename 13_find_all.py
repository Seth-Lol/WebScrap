from bs4 import BeautifulSoup
import requests


website = 'https://subslikescript.com/movie/Titanic-120338'
response = requests.get(website)
content = response.text

soup = BeautifulSoup(content,'lxml')

box = soup.find('article', class_ = 'main-article')

title = box.find('h1').get_text()
transcripts  = box.find_all('p', class_ = 'cue-line')
transcript_texts = [transcript.get_text(strip=True, separator='\n') for transcript in transcripts]


with open(f'{title}_all.txt','w+') as file:
    for transcript in transcript_texts:
        file.write("%s\n" % transcript) 

print("End of the program")
