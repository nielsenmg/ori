# -*- coding: utf-8 -*-
from string import ascii_letters
from collections import OrderedDict
import unicodedata


class FrequencyCounter:
    ASC = False
    DESC = True

    def __init__(self):
        self.frequences = {}

    @staticmethod
    def normalize_word(word):
        return word.strip('\'\"!?,:;. ').lower()

    def count_word_frequences(self, input_file):
        try:
            file = open(input_file, 'r')
            words = file.read().replace('\n', ' ').split(' ')
            for word in words:
                word = FrequencyCounter.normalize_word(word)
                if len(word) > 3:
                    if word in self.frequences:
                        self.frequences[word] += 1
                    else:
                        self.frequences[word] = 1
            return self.get_frequences()
        except IOError:
            print("The file '" + input_file + "' was not found.")

    def get_frequences(self, sort_type=DESC):
        return OrderedDict(sorted(self.frequences.items(), key=lambda v: v[1], reverse=sort_type))
