#!/sur/bin/python3

def multiply_by_2(a_dictionary):
    dictionary = dict(a_dictionary)
    for dictkey, value in dictionary.items():
        dictionary[dictkey] = value * 2
    return dictionary
