import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.bloomberg import ParserBloomberg

requester = ParserBloomberg()
data = requester.get_rates(time.time())
pprint(data)

"""
{
    'EUR': {
        'rate': 6.0439, 
        'timestamp': 1544392312.6747108, 
        'type': 4
    },
    'USD': {
        'rate': 5.3085, 
        'timestamp': 1544392312.6747108, 
        'type': 4
    }
}
"""