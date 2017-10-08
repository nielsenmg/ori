#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from optparse import OptionParser
from inverted_index import InvertedIndex


def main():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-d", "--documents", action="store", type="string", default="./inputs.txt",
                      dest="documents_path_file", help="Set the path for the input file with the documents location.")
    parser.add_option("-o", "--output", action="store", type="string", default="./indice.txt", dest="output_file",
                      help="Set the path for the output file.")
    parser.add_option("-s", "--stopwords", action="store", type="string", default="./stopwords.txt",
                      dest="stopwords_file", help="Set the path of the stopwords file.")
    (options, args) = parser.parse_args()
    inverted_index = InvertedIndex()
    inverted_index.generate_index(options.documents_path_file, options.stopwords_file, options.output_file)


if __name__ == '__main__':
    main()
