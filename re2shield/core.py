import pickle
import re2

class Re2ShieldDatabase:
    def __init__(self, re2_patterns, raw_patterns):
        self.re2_patterns = re2_patterns
        self.raw_patterns = raw_patterns

    def findall(self, text, callback):
        for id, pattern in self.re2_patterns.items():
            matches = pattern.finditer(text)
            for match in matches:
                callback(id, match.start(), match.end(), None, match.group())

    def count_patterns(self):
        return len(self.re2_patterns)

class Re2Shield:
    def __init__(self):
        self.db = None
        self.version = None

    def __str__(self):
        message = {
            "version": self.version,
            "pattern_counts": self.db.count_patterns() if self.db is not None else 0
        }
        return str(message)

    def compile(self, expressions, ids, overwrite=False):
        if len(expressions) != len(ids):
            raise ValueError("All parameters should have the same length")

        re2_patterns = {}
        raw_patterns = {}
        if not overwrite and self.db is not None:
            re2_patterns = self.db.re2_patterns.copy()
            raw_patterns = self.db.raw_patterns.copy()

        for id, expr in zip(ids, expressions):
            if id in re2_patterns:
                raise ValueError(f"ID {id} already exists in the database. To overwrite, set overwrite=True.")
            re2_patterns[id] = re2.compile(expr)
            raw_patterns[id] = expr

        self.db = Re2ShieldDatabase(re2_patterns, raw_patterns)

    def dump(self, file_path):
        if self.db is not None:
            with open(file_path, 'wb') as f:
                pickle.dump(self.db.raw_patterns, f)
        else:
            raise ValueError("No compiled database found. Please compile patterns first.")

    def scan(self, text, callback):
        if self.db is not None:
            self.db.findall(text, callback)
        else:
            raise ValueError("No compiled database found. Please compile patterns first.")

Database = Re2Shield

def load(file_path):
    with open(file_path, 'rb') as f:
        raw_patterns = pickle.load(f)
        re2_patterns = {id: re2.compile(expr) for id, expr in raw_patterns.items()}
    re2_shield = Re2Shield()
    re2_shield.db = Re2ShieldDatabase(re2_patterns, raw_patterns)
    return re2_shield
