#! python3
#USAGE: this program takes in a Magic: the Gathering card name (no punctuation)
#   from the command line and searches for it on CardKingdom.com
#   It then returns the first available version of that card
import sys, functions

#input from command line
input = ' '.join(sys.argv[1:])

functions.CardKingdomScrape(input)
functions.ChannelFireballScrape(input)
functions.TCGPlayerScrape(input)
functions.SCGamesScrape(input)
