"""
Course: CSE 251
Lesson Week: 04
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- See in I-Learn

"""

from multiprocessing import Semaphore
import threading
import queue
from urllib import response
import requests
import json

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

RETRIEVE_THREADS = 4        # Number of retrieve_threads
NO_MORE_VALUES = 'No more'  # Special value to indicate no more items in the queue

def retrieve_thread(log,data_queue,semaphore):  # TODO add arguments
    """ Process values from the data_queue """
    while True:
        semaphore.acquire()
        # TODO check to see if anything is in the queue
        if len(data_queue) > 0:
            value = data_queue.pop(0)
            if value == NO_MORE_VALUES:
                data_queue.append(value)
                return
        # TODO process the value retrieved from the queue
            answer = requests.get(url=value)
        # TODO make Internet call to get characters name and log it
            log.write(answer.text)

        semaphore.release()

        
def file_reader(log,data_queue): # TODO add arguments
    """ This thread reading the data file and places the values in the data_queue """

    # TODO Open the data file "data.txt" and place items into a queue
    with open("data.txt",'r') as datafile:
        for line in datafile:
            line = line.strip()
            data_queue.append(line)

    log.write('finished reading file')

    # TODO signal the retrieve threads one more time that there are "no more values"
    data_queue.append(NO_MORE_VALUES)


def main():
    """ Main function """

    log = Log(show_terminal=True)

    # TODO create queue
    data_queue = []
    thread_list = []

    # TODO create semaphore (if needed)
    semaphore = threading.Semaphore(RETRIEVE_THREADS)

    # TODO create the threads. 1 filereader() and RETRIEVE_THREADS retrieve_thread()s
    # Pass any arguments to these thread need to do their job

    filereader = threading.Thread(target=file_reader,args=(log,data_queue))
    for i in range(RETRIEVE_THREADS):                                                                   #<---- Generates i namless threads and places them in the thread_queue
        thread_list.append(threading.Thread(target=retrieve_thread,args=(log,data_queue,semaphore)))

    thread_list.append(filereader)

    log.start_timer()

    # TODO Get them going - start the retrieve_threads first, then file_reader

    for item in thread_list:
        item.start()

    # TODO Wait for them to finish - The order doesn't matter
    for item in thread_list:
        item.join()


    log.stop_timer('Time to process all URLS')


if __name__ == '__main__':
    main()




