import re
from textwrap import dedent


def intro():
    print(dedent("""
    **************************************
    **  Welcome to Madlib CLI Edition!  **
    **          as they appear          **
    **   Type in adjectives and nouns   **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    """))


def read_template(x):
    try:
        with open(x, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError


def parse_template(string):
    base_string = ""
    extract_parts = []
    is_a_part = False
    part = ""
    for char in string:
        if char == "{":
            base_string += char
            is_a_part = True
        elif char == "}":
            base_string += char
            extract_parts.append(part)
            part = ""
            is_a_part = False
        elif is_a_part is False:
            base_string += char
        elif is_a_part is True:
            part += char
    return base_string, tuple(extract_parts)


def merge(stripped, inputs):
    return stripped.format(*inputs)


def main():
    intro()

    adjective = input("Enter a Adjective ")
    adjective1 = input("Enter another Adjective ")
    noun = input("Enter a noun ")

    madlib = f"It was a {adjective} and {adjective1} {noun}."

    print(madlib)

    with open("madlib_cli/madlib.py", "r") as f:
        contents = f.read()

    with open("assets/dark_and_stormy_night_template_complete.txt", "w+") as f2:
        f2.write(madlib)


if __name__ == "__main__":
    main()
