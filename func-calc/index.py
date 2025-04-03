restart = 0
data = [0, 0, 0]

def operacoes(opcao, n1, n2):
  match opcao:
    case 1:
      return(n1 + n2)
    case 2:
      return(n1 - n2)
    case 3:
      return(n1 * n2)
    case 4:
      return(n1 / n2)
    case 5:
      return(n1 ** n2)
    case 6:
      return(n1 // n2)
    case 7:
      return(n1 % n2)
    
def getData(opcao):
  match opcao:
    case 1:
      try:
        for i in range(0, 2):
          data[i] = (float(input('Digite o ' + str(i + 1) + '° número \n')))
      except:
        print('Tente novamente')
        getData(1)
    case 2:
      try:
        data[2] = int(input('Digite os valores para as respectivas operações: \n[1] - Somar \n[2] - Subtrair \n[3] - Multiplicar \n[4] - Dividir \n[5] - Exponenciação \n[6] - Divisão inteira \n[7] - Módulo \nSelec: '))
      except:
        print('Tente novamente')
        getData(2)

    
def main():
  getData(1)
  getData(2)

  if(data[2] == 4 or data[2] == 6 or data[2] == 7):
    if(data[0] == 0 or data[1] == 0):
      print('Não é possível dividir por zero! Tente novamente')
      main()

  print('Res:', operacoes(data[2], data[0], data[1]))

  print('\n--------------------------------\n')

  restart = int(input('Escolha se deseja continuar: \n[1] - Sim \n[2] - Não \nSelec: '))

  if(restart == 1):
    print('\n--------------------------------\n')
    main()
  else:
    print('\n--------------------------------\n')
    print('Até a próxima!')

main()
