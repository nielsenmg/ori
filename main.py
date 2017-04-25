#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from optparse import OptionParser

import sys
import glob

from frequency_counter import FrequencyCounter
from graph import Graph

def main():
    parser = OptionParser("usage: %prog [options]")
    parser.add_option("-i", "--input", action="store", type="string", default="./input/*txt", dest="inputFolder",
                      help="Set the input folder")
    parser.add_option("-o", "--output", action="store", type="string", default="./output/", dest="outputFolder",
                      help="Set the output folder")
    (options, args) = parser.parse_args()

    fc = FrequencyCounter()
    files = glob.glob(options.inputFolder)
    for file in files:
        fc.count_word_frequences(file)

    frequences = fc.get_frequences()

    try:
        output = open(options.outputFolder + "output.txt", 'w+')
        for key, value in frequences.items():
            output.write("%s %s\n" % (key, value))
        output.close()
    except IOError:
        sys.stderr.write("Failed to open the file '" + options.outputFile + "' for writting.")

    Graph.draw(options.outputFolder + "output.txt")

if __name__ == '__main__':
    main()
