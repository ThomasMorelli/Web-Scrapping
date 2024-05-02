import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

x = random.randint(1,21)
if x<10:
    x = f"0{x}"

webpage = f"https://ebible.org/asv/JHN{x}.htm"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)


page_verses = soup.findAll('span', class_='verse')

random_verse_element = random.choice(page_verses)
random_verse_text = random_verse_element.nextSibling


print(random_verse_text)

