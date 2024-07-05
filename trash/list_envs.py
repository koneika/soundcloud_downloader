import os
import sysconfig

def list_virtual_envs():
    venv_paths = []
    for scheme in ["nt", "posix_prefix", "posix_home"]:
        venv_paths.extend(sysconfig.get_path("scripts", scheme).split(os.pathsep))
    
    for path in venv_paths:
        if os.path.exists(path):
            for entry in os.listdir(path):
                if entry != "python.exe":  # Исключаем основной интерпретатор Python
                    print(entry)

if __name__ == "__main__":
    list_virtual_envs()
