import threading
import time
from conf import condition

def thread1(cv):
    print("Sleeping for 5 secs ...")
    time.sleep(5)
    print("After sleeping ...")

    with cv:
        cv.notifyAll()


if __name__ == "__main__":

    cs2 = threading.Thread(name='thread1', target=thread1, args=(condition,))
    cs2.start()

