import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.investing import ParserInvesting

requester = ParserInvesting()
data = requester.get_rates(time.time())
pprint(data)
"""
{
    'EUR': {
        'rate': '6.0385', 
        'timestamp': 1544391831.360719, 
        'type': 3},
   
    'USD': {
         'rate': '5.3029', 
         'timestamp': 1544391831.360719, 
         'type': 3}
}
"""