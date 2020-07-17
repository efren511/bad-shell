#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored
import subprocess
import os

banner = """
 ▄▄▄▄    ▄▄▄      ▓█████▄   ██████  ██░ ██ ▓█████  ██▓     ██▓      ██████
▓█████▄ ▒████▄    ▒██▀ ██▌▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒██    ▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    ░ ▓██▄
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░      ▒   ██▒
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓ ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒▒██████▒▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒ ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░
 ░    ░   ░   ▒    ░ ░  ░ ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   ░  ░  ░
 ░            ░  ░   ░          ░   ░  ░  ░   ░  ░    ░  ░    ░  ░      ░
      ░            ░
                              BY QUEEN HACK
                              MelissaCrack
                              RollersProto
                              Efrén Garcia
"""

menu = """
                          Seleecione una opcion

                            1) Listar Shells

                    2) Mostrar Información de una Shell

                          3) Escoger una Shell

                                4) Salir
"""

error = """
                            _  _   _   _   _
                           |_ |_) |_) / \ |_)
                           |_ | \ | \ \_/ | \\
"""

bye = """
 ____ ____ ____ _________ ____ ____ ____ _________
||B |||Y |||E |||       |||B |||Y |||E |||       ||
||__|||__|||__|||_______|||__|||__|||__|||_______||
|/__\\|/__\\|/__\\|/_______\\|/__\\|/__\\|/__\\|/_______\\|
"""

def main():
    print(colored(banner, "red"))
    while True:
        origen = os.getcwd()
        print(colored(menu, "blue"))
        opcion = input(": ")
        if opcion == "1":
            os.chdir("datos")
            subprocess.run("ls")
            os.chdir(origen)
        elif opcion == "2":
            carpeta = input(colored("Escribre el nombre de la shell: ", "green"))
            ruta = "datos/"+carpeta
            os.chdir(ruta)
            subprocess.run(["cat", "info.txt"])
            os.chdir(origen)
        elif opcion == "3":
            carpeta = input(colored("Escribre el nombre de la shell: ", "green"))
            ruta = "datos/"+carpeta
            script = carpeta+".php"
            os.chdir(ruta)
            subprocess.run(["cp", script, origen])
            print(colored("Tu shell se encuentra en ", "green"), origen)
            os.chdir(origen)
        elif opcion == "4":
            print(colored(bye, "yellow"))
            exit()
        else:
            print(colored(error, "red"))
if __name__ == '__main__':
    main()
