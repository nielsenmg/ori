from string import ascii_letters
from collections import OrderedDict
from unicodedata import normalize


class FrequencyCounter:
    ASC = False
    DESC = True

    def __init__(self):
        self.frequences = {}

    @staticmethod
    def normalize_word(word):
        return ''.join(x for x in normalize('NFKD', word) if x in ascii_letters).lower()

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
            return self.sort_frequences()
        except IOError:
            print("The file '" + input_file + "' was not found.")

    def sort_frequences(self, sort_type=DESC):
        return OrderedDict(sorted(self.frequences.items(), key=lambda v: v[1], reverse=sort_type))
