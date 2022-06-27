from pycoingecko import CoinGeckoAPI
from playsound import playsound
import time
cg = CoinGeckoAPI()

while 1:
	pair = cg.get_price(ids='eterland', vs_currencies='usd')
	
	price= float(pair['eterland']['usd'])
	wanted_price= 'The price you want'


	if price == wanted_price:  ##### here you could use every comparative you need.
		print(f'Current price: {price}')
		print('It\'s the show time'.center(50,"!"))
		playsound('alarm.mp3')
		time.sleep(10)
	else:
		print(f'Current price: {price}')
		print('Waiting for the right moment.')
		time.sleep(60)

