"""
Course: CSE 251
Lesson Week: 07
File: assingnment.py
Author: <Your name here>
Purpose: Process Task Files

Instructions:  See I-Learn

TODO

Add you comments here on the pool sizes that you used for your assignment and
why they were the best choices.


"""

from datetime import datetime, timedelta
import requests
import multiprocessing as mp
from matplotlib.pylab import plt
import numpy as np
import glob
import math 

# Include cse 251 common Python files - Dont change
from cse251 import *
set_working_directory(__file__)

TYPE_PRIME  = 'prime'
TYPE_WORD   = 'word'
TYPE_UPPER  = 'upper'
TYPE_SUM    = 'sum'
TYPE_NAME   = 'name'

# Global lists to collect the task results
result_primes = []
result_words = []
result_upper = []
result_sums = []
result_names = []

def is_prime(n: int):
    """Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
 
def task_prime(value):
    """
    Use the is_prime() above
    Add the following to the global list:
        {value} is prime
            - or -
        {value} is not prime
    """
    if is_prime(value):
        return(f"{value} is prime")
    else:
        return(f"{value} is not prime")

def log_prime(value):
    #records the output of task_prime
    result_primes.append(value)

def task_word(word):
    """
    search in file 'words.txt'
    Add the following to the global list:
        {word} Found
            - or -
        {word} not found *****
    """
    with open('words.txt') as word_file:
        contents = word_file.read()
        if word in contents:
            return(f"{word} Found")
        else:
            return(f"{word} not found")

def log_word(value):
    result_words.append(value)

def task_upper(text):
    """
    Add the following to the global list:
        {text} ==>  uppercase version of {text}
    """
    return(f"{text} ==>  uppercase version of {text.upper()}")

def log_upper(value):
    result_upper.append(value)

def task_sum(values):
    """
    Add the following to the global list:
        sum of {start_value:,} to {end_value:,} = {total:,}
    """
    start_value = values[0]
    end_value = values[1]
    total = sum(range(start_value,end_value))
    return(f"sum of {start_value} to {end_value} = {total}")

def log_sum(value):
    result_sums.append(value)

def task_name(url):
    """
    use requests module
    Add the following to the global list:
        {url} has name <name>
            - or -
        {url} had an error receiving the information
    """
    responce = requests.get(url)

    if responce.status_code  == 200:
        data = responce.json()
        return(f"{url} has name {data['name']}")
    else:
        return(f"{url} had an error receiving the information")

def log_name(value):
    result_names.append(value)

def main():
    log = Log(show_terminal=True)
    log.start_timer()

    # These are the lists of toDo for each pool to complete
    toDo_prime = []
    toDo_word = []
    toDo_upper = []
    toDo_sum = []
    toDo_name = []

    # These are the pools 
    pool_prime = mp.Pool(10)
    pool_word = mp.Pool(10)
    pool_upper = mp.Pool(10)
    pool_sum = mp.Pool(10)
    pool_name = mp.Pool(10)

    # This sorts the tasks into the proper "to do" lists
    count = 0
    task_files = glob.glob("*.task")
    for filename in task_files:
        # print()
        # print(filename)
        task = load_json_file(filename)
        #print(task)
        count += 1
        task_type = task['task']
        if task_type == TYPE_PRIME:
            toDo_prime.append(task['value'])
        elif task_type == TYPE_WORD:
            toDo_word.append(task['word'])

        elif task_type == TYPE_UPPER:
            toDo_upper.append(task['text'])

        elif task_type == TYPE_SUM:
            toDo_sum.append([task['start'], task['end']])

        elif task_type == TYPE_NAME:
            toDo_name.append(task['url'])

        else:
            log.write(f'Error: unknown task type {task_type}')



    # feeds each pool its list of "to dos" and assigns the outputs to the results variables.
    [pool_prime.apply_async(task_prime,args=(x,),callback=log_prime) for x in toDo_prime]
    [pool_word.apply_async(task_word,args=(x,),callback=log_word) for x in toDo_word]
    [pool_upper.apply_async(task_upper,args=(x,),callback=log_upper) for x in toDo_upper]
    [pool_sum.apply_async(task_sum,args=(x,),callback=log_sum) for x in toDo_sum]
    [pool_name.apply_async(task_name,args=(x,),callback=log_name) for x in toDo_name]

    # Close the pools when complete
    pool_prime.close()
    pool_word.close()
    pool_upper.close()
    pool_sum.close()
    pool_name.close()

    pool_prime.join()
    pool_word.join()
    pool_upper.join()
    pool_sum.join()
    pool_name.join()


    # Do not change the following code (to the end of the main function)
    def log_list(lst, log):
        for item in lst:
            log.write(item)
        log.write(' ')
    
    log.write('-' * 80)
    log.write(f'Primes: {len(result_primes)}')
    log_list(result_primes, log)

    log.write('-' * 80)
    log.write(f'Words: {len(result_words)}')
    log_list(result_words, log)

    log.write('-' * 80)
    log.write(f'Uppercase: {len(result_upper)}')
    log_list(result_upper, log)

    log.write('-' * 80)
    log.write(f'Sums: {len(result_sums)}')
    log_list(result_sums, log)

    log.write('-' * 80)
    log.write(f'Names: {len(result_names)}')
    log_list(result_names, log)

    log.write(f'Primes: {len(result_primes)}')
    log.write(f'Words: {len(result_words)}')
    log.write(f'Uppercase: {len(result_upper)}')
    log.write(f'Sums: {len(result_sums)}')
    log.write(f'Names: {len(result_names)}')
    log.stop_timer(f'Finished processes {count} toDo')

if __name__ == '__main__':
    main()
