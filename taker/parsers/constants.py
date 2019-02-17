from decimal import Decimal as D

TCMB_TODAY_URL = 'http://www.tcmb.gov.tr/kurlar/today.xml'
TCMB_ARCHIVE_URL = 'http://www.tcmb.gov.tr/kurlar/%Y%m/%d%m%Y.xml?_=%s'
ISBANK_URL = 'https://www.isbank.com.tr/_layouts/ISB_DA/HttpHandlers/FxRatesHandler.ashx?Lang=tr&fxRateType=INTERACTIVE&date=%(date)s&time=%(timestamp)s'
YAPIKREDI_URL = 'https://api.yapikredi.com.tr/api/investmentrates/v1/currencyRates'
BLOOMBERG_URL_DOLAR = 'https://www.bloomberght.com/doviz/dolar'
BLOOMBERG_URL_EURO = 'https://www.bloomberght.com/doviz/euro'

INVESTING_PARAMETERS = "/usr/bin/google-chrome-stable --headless --no-sandbox --disable-gpu --dump-dom".split(" ")
INVESTING_URL = 'https://www.widgets.investing.com/live-currency-cross-rates?cols=bid,ask&pairs=18,66'

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"


STANDARD_CODES = {
    'TL': 'TRY',
    'TRL': 'TRY',
    'YTL': 'TRY',
}

BUILTIN_RATES = {'TRY': D('1.0')}

CONVERSATION_DICT = {
    'forex_sell': 'ForexSelling',
    'fs': 'ForexSelling',
    'forex_buy': 'ForexBuying',
    'fb': 'ForexBuying',
    'banknote_buy': 'BanknoteBuying',
    'banknote_sell': 'BanknoteSelling',
    'b': 'BanknoteBuying',
    's': 'BanknoteSelling',
    'bb': 'BanknoteBuying',
    'bs': 'BanknoteSelling',
    None: 'BanknoteSelling',
}

CURRENCY_TRY = "TRY"
CURRENCY_TRY_DESCRIPTION = "TÜRK LİRASI"
CURRENCY_EUR = "EUR"
CURRENCY_EUR_DESCRIPTION = "EURO"
CURRENCY_USD = "USD"
CURRENCY_USD_DESCRIPTION = "AMERİKAN DOLARI"

PARSER_TYPE_TCMB = 0
PARSER_TYPE_ISBANK = 1
PARSER_TYPE_YAPIKREDI = 2
PARSER_TYPE_INVESTING = 3
PARSER_TYPE_BLOOMBERG = 4

TIME_FORMAT = "%Y%m%d%H%M%S"
DATA_PATH = "/currency/"