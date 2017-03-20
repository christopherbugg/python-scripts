#   bad_cpu.py
#   python 2.7 & 3

#   Uses all your cpus

#   Chris Bugg
#   3/8/16

from multiprocessing import Process, cpu_count


def do_bad():

    x = 2

    while 1:

        x *= x

    while 1:

        pass

if __name__ == '__main__':

    proc_list = []

    for k in range(0, cpu_count() * 4):

        proc_list.append(Process(target=do_bad, args=()))

    for p in proc_list:

        p.start()