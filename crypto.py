from bs4 import BeautifulSoup
import requests

def scrape_crypto_data():
    url = 'https://coinmarketcap.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    cryptos = soup.find_all('tr', style='cursor:pointer')
    
    for crypto in cryptos[:5]:
        name = crypto.find('p', class_='sc-4984dd93-0 iWSjWE').text.strip()
        symbol = crypto.find('p', class_='coin-item-symbol').text.strip()
        price = crypto.find('span').text.strip()
        percent_change_24h = crypto.find_all('td', style="text-align:end")[1].text.strip()
        price_change_24h = crypto.find_all('td', style="text-align:end")[2].text.strip()
        
        print(f"Name: {name}")
        print(f"Symbol: {symbol}")
        print(f"Price: {price}")
        print(f"Percent Change (24h): {percent_change_24h}")
        print(f"Price Change (24h): {price_change_24h}")
        print("\n")

scrape_crypto_data()