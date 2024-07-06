import random

bingo = [[None,None,None],[None,'BINGO',None],[None,None,None]]

def generate_list():
  list = []
  for i in range(8):
    list.append(random.randint(0,90))
  list = sorted(list)
  return list

def board():
  count = 0
  generator = generate_list()
  bingo = [[None,None,None],[None,'BINGO',None],[None,None,None]]
  for i in range(3):
     for y in range(3):
        if bingo[i][y] == 'BINGO':
           continue
        else:
           bingo[i][y] = generator[count]
           count += 1
  return bingo

def print_board(bingo_board):
  for row in bingo_board:
    print(row)

X_count = 0
player_board = board()
print_board(player_board)
while True:
  next_num = int(input('Next Number: '))
  for i in range(3):
     for y in range(3):
      if X_count == 8:
        print('You have won')
        print_board(player_board)
        exit() 
      elif next_num == player_board[i][y]:
        player_board[i][y] = 'X'
        X_count += 1
        print_board(player_board)