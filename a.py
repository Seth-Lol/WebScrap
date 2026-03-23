from bs4 import BeautifulSoup
import requests

website = 'https://www.bible.com/bible/107/GEN.1.NET'

# 1. Add headers to act like a real web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(website, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')

# 2. Safely extract the title directly from the h1 tag
h1_tag = soup.find('h1')
title = h1_tag.get_text(strip=True) if h1_tag else 'Genesis_1'

# 3. Extract the text by finding the standard Bible.com verse tags
# We bypass the randomized class names and look for elements with 'data-usfm'
verses = soup.find_all(lambda tag: tag.has_attr('data-usfm'))

# Combine all the verse text into one transcript
transcript = "\n".join([verse.get_text(strip=True) for verse in verses])

# If data-usfm tags aren't found for any reason, fallback to a broader extraction
if not transcript:
    print("Warning: Could not find verse attributes. Check if the page layout changed.")

# 4. Save to a text file
# Using encoding='utf-8' prevents errors with special characters (like smart quotes)
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)

print(f"End of the program. Saved to {title}.txt")