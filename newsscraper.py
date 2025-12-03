import requests
import certifi
from bs4 import BeautifulSoup
import csv

def news_scraper(url):
    response = requests.get(url, verify=certifi.where())
    soup = BeautifulSoup(response.text, 'html.parser')
    # with open ('news.html', 'w') as f:
    #     f.write(str(soup))
    articles = soup.find_all("article", class_="type-post")
    print(articles)
    # with open ('news.csv', 'w') as f:
    #     write = csv.writer(f)
    #     write.writerow(["Index", "Headline", "Summary"])
    #     for hl in heads:
    #         pass
if __name__ == '__main__':
    news_scraper('https://newsblaze.co.ke/')