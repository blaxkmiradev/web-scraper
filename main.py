import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Cannot access this URL"

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title")
    title_text = title.text.strip() if title else "No title"

    paragraphs = soup.find_all("p")
    intro = ""

    for p in paragraphs:
        text = p.get_text().strip()
        if text:
            intro = text
            break

    return {
        "title": title_text,
        "intro": intro,
        "url": url
    }

url = input("Enter URL: ")
data = scrape_url(url)

print("\n===== RESULT =====")
print("Title:", data["title"])
print("Intro:", data["intro"])
print("URL:", data["url"])
