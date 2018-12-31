import requests
from bs4 import BeautifulSoup as bs
from enum import Enum
from .common import BaseRefresher
from .common import UnrecongnizedDataException

class OptionRefresher(BaseRefresher):
  
  def __init__(self, db_client, ticker_name):
    super(OptionRefresher, self).__init__(db_client)
    self._mongo_collection = 'OptionChains'


class OptionType(Enum):
  CALL = 1
  PUT = 2


class OptionQuote(object):  

  static_fields = ['symbol', 'type', 'strike_price', 'due_date']
  dynamic_fields = ['last_price', 'vol', 'open_int', 'today_date']
  all_fields = static_fields + dynamic_fields

  def __init__(self, **kwargs):
    self._data = {f: kwargs.get(f) for f in self.all_fields}

  def __repr__(self):
    return repr(self._data)

  def getkey(self):
    return (self._data[f] for f in self.static_fields)

class OptionChain(object):
  
  def __init__(self, symbol, today_date):
    self._symbol = symbol
    self._today_date = today_date
    self._data = {}

  def with_quote(self, quote):
    self._data[quote.getkey()] = quote
    return self

  def __repr__(self):
    representation = '(symbol: %r, today_date: %r, data: %r)' % (
        self._symbol, self._today_date, self._data)
    return representation

