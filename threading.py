import time
import threading

class TIMER(object):
    def __init__(self, number, seconds, incrementation):
        self.number = number
        self.seconds = seconds
        self.incrementation = incrementation
        self.tstart()

    def tstart(self):
        while True:
            self.number = self.number * self.incrementation
            time.sleep(self.seconds)
            print self.number

def main():
    t1 = threading.Thread(target = TIMER, args =  (1, 1, 1.2))
    t1.start()
    tt = threading.Thread(target = TIMER, args = (1, 2, 2))
    tt.start()

if __name__ == '__main__':
    main()
