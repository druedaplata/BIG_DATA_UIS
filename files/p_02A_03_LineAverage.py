from mrjob.job import MRJob
import numpy as np

class LineAverage(MRJob):

    def mapper(self, _, line):
        yield "line", len(line.split())
        
    def reducer(self, key, values):
        yield "avg", np.mean([i for i in values])
        
if __name__ == '__main__':
    LineAverage.run()