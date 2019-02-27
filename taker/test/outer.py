import os, sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
import argparse
from datetime import datetime
from pytz import utc, timezone
from time import mktime
from mrq.context import connections, log, setup_context
from taker.parsers.constants import *
from pprint import pprint

parser = argparse.ArgumentParser(description='Add assets to tags from file.')

parser.add_argument('--currency', dest='currency', action='store', required=True, help='"eur" veya "usd"')
parser.add_argument('--start', dest='start', action='store', required=False, default= "",  help='baslangic tarihi: format Yyyymmddhhmmss')
parser.add_argument('--end', dest='end', action='store', required=False, default= "", help='bitis tarihi: format Yyyymmddhhmmss')
time_format = "%Y%m%d%H%M%S"


def _flatten(data):
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


if __name__ == '__main__':
    setup_context(file_path=BASEPATH + 'taker/config/config.py', config_type='run')
    args = parser.parse_args()
    _query = {}
    if args.start:
        start_timestamp = mktime(utc.localize(datetime.strptime(args.start, time_format)).utctimetuple())
        end_timestamp = mktime(utc.localize(datetime.strptime(args.end, time_format)).utctimetuple())
        _query = {
            "timestamp": {
                "$gte": start_timestamp, "$lt": end_timestamp,
            }
        }

    if args.currency == "usd":
        usd_collection = connections.mongodb_jobs.ex_usd_try

        _query["type"] = PARSER_TYPE_BLOOMBERG
        bloomberg = usd_collection.find(_query)
        with open("usd-bloomberg-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(bloomberg))

        _query["type"] = PARSER_TYPE_INVESTING
        investing = usd_collection.find(_query)
        with open("usd-investing-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(investing))

        _query["type"] = PARSER_TYPE_ISBANK
        isbank = usd_collection.find(_query)
        with open("usd-isbank-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(isbank))

        _query["type"] = PARSER_TYPE_TCMB
        tcmb = usd_collection.find(_query)
        with open("usd-tcmb-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(tcmb))

    if args.currency == "eur":
        _query["type"] = PARSER_TYPE_BLOOMBERG
        eur_collection = connections.mongodb_jobs.ex_eur_try
        bloomberg = eur_collection.find(_query)
        with open("eur-bloomberg-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(bloomberg))

        _query["type"] = PARSER_TYPE_INVESTING
        investing = eur_collection.find(_query)
        with open("eur-investing-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(investing))

        _query["type"] = PARSER_TYPE_ISBANK
        isbank = eur_collection.find(_query)
        with open("eur-isbank-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(isbank))

        _query["type"] = PARSER_TYPE_TCMB
        tcmb = eur_collection.find(_query)
        with open("eur-tcmb-%s-%s.csv" % (args.start, args.end), "w") as ff:
            ff.writelines(_flatten(tcmb))


