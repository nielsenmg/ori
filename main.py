#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import OrderedDict
f = open(sys.argv[1], 'r')
index = {}
for line in f:
    words = line.split(" ")
    for word in words:
        word = word.strip().strip('\n').strip(',.?!;:\n').upper()

        if len(word) > 3:
          if word in index:
              index[word] = index[word] + 1
          else:
              index[word] = 1

orderedDictionary = OrderedDict(sorted(index.items(), key=lambda v: v[1], reverse=True))
fo = open(sys.argv[2], 'w+')
for word in orderedDictionary.items():
  fo.write(str(word[0]) + " " + str(word[1]) + '\n')
