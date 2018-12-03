class UnrecongnizedDataException(Exception):
  pass


class BaseRefresher(object):

  def __init__(self, db_client):
    self._client = db_client
    self._collection = None
    self._data = None

  def _read(self):
    pass

  def _write(self):
    if not self._collection:
      raise RuntimeError('No MongoDB collection is specified for write destination.')
    # TODO: write entity to mongodb
    return

  def refresh(self):
    self._read()
    self._write()

  def __del__(self):
    self._client.close()

