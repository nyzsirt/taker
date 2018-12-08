import os,sys
BASEPATH = os.path.dirname(os.path.realpath(__file__)) + '/../../'
sys.path.append(BASEPATH)
import datetime
from decimal import ROUND_HALF_EVEN, InvalidOperation
from urllib.request import urlopen
from xml.dom import minidom

from .contants import *


class Tcmb:
    def __init__(self):
        self.earliest_date = datetime.date(1996, 4, 16)

    def daystamp(self, date=None):
        if date is None:
            return datetime.datetime.now().strftime('%d%m%Y')
        else:
            return date.strftime('%d%m%Y')

    def get_float(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        try:
            return float(''.join(rc))
        except (ValueError, InvalidOperation):
            return 0.0

    def load_tcmb_archive(self, for_date):
        try:
            import time
            f = urlopen(for_date.strftime(TCMB_ARCHIVE_URL)+str(time.time()).split(".")[0])
        except:
            f = urlopen(for_date.strftime(TCMB_TODAY_URL))
        if f.getcode() != 200:
            # Can't get the file.
            return None
        dom = minidom.parse(f)
        date_str = dom.getElementsByTagName('Tarih_Date')[0].getAttribute('Tarih').replace('.', '')
        date = datetime.datetime.strptime(date_str, '%d%m%Y').date()
        return dom, date

    def load_tcmb_today(self):
        f = urlopen(TCMB_TODAY_URL)
        dom = minidom.parse(f)
        date_str = dom.getElementsByTagName('Tarih_Date')[0].getAttribute('Tarih').replace('.', '')
        date = datetime.datetime.strptime(date_str, '%d%m%Y')


        return dom, date

    def load_tcmb(self, date=None):
        """
        :param date: datetime.date
        :return dom, date:
        """
        if date is None:
            return self.load_tcmb_today()

        # Check if the given date is sensical.
        if date > datetime.datetime.today().date():
            # A date in the future? Surely today's rates apply.
            return self.load_tcmb_today()

        if date < self.earliest_date:
            raise RuntimeError("TCMB only provides rated for dates after April 16, 1996.")

        for_date = date
        if date.isoweekday() in (6, 7):
            # A weekend. Try to read the previous Friday.
            for_date -= datetime.timedelta(date.isoweekday() - 5)

        # Try to download the date's data from tcmb. If can't find (get 404),
        # successively try to get earlier dates.
        while True:
            ret = self.load_tcmb_archive(for_date)
            if ret is not None:
                dom, for_date = ret
                return dom, for_date
            for_date -= datetime.timedelta(-1)

    def quantize(self, dec, scale):
        return dec.quantize(D('1').scaleb(-scale), rounding=ROUND_HALF_EVEN)

    def get_rates(self, for_date=None):
        """
        Get TCMB currency data
        :param for_date date | datetime.date
        :return: dict
        """
        if for_date is None:
            for_date = datetime.datetime.today().date()

        dom, date = self.load_tcmb(for_date)

        rates = {}
        for curr in dom.getElementsByTagName('Currency'):
            rate = {}
            try:
                for key in CONVERSATION_DICT.keys():
                    if curr.getElementsByTagName(CONVERSATION_DICT[key]) and not key is None:
                        rate[CONVERSATION_DICT[key]] = self.get_float(
                            curr.getElementsByTagName(CONVERSATION_DICT[key])[0].childNodes)
                        code = curr.getAttribute('CurrencyCode')
                        rate["name"] = curr.getElementsByTagName("Isim")[0].childNodes[0].data
                        rate["code"] = code
                rates[rate["code"]] = rate
            except IndexError:
                continue
        return rates
