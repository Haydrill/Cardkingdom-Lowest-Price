#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card

import sys
from requests_html import HTMLSession
from time import sleep

def CardKingdomScrape(input) :
    print('\nChecking CardKingdom for:' , input, '...')

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
    found = False

    # loop through each card, check if correct name, and print first one (cheapest)
    for card in card_amt_and_qty :
        set_tracker //= 4
        current_card = card_name_and_sets[set_tracker]

        card_name = current_card.find('.productDetailTitle', first=True).text
        card_set = current_card.find('.productDetailSet', first=True).text

        # remove punctation, make uppercase, compare card names, print if amt != 0
        if input.replace(',' , '').upper() in card_name.replace(',' , '').upper() :
            if '0' not in card.text :
                print('Card found!\n')
                print(card_name)
                print(card_set)
                print(card.text)
                found = True
                return

    # if looped through and all cards have quantity of 0, this is the message
    if found is False :
        print('Sorry, that card is not currently available on CardKingdom')
## END OF CardKingdomScrape

def SCGamesScrape(input) :
    print('\nChecking StarCityGames for:', input, '...')

    #create url with card name and print it. Filtered by lowest-highest price
    url = 'https://starcitygames.com/search.php?search_query='
    url = url + input
    print(url)

    #go to url and render html (using sleep to ensure full render)
    session = HTMLSession()
    scg = session.get(url)
    scg.html.render(sleep=1)

    # find all card_names, sets, prices, and quantities
    card_name = scg.html.find('.listItem-details')
    card_set = scg.html.find('.category-row-name-search')
    card_qty = scg.html.find('td.\-\-Stock')
    card_price = scg.html.find('p.product-price.sort-name')
    scg.close()

    # loop through the cards and find cheapest card that matches input
    index_tracker = 0
    cheapest_index = None
    for name, qty in zip(card_name, card_qty) :
        if input.replace(',' ,'').upper() in name.text.replace(',' ,'').upper() :
            if 'Out of Stock' not in qty.text :
                if cheapest_index is None :
                    cheapest_index = index_tracker
                elif card_price[index_tracker].text > card_price[cheapest_index].text :
                    cheapest_index = index_tracker
        index_tracker += 1

    if cheapest_index is not None :
        print('Card found!\n')
        print(card_name[cheapest_index].text)
        print(card_set[cheapest_index].text)
        print(card_qty[cheapest_index].text, 'available @' ,
            card_price[cheapest_index].text)
    else :
        print('Sorry, card was not found on StarCityGames...')

## END OF SCGamesScrape

# def TCGPlayerScrape(input) :
#     #create url with card name and print it. Filtered by lowest-highest price
#     url = 'https://www.tcgplayer.com/search/magic/product?productLineName=magic&q='
#     url = url + input + '&page=1&productTypeName=Cards'
#     print(url)
#
#     #go to url and make sure it is valid
#     res = requests.get(url)
#     res.raise_for_status()
#
#     soup = BeautifulSoup(res.text, features='html.parser')
#     res.close()
#     print(soup.get_text())
#
#     #grab the html of the amount and price of the cards listed
#     #card_data = soup.find_all('div', {'class': 'search-result__category-name'})
#     #print(card_data)
#     #price_data = soup.find_all('div', {'class': 'amtAndPrice'})
#     #print('Searching for card...')
