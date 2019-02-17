import requests, time, os, sys,re
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
from datetime import datetime
from  pprint import pprint
from taker.parsers.constants import *
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

        """
        GET /live-currency-cross-rates?cols=last&pairs=66,18 HTTP/1.1
        Host: www.widgets.investing.com
        Cache-Control: no-cache
        Save-Data: on
        User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
        Postman-Token: 067329fa-9a6e-f1fc-de14-a51c3cd286a1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Accept-Language: en,en-US;q=0.9,tr;q=0.8
        Cookie: PHPSESSID=1a3b9e6khvmffabhufhdqeuj0p; geoC=TR

        HTTP/1.1 301 https://www.widgets.investing.com/live-currency-cross-rates?cols=last&pairs=66,18
        Server: Varnish
        Location: https://www.widgets.investing.com/live-currency-cross-rates?cols=last&pairs=66,18
        Accept-Ranges: bytes
        Date: Thu, 20 Dec 2018 20:27:22 GMT
        X-Varnish: 681011426
        Age: 0
        Via: 1.1 varnish
        Connection: close
        """
        _headers = {
            "User-Agent": USER_AGENT,
        }

        response =requests.get(INVESTING_URL, headers=_headers)

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
        for line in response.text.split("\n"):
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

