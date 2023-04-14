"""
Course: CSE 251
Lesson Week: 02 - Team Activity
File: team.py
Author: Brother Comeau

Purpose: Playing Card API calls

Instructions:

- Review instructions in I-Learn.

"""

from datetime import datetime, timedelta
import threading
import requests
import json

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

# TODO Create a class based on (threading.Thread) that will
# make the API call to request data from the website

class Request_thread(threading.Thread):
    # TODO - Add code to make an API call and return the results
    # https://realpython.com/python-requests/

    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.response = response.json()
            print(self.response)
        else:
            print('RESPONSE = ', response.status_code)

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()
        self.remaining = 52

    def reshuffle(self):
        # TODO - add call to reshuffle
        request = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/shuffle/')
        request.start()
        request.join()

    def draw_card(self):
        # TODO add call to get a card
        request = Request_thread(rf'https://deckofcardsapi.com/api/deck/{self.id}/draw/')
        request.start()
        request.join()
        if request.response != {}:
            self.remaining = request.response['remaining']
            return request.response['cards'][0]['code']
        else:
            return ''

    def cards_remaining(self):
        return self.remaining

    def draw_endless(self):
        if self.remaining <= 0:
            self.reshuffle()
        return self.draw_card()


if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here.  You only need to run the 
    #        team_get_deck_id.py program once. You can have
    #        multiple decks if you need them

    deck_id = '9kypbjx12x5g'

    # Testing Code >>>>>
    deck = Deck(deck_id)
    for i in range(55):
        card = deck.draw_endless()
        print(i, card, flush=True)
    print()
    # <<<<<<<<<<<<<<<<<<

