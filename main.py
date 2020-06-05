#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card
import webbrowser, requests, os, sys
from bs4 import BeautifulSoup

#input from command line
input = ' '.join(sys.argv[1:])

#create url with card name and print it. Filtered by lowest-highest price
url = 'https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D='
url = url + input.replace(' ', '+') #the website url uses '+' to join words
print(url)

#go to url and make sure it is valid
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='html.parser')

#grab the html of the amount and price of the cards listed
card_data = soup.find_all('div', {'class': 'itemContentWrapper'})
price_data = soup.find_all('div', {'class': 'amtAndPrice'})
print('Searching for card...')

#loop through the card_data and amount_data
for card, price in zip(card_data, price_data) :
    #set amount of each card on each loop
    amount = price.find(class_ = 'styleQty')
    print(card.get_text() + price.get_text())

    #if the amount is not 0, print the price and amount, then exit program
    #if str(price.get_text()) != '0' :
    if '0' not in str(price.get_text()) :
        card_name = card.find('span', {'class': 'productDetailTitle'}).get_text()
        set = card.find('div', {'class': 'productDetailSet'}).get_text()
        if input.replace(',','') in card_name.replace(',','') :
            print('Card found!')
            print(card_name + set.rstrip('\n'))
            print('\bThere are currently ' + price.get_text().rstrip('\n'))
            sys.exit(0)

#if looped through and all cards have quantity of 0, this is the message
print('Sorry, that card is not currently available on CardKingdom')
