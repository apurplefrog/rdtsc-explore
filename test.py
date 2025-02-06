import subprocess
import numpy
import matplotlib.pyplot as plt

def main():
    numbers = numpy.array(range(0,256))
    counters = numpy.zeros(256)
    for _ in range(0,10000):
        result = subprocess.run(["./test"]);
        counters[result.returncode] += 1
    plt.plot(numbers,counters) 
    plt.show()

if __name__ == "__main__":
    main()
