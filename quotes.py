import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as go
import plotly.io as pio

url = 'https://quotes.toscrape.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

author_quotes = {}
quotes = []
authors = {}
tags = []

for page in range(1, 11):
    response = requests.get(f"{url}page/{page}/")
    soup = BeautifulSoup(response.text, 'html.parser')
    for quote in soup.find_all(class_='quote'):
        text = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        quotes.append(text)
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1
        tags.extend(tag.get_text() for tag in quote.find_all('a', class_='tag'))
        if author in author_quotes:
            author_quotes[author].append(text)
        else:
            author_quotes[author] = [text]

most_quotes_author = max(authors, key=authors.get)
least_quotes_author = min(authors, key=authors.get)

authors_quotes_count = {author: len(quotes) for author, quotes in author_quotes.items()}

for author, count in authors_quotes_count.items():
    print(f"{author}: {count} quotes")

avg_quote_length = sum(len(quote) for quote in quotes) / len(quotes)
longest_quote = max(quotes, key=len)
shortest_quote = min(quotes, key=len)

tag_counts = {}
for tag in tags:
    if tag in tag_counts:
        tag_counts[tag] += 1
    else:
        tag_counts[tag] = 1

most_pop_tag = max(tag_counts, key=tag_counts.get)
total_tags = len(tag_counts)

print("\n")
print(f"Most Quotes Author: {most_quotes_author}")
print(f"Least Quotes Author: {least_quotes_author}")
print("\n")
print(f"Average Quote Length: {avg_quote_length}")
print(f"Shortest Quote: {shortest_quote}")
print(f"Longest Quote: {longest_quote}")
print("\n")
print(f"Most Popular Tag: {most_pop_tag}")
print(f"Total Tags: {total_tags}")

sorted_authors = sorted(authors_quotes_count.items(), key=lambda x: x[1], reverse=True)[:10]
author_names = [author[0] for author in sorted_authors]
quote_count = [author[1] for author in sorted_authors]