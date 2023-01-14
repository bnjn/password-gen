# Password Generator

Outputs random password of length (2-100) with or without special characters. Requires `python3`.

### Usage as module:

`gen_pass.generate_password(length, special)`

`length` must be an integer between 2 and 100. `special` is optional, password will contain special characters if `True`.

### Usage as terminal app:

Run `python3 gen_pass.py` and follow prompts.

Example output:

    python3 gen_pass.py    
    Length of password (2-100): 25
    Special characters? (Yes/No/Y/N): yes
    dtf=m2]Py[&{~OZjErI66 '?e

### Run unit tests:

`python3 gen_pass_test.py`