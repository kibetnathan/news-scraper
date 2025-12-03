import requests
# import certifi
from bs4 import BeautifulSoup
import csv

def news_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # with open ('news.html', 'w') as f:
    #     f.write(str(soup))
    articles = soup.find_all("article", class_="type-post")
    i = 0

    with open ('news.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(["Headline", "Summary"])
        for article in articles:
            header = article.find("a")
            summary = article.find("p")

            head = header.text.strip() if header else "No header"
            summ = summary.text.strip() if summary else "No header"

            write.writerow([head, summ])
        print("Write successful")


if __name__ == '__main__':
    news_scraper('https://newsblaze.co.ke/')