@echo off
setlocal enabledelayedexpansion
rem Robot/Automation Skeleton

cd C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\automation\summon_skeletons\

set PYTHON_ENV=C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\automation\summon_skeletons\venv\
set SCRIPTS_DIR=C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\automation\summon_skeletons\
set "pathLog=C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\_Logs\summon_skeletons"

set ROBOT_NAME=Skeletinhuuuuu
set "CAMINHO_ROBO=C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\"
set "ROBOT_LOG=C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\_Logs\"

echo Variaveis de ambiente OK

%SystemRoot%\System32\taskkill.exe /IM python.exe
REM taskkill /IM python.exe /F

REM C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\automation\summon_skeletons\venv\Scripts\Activate.ps1 & 
python C:\Users\Matheus\Documents\DATA_SCIENCE\Projetos\automation\summon_skeletons\summon_skeletons.py

endlocal