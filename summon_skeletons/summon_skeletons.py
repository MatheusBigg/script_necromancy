# coding: ISO-8859-1
import os
import sys
import time
import subprocess
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from Utilitarios.Log import Log
from Utilitarios.Timer import Timer

Log(pathLog=os.environ.get("pathLog"))

nome_robo = os.environ.get("ROBOT_NAME")
caminho_robo = os.environ.get("CAMINHO_ROBO") + f"{nome_robo}"
caminho_log = os.environ.get("ROBOT_LOG") + f"{nome_robo}"


#.bat
skeleton_bat = f"""
@CHCP 1252 > NUL
@echo off

cd {caminho_robo}\\
set PYTHONPATH={caminho_robo}\\

set "ROBOT_NAME={nome_robo}"
set "ROBOT_LOG={caminho_log}\\"
set INPUTS={caminho_robo}\\INPUTS\\
set OUTPUTS={caminho_robo}\\OUTPUTS\\
set LOCAL_PATH=C:\\LOCAL_ROBOT_FILES\\{nome_robo}\\

echo Variaveis de ambiente OK

%SystemRoot%\\System32\\taskkill.exe /IM python.exe
REM taskkill /IM python.exe /F

{caminho_robo}\\venv\\Scripts\\Activate.bat & python {nome_robo}.py

"""

#.sh
skeleton_sh = f"""
#!/bin/bash

export ROBOT_NAME={nome_robo}/
export ROBOT_LOG={caminho_log}/"
export INPUTS={caminho_robo}/INPUTS/
export OUTPUTS={caminho_robo}/OUTPUTS/
export LOCAL_PATH=/c/LOCAL_ROBOT_FILES/{nome_robo}/

echo "Variáveis de ambiente OK"

pkill python

source {caminho_robo}/venv/bin/activate

# Execute o script Python
python {nome_robo}.py

"""

#.py
skeleton_py = f"""
# coding: ISO-8859-1

import sys
import os
import re
import pandas
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from Utilitarios.Log import Log
from Utilitarios.Timer import Timer


__NOME_ROBO     = os.environ.get("ROBOT_NAME")
__DATA          = datetime.now().strftime("%Y-%m-%d")
__CAMINHO_LOG   = os.environ.get("ROBOT_LOG")
__INPUTS        = os.environ.get("INPUTS")
__OUTPUTS       = os.environ.get("OUTPUTS")
__LOCAL_PATH    = os.environ.get("LOCAL_PATH")

Log(pathLog=__CAMINHO_LOG)

Log.info(f"Criando pastas, configuracoes e verificacoes")
pastas = [__CAMINHO_LOG, __INPUTS, __OUTPUTS, __LOCAL_PATH]
for pasta in pastas:
    if not os.path.exists(pasta):
        os.makedirs(pasta)


        
def main():
    Log.info(f"Comecando execucao do robo {{__NOME_ROBO}}")
    timer = Timer()
    try:
        breakpoint()

    
        Log.info(f"Finalizando execucao do robo {{__NOME_ROBO}}")
        Log.info(f"{{timer.elapsed}}ms")
    except Exception as e:
        Log.error(f"Erro no {{__NOME_ROBO}}: " + str(e))
        raise Exception(f"Erro no {{__NOME_ROBO}}")

        

if __name__ == "__main__":
    main()

"""

if __name__ == "__main__":
    Log.info(f"Sumonando {nome_robo}")
    timer = Timer()
    magia = 'Chamado dos Ossos Eternos'
    cast = '''
                        :::!~!!!!!:.
                    .xUHWH!! !!?M88WHX:.
                    .X*#M@$!!  !X!M$$$$$$WWx:.
                :!!!!!!?H! :!$!$$$$$$$$$$8X:
                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                ~?WuxiW*`   `"#$$$$8!!!!??!!!
                :X- M$$$$       `"T#$T~!8$WUXU~
                :%`  ~#$$$m:        ~!~ ?$$$$$$
            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
    .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
    W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
    #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
    :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
    .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
    Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
    $R@i.~~ !     :   ~$$$$$B$$en:``
    ?MXT@Wx.~    :     ~"##*$$$$M~
'''


    for char in magia:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    print('\n\n')

    for linha in cast.splitlines():
        print(linha)
        time.sleep(0.05)

    
    Log.info(f"Criando as pastas")
    pastas = [caminho_robo, caminho_log]
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.mkdir(pasta)

    
    Log.info(f"Criando a venv")
    try:
        subprocess.run(["python", "-m", "venv", caminho_robo+'/venv/'], check=True)
        print("venv criada")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar venv: {e}")


    Log.info(f"Criando o requirements.txt, ativando a venv, atualizando o pip e instalando as dependencias")
    bibliotecas = ["pyautogui", "psutil", "pandas", "openpyxl", "pywin32"]
    try:
        if sys.platform == 'win32':
            # Windows
            with open(f"{caminho_robo}\\requirements.txt", "w") as f:
                f.write("\n".join(bibliotecas))
            subprocess.run([f"{caminho_robo}\\venv\\Scripts\\python.exe", "-m", "pip", "install", "--upgrade", "pip"], check=True)
            subprocess.run([f"{caminho_robo}\\venv\\Scripts\\python.exe", "-m", "pip", "install", "-r", f"{caminho_robo}\\requirements.txt"], check=True)
        elif sys.platform == 'linux' or sys.platform == 'darwin':
            # Linux ou macOS
            with open(f"{caminho_robo}/requirements.txt", "w") as f:
                f.write("\n".join(bibliotecas))
            subprocess.run([f"{caminho_robo}/venv/bin/python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
            subprocess.run([f"{caminho_robo}/venv/bin/python", "-m", "pip", "install", "-r", f"{caminho_robo}/requirements.txt"], check=True)
        else:
            print("Sistema operacional não suportado")
    except subprocess.CalledProcessError as e:
            print(f"Erro ao fazer upgrade do pip e instalar dependencias: {e}")
    print("Upgrade e Dependencias instaladas")


    # command_windows = f'{caminho_robo}\\venv\\\\Scripts\\activate.ps1; pip freeze'
    # command_linux = f"source {caminho_robo}/venv/bin/activate; pip freeze; exec bash"

    # Log.info(f"Abre um PowerShell/Bash e ativa a venv criada e executa pip freeze")
    # if sys.platform == 'win32':
    #     os.system(f'start powershell -NoExit -Command {command_windows}')
    # elif sys.platform == 'linux' or sys.platform == 'darwin':
    #     os.system(f'gnome-terminal -- bash -c "{command_linux}"')
    # else:
    #     print("Sistema operacional nao suportado")



    Log.info(f"Criando o .bat, .sh e .py")
    skeletons_dict = {
        f"{caminho_robo}\\{nome_robo}.bat": skeleton_bat,
        f"{caminho_robo}/{nome_robo}.sh": skeleton_sh,
        f"{caminho_robo}\\{nome_robo}.py": skeleton_py
    }

    for skeleton, script in skeletons_dict.items():
        if (skeleton.endswith('.bat') and sys.platform == 'win32') or \
        (skeleton.endswith('.sh') and sys.platform != 'win32') or \
        skeleton.endswith('.py'):
            with open(skeleton, "w") as f:
                f.write(script)


    Log.info(f"Abre as pastas")
    os.startfile(caminho_robo)
    os.startfile(caminho_log)

    Log.info(f"Skeleton Sumonado: {nome_robo} - {timer.elapsed/1000}s")
    print(f"Skeleton Sumonado: {nome_robo} - {timer.elapsed/1000}s")