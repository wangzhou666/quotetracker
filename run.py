from lib import ticker
from optparse import OptionParser
from pymongo import MongoClient

MONGO_ENDPOINT = 'mongodb://root:jHabTlqz23@localhost:27017'

def refresh_indices_ticker(db_client):
  sp_refresher = ticker.SP500TickerRefresher(db_client)
  sp_refresher.refresh() 

def main():
  op = OptionParser()
  op.add_option('--dryrun', dest='dryrun', action='store_true')
  op.add_option('--refresh_index_tickers', dest='refresh_index_tickers', action='store_true')
  option, _ = op.parse_args()

  if option.dryrun:
    return
  if option.refresh_index_tickers:
    db_client = MongoClient(MONGO_ENDPOINT)
    refresh_indices_ticker(db_client)

if __name__ == '__main__':
  main()

