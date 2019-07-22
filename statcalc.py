import stats

#sample = open('sample.txt','r').read()
data = stats.Sample('sample.txt')
data.read()
#print(data.sample)
basics = stats.Basic_Stats(data.sample)
frequency = stats.Frequency(data.sample)
#print(basics.elements)
basics.calc_mean()
basics.calc_median()
basics.calc_variance()
basics.calc_stddev()

#print(data.sample)
frequency.grouping()
print('\n')
print("Sample Size: " + str(basics.length))
print("Mean: " + str(basics.mean))
print("Quartile 1: " + str(basics.q1))
print("Median: " + str(basics.median))
print("Quartile 3: " + str(basics.q3))
print("Variance: " + str(basics.variance))
print("Std Dev: " + str(basics.std_dev))

#sample = [float(x) for x in sample]
#basic_stats = stats.Basic_Stats(sample)

#print(sample)

#basic_stats.mean = basic_stats.calc_mean(sample)

#print(mean)
