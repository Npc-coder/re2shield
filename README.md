# re2shield
`re2shield` is a Python library that provides a shield for working with regular expressions using the `re2` module. 

It allows you to compile and search for patterns in text using the powerful regular expression engine provided by `re2`.

It allows you to hide the complexity of regular expressions and work with pattern identifiers instead.

This project utilizes the `google/re2` library, which is licensed under the BSD 3-Clause License. Please refer to the [LICENSE](https://github.com/google/re2/blob/main/LICENSE) file of `google/re2` for more information.



## Installation
Before installing `re2shield`, make sure that `re2` is installed on your system. You can install `re2` by following the instructions on the [google/re2](https://github.com/google/re2.git) GitHub repository.

Alternatively, you can use the `re2-installer.sh` script located in the `package/installed` directory. This script automates the installation process for `re2` and its dependencies. Simply run the script using the following command:

```shell
git clone https://github.com/Npc-coder/re2shield.git
cd re2shield/installed
sh re2-installer.sh
```

You can install `re2shield` using pip:
```shell
pip install re2shield
```
or
```shell
git clone https://github.com/Npc-coder/re2shield.git
cd re2shield
pip install .
```

## Updates
### Version 0.2.1
- Bug Fix
    - Removed flag
- Added type and date fields to the Re2Shield class for additional metadata.
- Updated dump and load functions to include the new type and date fields when saving and loading the compiled patterns.
- Enhanced the __str__ method of the Re2Shield class to include the new fields in the output.

Please refer to the [Usage](#usage) section for examples of how to use these new features.

## Usage
### Importing the Library
Here is a simple example demonstrating how to use re2shield:

```python
import re2shield

if __name__ == "__main__":
    db = re2shield.Database(version='1.0.0')
    # Load patterns from file
    try:
        db = re2shield.load('patterns.db')
    except FileNotFoundError:
        # If pattern file doesn't exist, compile the patterns
        patterns = [
            (r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 1),
            (r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b', 2),
            (r'\d+', 3)
        ]

        expressions, ids = zip(*patterns)
        db.compile(expressions=expressions, ids=ids, overwrite=False)
        db.dump('patterns.db')

    # Find patterns in text
    def match_handler(id, from_, to, context):
        print(f"Match found for pattern {id} from {from_} to {to}: {context}")

    db.scan('test@ex12ample12.com', match_handler)
```
In this example, we create a re2shield.Database object, compile a list of patterns with their corresponding identifiers, and then search for those patterns in the provided text. 

The match_handler function is called for each match found, allowing you to process the matches as desired.

## Use Case
One of the key advantages of re2shield is its ability to hide the actual regular expression patterns from users during distribution. By compiling the patterns with re2 and using pattern identifiers, you can distribute your code without exposing the underlying regular expression logic. This provides an additional layer of abstraction and enhances the security of your regular expression patterns.

## Features
- Hide the complexity of regular expressions
- Work with pattern identifiers instead of exposing the actual regular expression patterns
- Compile patterns for efficient matching
- Find all occurrences of patterns in text
- Customize the handling of matches using callback functions

## License
This project is licensed under the BSD 3-Clause License. See the [LICENSE](https://opensource.org/license/bsd-3-clause/) file for details.
