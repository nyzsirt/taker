import os, sys, time
from datetime import datetime, timedelta
from mrq.task import Task
from mrq.context import log, connections, run_task
from mrq.basetasks.utils import JobAction
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from pprint import pprint
from parsers.constants import *
from mrq.context import subpool_imap


class Regulator(Task):

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

    def export_data(self, collection, start, end):
        start_timestamp = start.timestamp()
        end_timestamp = end.timestamp()

        bloomberg = collection.find(
            {"type": PARSER_TYPE_BLOOMBERG, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "usd-bloomberg-%s-%s.csv" % (start, end), "w") as ff:
            ff.writelines(self._flatten(bloomberg))

        investing = collection.find(
            {"type": PARSER_TYPE_INVESTING, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "usd-investing-%s-%s.csv" % (start, end), "w") as ff:
            ff.writelines(self._flatten(investing))

        isbank = collection.find(
            {"type": PARSER_TYPE_ISBANK, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "usd-isbank-%s-%s.csv" % (start, end), "w") as ff:
            ff.writelines(self._flatten(isbank))

        tcmb = collection.find(
            {"type": PARSER_TYPE_TCMB, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open(DATA_PATH + "usd-tcmb-%s-%s.csv" % (start, end), "w") as ff:
            ff.writelines(self._flatten(tcmb))

    def subb(self, collection, start, end):
        self.export_data(collection, start, end)
        collection.remove()
        return[{"succes": True}]

    def run(self, params):

        curr_time = time.time()
        start = (datetime.fromtimestamp(curr_time) - timedelta(hours=24)).strftime(TIME_FORMAT)
        end = datetime.fromtimestamp(curr_time).strftime(TIME_FORMAT)

        eur_rates = connections.mongodb_jobs.ex_eur_try
        usd_rates = connections.mongodb_jobs.ex_usd_try
        iterator = [
            [eur_rates, start, end],
            [usd_rates, start, end],
        ]
        ret = []
        for res in subpool_imap(len(iterator), self.subb, iterator, unordered=True):
            ret += res



