#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) < 1:
        first = None
        leng = 0
    else:
        leng = len(sentence)
        first = sentence[0]
        return (leng, first)
