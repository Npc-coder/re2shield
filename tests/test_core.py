import re2shield

if __name__ == "__main__":
    db = re2shield.Database()

    # 파일에서 패턴 불러오기
    try:
        db = re2shield.load('patterns.pkl')
        print("DB load")
    except FileNotFoundError:
        # 패턴 파일이 없는 경우 패턴 컴파일
        patterns = [
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 1, None),
            (r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', 2, None),
            (r'\d+', 3, None)
        ]

        expressions, ids, flags = zip(*patterns)
        db.compile(expressions=expressions, ids=ids, flags=flags)
        db.dump('patterns.pkl')

    # 텍스트에서 패턴 찾기
    def match_handler(id, from_, to, flags, context):
        print(f"Match found for pattern {id} from {from_} to {to}: {context}")

    db.scan('test@ex12ample12.com', match_handler)
