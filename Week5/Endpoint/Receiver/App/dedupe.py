import hashlib
import time

class Dedupe:
    def __init__(self):
        self.cache = {}

    def key(self, alert):
        base = alert['rule'] + alert['host']
        return hashlib.md5(base.encode()).hexdigest()

    def is_new(self, alert):
        k = self.key(alert)
        now = time.time()
        if k in self.cache and now - self.cache[k] < 300:
            return False
        self.cache[k] = now
        return True
