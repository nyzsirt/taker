import os, sys, time
from mrq.task import Task
from mrq.context import log, connections, run_task
from mrq.basetasks.utils import JobAction
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.tcmb import ParserTcmb
from taker.parsers.contants import *
from datetime import datetime


class Tcmb(Task):
    def run(self, params):
        requester = ParserTcmb()
        rates = requester.get_rates()
        current_timestamp = time.time()
        exchange_usd = connections.mongodb_jobs.ex_usd_try
        exchange_eur = connections.mongodb_jobs.ex_eur_try
        for key in rates.keys():
            if key in [CURRENCY_EUR, CURRENCY_USD]:
                _rate = {
                    "timestamp": current_timestamp,
                    "type": PARSER_TYPE_TCMB,
                    "ask": rates[key]["BanknoteSelling"],
                    "bid": rates[key]["BanknoteBuying"],
                }
                if key in [CURRENCY_EUR]:
                    exchange_eur.save(_rate)
                else:
                    exchange_usd.save(_rate)
