print("""
    **************************************
    **  Welcome to Madlib CLI Edition!  **
    **          as they appear          **
    **   Type in adjectives and nouns   **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    """)


def read_template(temp):
    try:
        with open(temp) as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template():
    with open() as p:
        return p()


def merge():
    with open() as m:
        return m()
