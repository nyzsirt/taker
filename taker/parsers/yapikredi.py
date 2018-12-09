import requests, time, os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from taker.parsers.contants import *


class ParserYapiKredi(object):
    """
    {
        "response":
            {
                "exchangeRateList": [

                    {
                        "averageRate": "4.469885687",
                        "sellRate": "4.477873177",
                        "minorCurrency": "TL",
                        "previousDaySellRate": "4.448264293",
                        "majorCurrency": "EUR",
                        "changeRatioDaily": "0.655391989",
                        "previousDayBuyRate": "4.433298033",
                        "previousDayAverageRate": "4.440781163",
                        "buyRate": "4.461898197"
                    },
                    {
                        "averageRate": "3.864718195",
                        "sellRate": "3.870502240",
                        "minorCurrency": "TL",
                        "previousDaySellRate": "3.838605919",
                        "majorCurrency": "USD",
                        "changeRatioDaily": "0.829550210",
                        "previousDayBuyRate": "3.827238442",
                        "previousDayAverageRate": "3.832922181",
                        "buyRate": "3.858934150"
                    },
                ]
            }
    }
    """

    def get_rates(self, timestamp):
        response = requests.get(YAPIKREDI_URL).json()
        ret = {}
        for exchange_list in response:
            for rate in exchange_list:
                _rate = {
                    "timestamp": timestamp,
                    "type": PARSER_TYPE_YAPIKREDI,
                }
                if rate["majorCurrency"] in [CURRENCY_EUR, CURRENCY_USD] and \
                        rate["minorCurrency"] in STANDARD_CODES.keys():

                    _rate["rate"] = rate["sellRate"]
                    ret[rate["majorCurrency"]] = _rate
        return ret

