import os, sys, time
from mrq.task import Task
from mrq.context import log, connections, run_task
from mrq.basetasks.utils import JobAction
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from taker.parsers.isbank import ParserIsbank
from taker.parsers.contants import CURRENCY_EUR


class IsBank(Task):
    def run(self, params):
        requester = ParserIsbank()
        rates = requester.get_rates(timestamp=time.time())
        exchange_usd = connections.mongodb_jobs.ex_usd_try
        exchange_eur = connections.mongodb_jobs.ex_eur_try
        for key in rates.keys():
            if key in [CURRENCY_EUR]:
                exchange_eur.save(rates[key])
            else:
                exchange_usd.save(rates[key])
