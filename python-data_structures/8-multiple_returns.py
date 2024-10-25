#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence < 1:
        firstchar = None
        length = 0
    else:
        leng = len(sentence)
        first = sentence[0]
        message = "Length: {:d} - First character: {}".format(leng, first)

        return message
