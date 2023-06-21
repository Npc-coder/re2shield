import re2shield

if __name__ == "__main__":
    db = re2shield.Database()

    # Load patterns from file
    try:
        db = re2shield.load('patterns.db')
        print(db)  # Prints the number of patterns in the database
    except FileNotFoundError:
        # If pattern file doesn't exist, compile the patterns
        patterns = [
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 1),
            (r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', 2),
            (r'\d+', 3)
        ]

        expressions, ids = zip(*patterns)
        db.compile(expressions=expressions, ids=ids, overwrite=False)
        print(db)  # Prints the number of patterns in the database
        db.dump('patterns.db')

    # Find patterns in text
    def match_handler(id, from_, to, flags, context):
        print(f"Match found for pattern {id} from {from_} to {to}: {context}")

    db.scan('test@ex12ample12.com', match_handler)
