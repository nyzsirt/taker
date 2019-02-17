import requests, time, os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from taker.parsers.constants import *
from pprint import pprint


class ParserIsbank():
    def get_rates(self, timestamp):
        parameters = {
            "timestamp": str(timestamp).split(".")[0],
            "date": datetime.now().strftime("%Y-%m-") + str(datetime.now().day)
        }
        response = requests.get(ISBANK_URL % parameters)
        ret = {}
        for rate in response.json():
            _rate = {
                "timestamp": timestamp,
                "type": PARSER_TYPE_ISBANK,
            }
            if rate["code"] in [CURRENCY_EUR, CURRENCY_USD]:
                _rate["ask"] = rate["effectiveRateSell"]
                _rate["bid"] = rate["effectiveRateBuy"]
                ret[rate["code"]] = _rate
        return ret
