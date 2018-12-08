import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.isbank import Isbank

requester = Isbank()
data = requester.get_rates(time.time())
pprint(data)
