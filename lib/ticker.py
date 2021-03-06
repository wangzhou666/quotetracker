import requests
from bs4 import BeautifulSoup as bs
from .common import BaseRefresher
from .common import UnrecongnizedDataException


class SP500TickerRefresher(BaseRefresher):
  
  def __init__(self, db_client):
    super(SP500TickerRefresher, self).__init__(db_client)
    self._mongo_collection = 'SP500'

  def _read(self):
    def is_table_changed(table):
      theads = [th.text for th in table.tr.find_all('th')]
      return (table.previous_sibling.previous_sibling.span['id'] != 'S.26P_500_Component_Stocks' or
              theads != ['Symbol', 'Security', 'SEC filings', 'GICS Sector', 'GICS Sub Industry', 'Location',
                         'Date first added[3][4]', 'CIK', 'Founded\n'])
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = requests.get(url).content
    soup = bs(html)
    if is_table_changed(soup.table):
      raise UnrecongnizedDataException('The wiki page has been changed. Please consider refactor _read method.')
    self._data = []
    for tr in soup.table.find_all('tr')[1:]:
      tds = tr.find_all('td')
      entity = Ticker(symbol=tds[0].text.rstrip(),
                      security=tds[1].text.rstrip(),
                      reports=tds[2].a['href'].rstrip(),
                      sector=tds[3].text.rstrip(),
                      sub_industry=tds[4].text.rstrip(),
                      location=tds[5].text.rstrip(),
                      cik=tds[7].text.rstrip(),
                      founded=tds[8].text.rstrip())
      self._data.append(entity)
    

class Ticker(object):

  def __init__(self, symbol, security, sector=None, sub_industry=None,
               location=None, founded=None, **kwargs):
    assert symbol and security
    self.symbol = symbol
    self.security = security
    self.misc  = {
        'sector': sector,
        'sub_industry': sub_industry,
        'location': location,
        'founded': founded,
    }
    self.misc.update(kwargs)

  def to_mongo_entity(self):
    return {
        'symbol': self.symbol,
        'security': self.security,
        'misc': self. misc,
    }

  def __repr__(self):
    return repr(self.to_mongo_entity())

