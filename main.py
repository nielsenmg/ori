#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from optparse import OptionParser

import sys

from frequency_counter import FrequencyCounter


def main():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-f", "--file", action="store", type="string", dest="inputFile", help="Source file")
    parser.add_option("-o", "--output", action="store", type="string", default="output.txt", dest="outputFile",
                      help="Output file")
    (options, args) = parser.parse_args()

    if options.inputFile is None:
        parser.error("Input file must be informed. \nRun again using option -f or --file to inform the input file.")

    fc = FrequencyCounter()
    frequences = fc.count_word_frequences(options.inputFile)

    try:
        output = open(options.outputFile, 'w+')
        for key, value in frequences.items():
            output.write("%s %s\n" % (key, value))

    except IOError:
        sys.stderr.write("Failed to open the file '" + options.outputFile + "' for writting.")

if __name__ == '__main__':
    main()
