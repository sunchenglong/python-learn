import re
import os
import numpy

"""
Common Process Latency Data
"""


class CommonFilter:
    def __init__(self, input = '../../../data/fvec.txt', output = '../../../output/fvec.txt'):
        self.instructSet = set([])
        self.type = {}
        self.clockDict = {}
        self.instructsDict = {}
        self.mean = {}
        self.var = {}
        self.readLatency(input)
        self.query()
        self.write(output)
        self.debug()

    def readLatency(self, fileSrc):
        file = open(fileSrc, 'r')
        for line in file:
            print line
            if re.match('Latency: ', line) or re.match('Instruction: ', line) or re.match('instruction: ', line) \
                    or re.match('Throughput: ', line) or re.match('Latency/throughput: ', line) \
                    or re.match(
                        '(SSE)|(taken)|(instructions)|(Instructions)|(Number)|(method: )'
                        '|(Throughput)|(Latency)|(register)|(chainlength)|(multiplication)', line):
                if re.match('Latency: ', line):
                    instruct = line.split('Latency: ')[1].strip()
                    self.type[instruct] = 'Latency'
                elif re.match('Instruction: ', line):
                    instruct = line.split('Instruction: ')[1].strip()
                    self.type[instruct] = 'Latency'
                elif re.match('Latency/throughput: ', line):
                    instruct = line.split('Latency/throughput: ')[1].strip()
                    self.type[instruct] = 'Latency'
                elif re.match('instruction: ', line):
                    instruct = line.split('instruction: ')[1].strip()
                    self.type[instruct] = 'Latency'
                elif re.match('Throughput: ', line):
                    instruct = line.split('Throughput: ')[1].strip()
                    self.type[instruct] = 'Throughput'
                elif re.match(
                        '(SSE)|(taken)|(instructions)|(Instructions)|(Number)|(method: )'
                        '|(Throughput)|(Latency)|(register)|(chainlength)|(multiplication)', line):
                    instruct = line.strip()
                    if re.match('(throughput)|(Throughput)', line):
                        self.type[instruct] = 'Throughput'
                    else:
                        self.type[instruct] = 'Latency'
                else:
                    print "nop"
                print "LOG:" + instruct
                self.instructSet.add(instruct)
                self.clockDict[instruct] = []
                self.instructsDict[instruct] = []
            elif re.match('( )*\d+( )*\d+', line):
                m = re.match('( )*(\d+)( )*(\d+)', line)
                try:
                    print instruct
                    self.clockDict[instruct].append(int(m.group(2)))
                    self.instructsDict[instruct].append(int(m.group(4)))
                except:
                    print "Except"

    def query(self):
        for key in self.instructSet:
            if len(self.clockDict.get(key)) != 0:
                clock = numpy.array(self.clockDict.get(key))
                instructs = numpy.array(self.instructsDict.get(key))
                self.mean[key] = 1.0 * clock.sum() / instructs.sum()
                self.var[key] = (1.0 * clock / instructs).var()

    def write(self, fileSrc):
        outFile = open(fileSrc, 'w')
        # outFile.write('Instruct name\tTest Type\tMean Latency(Clock Cycle)\tVar\n')
        for key in self.instructSet:
            try:
                outFile.write(
                    key + '\t' + self.type.get(key) + '\t' + str(round(self.mean.get(key), 2)) + '\t' + \
                    str(round(self.var.get(key), 2)) + '\n')
            except:
                print self.var.get(key)


    def debug(self):
        for key in self.instructSet:
            print key
            print self.type.get(key)
            print self.clockDict.get(key)
            print self.instructsDict.get(key)
            print self.mean.get(key)
            print self.var.get(key)


class Driver:
    def __init__(self):
        self.listFiles('../../../result20160817', '../../../out20160817')

    def listFiles(self, inputSrc, outputSrc):
        list = os.listdir(inputSrc)
        for file in list:
            input = inputSrc + '/' + file
            output = outputSrc + '/' + file
            print input
            print output
            CommonFilter(input = input, output = output)


if __name__ == '__main__':
    #commonFilter = CommonFilter(input = '../../../data/fvec.txt', output = '../../../output/fvec.txt')
    driver = Driver()
