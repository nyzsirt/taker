import requests, time, os, sys,re
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from  pprint import pprint
from taker.parsers.contants import *
from xml.dom import minidom
import subprocess


class ParserInvesting(object):

    def run_subprocess(self, url):
        # Launch scan
        args = INVESTING_PARAMETERS + [url]

        # print(args)
        p = subprocess.Popen(
            args,
            bufsize=100000,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # wait until finished
        # get output
        (_last_output, tool_err) = p.communicate()
        _last_output = bytes.decode(_last_output)
        tool_err = bytes.decode(tool_err)
        return _last_output, tool_err

    def get_rates(self, timestamp):
        response = self.run_subprocess(INVESTING_URL)
        ret = {}

        for exchange_list in response[0].split("\n"):
            if re.search("pid-66-last", exchange_list):
                dom = minidom.parseString(exchange_list.strip())
                ret[CURRENCY_EUR] = {
                    "timestamp": timestamp,
                    "type": PARSER_TYPE_INVESTING,
                    "rate": dom.getElementsByTagName("div")[0].childNodes[0].data,
                }
            if re.search("pid-18-last", exchange_list):
                dom = minidom.parseString(exchange_list.strip())
                ret[CURRENCY_USD] = {
                    "timestamp": timestamp,
                    "type": PARSER_TYPE_INVESTING,
                    "rate": dom.getElementsByTagName("div")[0].childNodes[0].data,
                }
        return ret

