import json
from storage import Storage
from dedupe import Dedupe

store = Storage()
dedupe = Dedupe()

def ingest(alert):
    if dedupe.is_new(alert):
        store.save(alert)

def summary():
    return store.stats()

if __name__ == '__main__':
    print(summary())
