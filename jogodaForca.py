from funcoes import clear, criarLog, menu, printHistorico
import logging

criarLog()

while True:
    listaLetras = []
    listaOculta = []
    tentativa = []
    numDica = 0
    erros = 0
    
    clear()
    menu()
    clear()
    desafiante = input("Digite o nome do desafiante: ")
    competidor = input("Digite o nome do competidor: ")
    clear()
    palavraChave = str(input("Palavra do desafiante: ").lower().strip())
    dica1 = str(input("Insira a primeira dica: "))
    dica2 = str(input("Insira a segunda dica: "))
    dica3 = str(input("Insira a terceira dica: "))
    clear()

    for i in (palavraChave):
        listaLetras.append(i)
    for x in range(len(listaLetras)):
        listaOculta.append("_ ")
    print(''.join(map(str, listaOculta)))

    while True:  
        try:
            print ("\nPara jogar, digite '1'!")
            print ("Para dicas, digite '2'!\n")
            comando = int(input())
        except:
            print("\nComando inválido\n")
            print ("\nPara jogar, digite '1'!")
            print ("Para dicas, digite '2'!\n")
            comando = int(input())
        clear()
        if comando == 1:
            print(''.join(map(str, listaOculta)))
            letra = str(input("\nDigite a sua letra: "))
            if letra in listaLetras:
                if letra in tentativa:
                    print("\nVocê já digitou essa letra!")
                    continue
                tentativa += letra
                print("\nVocê acertou!\n")
                for i in range(len(listaLetras)):
                    if letra == listaLetras[i]:
                        listaOculta[i] = letra
                print(''.join(map(str, listaOculta)))
                if listaLetras == listaOculta:
                    clear()
                    print("Parabéns! Você acertou a palavra imposta pelo desafiante!\n")
                    print(''.join(map(str, listaOculta)))
                    logging.info(f"Palavra: {''.join(listaLetras)} - Vencedor: Competidor {competidor}, Perdedor: Desafiante {desafiante}")
                    printHistorico()
                    break
            else:
                if letra in tentativa:
                    print("\nVocê já digitou essa letra!")
                    continue
                else:
                    tentativa += letra
                    erros +=1
                    if erros == 1:
                        print("\nErro 1")
                    elif erros == 2:
                        print("\nErro 2")
                    elif erros == 3:
                        print("\nErro 3")
                    elif erros == 4:
                        print("\nErro 4")  
                    elif erros == 5:
                        print("\nErro 5") 
                    else:
                        print("\nVocê perdeu!")
                        logging.info(f"Palavra: {''.join(listaLetras)} - Vencedor: Desafiante {competidor}, Perdedor: Competidor {desafiante}")
                        printHistorico()
                        break
                    
        if comando == 2:
            numDica += 1
            if numDica == 1:
                print(f"\nDica 1: {dica1}")
            elif numDica == 2:
                print(f"\nDica 2: {dica2}")
            elif numDica == 3:
                print(f"\nDica 3: {dica3}")
            else:
                print("\nVôce utilizou todas as dicas disponíveis!")  

    jogarNovamente = input("\nSe deseja jogar novamente digite '1' se deseja fechar o jogo digite '2': ")
    if jogarNovamente == '1':
        continue
    else:
        break