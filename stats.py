
class Sample:
    def __init__(self, file):
        self.file = file
        self.sample = []

    def read(self):
        file = open(self.file, "r")
        file = file.read().replace('\n', ' ')
        str = file.split()
        #print(str)
        for i in str:
            self.sample.append(float(i))
        self.sample = sorted(self.sample)
        #print(self.sample)

class Basic_Stats:
    def __init__(self, elements):
        self.length = 0;
        self.mean = 0
        self.q1 = 0
        self.median = 0
        self.q3 = 0
        self.variance = 0
        self.std_dev = 0
        self.elements = elements

    def calc_mean(self):
        self.length = len(self.elements)
        sum = 0
        for elem in self.elements:
            sum = sum + elem
        self.mean = sum/len(self.elements)

    def calc_median(self):
        midpoint = int(self.length/2)
        #nextpoint = midpoint + 1
        #if odd
        if (self.length%2 != 0):
            self.median = self.elements[midpoint]
            qp = self.calc_q1(midpoint)
            self.calc_q3(midpoint, qp)
        #if even
        else:
            nextpoint = midpoint
            midpoint -= 1
            self.median = (self.elements[midpoint] + self.elements[nextpoint])/2
            qp = self.calc_q1(midpoint)
            self.calc_q3(midpoint, qp)

    def calc_q1(self, midpoint):
        #odd
        qp = int(midpoint/2)
        self.q1 = self.elements[qp]
        return qp

    def calc_q3(self, midpoint, qp):
        qp3 = midpoint + qp + 1
        self.q3 = self.elements[qp3]

    def calc_variance(self):
        sum = 0
        n = len(self.elements)
        for i in range(n):
            sum += (self.elements[i] - self.mean) ** 2
        n -= 1
        self.variance = sum/n

    def calc_stddev(self):
        self.std_dev = (self.variance) ** (1/2)

class Frequency:
    def __init__(self, elements):
        self.elements = elements
        self.length = len(elements)
        self.frequency = {}

    def grouping(self):
        count = 0
        for i in range(self.length):
            if (i == self.length-1):
                print(self.elements[i], end = ", ")
                count += 1
                print(str(count))
                count = 0
            elif (self.elements[i] == self.elements[i+1]):
                print(self.elements[i], end = " ")
                count += 1
            else:
                print(self.elements[i], end = ", ")
                count += 1
                print(str(count))
                count = 0
