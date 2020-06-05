#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card
import webbrowser, requests, os, sys
from bs4 import BeautifulSoup

#input from command line
card = '+'.join(sys.argv[1:])

#create url with card name and print it. Filtered by lowest-highest price
url = 'https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D=' + card
print(url)

#go to url and make sure it is valid
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='html.parser')

#grab the html of the amount and price of the cards listed
card_data = soup.find_all('div', {'class': 'itemContentWrapper'})
second_data = soup.find_all('div', {'class': 'amtAndPrice'})

#loop through the
for card, second in zip(card_data, second_data) :
    #set amount of each card on each loop
    amount = second.find(class_ = 'styleQty')

    #if the amount is not 0, print the price and amount, then exit program
    if str(second.get_text()) != '0' :
        card_name = card.find('span', {'class': 'productDetailTitle'})
        set = card.find('div', {'class': 'productDetailSet'})
        print(card_name.get_text() + set.get_text().rstrip('\n'))
        print('\bCheapest price at the highest grade is: '
             + second.find(class_ = 'stylePrice').get_text() +
             'There are currently ' + amount.get_text() + ' in stock')
        sys.exit(0)

#if looped through and all cards have quantity of 0, this is the message
print('Sorry, that card is not currently available on CardKingdom')
