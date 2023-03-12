#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        pau = len(tuple_a)
        mos = len(tuple_b)
        if pau == 2 and mos == 2:
            c = tuple_a[0] + tuple_b[0]
            d = tuple_a[1] + tuple_b[1]
        elif pau == 2 and mos == 1:
            c = tuple_a[0] + tuple_b[0]
            d = tuple_a[1] + 0
        elif pau == 2 and mos == 0:
            c = tuple_a[0] + 0
            d = tuple_a[1] + 0
        elif pau == 1 and mos == 2:
            c = tuple_a[0] + tuple_b[0]
            d = 0 + tuple_b[1]
        elif pau == 0 and mos == 2:
            c = 0 + tuple_b[0]
            d = 0 + tuple_b[1]
        elif pau == 1 and mos == 1:
            c = tuple_a[0] + tuple_b[0]
            d = 0 + 0
        elif pau == 0 and mos == 1:
            c = 0 + tuple_b[0]
            d = 0 + 0
        elif pau == 0 and mos == 0:
            c = 0 + 0
            d = 0 + 0
        elif pau == 1 and mos == 0:
            c = tuple_a[0] + 0
            d = 0 + 0
        x = c, d
        return x
