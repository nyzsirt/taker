import os, sys, time
from pytz import utc
from time import mktime
from datetime import datetime, timedelta
from mrq.task import Task
from mrq.context import log, connections, run_task
from mrq.basetasks.utils import JobAction
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from parsers.constants import *
from mrq.context import subpool_imap


class Export(object):

    def _flatten(self, data):
        content = []
        for line in data:
            line["date"] = datetime.fromtimestamp(line["timestamp"]).strftime(TIME_FORMAT)
            try:
                content.append(
                    "%(date)s %(ask)s %(bid)s\n" % line
                )
            except KeyError as error:
                pass
        return content

    def export_data(self, currency_type, start, end):
        start_timestamp = mktime(utc.localize(datetime.strptime(start, TIME_FORMAT)).utctimetuple())
        end_timestamp = mktime(utc.localize(datetime.strptime(end, TIME_FORMAT)).utctimetuple())

        if currency_type == CURRENCY_EUR:
            collection = connections.mongodb_jobs.ex_eur_try
        else:
            collection = connections.mongodb_jobs.ex_usd_try

        bloomberg = collection.find(
            {"type": PARSER_TYPE_BLOOMBERG, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "%s-bloomberg-%s-%s.csv" % (currency_type, start, end), "w") as ff:
            ff.writelines(self._flatten(bloomberg))

        investing = collection.find(
            {"type": PARSER_TYPE_INVESTING, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "%s-investing-%s-%s.csv" % (currency_type, start, end), "w") as ff:
            ff.writelines(self._flatten(investing))

        isbank = collection.find(
            {"type": PARSER_TYPE_ISBANK, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "%s-isbank-%s-%s.csv" % (currency_type, start, end), "w") as ff:
            ff.writelines(self._flatten(isbank))

        tcmb = collection.find(
            {"type": PARSER_TYPE_TCMB, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "%s-tcmb-%s-%s.csv" % (currency_type, start, end), "w") as ff:
            ff.writelines(self._flatten(tcmb))
        collection.delete_many({})

    def subb(self, currency_type, start, end):
        self.export_data(currency_type, start, end)
        return[{"success": True}]


class Regulator(Task):

    @staticmethod
    def wrapper(arguments):
        exporter = Export()
        return exporter.subb(*arguments)

    def run(self, params):
        curr_date = datetime.now()
        if curr_date.hour == 22 and curr_date.minute == 32:
            curr_time = time.time()
            start = (datetime.fromtimestamp(curr_time) - timedelta(hours=24)).strftime(TIME_FORMAT)
            end = datetime.fromtimestamp(curr_time).strftime(TIME_FORMAT)

            iterator = [
                (CURRENCY_EUR, start, end),
                (CURRENCY_USD, start, end),
            ]
            ret = []
            for res in subpool_imap(len(iterator), Regulator.wrapper, iterator, unordered=True):
                ret += res
        return "success"



