from mrjob.job import MRJob

class Compras(MRJob):

    def mapper(self, _, line):
        tokens = line.split()
        yield tokens[2], float(tokens[4])

    def reducer(self, key, values):
        yield key, sum(values)
        
if __name__ == '__main__':
    Compras.run()