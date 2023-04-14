"""
Course: CSE 251 
Lesson Week: 09
File: assignment09-p1.py 
Author: <Add name here>

Purpose: Part 1 of assignment 09, finding a path to the end position in a maze

Instructions:
- Do not create classes for this assignment, just functions
- Do not use any other Python modules other than the ones included

"""
import math
import sys

from cv2 import solve
from screen import Screen
from maze import Maze
import cv2

# Include cse 251 common Python files - Dont change
from cse251 import *
set_working_directory(__file__)

SCREEN_SIZE = 800
COLOR = (0, 0, 255)


def solve_path(maze,coordinates = (0,0),first = True,path = []):
    """ Solve the maze and return the path found between the start and end positions.  
        The path is a list of positions, (x, y) """

    if first == True:
        first = False
        coordinates = maze.get_start_pos()
        maze.move(coordinates[0],coordinates[1],COLOR)

    if maze.at_end(coordinates[0],coordinates[1]):
        path.append(coordinates)
        return(path)

    else:
        moves = maze.get_possible_moves(coordinates[0],coordinates[1])
        for move in moves:
            if maze.can_move_here(move[0],move[1]):
                path.append(coordinates)
                print(path)
                maze.move(move[0],move[1],COLOR)
                found = solve_path(maze,move,first,path)
                if found:
                    return(found)
                path.pop()
                maze.restore(move[0],move[1])


def get_path(log, filename):
    """ Do not change this function """

    # create a Screen Object that will contain all of the drawing commands
    screen = Screen(SCREEN_SIZE, SCREEN_SIZE)
    screen.background((255, 255, 0))

    maze = Maze(screen, SCREEN_SIZE, SCREEN_SIZE, filename)

    path = solve_path(maze)

    log.write(f'Number of drawing commands for = {screen.get_command_count()}')

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

    return path


def find_paths(log):
    """ Do not change this function """

    files = ('verysmall.bmp', 'verysmall-loops.bmp', 
            'small.bmp', 'small-loops.bmp', 
            'small-odd.bmp', 'small-open.bmp', 'large.bmp', 'large-loops.bmp')

    log.write('*' * 40)
    log.write('Part 1')
    for filename in files:
        log.write()
        log.write(f'File: {filename}')
        path = get_path(log, filename)
        log.write(f'Found path has length          = {len(path)}')
    log.write('*' * 40)


def main():
    """ Do not change this function """
    sys.setrecursionlimit(5000)
    log = Log(show_terminal=True)
    find_paths(log)


if __name__ == "__main__":
    main()