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
        self.id_counter = 0

    def __str__(self):
        if self.db is not None:
            return f"Database with {self.db.count_patterns()} patterns."
        else:
            return "Database is not compiled."

    def compile(self, expressions, overwrite=False):
        if overwrite or self.db is None:
            self.db = Re2ShieldDatabase({}, {})
            self.id_counter = 0

        for expr in expressions:
            self.db.re2_patterns[self.id_counter] = re2.compile(expr)
            self.db.raw_patterns[self.id_counter] = expr
            self.id_counter += 1

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
    re2_shield.id_counter = max(raw_patterns.keys()) + 1
    return re2_shield
