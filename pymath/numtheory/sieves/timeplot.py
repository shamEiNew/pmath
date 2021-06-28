import sieve_of_eratosthenes as esieve
import matplotlib.pyplot as plt
import numpy as np

y_sizedata = []
x_timedata = []
for size in range(100, 10000, 100):
    x_timedata.append(esieve.eratosthenes_sieve(size))
    y_sizedata.append(size)

#print(x_timedata)
x_timedata = np.array(x_timedata)
x_timedata = x_timedata*100000
#print(x_timedata)
y_sizedata = np.array(y_sizedata)
fig = plt.figure()
plt.xlim(0, max(y_sizedata))
plt.xticks(np.arange(0, max(y_sizedata), step = 500))
plt.ylim()
plt.yticks(np.arange(0, max(x_timedata), step = 100))
plt.scatter(y_sizedata, x_timedata, c='red', marker = 'x')
#plt.show()
plt.savefig('time.png')