from bs4 import BeautifulSoup
import requests
import random

mobile_brand = input("What brand of mobile phone do you want?")
url = f"https://extra.ge/search?k={mobile_brand}&cat=teqnika%2Ftelefonebi-da-aqsesuarebi%2Fmobiluri-telefoni&p=1"


def user_agent():
    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
    ]

    return random.choice(uastrings)


def getItems(productUrl):
    found_items = {}

    # getting number of pages
    headers = {"User-Agent": user_agent()}
    res = requests.get(productUrl, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    num_of_pages = soup.find("app-pagination")
    final_page = int(num_of_pages.find_all("span")[-1].text)

    # getting all items and item information
    for page in range(1, final_page + 1):
        url = f"https://extra.ge/search?k={mobile_brand}&cat=teqnika%2Ftelefonebi-da-aqsesuarebi%2Fmobiluri-telefoni&p={page}"
        headers = {"User-Agent": user_agent()}
        res = requests.get(productUrl, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        table = soup.find(class_="_x_grid")
        items = table.find_all("app-product-card")
        for i in items:
            price = i.find(class_="_x_ml-2").text
            model = i.find(class_="_x_line-clamp-2").text
            vendor = i.find(class_="_x_line-clamp-1").text

            found_items[model] = {"Price": price, "Merchant": vendor}

    return found_items


prices = getItems(url)

print(prices)
