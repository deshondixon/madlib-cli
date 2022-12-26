# LAB 3 - Class 401d20

## madlib-cli

#### *Author:* DeShon Dixon

---

## Overview

- Prints a welcome message to the user, explaining the Madlib process and command line interactions.

- Reads a template Madlib file , and parses that file into usable parts.

- Prompts the user to submit a series of words to fit each of the required components of the Madlib template.

- With the collected user inputs, it populates the template that each provided input is placed into the correct position within the template.

- After the resulting Madlib has been completed, it provides the completed response back to the user in the command line.

- Writes the completed text to a new file.

---

## Setup

- Create repo on desktop
- Create virtual environment: 
*python3.11 -m venv .venv*
- Activate environment: 
*source .venv/bin/activate*
- Install pywatch: 
*pip install pytest-watch*
- Clone repo: *https://github.com/deshondixon/madlib-cli*


---

## Run

- Run test with:  
*pytest-watch*
---
- Run program with: 
*python3.11 ./madlib_cli/madlib.py*

## Tests

- Use *pytest-watch* to test program.
---
- test_read_template_returns_stripped_string tests if read_template gets file from file path.
- test_parse_template test if parse_template separates content correct
- test_merge test if users input are combined correct
- test_read_template_raises_exception_with_bad_path test is try catch rasies an error when file path is not correct



