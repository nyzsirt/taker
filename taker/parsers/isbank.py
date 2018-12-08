import requests, time, os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from taker.parsers.contants import *


class Isbank():
    def get_rates(self, timestamp):
        parameters = {
            "timestamp": str(timestamp).split(".")[0],
            "date": datetime.now().strftime("%Y-%m-") + str(datetime.now().day)
        }
        response = requests.get(ISBANK_URL % parameters)
        ret = {}
        for rate in response:
            rate["timestamp"] = timestamp
            if rate["code"] in [CURRENCY_EUR, CURRENCY_USD]:
                ret[rate["code"]] = rate
        return ret
