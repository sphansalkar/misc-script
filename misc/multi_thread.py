import threading
import time
from conf import condition

def main_thread(cv):
    print("In main_thread ...")

    with cv:
        print("Waiting in main thread ...")
        cv.wait()
        print("After waiting in main_thread ...")


if __name__ == "__main__":

    cs1 = threading.Thread(name='main_thread', target=main_thread, args=(condition,))
    cs1.start()


