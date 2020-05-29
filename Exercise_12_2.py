import numpy as np
from PIL import Image
import os
# Similar to Rule 110 we are going to use np.roll and a rule given in the nonalsystem: first digit gives
# number of alive cells in nbhd, second digit is either 1 or 0 and determines if the cell itself is alive.
conway = np.array(np.zeros(shape=18, dtype=bool))
# if cell is dead (0*9^1) then precisely 3 cells have to be alive (3*9^0) for the cell to be alive after this step
# if cell is alive (1*9^1) then 2 or 3 cells have to be alive (2*9^0 or 3*9^0) for the cell to be alive after this step
# so only "alive" cases are
#  - 0*9^1 + 3*9^0 = 3
#  - 1*9^1 + 2*9^0 = 11
#  - 1*9^1 + 3*9^0 = 12
for i in [3, 11, 12]:
    conway[i] = True
evolution_steps = 150
size = (300, 300)
state = np.random.choice([True, False], size=size)
# We are going to save all states as pictures in a list to create a GIF afterwards
imgs = []
for i in range(evolution_steps):
    imgs.append(Image.fromarray(state).convert(mode='RGB'))
    state_nbhd = sum(sum(np.roll(np.roll(state, y, axis=1), x, axis =0) for y in [-1, 0, 1])for x in [-1, 0, 1]) - state
    state = conway[state_nbhd + 9 * state]
imgs.append(Image.fromarray(state).convert(mode='RGB'))
# The GIF is going to be saved in a folder "pictures"
if not os.path.isdir("pictures"):
    os.mkdir("pictures")
imgs[0].save('pictures/conway.gif', save_all=True, append_images=imgs[1:], optimize=False, duration=40, loop=0)