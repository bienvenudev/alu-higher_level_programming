#!/usr/bin/python3
'''a function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
  '''read a text file (UTF8) and print it to stdout'''
  with open(f'{filename}', encoding='utf-8') as file:
    print(file.read())
