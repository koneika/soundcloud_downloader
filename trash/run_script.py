import subprocess
import sys
import os

# Путь к вашему файлу requirements.txt
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Установка всех библиотек из requirements.txt
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])

# Запуск вашего скрипта second.py
script_path = os.path.join(os.path.dirname(__file__), 'second.py')
subprocess.check_call([sys.executable, script_path])
