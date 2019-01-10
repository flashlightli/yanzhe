# -*- coding: utf-8 -*-


def test_a(a=1):
    print('a==', a)
    return {'a': a}


# @bind('test/b')
def test_b(b=2):
    print('b==', b)
    return {'b': b}
