import requests

from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class BaseIndexTickerRefresher(ABC):

  @abstractmethod
  def __init__(self, db_client):
    self._client = db_client
    self._collection = None
    self._data = {
      'keys': [],
      'values': [],
    }

  @abstractmethod
  def _read(self):
    pass

  def _write(self):
    if not self._collection:
      raise RuntimeError('No MongoDB collection is specified for write destination.')
    # TODO
    return

  def refresh(self):
    self._read()
    self._write()

  def __del__(self):
    self._client.close()

class SP500TickerRefresher(BaseIndexTickerRefresher):
  
  def __init__(self, db_client):
    super(SP500TikerRefresher, self).__init__(db_client)
    self._collection = 'SP500'

  def _read(self):
    pass
