import requests
from bs4 import BeautifulSoup as bs
from .common import BaseRefresher
from .common import UnrecongnizedDataException

class OptionRefresher(BaseRefresher):
  
  def __init__(self, db_client, ticker_name):
    super(OptionRefresher, self).__init__(db_client)
    self._mongo_collection = 'OptionChains'

class OptionQuote(object):
  pass

class OptionChain(object):
  pass

