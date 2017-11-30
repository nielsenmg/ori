from collections import OrderedDict
import os
import sys


class InvertedIndex:

    def __init__(self):
        self.current_file = ""
        self.frequencies = {}
        self.stopwords = []
        self.documents_paths = []

    @staticmethod
    def normalize_word(word):
        return word.strip('\'\"#!?,:;. ').lower()

    def generate_file(self, documents_path_file, stopwords_file, output_file):
        self.__load_documents_path(documents_path_file)
        self.__load_stop_words(stopwords_file)

        for document_file in self.documents_paths:
            self.__count_frequencies_from_file(document_file)

        self.__sort_frequencies()
        self.__write_output_file(output_file)

    def __count_frequencies_from_file(self, document_file):
        try:
            file = open(document_file, 'r')
            _, self.current_file = os.path.split(document_file)
            words = file.read().replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ')\
                .replace('?', ' ').split(' ')
            for word in words:
                word = InvertedIndex.normalize_word(word)
                if word in self.stopwords or len(word.strip()) == 0:
                    continue

                if word in self.frequencies and self.current_file in self.frequencies[word]:
                    self.frequencies[word][self.current_file] += 1
                elif word in self.frequencies:
                    self.frequencies[word][self.current_file] = 1
                else:
                    self.frequencies[word] = {}
                    self.frequencies[word][self.current_file] = 1
        except IOError:
            print("[WARNING] - Failed to open the document file %s." % document_file)

    def __load_documents_path(self, documents_path_file):
        try:
            file = open(documents_path_file, 'r')
            self.documents_paths = file.read().split('\n')
            file.close()
        except IOError:
            raise IOError

    def __load_stop_words(self, stopwords_file):
        try:
            file = open(stopwords_file, 'r')
            self.stopwords = file.read().replace('\n', ' ').split(' ')
            file.close()
        except IOError:
            raise IOError

    def __sort_frequencies(self):
        self.frequencies = OrderedDict(sorted(self.frequencies.items()))

    def __write_output_file(self, output_file):
        try:
            file = open(output_file, 'w+')
            for key, value in self.frequencies.items():
                file.write("%s:" % key)
                for doc, freq in value.items():
                    file.write(" %s,%s" % (doc, freq))
                file.write("\n")
            file.close()
        except IOError:
            sys.stderr.write("Failed to open the file %s for writing." % output_file)
