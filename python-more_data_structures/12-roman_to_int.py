#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    elif not roman_string:
        return 0
    else:

        rom_val = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
        }
        result = 0
        prev_val = 0

        for char in reversed(roman_string):
            current_val = rom_val[char]

            if current_val >= prev_val:
                result += current_val
            else:
                result -= current_val

            prev_val = current_val
        return result
