import re
import os
import numpy

"""
Common Process Latency Data
"""


class CommonFilter:
    def __init__(self, input='../../../data/fvec.txt', output='../../../output/fvec.txt'):
        self.instructSet = set([])
        self.clockDict = {}
        self.instructsDict = {}
        self.mean = {}
        self.var = {}
        self.readLatency(input)
        self.query()
        self.write(output)
        #self.debug()

    def readLatency(self, fileSrc):
        file = open(fileSrc, 'r')
        for line in file:
            print line
            if re.match('Latency: ', line) or re.match('Instruction: ', line) or re.match('instruction: ', line) \
                    or re.match('Throughput: ', line) or re.match('Latency/throughput: ', line) \
                    or re.match(
                        '(taken)|(instructions)|(Instructions)|(method: )|(Throughput)|(Latency)', line):
                if re.match('Latency: ', line):
                    instruct = line.split('Latency: ')[1].strip()
                    type = 'Latency'
                elif re.match('Instruction: ', line):
                    instruct = line.split('Instruction: ')[1].strip()
                    type = 'Latency'
                elif re.match('Latency/throughput: ', line):
                    instruct = line.split('Latency/throughput: ')[1].strip()
                    type = 'Latency'
                elif re.match('instruction: ', line):
                    instruct = line.split('instruction: ')[1].strip()
                    type = 'Latency'
                elif re.match('Throughput with memory operand: ', line):
                    instruct = line.split('Throughput with memory operand: ')[1].strip()
                    type = 'Throughput'
                elif re.match('Throughput with memory source operand: ', line):
                    instruct = line.split('Throughput with memory source operand: ')[1].strip()
                    type = 'Throughput'
                elif re.match('Throughput with memory destination operand: ', line):
                    instruct = line.split('Throughput with memory destination operand: ')[1].strip()
                    type = 'Throughput'
                elif re.match('Latency with memory destination operand: ', line):
                    instruct = line.split('Latency with memory destination operand: ')[1].strip()
                    type = 'Latency'
                elif re.match('Throughput: ', line):
                    instruct = line.split('Throughput: ')[1].strip()
                    type = 'Throughput'
                elif re.match(
                        '(taken)|(instructions)|(Instructions)|(method: )|(Throughput)|(Latency)', line):
                    instruct = line.strip()
                    if re.match('(throughput)|(Throughput)', line):
                        type = 'Throughput'
                    else:
                        type = 'Latency'
                else:
                    print "nop"
                print "LOG:" + instruct
                print "LOG:" + type
                self.instructSet.add(instruct)
                if instruct not in self.clockDict:
                    self.clockDict[instruct] = {}
                    self.instructsDict[instruct] = {}
                self.clockDict[instruct][type] = []
                self.instructsDict[instruct][type] = []
            elif re.match('( )*\d+( )*\d+', line):
                m = re.match('( )*(\d+)( )*(\d+)', line)
                try:
                    print instruct
                    print type
                    self.clockDict[instruct][type].append(int(m.group(2)))
                    self.instructsDict[instruct][type].append(int(m.group(4)))
                except:
                    print "Except"

    def query(self):
        for key in self.instructSet:
            if key not in self.mean:
                self.mean[key] = {}
                self.var[key] = {}
            if 'Latency' in self.clockDict[key] and len(self.clockDict[key]['Latency']) != 0:
                clock = numpy.array(self.clockDict[key]['Latency'])
                instructs = numpy.array(self.instructsDict[key]['Latency'])
                self.mean[key]['Latency'] = 1.0 * clock.sum() / instructs.sum()
                self.var[key]['Latency'] = (1.0 * clock / instructs).var()
            if 'Throughput' in self.clockDict[key] and len(self.clockDict[key]['Throughput']) != 0:
                clock = numpy.array(self.clockDict[key]['Throughput'])
                instructs = numpy.array(self.instructsDict[key]['Throughput'])
                self.mean[key]['Throughput'] = 1.0 * clock.sum() / instructs.sum()
                self.var[key]['Throughput'] = (1.0 * clock / instructs).var()

    def write(self, fileSrc):
        outFile = open(fileSrc, 'w')
        # outFile.write('Instruct name\tTest Type\tMean Latency(Clock Cycle)\tVar\n')
        for key in self.instructSet:
            try:
                throughput = str(round(self.mean[key]['Throughput'], 2))
            except:
                throughput = 'miss'
            try:
                latency = str(round(self.mean[key]['Latency'], 2))
            except:
                latency = 'miss'
            outFile.write(
                    key + '\t' + latency + '\t' + throughput + '\n')

    def debug(self):
        for key in self.instructSet:
            print key
            print self.clockDict.get(key)
            print self.instructsDict.get(key)
            print self.mean.get(key)
            print self.var.get(key)


class Driver:
    def __init__(self):
        self.listFiles('../../../result20160831', '../../../out20160831')
        #self.listFiles('../../../result20160817', '../../../out20160817')
        #self.mergeFiles('../../../out20160817', '../../../output/result.xls')

    def listFiles(self, inputSrc, outputSrc):
        list = os.listdir(inputSrc)
        for file in list:
            input = inputSrc + '/' + file
            output = outputSrc + '/' + file
            print input
            print output
            CommonFilter(input=input, output=output)

    def mergeFiles(self, inputSrc, outputFile):
        outputWriter = open(outputFile, 'w')
        list = os.listdir(inputSrc)
        for file in list:
            input = inputSrc + '/' + file
            inputReader = open(input, 'r')
            outputWriter.write(inputReader.read())


if __name__ == '__main__':
    # commonFilter = CommonFilter(input = '../../../data/fvec.txt', output = '../../../output/fvec.txt')
    driver = Driver()
