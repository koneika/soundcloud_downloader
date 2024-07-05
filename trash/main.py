# import subprocess

# def run_commands():
#     """Выполняет команды для активации окружения и запуска скрипта."""

#     commands = [
#         r"scludam-env\Scripts\activate",
#         r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"
#     ]

#     for command in commands:
#         subprocess.run(command, shell=True)

# if __name__ == "__main__":
#     run_commands()

# import os

# def activate_venv_and_run():
#     """Активирует виртуальное окружение и запускает скрипт, изменяя переменные окружения."""

#     venv_path = r"scludam-env"  # Путь к виртуальному окружению
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Активация окружения
#     activate_this = os.path.join(venv_path, 'Scripts', 'activate_this.py')
#     with open(activate_this) as f:
#         exec(f.read(), dict(__file__=activate_this))

#     # Запуск скрипта
#     os.system(f'python "{script_path}"')

# if __name__ == "__main__":
#     activate_venv_and_run()


# import os

# def activate_venv_and_run():
#     """Активирует виртуальное окружение и запускает скрипт с помощью os.system."""

#     venv_path = r"scludam-env"  # Путь к виртуальному окружению
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Активация окружения
#     activate_command = f"{venv_path}\Scripts\activate"  # Windows
#     os.system(activate_command + " && " + f'python "{script_path}"')  # Выполняем activate и запуск скрипта

# if __name__ == "__main__":
#     activate_venv_and_run()




# import os

# def activate_venv_and_run():
#     """Активирует виртуальное окружение и запускает скрипт с помощью os.system."""

#     venv_path = r"scludam-env"  # Путь к виртуальному окружению
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Активация окружения (Windows)
#     activate_command = f'"{venv_path}\\Scripts\\activate"' 
#     #Обратите внимание на кавычки вокруг пути и двойные слэши

#     # Запуск скрипта
#     os.system(activate_command + " & " + f'python "{script_path}"') 
#     # Используем & вместо && для параллельного выполнения команд в Windows

# if __name__ == "__main__":
#     activate_venv_and_run()


import subprocess

def activate_venv_and_run():
    venv_path = r"scludam-env"
    script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

    # Активация и запуск в одной команде с явным указанием оболочки
    command = f'"{venv_path}\\Scripts\\activate" && python "{script_path}"'
    subprocess.run(command, shell=True)  

if __name__ == "__main__":
    activate_venv_and_run()


