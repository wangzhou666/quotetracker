from argparse import ArgumentParser
from lib import ticker
from pymongo import MongoClient

MONGO_ENDPOINT = 'mongodb://root:jHabTlqz23@localhost:27017'

def refresh_indices_ticker(db_client):
  sp_refresher = ticker.SP500TickerRefresher(db_client)
  sp_refresher.refresh() 

def main():
  parser = ArgumentParser(description='Track the market.')
  parser.add_argument('--dryrun', dest='dryrun', action='store_true')
  parser.add_argument('--refresh_index_tickers', dest='refresh_index_tickers', action='store_true')
  args = parser.parse_args()

  if args.dryrun:
    return
  if args.refresh_index_tickers:
    db_client = MongoClient(MONGO_ENDPOINT)
    refresh_indices_ticker(db_client)

if __name__ == '__main__':
  main()

