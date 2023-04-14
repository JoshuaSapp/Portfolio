"""
Course: CSE 251
Lesson Week: 06
File: team.py
Author: Brother Comeau

Purpose: Team Activity

Instructions:

- Implement the process functions to copy a text file exactly using a pipe

After you can copy a text file word by word exactly
- Change the program to be faster (Still using the processes)

"""

import multiprocessing as mp
from multiprocessing import Value, Process
import filecmp 

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

def sender(con,filename):
    """ function to send messages to other end of pipe """
    '''
    open the file
    send all contents of the file over a pipe to the other process
    Note: you must break each line in the file into words and
          send those words through the pipe
    '''
    readList = []
    with open(filename,"r") as rDocument:
        for line in rDocument:
            for word in line.split(" "):
                readList.append(word)
    readList.append("you are done")
    for item in readList:
        con.send(item)

    con.close()


def receiver(con,tracker,filename):
    """ function to print the messages received from other end of pipe """
    ''' 
    open the file for writing
    receive all content through the shared pipe and write to the file
    Keep track of the number of items sent over the pipe
    '''

    with open(filename,"w") as wDocument:
        data = "start"
        while data == str():
            data = con.recv()
            wDocument.write(con.recv())
            tracker += 1
            print(tracker)




def are_files_same(filename1, filename2):
    """ Return True if two files are the same """
    return filecmp.cmp(filename1, filename2, shallow = False) 


def copy_file(log, filename1, filename2):
    # TODO create a pipe 
    parent_conn, child_conn = mp.Pipe()
    
    # TODO create variable to count items sent over the pipe
    message_count = 0

    # TODO create processes 
    p1 = mp.Process(target=sender, args=(parent_conn,filename1)) 
    p2 = mp.Process(target=receiver, args=(child_conn,message_count,filename2)) 

    log.start_timer()
    start_time = log.get_time()

    # TODO start processes 
    
    p1.start()
    p2.start()

    # TODO wait for processes to finish

    p1.join()
    p2.join()

    stop_time = log.get_time()

    log.stop_timer(f'Total time to transfer content = {message_count}: ')
    log.write(f'items / second = {message_count / (stop_time - start_time)}')

    if are_files_same(filename1, filename2):
        log.write(f'{filename1} - Files are the same')
    else:
        log.write(f'{filename1} - Files are different')


if __name__ == "__main__": 

    log = Log(show_terminal=True)

    copy_file(log, 'gettysburg.txt', 'gettysburg-copy.txt')
    
    # After you get the gettysburg.txt file working, uncomment this statement
    # copy_file(log, 'bom.txt', 'bom-copy.txt')

