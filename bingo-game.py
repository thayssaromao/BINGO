#.sort() é usado para ordenar uma lista em ordem ascendente (por padrão) ou em uma ordem específica especificada pelo usuário

import random, os, time
bingo = []
numbs = []

def sort():
  sort = random.randint(0,90)
  return  sort


def printCartela():
  print("\n")
  for i in range(3):
    for j in range(3):
      print(f"| {bingo[i][j]:^7}    ", end="|")
      
    print("\n\n")


for i in range(8):
  numbs.append(sort())

numbs.sort()

bingo = [ [ numbs[0],      numbs[1],       numbs[2]],
  [ numbs[3],"BINGO", numbs[4] ],
  [ numbs [5], numbs[6], numbs[7]]
]

printCartela()


while True:
  print()
  prox = input("PROXIMO NUMERO SORTEADO > y/n ")
  if prox == "y":
    os.system('cls')
    numeroSorteado = sort()
    print(f" \033[31mSORTEIO > {numeroSorteado:^7} \033[0m")
    printCartela()
    for vetor in range(3):
      for item in range(3):
        if bingo[vetor][item] == numeroSorteado:
          bingo[vetor][item] = "X"
          printCartela()
          time.sleep(2)
          os.system('cls')
    exes = 0
    for row in bingo:
      for item in row:
        if item=="X":
          exes+=1
    if exes == 8:
      print("You have won")
      break
  else:
    print("\ntchauzinho")
    exit(1)