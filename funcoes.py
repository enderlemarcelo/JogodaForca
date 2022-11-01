import os
import logging

def clear():
    os.system("cls")

def criarLog():
    logging.basicConfig(filename="log.txt", level = logging.INFO, format="%(asctime)s %(message)s")

def menu():
    print("""

▒█▀▀█ █▀▀ █▀▄▀█ 　 ▒█░░▒█ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ 
▒█▀▀▄ █▀▀ █░▀░█ 　 ░▒█▒█░ ▀█▀ █░░█ █░░█ █░░█ 
▒█▄▄█ ▀▀▀ ▀░░░▀ 　 ░░▀▄▀░ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ 

　 　 　 　 　 　 　 ░█▀▀█ 
　 　 　 　 　 　 　 ▒█▄▄█       
　 　 　 　 　 　 　 ▒█░▒█ 

　 ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█ ▒█▀▀█ ░█▀▀█ 　 █                          
　 ▒█▀▀▀ ▒█░░▒█ ▒█▄▄▀ ▒█░░░ ▒█▄▄█ 　 ▀ 
　 ▒█░░░ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ 　 ▄     
     
    """)
    os.system("pause")

def printHistorico():
    arquivo = open("log.txt","r")
    conteudo = arquivo.read()
    print("\nHistórico de Partidas:")
    print("\n"+conteudo)
    arquivo.close()
