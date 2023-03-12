#!/usr/bin/python3
def multiple_returns(sentence):
    pau = len(sentence)
    if pau == 0:
        return pau, None
    else:
        return pau, sentence[0]
