from datetime import datetime, timedelta
import requests
import json
import threading
import multiprocessing as mp

from cse251 import *
set_working_directory(__file__)

TOP_API_URL = 'https://swapi.dev/api'

urls = []

def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return(response.json())

def save_urls(urls):
    urls.append(urls)
    print(urls)

def main():
    log = Log(show_terminal=True)

    log.start_timer('Starting to retrieve data from swapi.dev')

    pool = mp.Pool(1)

    urls = pool.apply_async(save_urls,args=(TOP_API_URL,),callback=save_urls)

    pool.close()
    pool.join()
    

main()