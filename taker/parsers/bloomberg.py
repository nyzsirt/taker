import requests, time, os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from lxml import html
from  pprint import pprint
from taker.parsers.constants import *


class ParserBloomberg(object):
    def get_currency(self, res, timestamp):
        return {
            "timestamp": timestamp,
            "bid": res[0],
            "ask": res[1],
            "type": PARSER_TYPE_BLOOMBERG,
        }

    def get_rates(self, timestamp):
        parse_key = """//div[@class="detailHeadLine3"]/div/span/b/text()"""
        res_usd = requests.get(BLOOMBERG_URL_DOLAR)
        usd_tree = html.fromstring(res_usd.content)
        usd = usd_tree.xpath(parse_key)

        res_eur = requests.get(BLOOMBERG_URL_EURO)
        eur_tree = html.fromstring(res_eur.content)
        eur = eur_tree.xpath(parse_key)
        ret = {
            CURRENCY_USD: self.get_currency(usd, timestamp),
            CURRENCY_EUR: self.get_currency(eur, timestamp)
        }
        return ret



