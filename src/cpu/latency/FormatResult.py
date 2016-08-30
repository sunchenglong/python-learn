# coding=utf-8

import re
import os


class FormatResult:
    def __init__(self):
        # self.fileFormat('../../../output/result.xls', '../../../output/formatResult.xls')
        self.listFiles('../../../out20160817', '../../../out20160830')

    def listFiles(self, inputSrc, outputSrc):
        list = os.listdir(inputSrc)
        for file in list:
            input = inputSrc + '/' + file
            output = outputSrc + '/' + file + '.xls'
            print input
            print output
            self.fileFormat(inputSrc=input, outputSrc=output)

    def fileFormat(self, inputSrc, outputSrc):
        inputFile = open(inputSrc, 'r')
        outputFile = open(outputSrc, 'w')
        outputFile.write('Instruct \t Operators \t Latency \t Throughput \t RawCommand \n')
        for line in inputFile.readlines():
            if re.match('(Throughput)|(Latency)|(Instructions)', line):
                continue
            try:
                second = line.split('+')[1].strip()
                first = line.split('+')[0].strip()
                result = first.split(' ')[0].strip() + '+' + second.split(' ')[0].strip() \
                         + '\t' + '' \
                         + '\t' + line.split('\t')[1].strip() \
                         + '\t' + line.split('\t')[2].strip() \
                         + '\t' + line.split('\t')[0].strip()
            except:
                print line
                try:
                    result = line.split('\t')[0].split(' ')[0].strip() \
                             + '\t' + line.split('\t')[0].split(' ', 1)[1] \
                             + '\t' + line.split('\t')[1].strip() \
                             + '\t' + line.split('\t')[2].strip() \
                             + '\t' + line.split('\t')[0].strip()
                except:
                    result = line.split('\t')[0].split(' ')[0].strip() \
                             + '\t' + '' \
                             + '\t' + line.split('\t')[1].strip() \
                             + '\t' + line.split('\t')[2].strip() \
                             + '\t' + line.split('\t')[0].strip()
            outputFile.write(result + '\n')


if __name__ == '__main__':
    formatResult = FormatResult()
