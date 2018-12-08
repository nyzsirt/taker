import os, sys, time
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.tcmb import Tcmb

requester = Tcmb()
data = requester.get_rates()
data["timestamp"] = time.time()
pprint(data["USD"])
pprint(data["EUR"])
