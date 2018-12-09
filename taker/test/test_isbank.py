import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.isbank import ParserIsbank

requester = ParserIsbank()
data = requester.get_rates(time.time())
pprint(data)




"""
{'EUR': {'rate': 6.153, 'timestamp': 1544392954.2879014, 'type': 2},
 'USD': {'rate': 5.4017, 'timestamp': 1544392954.2879014, 'type': 2}}
"""


"""
{'EUR': {'category': '',
         'code': 'EUR',
         'description': 'Avrupa Para Birimi',
         'effectiveRateBuy': 5.9426,
         'effectiveRateSell': 6.153,
         'fxRateBuy': 5.9485,
         'fxRateSell': 6.1469,
         'index': '103',
         'timestamp': 1544391532.2387981,
         'type': 1},
 'USD': {'category': '',
         'code': 'USD',
         'description': 'Amerikan Doları',
         'effectiveRateBuy': 5.2169,
         'effectiveRateSell': 5.4017,
         'fxRateBuy': 5.2221,
         'fxRateSell': 5.3963,
         'index': '102',
         'timestamp': 1544391532.2387981,
         'type': 1}}

"""