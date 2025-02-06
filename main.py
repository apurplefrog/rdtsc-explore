import subprocess
import numpy
import matplotlib.pyplot as plt

def main():
    numbers = numpy.array(range(0,10))
    counters = numpy.zeros(10)
    for _ in range(0,10000):
        result = subprocess.run(["./main"]);
        counters[result.returncode] += 1
    plt.plot(numbers,counters) 
    plt.show()

if __name__ == "__main__":
    main()
