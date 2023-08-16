#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = 0
    old_val = 0

    for symbol in reversed(roman_string):
        val = roman_val.get(symbol, 0)
        if val >= old_val:
            res += val
        else:
            res -= val
        old_val = val

    return res
