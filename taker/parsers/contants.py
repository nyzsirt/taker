from decimal import Decimal as D

TCMB_TODAY_URL = 'http://www.tcmb.gov.tr/kurlar/today.xml'
TCMB_ARCHIVE_URL = 'http://www.tcmb.gov.tr/kurlar/%Y%m/%d%m%Y.xml?_=%s'
ISBANK_URL = 'https://www.isbank.com.tr/layouts/ISB_DA/HttpHandlers/FxRatesHandler.ashx?Lang=tr&fxRateType=INTERACTIVE&date=%(date)s&time=%(timestamp)s'
YAPIKREDI_URL = 'https://api.yapikredi.com.tr/api/investmentrates/v1/currencyRates'

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
PARSER_TYPE_INVESTING = 2
PARSER_TYPE_BLOOMBERG = 2