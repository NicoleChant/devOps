from bs4 import BeautifulSoup
import requests
import re
from dataclasses import dataclass , field

class Spider:

    headers : dict[str,str] = {"Accept":"*/*",
                                         "Accept-Encoding" : "gzip, deflate, br",
                                         "Accept-Language": "en-US,en;q=0.9",
                                         "Connection":"keep-alive",
                                         "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
                                            }

    def __init__(self) -> None:
        self.url = "https://www.skroutz.gr/c/25/laptop.html?o=laptop"
        self.soup = None
        self.response = None
        self.session = requests.Session()
        self.session.headers = Spider.headers

    def crawl(self) -> None:
        self.response = self.session.get(self.url)
        self.soup = BeautifulSoup( self.response.text , "html.parser")

    def parse(self) -> dict[str,str]:
        self.crawl()
        for laptop in self.soup.find_all("div" , {"class":"card-content"}):
            try:
                product_id = laptop.find("a").attrs["href"].split("/")[2]
                title = re.findall( re.compile(r"/([A-Z][\w\W0-9]*).html") ,laptop.find("a").attrs["href"])[0]
                reviews = laptop.find("a" , class_ = "rating stars").attrs["title"].replace(",",".")
                rating = reviews.split(' ')[0]
                total_reviews = reviews.split(' ')[-2]
                price = laptop.select_one("div a[class='js-sku-link sku-link'] span").next_sibling.replace(",",".")
                shop_availability = laptop.find("span" , class_ = "shop-count").string.split(' ')[1]

                yield {"product_id": product_id,
                    "title": title,
                    "reviews": reviews,
                    "rating": rating,
                    "total_reviews": total_reviews,
                    "price": price,
                    "shop_availability": shop_availability}

            except KeyError:
                print(laptop)
                raise KeyError()
