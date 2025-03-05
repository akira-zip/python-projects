def Operacoes(Opcao, number1, number2):
  match Opcao:
    case 1:
      return(number1 + number2)
    case 2:
      return(number1 - number2)
    case 3:
      return(number1 * number2)
    case 4:
      return(number1 / number2)
    
def main():
  Restart = 0
  Data =[]

  for i in range(0, 2):
    Data.append(float(input('Digite o ' + str(i + 1) + '° número \n')))

  Data.append(int(input('Escolha uma operação: Somar(1), Subtrair(2), Multiplicar(3), Dividir(4) \n')))

  if((Data[2] == 4) and (Data[0] or Data[1] == 0)):
    print('Não é possível dividir por zero! Tente novamente')
    main()

  print(Operacoes(Data[2], Data[0], Data[1]))
  Restart = int(input('Escolha se deseja continuar: Sim(1), Não(2) \n'))

  if(Restart == 1):
    main()
  else:
    print('Até a próxima!')

main()