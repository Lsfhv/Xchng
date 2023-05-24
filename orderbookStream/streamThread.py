from wssorderbookbinance import wssRun
from threading import Thread



def threadMain():

    threads = []

    thread1 = Thread(target=wssRun)
    thread1.start()
    threads.append(thread1)

    
    for thread in threads:
        thread.join()

threadMain()