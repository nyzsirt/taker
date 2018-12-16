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
        ret = {
            CURRENCY_EUR: {
                "timestamp": timestamp,
                "type": PARSER_TYPE_INVESTING,
            },
            CURRENCY_USD: {
                "timestamp": timestamp,
                "type": PARSER_TYPE_INVESTING,
            }
        }
        for line in response[0].split("\n"):
            if re.search("pid-66-bid", line):
                dom = minidom.parseString(line.strip())
                ret[CURRENCY_EUR]["bid"] = dom.getElementsByTagName("div")[0].childNodes[0].data

            elif re.search("pid-66-ask", line):
                dom = minidom.parseString(line.strip())
                ret[CURRENCY_EUR]["ask"] = dom.getElementsByTagName("div")[0].childNodes[0].data

            elif re.search("pid-18-bid", line):
                dom = minidom.parseString(line.strip())
                ret[CURRENCY_USD]["bid"] = dom.getElementsByTagName("div")[0].childNodes[0].data

            elif re.search("pid-18-ask", line):
                dom = minidom.parseString(line.strip())
                ret[CURRENCY_USD]["ask"]= dom.getElementsByTagName("div")[0].childNodes[0].data
        return ret

