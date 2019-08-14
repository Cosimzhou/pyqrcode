#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年7月22日

@author: cosimzhou
'''
from bitutil import makeBits2String, char2bool, bit2char

class BCHCoder(object):
    def __init__(self, m, n, gen = None):
        assert isinstance(m, int) and isinstance(n, int)
        self.__M, self.__N, self.__bchGen = m, n, None

        if self.__M <= self.__N or self.__N < 1:
            return
        else:
            gen = makeBits2String(gen)
            if gen is None:
                return
            gen = gen.lstrip('0')

        if len(gen) < 2 or '1' not in gen:
            return

        self.__bchGen = gen[::-1]

    def encode(self, data):
        if self.__bchGen is None:
            return None
        data = makeBits2String(data)
        if data is None:
            return None

        data = data.lstrip('0')[::-1]

        DMN = self.__M - self.__N
        memory = ([False]*DMN) + map(char2bool, data)
        assert memory[-1] or data==''
        top, genlen = len(memory), len(self.__bchGen)
        while top >= genlen:
            for i in xrange(-1, -(genlen+1), -1):
                if self.__bchGen[i] == '1':
                    memory[top+i] = not memory[top+i]
            top = 0
            for i in xrange(len(memory), 0, -1):
                if memory[i-1]:
                    top = i
                    break
        return ''.join(map(bit2char, memory[:DMN][::-1]))

