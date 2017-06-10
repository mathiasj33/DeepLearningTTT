from os.path import expanduser, join
import os

FOLDER = join(expanduser('~'), '.tictactoe')
VAL_FOLDER = join(FOLDER, 'val')

for root, dirs, files in os.walk(VAL_FOLDER):
    for file in files:
        print(root + '/' + file)