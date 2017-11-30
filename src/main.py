#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from optparse import OptionParser

from src.inverted_index import InvertedIndex
from src.vector_representation import VectorRepresentation
# from src.query_handler import QueryHandler


def main():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-d", "--documents", action="store", type="string", default="./inputs/inputs.txt",
                      dest="docs_path", help="Set the path for the input file with the documents location.")
    parser.add_option("-i", "--index", action="store", type="string", default="./outputs/indice.txt",
                      dest="index_path", help="Set the path for the output file.")
    parser.add_option("-s", "--stopwords", action="store", type="string", default="./inputs/stopwords.txt",
                      dest="stopwords_file", help="Set the path of the stopwords file.")
    parser.add_option("-q", "--query", action="store", type="string", default="./inputs/query.txt",
                      dest="query_file", help="Set the path of the query file.")
    parser.add_option("-v", "--vector", action="store", type="string", default="./outputs/repdocs.txt",
                      dest="vector_rep", help="Set the path of the vector representation file.")
    parser.add_option("-a", "--answer", action="store", type="string", default="./outputs/answer.txt",
                      dest="answer_file", help="Set the path of the answer file.")
    (options, args) = parser.parse_args()
    inverted_index = InvertedIndex()
    inverted_index.generate_file(options.docs_path, options.stopwords_file, options.index_path)

    vector_representation = VectorRepresentation(options.docs_path, options.index_path)
    vector_representation.generate_file(options.vector_rep)

    # query_handler = QueryHandler(options.query_file, vector_representation.get_representation())
    # query_handler.generate_file(options.answer_file)


if __name__ == '__main__':
    main()
