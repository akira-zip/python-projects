def Operacoes(Opcao, Number1, Number2):
  match Opcao:
    case 1:
      return(Number1 + Number2)
    case 2:
      return(Number1 - Number2)
    case 3:
      return(Number1 * Number2)
    case 4:
      return(Number1 / Number2)
    case 5:
      return(Number1 ** Number2)
    case 6:
      return(Number1 // Number2)
    case 7:
      return(Number1 % Number2)
    
def Main():
  Restart = 0
  Data = []

  for i in range(0, 2):
    Data.append(float(input('Digite o ' + str(i + 1) + '° número \n')))

  Data.append(int(input('Escolha uma operação: Somar(1), Subtrair(2), Multiplicar(3), Dividir(4), Exponenciação(5), Divisão inteira(6), Módulo(7) \n')))

  if(Data[2] == 4 or Data[2] == 6 or Data[2] == 7):
    if(Data[0] == 0 or Data[1] == 0):
      print('Não é possível dividir por zero! Tente novamente')
      Main()

  print(Operacoes(Data[2], Data[0], Data[1]))
  Restart = int(input('Escolha se deseja continuar: Sim(1), Não(2) \n'))

  if(Restart == 1):
    Main()
  else:
    print('Até a próxima!')

Main()
