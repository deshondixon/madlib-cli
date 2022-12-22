print("""
    **************************************
    **  Welcome to Madlib CLI Edition!  **
    **          as they appear          **
    **   Type in adjectives and nouns   **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    """)


def read_template(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(template):
    stripped_string = ""
    actual_parts_string = ""
    actual_parts = []

    is_part = False
    for char in template:
        if char == "{":
            stripped_string += char
            is_part = True
        elif is_part == True and char != "}":
            actual_parts_string += char
        elif is_part == True and char == "}":
            stripped_string += char
            is_part = False
            actual_parts.append(actual_parts_string)
            actual_parts_string = ""
        else:
            stripped_string += char
    return stripped_string, tuple(actual_parts)


def merge(text, inputs):
    print(text.format(*inputs))
    return text.format(*inputs)
