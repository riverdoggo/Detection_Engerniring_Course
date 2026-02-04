import json
import sqlite3

class Storage:
    def __init__(self):
        self.db = sqlite3.connect('alerts.db')
        self.db.execute('CREATE TABLE IF NOT EXISTS alerts (id TEXT, data TEXT)')

    def save(self, alert):
        self.db.execute('INSERT INTO alerts VALUES (?,?)',
                        (alert['id'], json.dumps(alert)))
        self.db.commit()

    def stats(self):
        cur = self.db.execute('SELECT COUNT(*) FROM alerts')
        return cur.fetchone()[0]
