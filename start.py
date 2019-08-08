import os
from os import listdir
from os.path import isfile, join, realpath
from random import shuffle
import time

print('ASCIIArtsy')
print('Created by Max Bridgland')
print('Art from http://artscene.textfiles.com/vt100/')
print('Press Ctrl+C to skip animation')
print('Press Ctrl+Z to quit')
print('Animations will begin in 3 seconds...')
time.sleep(3)
if not os.environ.get('AA_SPEED'):
    speed = '1500'
else:
    speed = os.environ.get('AA_SPEED')
all_files = [f for f in listdir('vt_files') if isfile(join('vt_files', f))]
shuffle(all_files)
for file in all_files:
    os.system('cat %s | pv -q -L %s' % (join('vt_files', file), speed))

