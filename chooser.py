import os
import random

path ='/home/pi/Music'
files = os.listdir(path)
index = random.randrange(0, len(files))
selection = files[index]
print('here comes the choice!')
print(selection)
