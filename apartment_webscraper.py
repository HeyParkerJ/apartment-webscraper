import requests
import pprint
from bs4 import BeautifulSoup


# our main url
url = "https://www.camdenliving.com/tempe-az-apartments/camden-sotelo/apartments"


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

    # shit goes down right here
    results = get_card_data(cards_soup)

    pprint.pprint(results)


def parse_name(card):
    # not returning data to unicode with str() would pass expensive Bs4 objects
    return str(card.find("div", "panel-pane pane-entity-field pane-node-field-title-display inverted pos-left pos-bottom").string.strip())


def parse_price(card):
    # Replaces newline and $
    return str(card.find("div", "price").contents[2].replace("\n", "").replace("$", "").strip())


def parse_cheapest_apartment_number(card):
    return str(card.find("div", "unit-name").contents[0])


def parse_move_in(card):
    return str(card.find("div", "move-in").contents[1]).strip()


def parse_lease_lenth(card):
    return str(card.find("div", "lease-contract").contents[1])


def get_card_data(cards_soup):
        data_list = list()
        # for each card in our list of cards_soup, parse important info
        for card in cards_soup:
            data = {"Lowest Price": parse_price(card),
                    "Style": parse_name(card),
                    "Apartment Number": parse_cheapest_apartment_number(card),
                    "Lease Length": parse_lease_lenth(card),
                    "Move In Day": parse_move_in(card)}

            data_list.append(data)

        return data_list


if __name__ == "__main__":
    scrape()
