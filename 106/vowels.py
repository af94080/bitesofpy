from typing import Tuple
import re

text = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!
All the way"""
vowels = 'aeiou'
vowels_uc = "".join([ele.upper() for ele in vowels])

vowels_pipe_delim = "|".join([ele for ele in vowels + vowels_uc])


def strip_vowels(text: str) -> Tuple[str, int]:
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    asterixed_text = re.sub(vowels_pipe_delim, '*', text)
    nbr_of_asterixes = len([ele for ele in asterixed_text if ele == '*'])
    return(asterixed_text, nbr_of_asterixes)

