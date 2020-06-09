#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card

import sys
from requests_html import HTMLSession
from time import sleep

def CardKingdomScrape(input) :

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

    # if looped through and all cards have quantity of 0, this is the message
    if found is False :
        print('Sorry, that card is not currently available on CardKingdom')
## END OF CardKingdomScrape

def SCGamesScrape(input) :
    #create url with card name and print it. Filtered by lowest-highest price
    url = 'https://starcitygames.com/search.php?search_query='
    url = url + input
    print(url)

    #go to url and make sure it is properly rendered with sleep
    session = HTMLSession()
    scg = session.get(url)
    scg.html.render(sleep=2)

    # find all card_names, sets, prices, and quantities
    card_data = scg.html.find('tr')
    card_price = scg.html.find('p.product-price.sort-name')
    card_name = scg.html.find('.listItem-details')
    card_set = scg.html.find('.category-row-name-search')
    card_qty = scg.html.find('td.\-\-Stock')
    scg.close()

    # cheapest_card = 'Sorry, that card was not found on StarCityGames'
    # # loop through the table and find first card with same name and is in stock
    # for card in card_data[1:] :
    #     if input in card.text :
    #         if 'Qty: Out of Stock' not in card.text :
    #             # cheapest_card.append(card.text)
    #             # print(card.text)
    #             # sys.exit(0)
    # print('Sorry, that card was not found on StarCityGames...')
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
