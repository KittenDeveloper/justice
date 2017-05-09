#!/usr/bin/python2

import multiprocessing
import subprocess
import os
from socket import *
from time import sleep

s = socket(AF_INET, SOCK_STREAM)

def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

if __name__ == '__main__':
    pool_size = 255

    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
             for i in range(pool_size) ]

    for p in pool:
        p.start()

    for i in range(1,255):
        jobs.put('192.168.200.{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    while not results.empty():
        
        ip = results.get()
        portresult = s.connect_ex((str(ip), 8060))
        sleep(.5)
        #portresult = s.connect_ex((str(ip), 8060))
        print(ip + ':  '+ str(portresult))