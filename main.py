import subprocess
import os

def activate_venv_and_run():
    venv_path = r"C:\Users\slava\scludam-env"
    script_path = r"C:\Users\slava\Desktop\py\soundcloud\github\pythons-main\list_of_prices\second.py"
    
    # Активация и запуск в одной команде с явным указанием оболочки
    command = f'"{venv_path}\\Scripts\\activate" && python "{script_path}"'
    subprocess.run(command, shell=True) 
    
if __name__ == "__main__":
    activate_venv_and_run()

