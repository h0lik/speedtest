#!/usr/bin/env python3 

import csv
from matplotlib import pyplot as plt
output = '/home/floki/tests/speedtest/output-sp.csv'
highs = []
with open(output) as files:
    reader = csv.reader(files)
    for row in reader:
        if row[3]=='':
            continue
        var1 = float(row[3])
        ping = int(var1)
        highs.append(ping)
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(highs, c = 'red')
    plt.title("Ping", fontsize = 20)
    plt.xlabel('Number of measurements per day',fontsize = 16)
    plt.ylabel("Ping", fontsize = 14)
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 14)
    plt.legend(['Ping'])    
    plt.savefig('/home/floki/tests/speedtest/report/img/ping.jpg')
    plt.show()