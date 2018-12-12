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

  fields = ['symbol', 'type', 'last_price', 'vol', 'open_int',
            'strike_price', 'due_date', 'today_date']

  def __init__(self, **kwargs):
    self._data = {f: kwargs.get(f) for f in self.fields}

  def __repr__(self):
    return repr(self._data)

class OptionChain(object):
  pass

