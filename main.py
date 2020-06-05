#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card
import webbrowser, requests, os, sys
from bs4 import BeautifulSoup

card = '+'.join(sys.argv[1:])
#url = 'https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D=birds+of+paradise'
url = 'https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D=' + card
print(url)
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, features='html.parser')

#print(soup)

target = soup.find_all('div', {'class': 'amtAndPrice'})
#target_text = [span.get_text() for span in target]
#print(target)
#amount = target(class_ = 'styleQty')
#print("Here's the quantity")
#print(amount.get_text())
for targets in target :
    #print(targets)
    amount = targets.find(class_ = 'styleQty')
    #print(amount.get_text())
    #break
#   print(amount)
    if str(amount.get_text()) != '0' :
        print('Cheapest price at the highest grade is: '
            + targets.find(class_ = 'stylePrice').get_text() +
            'There are currently ' + amount.get_text() + ' in stock')
        #print(targets.parent.parent.parent.parent.find(class_ = 'productDetailSet'))
        sys.exit(0)
print('Sorry, that card is not currently available on CardKingdom')
