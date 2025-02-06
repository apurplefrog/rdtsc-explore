Running main.py on i5-5200U processor:

![Graph of results on the i5-5200U showing the disparity between even and odd results](./figures/i5-5200U.png)

Running main.py on Ryzen 5 7500F:

![Graph of results on the Ryzen 5 7500F showing proper pseudo-random number generation](./figures/Ryzen7500F.png)

For whatever reason, on the Intel chip, the RDTSC operation returns even results the vast majority of the time, whereas the AMD chip returns proper pseudo-random number generation as expected. Can anyone explain the disparity between the results on the two chips?
