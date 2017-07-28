#!/usr/bin/env python3
__author__ = 'Derek King'

# Timer functions that allow easy timing of code

import time
class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.total = 0.0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        end = time.time()
        secs = end - self.start
        self.total += secs
        # msecs = secs * 1000  # milliseconds
        if self.verbose:
            print("Elapsed time: " + secs + "s")

    def __str__(self):
        return "Total elapsed time: " + str(self.total) + "s"

def timed():
    with Timer(True):
        # Stuff to time
        x = 1
        x += 1

def timed2():
    timer = Timer(False)
    with timer:
        # Stuff to time
        x = 1
        x += 1

    x = 2

    with timer:
        # More stuff to time
        x = 3
        x += 1

    print(timer)


def timer2():
    import timeit
    start_time, time = timeit.default_timer(), 0
    print("Code to be timed goes here")
    time = timeit.default_timer() - start_time - time
    print("Time taken for part 1:", time)

    print("Or here")
    time = timeit.default_timer() - start_time - time
    print("Time taken for part 2:", time)


if __name__ == '__main__':
    timed()
    timed2()
    timer2()
