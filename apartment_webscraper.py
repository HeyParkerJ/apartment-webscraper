import requests
import csv
from datetime import date
from bs4 import BeautifulSoup
from config import url

def scrape():
    # Not a bot
    headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "accept-encoding": "gzip,deflate,sdch",
            "accept-language": "en-US,en;q=0.8"
        }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + url)

    soup = BeautifulSoup(response.text, "lxml")
    cards_soup = soup.find_all("div", "available-apartment-card")

    return get_card_data(cards_soup)


def log_data_to_csv(data):
    # a+ appends, b opens in binary and prevents extra carriage returns
    with open('/home/parker/webscraper/apartment_data.csv', 'a+b') as csvfile:
        fieldnames = ['Price', 'Style', 'Number', 'Length', 'Move In', 'On Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="excel")

        # Never quite figured out how to insert the header only if it doens't exist here
        writer.writerows(data)


def get_card_data(cards_soup):
        data_list = list()
        # for each card in our list of cards_soup, parse respective info
        for card in cards_soup:
            data = {"On Date": date.today(),
                    "Price": parse_price(card),
                    "Style": parse_style(card),
                    "Number": parse_cheapest_apartment_number(card),
                    "Length": parse_lease_lenth(card),
                    "Move In": parse_move_in(card)}

            data_list.append(data)

        return data_list


def parse_price(card):
    # Replaces newline and $
    return str(card.find("div", "price").contents[2].replace("\n", "").replace("$", "").strip())


def parse_style(card):
    # not returning data to unicode with str() would pass expensive Bs4 objects
    return str(card.find("div", "panel-pane pane-entity-field pane-node-field-title-display inverted pos-left pos-bottom").string.strip())


def parse_cheapest_apartment_number(card):
    return str(card.find("div", "unit-name").contents[0])


def parse_lease_lenth(card):
    return str(card.find("div", "lease-contract").contents[1])


def parse_move_in(card):
    return str(card.find("div", "move-in").contents[1])


if __name__ == "__main__":
    log_data_to_csv(scrape())
