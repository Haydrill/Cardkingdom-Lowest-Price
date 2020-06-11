# Cardkingdom-Lowest-Price
This python project is a tool that allows the input of a Magic: the Gathering card name in the command line, searches for it on Cardkingdom and StarCityGames, and prints the lowest price available on those sites

Disclaimer : I use CardKingdom's price filter, so it might not return the very cheapest version but will return the cheapest version at the highest grade.

As of 6/7/20, I am extending the project to other popular MtG card sites (StarCityGames, TCGPlayer, Channel Fireball). Finished SCG (hopefully). Currently working on TCGPlayer integration.


Demonstration:
  USER INPUT : main.py Marchesa, the Black Rose
  OUTPUT : 
  Checking CardKingdom for: Marchesa, the Black Rose ...
  https://www.cardkingdom.com/catalog/search?filter%5Bipp%5D=20&filter%5Bsort%5D=price_asc&filter%5Bname%5D=Marchesa,+the+Black+Rose
  Searching for card...
  Card found!

  Marchesa, the Black Rose
  Commander 2017 (M)
  1 available @ $4.99

  Checking StarCityGames for: Marchesa, the Black Rose ...
  https://starcitygames.com/search.php?search_query=Marchesa, the Black Rose
  Card found!

  Marchesa, the Black Rose
  English
  Conspiracy: 2014 Edition
  Qty: 19 available @ $2.45
