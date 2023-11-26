#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    input_string = input('Enter string: ')
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    string_vowels = [char for char in input_string if char in vowels]
    print(f'General vowel count: {len(string_vowels)}')