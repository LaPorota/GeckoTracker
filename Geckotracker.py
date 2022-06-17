from pycoingecko import CoinGeckoAPI
from playsound import playsound
import time
cg = CoinGeckoAPI()

while 1:
	par = cg.get_price(ids='eterland', vs_currencies='usd')
	
	precio= float(par['eterland']['usd'])

	if precio == precio:
		print(f'Eter: {precio}')
		print('TIEMPO DE LA ACCION'.center(50,"!"))
		playsound('alarm.mp3')
		time.sleep(10)
	else:
		print(f'Precio actual: {precio}')
		print('Esperando precio')
		time.sleep(5)

