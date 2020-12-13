import time
import sys

def lbl(string, timer = .25):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(timer)

