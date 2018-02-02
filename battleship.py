import time
import random
from pygame import mixer
mixer.init()
mixer.music.load('back.mp3')
mixer.music.play()
grid=[[" # "," # "," # "," # "," # "],[" # "," # "," # "," # "," # "],[" # "," # "," # "," # "," # "],[" # "," # "," # "," # "," # "],[" # "," # "," # "," # "," # "]]
def get_board(x,y,board):
    for i in range(0,5):
        for j in range(0,5):
            if i==(x-1) and j==(y-1):
                board[i][j]=" X "
                print board[i][j],
            else:
                print board[i][j],
        print
time.sleep(1)
name=raw_input("Enter your Name: ")
time.sleep(1)
print "Hello,",name.capitalize()," Welcome to Battleship the game\n"
time.sleep(1)
print "You get 5 chances to find the enemy Battleship in this sea of #s"
time.sleep(1)
for i in range(1,6):
    for j in range(1,6):
        print " # ",
    print
time.sleep(1)
x=int(raw_input("Enter the Row: "))
y=int(raw_input("Enter the col: "))
#random_row=random.randint(1,5)
#random_col=random.randint(1,5)
random_row=3
random_col=3
count=0
while count<4:
    if x==random_row and y==random_col:
        print "YOU WIN"
        mixer.music.load('win.mp3')
        mixer.music.play()
        break
        
    else:
        get_board(x,y,grid)
        print "Try again"
        x=int(raw_input("Enter the Row: "))
        y=int(raw_input("Enter the col: "))
        count+=1
if(count==4):
    get_board(x,y,grid)
    mixer.music.load('lose.mp3')
    mixer.music.play()
    print "YOU LOSE"
