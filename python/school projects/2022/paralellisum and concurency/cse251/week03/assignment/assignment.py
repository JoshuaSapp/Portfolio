"""
------------------------------------------------------------------------------
Course: CSE 251
Lesson Week: 03
File: assignment.py
Author: <Your Name>

Purpose: Video Frame Processing

Instructions:

- Follow the instructions found in Canvas for this assignment
- No other packages or modules are allowed to be used in this assignment.
  Do not change any of the from and import statements.
- Only process the given MP4 files for this assignment

------------------------------------------------------------------------------
"""

from matplotlib.pylab import plt  # load plot library
from PIL import Image
import numpy as np
import timeit
import multiprocessing as mp
import math

# Include cse 251 common Python files
from cse251 import *
set_working_directory(__file__)

# 4 more than the number of cpu's on your computer
CPU_COUNT = mp.cpu_count() + 4  

# TODO Your final video need to have 300 processed frames.  However, while you are 
# testing your code, set this much lower
FRAME_COUNT = 160

RED   = 0
GREEN = 1
BLUE  = 2


def create_new_frame(image_file, green_file, process_file):
    """ Creates a new image file from image_file and green_file """

    # this print() statement is there to help see which frame is being processed
    print(f'{process_file[-7:-4]}', end=',', flush=True)

    image_img = Image.open(image_file)
    green_img = Image.open(green_file)

    # Make Numpy array
    np_img = np.array(green_img)

    # Mask pixels 
    mask = (np_img[:, :, BLUE] < 120) & (np_img[:, :, GREEN] > 120) & (np_img[:, :, RED] < 120)

    # Create mask image
    mask_img = Image.fromarray((mask*255).astype(np.uint8))

    image_new = Image.composite(image_img, green_img, mask_img)
    image_new.save(process_file)


# TODO add any functions to need here

def process_frame(image_number):
    image_file = rf'elephant/image{image_number:03d}.png'
    green_file = rf'green/image{image_number:03d}.png'
    process_file = rf'processed/image{image_number:03d}.png'

    start_time = timeit.default_timer()
    create_new_frame(image_file, green_file, process_file)
    print(f'\nTime To Process all images = {timeit.default_timer() - start_time}')  

def cpu_process(start,end):
  current = start
  while current <= end:
    process_frame(current)
    #print(f"processing frame {current}")
    current += 1

def run_test(cpu_count):
  print(f"testing {cpu_count} cpus")
  xaxis_cpus.append(cpu)
  count = 0
  start = 1
  end = FRAME_COUNT
  chunk = int(math.ceil(FRAME_COUNT/cpu_count))
  #print(chunk)
  segment = start + chunk
  cpu_list = []
  while count != cpu_count:
    if segment > end:
      segment = end
    p = mp.Process(target=cpu_process,args=(start,segment,))
    p.start()
    start += chunk
    segment += chunk
    cpu_list.append(p)
    count += 1

  test_start_time = timeit.default_timer()
  for item in cpu_list:
    item.join()
  test_end_time =  timeit.default_timer() - test_start_time 
  yaxis_times.append(test_end_time)



if __name__ == '__main__':
    # single_file_processing(300)
    # print('cpu_count() =', cpu_count())

    all_process_time = timeit.default_timer()
    log = Log(show_terminal=True)

    xaxis_cpus = []
    yaxis_times = []

    # TODO Process all frames trying 1 cpu, then 2, then 3, ... to CPU_COUNT
    #      add results to xaxis_cpus and yaxis_times

    cpu = 1
    while cpu <= CPU_COUNT:
      run_test(cpu)
      cpu += 1



    log.write(f'Total Time for ALL processing: {timeit.default_timer() - all_process_time}')

    # create plot of results and also save it to a PNG file
    plt.plot(xaxis_cpus, yaxis_times, label=f'{FRAME_COUNT}')
    
    plt.title('CPU Core yaxis_times VS CPUs')
    plt.xlabel('CPU Cores')
    plt.ylabel('Seconds')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.savefig(f'Plot for {FRAME_COUNT} frames.png')
    plt.show()
