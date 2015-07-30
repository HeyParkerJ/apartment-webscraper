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

    # request the url, push the headers, store the response
    response = requests.get(url, headers=headers)

    # check for gucci status code
    if response.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + url)

    soup = BeautifulSoup(response.text, "lxml")
    # assigns ResultSet of cards to "cards"
    # these are tags
    cards = soup.find_all("div", "available-apartment-card")

    # get a ton of stuff done
    results = get_card_data(cards)

    pprint.pprint(results)


def parse_name(card):
    return card.find("div", "panel-pane pane-entity-field pane-node-field-title-display inverted pos-left pos-bottom").string.strip()


def parse_price(card):
    # These originally parse out with a span tag in front, contents[2] fixes
    # removed newline and $, strips out extra spacing
    price = card.find("div", "price").contents[2].replace("\n", "").replace("$", "").strip()
    return price


def parse_cheapest_apartment_number(card):
    return card.find("div", "unit-name").contents[0]


def get_card_data(cards):
        # create a list
        data_list = list()
        # for each card in our list of cards, parse important info
        for card in cards:
            name = parse_name(card)
            lowest_price = parse_price(card)
            cheapest_apartment = parse_cheapest_apartment_number(card)

            # put data in a dictionary, str removes what looks like bs4
            data = {"Lowest Price": str(lowest_price),
                    "Name": str(name),
                    "Cheapest Apartment": str(cheapest_apartment)}
            # add card's dictionary to a list of cards
            data_list.append(data)

        return data_list


if __name__ == "__main__":
    scrape()
