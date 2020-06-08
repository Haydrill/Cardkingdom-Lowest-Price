#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card
import sys
from requests_html import HTMLSession

# input from command line
input = ' '.join(sys.argv[1:])
# input = 'Marchesa, the Black Rose'  # test case

#create url with card name and print it. Filtered by lowest-highest price
url = 'https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D='
url = url + input.replace(' ', '+') #the website url uses '+' to join words
print(url)
# go to url and make sure it is valid
session = HTMLSession()
card_kingdom = session.get(url)

# grab the proper elements for the card's data. then close site
card_name_and_sets = card_kingdom.html.find('.itemContentWrapper')
card_amt_and_qty = card_kingdom.html.find('.amtAndPrice')
card_kingdom.close()

print('Searching for card...')

# variable to track current set when looping (intervals of 4)
set_tracker = 0

# loop through each card, check if correct name, and print first one (cheapest)
for card in card_amt_and_qty :
    set_tracker //= 4
    current_card = card_name_and_sets[set_tracker]

    card_name = current_card.find('.productDetailTitle', first=True).text
    card_set = current_card.find('.productDetailSet', first=True).text

    # remove punctation, make uppercase, compare card names, print if same
    if input.replace(',' , '').upper() in card_name.replace(',' , '').upper() :
        if '0' not in card.text :
            print('Card found!\n')
            print(card_name)
            print(card_set)
            print(card.text)
            sys.exit(0)

# if looped through and all cards have quantity of 0, this is the message
print('Sorry, that card is not currently available on CardKingdom')
