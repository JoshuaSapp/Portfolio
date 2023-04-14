from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

# Const Values
TOP_API_URL = 'https://swapi.dev/api'

# Global Variables
call_count = 0

# -------------------------------------------------------------------------------
class Request_thread(threading.Thread):

    def __init__(self, url, data):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.data = data

    def run(self):
        global call_count
        response = requests.get(self.url)
        call_count += 1
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.data.append(response.json())


def get_all_data_threads(urls):
    results = []
    threads = []

    for url in urls:
        t = Request_thread(url, results)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return results


def print_film_details(log, film, chars, planets, starships, vehicles, species):

    def display_names(title, name_list):
        log.write('')
        log.write(f'{title}: {len(name_list)}')
        names = sorted([item["name"] for item in name_list])
        log.write(str(names)[1:-1].replace("'", ""))


    log.write('-' * 40)
    log.write(f'Title   : {film["title"]}')
    log.write(f'Director: {film["director"]}')
    log.write(f'Producer: {film["producer"]}')
    log.write(f'Released: {film["release_date"]}')

    display_names('Characters', chars)
    display_names('Planets', planets)
    display_names('Starships', starships)
    display_names('Vehicles', vehicles)
    display_names('Species', species)


def main():
    log = Log(show_terminal=True)

    log.start_timer('Starting to retrieve data from swapi.dev')

    # Retrieve Top API urls
    urls = []
    t = Request_thread(TOP_API_URL, urls)
    t.start()
    t.join()
    # log.write(urls)

    # Retrieve film 6 details   
    top_urls = urls[0]
    film_url = top_urls['films']

    film6 = []
    t = Request_thread(f'{film_url}6', film6)
    t.start()
    t.join()
    # log.write(film6)
    film_data = film6[0]

    # Retrieve details about the film
    char_data = get_all_data_threads(film_data['characters'])
    planet_data = get_all_data_threads(film_data['planets'])
    starship_data = get_all_data_threads(film_data['starships'])
    vehicles_data = get_all_data_threads(film_data['vehicles'])
    species_data = get_all_data_threads(film_data['species'])

    # Display results
    print_film_details(log, film_data, char_data, planet_data, starship_data, vehicles_data, species_data)

    log.write('')
    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to swapi server')


if __name__ == "__main__":
    main()