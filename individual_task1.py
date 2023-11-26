#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = {'b', 'f', 'g', 'm', 'o'}
    b = {'b', 'g', 'h', 'l', 'u'}
    c = {'e', 'f', 'm'}
    d = {'e', 'g', 'l', 'p', 'q', 'u', 'v'}
    all_ = a.union(b).union(c).union(d)

    x = (a.intersection(c)).union(b)
    y = (a.intersection(all_.difference(b))).union(c.difference(d))

    print(f'x = {x}')
    print(f'y = {y}')