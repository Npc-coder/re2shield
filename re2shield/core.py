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

class Re2Shield:
    def __init__(self):
        self.db = None

    def compile(self, expressions, ids, flags):
        if len(expressions) != len(ids) != len(flags):
            raise ValueError("All parameters should have the same length")

        # 중복된 ID가 있는지 확인
        if len(ids) != len(set(ids)):
            raise ValueError("IDs should be unique")

        re2_patterns = {}
        raw_patterns = {}
        for id, expr, flag in zip(ids, expressions, flags):
            re2_patterns[id] = re2.compile(expr, flag)
            raw_patterns[id] = (expr, flag)

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
        re2_patterns = {id: re2.compile(expr, flag) for id, (expr, flag) in raw_patterns.items()}
    re2_shield = Re2Shield()
    re2_shield.db = Re2ShieldDatabase(re2_patterns, raw_patterns)
    return re2_shield
    return db

