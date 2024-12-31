#!/bin/bash
# Robot/Automation Skeleton

# Define o diretório base do projeto
cd /home/matheus/DATA_SCIENCE/Projetos/automation/summon_skeletons/ || exit

# Define variáveis de ambiente
export PYTHON_ENV="/home/matheus/DATA_SCIENCE/Projetos/automation/summon_skeletons/venv/"
export SCRIPTS_DIR="/home/matheus/DATA_SCIENCE/Projetos/automation/summon_skeletons/"
export pathLog="/home/matheus/DATA_SCIENCE/Projetos/_Logs/summon_skeletons"

export ROBOT_NAME="MainRobot"
export CAMINHO_ROBO="/home/matheus/DATA_SCIENCE/Projetos/"
export ROBOT_LOG="/home/matheus/DATA_SCIENCE/Projetos/_Logs/"

echo "Variaveis de ambiente OK"

# Mata processos python em execução
pkill -f python

# Ativa o ambiente virtual e executa o script Python
source "$PYTHON_ENV/bin/activate"
python "$SCRIPTS_DIR/summon_skeletons.py"


# Torne o arquivo executável:
# chmod +x start_robot.sh