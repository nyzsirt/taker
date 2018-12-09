import requests, time, os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from  pprint import pprint
from taker.parsers.contants import *


class ParserBloomberg(object):
    def get_currency(self, res, timestamp):
        data =res["SeriesData"][-1]
        return {
            "timestamp": timestamp,
            "rate": data[1],
            "type": PARSER_TYPE_BLOOMBERG,
        }

    def get_rates(self, timestamp):
        res_usd = requests.get(BLOOMBERG_URL_DOLAR)
        res_eur = requests.get(BLOOMBERG_URL_EURO)
        ret = {
            CURRENCY_USD: self.get_currency(res_usd.json(), timestamp),
            CURRENCY_EUR: self.get_currency(res_eur.json(), timestamp)
        }
        return ret



