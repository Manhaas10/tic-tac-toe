import os
board=[' ']*9
x=[' ']*9

#starting
def start():
  chaos="hero"
  while chaos not in ["Y","N","y","n"]:
   chaos=input("do want to start the game Y or N :")
   if chaos not in ["Y","N","y","n"]:
     print("sry invalid input")
  if chaos=="Y" or chaos=="y":
   return True
  elif chaos=="N" or chaos=="n":
   return False  


def bored():
 print(board[6]+"|"+board[7]+"|"+board[8])
 print("-----")
 print(board[3]+"|"+board[4]+"|"+board[5])
 print("-----")
 print(board[0]+"|"+board[1]+"|"+board[2])

#player input  X OR O
def inut():
    input1="voi"
    while input1 not in ["x","o"]:
      inp=input("player1 choose 'x' or 'o':")
      input1=inp.lower()
      if input1 not in ["x","o"]:
        print("invalid input")
    return input1

#player input for placinf X or O in the position

def ink():
  inpu=0
  while inpu not in range(1, 10):
    try:
      inpu = int(input("Enter a number (1-9): "))
      if inpu not in range(1, 10):
        print("Number must be between 1 and 9.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  return inpu

#puting in the respecting position
def func(inpu,player):
    board[inpu-1]=player
    return board

#checking winning possibilties
def check():
 if board[6]==board[7] and board[6]==board[8]:
   v=board[6]
   return v
 elif board[3]==board[4] and board[3]==board[5]:
   v=board[3]
   return v
 elif board[0]==board[1] and board[1]==board[2]:
   v=board[0]
   return v
 elif board[6]==board[3] and board[3]==board[0]:
   v=board[6]
   return v
 elif board[4]==board[7] and board[4]==board[1]:
   v=board[4]
   return v
 elif board[8]==board[5] and board[5]==board[2]:
   v=board[8]
   return v
 elif board[6]==board[4] and board[4]==board[2]:
   v=board[6]
   return v
 elif board[0]==board[4] and board[4]==board[8]:
   v=board[0]
   return v


def ch(x,inp):
  if inp in x:
    return True
  else:
    return False 
  
#continuing game
def conti():
  chaos="hero"
  while chaos not in ["Y","N"]:
   cha=input("do want to continue the game Y or N :")
   chaos=cha.upper()
   if chaos not in ["Y","N"]:
     print("sry invalid input")
  if chaos=="Y":
   return True
  else:
   return False 

#taking input converting into int
def dink(x):
  inpu="amaterasu"
  while inpu not in range(1,10) or inpu in x:
   inpu=int(input("enter a number (1-9):"))
   if inpu not in range(1,10) or inpu in x:
     print("wrong input")
  return inpu
#board
def bor():
 print(board[6]+"|"+board[7]+"|"+board[8])
 print("-----")
 print(board[3]+"|"+board[4]+"|"+board[5])
 print("-----")
 print(board[0]+"|"+board[1]+"|"+board[2])

#MAIN
print("welcome to tic tac toe game")
print("rules are simple according to classic tic tac toe game")

star=start()#askes y or n
#if yes
if star:
  os.system('cls')#clear the terminal
  print("you are player 1 u make the first move")
  print("Here is your board,grids are same like a number pad so acordingly choose the number")
  bored()#prints empty board
  print("player1 go ahead")
  input1=inut()#input asks whether he chose x or o
  if input1=='x':
     input2='o'
  else:
     input2='x'
#if yes
if star:
  os.system('cls')
  print("player1 your input")
  inpu1=ink()#asks number
  os.system('cls')
  x[0]=inpu1
  board=func(inpu1,input1)#builts the board
  bored()
  print("player2 your input")
  inpu2=dink(x)
  os.system('cls')
  x[1]=inpu2
  board=func(inpu2,input2)
  bored()
  print("player1 your input")
  inpu3=dink(x)
  os.system('cls')
  x[2]=inpu3
  board=func(inpu3,input1)
  bored()
  print("player2 your input")
  inpu4=dink(x)
  os.system('cls')
  x[3]=inpu4
  board=func(inpu4,input2)
  bored()
i=3
while i<8:
  print("player1 your input")
  i1=dink(x)
  os.system('cls')
  i+=1
  x[i]=i1
  if check()=='x':
    board=func(i1,input1)
    bored()
    print("congo player1 winner")
    break
  elif i==8:
    bored()
    print("its a draw!!")
    break
  else:
    bored()
  
  print("player2 your input")
  i2=dink(x)
  os.system('cls')
  i+=1
  x[i]=i2
  board=func(i2,input2)
  if check()=='o':
    bored()
    print("congo player 2 winner")
    break
  else:
    bored()

  
     
   

    

