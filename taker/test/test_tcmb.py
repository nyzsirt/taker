import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.tcmb import ParserTcmb

requester = ParserTcmb()
data = requester.get_rates()
data["timestamp"] = time.time()
pprint(data)

"""
 'EUR': {'BanknoteBuying': 6.0529,
         'BanknoteSelling': 6.0772,
         'ForexBuying': 6.0572,
         'ForexSelling': 6.0681,
         'code': 'EUR',
         'name': 'EURO'},
 'USD': {'BanknoteBuying': 5.322,
         'BanknoteSelling': 5.3433,
         'ForexBuying': 5.3257,
         'ForexSelling': 5.3353,
         'code': 'USD',
         'name': 'ABD DOLARI'},
 'timestamp': 1544391614.3245983}

"""