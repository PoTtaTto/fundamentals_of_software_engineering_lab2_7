#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    input_str1 = input('Enter first string: ')
    input_str2 = input('Enter second string: ')
    general_symbols = set(input_str1).intersection(set(input_str2))

    print('General symbols: ', ', '.join(general_symbols))