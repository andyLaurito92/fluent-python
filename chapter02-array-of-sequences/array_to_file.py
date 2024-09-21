from array import array
from random import random
import time

print("=============== ARRAY ===================")
## Generate array of 10^7 random numbers

start = time.time()
floats = array('d', (random() for i in range(10**7)))
end = time.time()

print(f"Time for generation was: {end - start} seconds. Last value: {floats[-1]} \n")

## Write them to a binary file
start = time.time()
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
end = time.time()
print(f"Time taken to store 10^7 float array to file {end - start} seconds \n")

## Read the file & store again in new array
start = time.time()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
end = time.time()

print(f"Time for reading file was: {end - start} seconds. Last value: {floats[-1]} \n")

print("=============== LIST ===================")

### Doing the same than above but w/lists
start = time.time()
floats_list = [random() for i in range(10**7)]
end = time.time()

print(f"Time for generation was: {end - start} seconds. Last value: {floats_list[-1]} \n")

## Write them to a binary file
start = time.time()
with open('common_list_text.txt', 'w') as myfile:
    for randomfloat in floats_list:
        myfile.write(f"{randomfloat} ")
end = time.time()
print(f"Time taken to store 10^7 float list to file {end - start} seconds \n")

## Read the file & store again in new array
start = time.time()
list_read = []
with open('common_list_text.txt', 'r') as myfile:
    list_read = myfile.read().split(' ')
end = time.time()

print(f"Time for reading file was: {end - start} seconds. Last value: {list_read[-2]} \n")

print("=============== LIST TO BINARY ===================")

## Using pickle instead

### Doing the same than above but w/lists
start = time.time()
floats_list = [random() for i in range(10**7)]
end = time.time()

print(f"Time for generation was: {end - start} seconds. Last value: {floats_list[-1]} \n")

import pickle

## Write them to a binary file
start = time.time()
another_file = open('binary_list.bin', 'wb')
pickle.dump(floats_list, another_file)
end = time.time()
print(f"Time taken to store 10^7 binary float list to file {end - start} seconds \n")

## Read the file & store again in new array
start = time.time()
list_read = []
another_file = open('binary_list.bin', 'rb')
list_read = pickle.load(another_file)
end = time.time()

print(f"Time for reading file was: {end - start} seconds. Last value: {list_read[-1]} \n")
