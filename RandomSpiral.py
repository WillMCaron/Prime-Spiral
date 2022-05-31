# sys for sys.exit(), better for comprehension
import pygame,sys
# contains many constant variables that will be used (QUIT)
# also shorter calls in program
from pygame.locals import *
from time import sleep
from random import random

# random selection
def prime(num):
  if random() > .89:
    return True
  return False

# initializes pygame so its ready for use
pygame.init()
pygame.font.init()
# size of steps
STEPS = 4
WIDTH = 0
#time delay
DELAY = 0
#500,400
SCR_WIDTH = 400
SCR_LENGTH = 400
# set up the window
windowSurface = pygame.display.set_mode((SCR_WIDTH,SCR_LENGTH), 0, 32)
pygame.display.set_caption('RANDOM SPIRAL')

# text
font = pygame.font.SysFont("Comic Sans MS", 16)

# set up the colors
#        r,g,b
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# draw the black background onto the surface
windowSurface.fill(BLACK)

# draw the window onto the screen
pygame.display.update()

# middle of screen
x = SCR_WIDTH/2
y = SCR_LENGTH/2
# number for each point
count = 1

numDisplay = font.render(str(count),1,GREEN)

# last position of line
last_pos = (x,y)

#              code to create spiral
# number of steps
numSteps = 1
# direction keeper
dir = 0
# keeps track of whether to increase numsteps
change = 0

for i in range(numSteps):
  #windowSurface.blit(numDisplay, (x-STEPS/4,y-STEPS/4))
  if dir == 0:
    # right
    x += STEPS
  elif dir == 1:
    # up
    y -= STEPS
  elif dir == 2:
    # left
    x -= STEPS
  elif dir == 3:
    # down
    y += STEPS
  # draw line
  pygame.draw.line(windowSurface, WHITE, last_pos,(x,y),WIDTH)
  # increment number count
  count+=1
  if prime(count):
    print(count, "SELECTED")
    # draw square
    #x,y,width,height
    pygame.draw.rect(windowSurface,RED, pygame.Rect(x-STEPS/4,y-STEPS/4,STEPS*(2/3),STEPS*(2/3)))  
  # delay
  pygame.display.update()
  numDisplay = font.render(str(count),1,GREEN)
  sleep(DELAY)
# increases side number
change +=1 
# updatre the step length
if change%2 == 0:
  numSteps +=1
# change direction and loop it
dir += 1
if dir > 3:
  dir = 0
  

#pygame.draw.line(windowSurface, WHITE, last_pos,(x,y),4)
    

# game loop
while True:
  # check for quit event
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # rest of program
  last_pos = (x,y)
  for i in range(numSteps):
    #windowSurface.blit(numDisplay, (x-STEPS/4,y-STEPS/4))
    if dir == 0:
      # right
      x += STEPS
    elif dir == 1:
      # up
      y -= STEPS
    elif dir == 2:
      # left
      x -= STEPS
    elif dir == 3:
      # down
      y += STEPS
    # draw line
    pygame.draw.line(windowSurface, WHITE, last_pos,(x,y),WIDTH)
      # increment number count
    count+=1
    if prime(count):
      print(count, "SELECTED")
      # draw square
      #x,y,width,height
      pygame.draw.rect(windowSurface,RED, pygame.Rect(x-STEPS/4,y-STEPS/4,STEPS*(2/3),STEPS*(2/3)))  
    # delay
    pygame.display.update()
    #a = input()

    # check if it is completely off screen
    if x > SCR_WIDTH:
      #pygame.quit()
      #sys.exit()
      a = input()
      pygame.quit()
      sys.exit()
    numDisplay = font.render(str(count),1,GREEN)
    sleep(DELAY)
  # increases side number
  change +=1 
  # updatre the step length
  if change%2 == 0:
    numSteps +=1
  # change direction and loop it
  dir += 1
  if dir > 3:
    dir = 0
  






