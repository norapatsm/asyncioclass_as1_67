# Starting a Thread
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread  %s: starting", name)
    time.sleep(2)
    loggin.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main   : before createing thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main   : before running thread")
    x.start()
    logging.info("main   :wait for the thread to finish")
    #  x.join()
    logging.info("main   ;all done")