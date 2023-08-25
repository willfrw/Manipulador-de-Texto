import func

func.linMsg('Atividade de Produção\n\nDisciplina: Laboratório de Programação\nCódigo: G-23100191\nProfessor:	Mozart Lemos de Siqueira\nAluno: William Freire Wang\nMatrícula: 202221378')

func.linMsg("Contador de Letras de Arquivo")

while True:
  opt = str(input("\nDigite a opção desejada:\n[1] - Ler o arquivo\n[2] - Contar os caracteres do arquivo\n[3] - Adicionar uma frase ao arquivo\n[4] - Finalizar o programa\n"))
  if opt == '1':
    rText = open("text.txt", "r")
    print("\nO arquivo aberto contém o seguinte texto:\n")
    
    func.linMsg('Começo do Arquivo')
    print(rText.read())
    func.linMsg('Fim do Arquivo')
  elif opt == '2':
    func.linMsg(f"O arquivo possui {func.countTxt('text.txt')} caracteres")
  elif opt == '3':
    # Pega o texto do usuário
    userTxt = str(input("\nEscreva uma frase para incluir ao arquivo:\n"))
    
    # Abre o arquivo, adiciona texto adicionado pelo usuário ao final do arquivo e fecha o arquivo
    aText = open("text.txt", "a")
    aText.write("\n")
    aText.write(userTxt)
    aText.close()

  elif opt == '4':
    break
  else:
    print("Erro: opção inválida")
  
func.linMsg("Fim do programa")
