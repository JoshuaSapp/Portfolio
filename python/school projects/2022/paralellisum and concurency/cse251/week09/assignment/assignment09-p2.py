"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p2.py 
Author: Joshua Sapp

Purpose: Part 2 of assignment 09, finding the end position in the maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included
- Each thread requires a different color by calling get_color()


This code is not interested in finding a path to the end position,
However, once you have completed this program, describe how you could 
change the program to display the found path to the exit position.

What would be your strategy?  

<Answer here>


Why would it work?

<Answer here>

"""
import sys
import math
import threading 
from screen import Screen
from maze import Maze

import cv2

# Include cse 251 common Python files - Dont change
from cse251 import *
set_working_directory(__file__)

SCREEN_SIZE = 800
COLOR = (0, 0, 255)
COLORS = (
    (0,0,255),
    (0,255,0),
    (255,0,0),
    (255,255,0),
    (0,255,255),
    (255,0,255),
    (128,0,0),
    (128,128,0),
    (0,128,0),
    (128,0,128),
    (0,128,128),
    (0,0,128),
    (72,61,139),
    (143,143,188),
    (226,138,43),
    (128,114,250)
)

# Globals
current_color_index = 0
thread_count = 0
stop = False
threads = []
done = False

def get_color():
    """ Returns a different color when called """
    global current_color_index
    if current_color_index >= len(COLORS):
        current_color_index = 0
    color = COLORS[current_color_index]
    current_color_index += 1
    return color

def runner(maze,color,coordinates = (0,1)):
    #single thread that will continue until it hits an intersecion, then split
    global done
    global thread_count

    maze.move(coordinates[0],coordinates[1],color)

    if maze.at_end(coordinates[0],coordinates[1]):
        #if at the end of the maze, kill all threads
        print("done")
        done = True
        return

    moves = maze.get_possible_moves(coordinates[0],coordinates[1])

    if len(moves) == 0:
        #if out of moves, end of path has been found
        return

    if len(moves) == 1:
        #if only one move exists, continue down that path
        move = moves[0]
        runner(maze,color,move)

    if len(moves) > 1:
        #send a runner down all but one path, then continue down remaining path
        options = len(moves)
        if done != True:
            while options > 1:
                move = moves[options-1]
                if maze.can_move_here(move[0],move[1]):
                    threads.append(threading.Thread(target=runner,args=(maze,get_color(),move)))
                    options -= 1
                    thread_count += 1
                    threads[-1].start()
            move = moves[0]
            runner(maze,color,move)
        else: 
            return


def solve_find_end(maze):
    """ finds the end position using threads.  Nothing is returned """
    # When one of the threads finds the end position, stop all of them
    threads = []
    global done
    global thread_count
    done = False
    threads.append(threading.Thread(target=runner,args=(maze,get_color())))
    for thread in threads:
        thread.start()
    thread_count += 1
    for thread in threads:
        thread.join()
    

def find_end(log, filename, delay):
    """ Do not change this function """

    global thread_count

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename, delay=delay)

    solve_find_end(maze)

    log.write(f'Number of drawing commands = {screen.get_command_count()}')
    log.write(f'Number of threads created  = {thread_count}')

    done = False
    speed = 1
    while not done:
        if screen.play_commands(speed): 
            key = cv2.waitKey(0)
            if key == ord('+'):
                speed = max(0, speed - 1)
            elif key == ord('-'):
                speed += 1
            elif key != ord('p'):
                done = True
        else:
            done = True



def find_ends(log):
    """ Do not change this function """

    files = (
        ('verysmall.bmp', True),
        ('verysmall-loops.bmp', True),
        ('small.bmp', True),
        ('small-loops.bmp', True),
        ('small-odd.bmp', True),
        ('small-open.bmp', False),
        ('large.bmp', False),
        ('large-loops.bmp', False)
    )

    log.write('*' * 40)
    log.write('Part 2')
    for filename, delay in files:
        log.write()
        log.write(f'File: {filename}')
        find_end(log, filename, delay)
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_ends(log)



if __name__ == "__main__":
    main()