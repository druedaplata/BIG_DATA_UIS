from mrjob.job import MRJob
import os

class Compras(MRJob):

    def mapper(self, _, line):
        tokens = line.split()
        yield tokens[2], float(tokens[4])

    def reducer(self, key, values):
        yield key, sum(values)
        
if __name__ == '__main__':
    c = Compras()
    c.run()