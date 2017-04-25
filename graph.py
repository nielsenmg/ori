from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt
import sys


class Graph:

    @staticmethod
    def draw(file):
        try:
            f = open(file, 'r')
            data = {}
            lines = f.readlines()
            for line in lines:
                k, v = line.split(' ')
                data[k] = int(v.strip("\n"))
            f.close()
            data = OrderedDict(sorted(data.items(), key=lambda v: v[1], reverse=True))

            plt.bar(range(len(data)), data.values(), align='center')
            plt.xticks(range(len(data)), list(data.keys()))
            plt.show()
        except IOError:
            sys.stderr.write("Failed to open the file '" + file + "'.")