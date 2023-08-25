# Cria título com linhas de acordo com tamanho do texto
def linMsg(msg):
  msgLen = len(msg)
  if msgLen > 30:
    msgLen = 30
  print("\n")
  print("*-" * (msgLen))
  print(" " * int(msgLen / 2) + f"{msg}")
  print("*-" * (msgLen))
  print("\n")


# Conta os caracteres do texto e retorna o valor contador
def countTxt(text):
  cT = open(text, "r")
  counter = 0
  for line in cT:
    for letter in line:
      if (letter != ' ' and letter != '\n'):
        counter += 1
  return counter
