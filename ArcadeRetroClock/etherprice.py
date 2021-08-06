#For displaying crypto currency
from pycoingecko import CoinGeckoAPI
price = CoinGeckoAPI().get_price(ids='ethereum', vs_currencies='usd')
print ('ETH ${}'.format(price['ethereum']['usd']))
