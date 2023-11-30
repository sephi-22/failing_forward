# This is going to scrape the web for USA gas prices
import requests
from bs4 import BeautifulSoup


def scrape_for_gas_prices(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/101.0.4951.54 Safari/537.36",
        "Connection": "keep-alive",
        "Referer": "https://google.com/",
        "DNT": "1",
        "Accept-Language": "en-GB,en;q=0.5",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        gas_table = soup.find("table", {"id": "sortable"})

        rows = gas_table.find("tbody").find_all("tr")
        gas_price = {}

        for row in rows:
            state = row.find("td").text.strip()

            regular_price = row.find("td", {"class": "regular"}).text.strip()[1:]
            mid_grade_price = row.find("td", {"class": "mid_grade"}).text.strip()[1:]
            premium_price = row.find("td", {"class": "premium"}).text.strip()[1:]
            diesel_price = row.find("td", {"class": "diesel"}).text.strip()[1:]

            state_prices = {
                "Regular": regular_price,
                "Midgrade": mid_grade_price,
                "Premium": premium_price,
                "Diesel": diesel_price,
            }

            gas_price[state] = state_prices
        return gas_price
