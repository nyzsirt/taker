import os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
import argparse
from datetime import datetime
from pytz import utc, timezone
from time import mktime
from mrq.context import connections, log, setup_context
from taker.parsers.contants import *
from pprint import pprint

parser = argparse.ArgumentParser(description='Add assets to tags from file.')

parser.add_argument('--currency', dest='currency', action='store', required=True, help='"eur" veya "usd"')
parser.add_argument('--start', dest='start', action='store', required=True, help='baslangic tarihi: format Yyyymmddhhmmss')
parser.add_argument('--end', dest='end', action='store', required=True, help='bitis tarihi: format Yyyymmddhhmmss')
time_format = "%Y%m%d%H%M%S"


def _flatten(data):
    content = []
    for line in data:
        line["date"] = datetime.fromtimestamp(line["timestamp"]).strftime(time_format)
        try:
            content.append(
                "%(date)s %(ask)s %(bid)s\n" % line
            )
        except KeyError as error:
            pass
    return content


if __name__ == '__main__':
    setup_context(file_path=BASEPATH + 'taker/config/config.py', config_type='run')
    args = parser.parse_args()
    start_timestamp = mktime(utc.localize(datetime.strptime(args.start, time_format)).utctimetuple())
    end_timestamp = mktime(utc.localize(datetime.strptime(args.end, time_format)).utctimetuple())

    if args.currency == "usd":
        usd_collection = connections.mongodb_jobs.ex_usd_try

        bloomberg = usd_collection.find({"type": PARSER_TYPE_BLOOMBERG, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("usd-bloomberg-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(bloomberg))

        investing = usd_collection.find({"type": PARSER_TYPE_INVESTING, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("usd-investing-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(investing))

        isbank = usd_collection.find({"type": PARSER_TYPE_ISBANK, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("usd-isbank-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(isbank))

        tcmb = usd_collection.find({"type": PARSER_TYPE_TCMB, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("usd-tcmb-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(tcmb))

    if args.currency == "eur":
        eur_collection = connections.mongodb_jobs.ex_eur_try
        bloomberg = eur_collection.find({"type": PARSER_TYPE_BLOOMBERG, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("eur-bloomberg-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(bloomberg))

        investing = eur_collection.find({"type": PARSER_TYPE_INVESTING, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("eur-investing-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(investing))

        isbank = eur_collection.find({"type": PARSER_TYPE_ISBANK, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("eur-isbank-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(isbank))

        tcmb = eur_collection.find({"type": PARSER_TYPE_TCMB, "timestamp": {"$gte": start_timestamp, "$lt": end_timestamp}})
        with open("eur-tcmb-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(tcmb))


