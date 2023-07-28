import sys

import PyPluMA

class CSVSmoothPlugin:
    def input(self, inputfile):
        filelist = open(inputfile, 'r')
        
        self.infile = open(PyPluMA.prefix()+"/"+filelist.readline().strip(), 'r')
        self.infile2 = open(PyPluMA.prefix()+"/"+filelist.readline().strip(), 'r')
        self.infile3 = open(PyPluMA.prefix()+"/"+filelist.readline().strip(), 'r')

    def run(self):
        firstline = self.infile.readline().strip()
        self.measurables = firstline.split(',')

        measurables2 = self.infile2.readline().strip().split(',')
        measurables3 = self.infile3.readline().strip().split(',')

        self.idx = [0]
        for i in range(1, len(self.measurables)):
           if (self.measurables[i] in measurables2 or self.measurables[i] in measurables3):
               self.idx.append(i)

    def output(self, outputfile):
      outfile = open(outputfile, 'w')
      for j in range(len(self.idx)):
        outfile.write(self.measurables[self.idx[j]])
        if (j != len(self.idx)-1):
            outfile.write(',')
        else:
            outfile.write('\n')

      for line in self.infile:
          line = line.strip()
          contents = line.split(',')
          for j in range(len(self.idx)):
              outfile.write(contents[self.idx[j]])
              if (j != len(self.idx)-1):
                  outfile.write(',')
              else:
                  outfile.write('\n')

