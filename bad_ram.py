#   bad_ram.py
#   python 2.7

#   Uses all your memory

#   Chris Bugg
#   3/8/16

import thread
import time


def do_bad():

    n = []

    for q in range(0, 10000000):

        z = []

        for y in range(0, 10000000):

            z.append(y)

        n.append(z)

while 1:

    thread.start_new_thread(do_bad, ())
    time.sleep(.5)

while 1:

    pass