#!/usr/bin/python3

def multiple_returns(sentence):
    """
    If the sentence is empty, the first character should be equal to None
    """
    if sentence == "":
        return(0, None)
    """
    return a tuple with the length of a string and its first character.
    """
    return (len(sentence), sentence[0])
