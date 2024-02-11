import string
import itertools

def generate_password_combinations(length_min, length_max, include_digits, include_special_chars):
    characters = string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    for length in range(length_min, length_max + 1):
        for combination in itertools.product(characters, repeat=length):
            yield ''.join(combination)