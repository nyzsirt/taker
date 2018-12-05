from decimal import Decimal as D

TCMB_TODAY_URL = 'http://www.tcmb.gov.tr/kurlar/today.xml'
TCMB_ARCHIVE_URL = 'http://www.tcmb.gov.tr/kurlar/%Y%m/%d%m%Y.xml?_=%s'

STANDARD_CODES = {'TL': 'TRY',
                  'TRL': 'TRY',
                  'YTL': 'TRY'}

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