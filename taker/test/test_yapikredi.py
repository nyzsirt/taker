import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.yapikredi import ParserYapiKredi

requester = ParserYapiKredi()
data = requester.get_rates(time.time())
pprint(data)

"""
{
    "EUR": {
        "rate": "4.477873177",
        'timestamp': 1544391831.360719, 
        'type': 3,

    },
    "USD":{
        "rate": "3.870502240",
        'timestamp': 1544391831.360719, 
        'type': 3,
    }    
}
"""
