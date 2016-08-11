import re

import numpy

"""
Process Latency Data
"""


class LatencyProcessor:
    def __init__(self):

        self.instructSet = set([])
        self.clockDict = {}
        self.instructsDict = {}
        self.mean = {}
        self.var = {}

        self.readLatency('../../../data/fvec.txt')
        self.query()
        self.write('../../../output/fvec.txt')
        # self.debug()

    def readLatency(self, fileSrc):
        file = open(fileSrc, 'r')
        for line in file:
            if (re.match('Latency: ', line)):
                instruct = line.split('Latency: ')[1].strip()
                print instruct
                self.instructSet.add(instruct)
                self.clockDict[instruct] = []
                self.instructsDict[instruct] = []
            elif (re.match('( )*\d+( )*\d+', line)):
                m = re.match('( )*(\d+)( )*(\d+)', line)
                self.clockDict[instruct].append(int(m.group(2)))
                self.instructsDict[instruct].append(int(m.group(4)))

    def query(self):
        for key in self.instructSet:
            clock = numpy.array(self.clockDict.get(key))
            instructs = numpy.array(self.instructsDict.get(key))
            self.mean[key] = 1.0 * clock.sum() / instructs.sum()
            self.var[key] = (1.0 * clock / instructs).var()

    def write(self, fileSrc):
        outFile = open(fileSrc, 'w')
        outFile.write('Instruct name\tMean Latency(Clock Cycle)\tVar\n')
        for key in self.instructSet:
            outFile.write(
                key + '\t' + str(round(self.mean.get(key), 2)) + '\t' + str(round(self.var.get(key), 2)) + '\n')

    def debug(self):
        for key in self.instructSet:
            print key
            print self.clockDict.get(key)
            print self.instructsDict.get(key)
            print self.mean.get(key)
            print self.var.get(key)


if __name__ == '__main__':
    latencyProcessor = LatencyProcessor()
