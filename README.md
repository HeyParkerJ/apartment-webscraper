# apartment-webscraper

## About

In 2015 I was looking for a new apartment and noticed that quite a few complexes in my area utilized 'dynamic pricing' - meaning monthly apartment cost could vary depending on the time of year, day of the week, or even week in a month based on the 'supply and demand' on the day you signed a lease. This meant you could be locking in a monthly lease up to $600 more than other months just because you signed during college student housing hunting season.

My curiousity, not satisfied with a catchall explanation of supply and demand, nor wanting to leave my living situation financially unoptimized, I threw together a webscraper for one particular website in python 2.7 to check the lowest price of their apartments every day with intent of manual analysis.

I rented a townhome instead.

As a Java dev at work, this is my first time writing in Python.


### How to run

You can't. For saftey reasons, I don't commit the website url anymore. But if you were me, you'd...

Assuming fresh vm, pip install the following

- `Beautifulsoup4`
- `lxml`

The script currently runs with a cron job on a VPS that I obtained and secured, learning a bit of administrative work on the way. For a single run, `python apartment_webscraper.py`

apartment_data.csv (if I wrote it again, we'd have a database) shows a small window of the extracted data for some manual excel formatting.
