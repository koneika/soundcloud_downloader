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


# import subprocess
# import os

# os.chdir(r"C:\Users\%USERNAME%\venv2")

# subprocess.run("cd C:\Users\%USERNAME%\venv2 && python -m venv venv2", shell=True)

# def activate_venv_and_run():
#     venv_path = r"venv2"
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Активация и запуск в одной команде с явным указанием оболочки
#     command = f'"{venv_path}\\Scripts\\activate" && python "{script_path}"'
#     subprocess.run(command, shell=True)  
#     os.system("pause")

# if __name__ == "__main__":
#     activate_venv_and_run()
#     os.system("pause")

# os.system("pause")

# import subprocess
# import os

# # Используйте сырые строки для предотвращения ошибок с обратными слэшами
# # Получение имени пользователя из переменной среды
# username = os.environ.get('USERNAME')

# # Использование полученного имени пользователя в пути
# venv_path = rf"C:\Users\{username}\venv2"

# # Переход в директорию виртуального окружения
# os.chdir(venv_path)

# # Исправленная команда с использованием сырых строк
# subprocess.run(r"cd C:\Users\%USERNAME%\venv2 && python -m venv venv2", shell=True)

# def activate_venv_and_run():
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Используйте сырые строки также здесь
#     command = rf'"{venv_path}\Scripts\activate" && python "{script_path}"'
#     subprocess.run(command, shell=True)  
#     os.system("pause")

# if __name__ == "__main__":
#     activate_venv_and_run()
#     os.system("pause")

# os.system("pause")


# import subprocess
# import os

# # Получение имени пользователя из переменной среды
# username = os.environ.get('USERNAME')

# # Путь к директории, где будет создано виртуальное окружение
# env_directory = rf"C:\Users\{username}"

# # Путь к новому виртуальному окружению
# venv_path = os.path.join(env_directory, 'myenv999999')

# # Проверка существования виртуального окружения
# if not os.path.exists(venv_path):
#     # Создание виртуального окружения, если оно не существует
#     subprocess.run([f"python", "-m", "venv", venv_path])
#     print(f"Виртуальное окружение {venv_path} создано.")
# else:
#     print(f"Виртуальное окружение {venv_path} уже существует.")

# def activate_venv_and_run():
#     script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"

#     # Активация виртуального окружения и запуск скрипта
#     command = f'"{venv_path}\\Scripts\\activate" && python "{script_path}"'
#     subprocess.run(command, shell=True)  
#     os.system("pause")

# if __name__ == "__main__":
#     activate_venv_and_run()
#     os.system("pause")

# os.system("pause")



import subprocess
import os

# username = os.environ.get('USERNAME')

# # Использование полученного имени пользователя в пути
# venv_path = rf"C:\Users\{username}\venv2"

# # Переход в директорию виртуального окружения
# os.chdir(venv_path)


def activate_venv_and_run():
    venv_path = r"C:\Users\slava\scludam-env"
    script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"
    os.system("pause")
    # Активация и запуск в одной команде с явным указанием оболочки
    command = f'"{venv_path}\\Scripts\\activate" && python "{script_path}"'
    subprocess.run(command, shell=True) 
    os.system("pause")


if __name__ == "__main__":
    activate_venv_and_run()

