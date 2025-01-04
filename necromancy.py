# coding: ISO-8859-1
import os
import sys
import time
import subprocess

                                                            # NECROMANCY # 
class Necromancy():
    def __init__(self):
        #Cemitery Variables
        is_windows = sys.platform.startswith("win")
        linux_username = os.environ.get("USER")
        base_caminho = "C:\\cemiterio\\" if is_windows else f"/home/{linux_username}/cemiterio/"
        self.caminho_cemiterio = os.path.join(base_caminho)
        self.caminho_capelas = os.path.join(base_caminho, "logs")
        self.caminho_venvs = os.path.join(base_caminho, "venvs")
        if is_windows:
            self.venvs = {'skeleton':['pyautogui', 'psutil', 'pywin32', 'rich', 'tqdm']}#,
                        # 'skeleton_knight':[ "pyautogui", "psutil", "pandas", "openpyxl", "pywin32", 'rich', 'tqdm'], 
                        # 'skeleton_warlord':['pyautogui', 'psutil', 'pandas', 'openpyxl', 'pywin32', 'selenium', 'webdriver_manager', 'beautifulsoup4', 'requests', 'PyMuPDF', 'SpaCy', 'rich', 'tqdm'],
                        # 'skeleton_mage': ['pandas', 'openpyxl', 'polars', 'rich', 'tqdm'],
                        # 'skeleton_archer': ['pandas', 'openpyxl', 'PyMuPDF', 'rich', 'tqdm'],
                        # 'skeleton_shaman': ['django', 'fastapi', 'taipy', 'flask', 'rich', 'tqdm'],}
        else:
            self.venvs = {'skeleton':['pyautogui', 'psutil', 'rich', 'tqdm']}#,
                    # 'skeleton_knight':[ "pyautogui", "psutil", "pandas", "openpyxl", 'rich', 'tqdm'], 
                    # 'skeleton_warlord':['pyautogui', 'psutil', 'pandas', 'openpyxl', 'selenium', 'webdriver_manager', 'beautifulsoup4', 'requests', 'PyMuPDF', 'SpaCy', 'rich', 'tqdm'],
                    # 'skeleton_mage': ['pandas', 'openpyxl', 'polars', 'rich', 'tqdm'],
                    # 'skeleton_archer': ['pandas', 'openpyxl', 'PyMuPDF', 'rich', 'tqdm'],
                    # 'skeleton_shaman': ['django', 'fastapi', 'taipy', 'flask', 'rich', 'tqdm'],}
        
        self.cemetery_magic = f"""  
        RISE MY CEMETERY, I DEMAND IT!              
                        _|_
                        _|___
                    /~/~   ~\\
                    | |       \\
                    \ \        \\
                    \ \        \\
                    --\ \       .\\''
                    --==\ \     ,,i!!i,
                        ''"'',,{{}}{{}},,
        """
        
        #Imps Variables
        self.imp_magic = f'''  
        COME TO ME, MY FLYING SERVANTS                                                     
.------.                                                                                
        :-+*=:                                                                           
        :#%%*=:                                                           .::---=---: 
            +%@@@%#+=.                                                 .-+*%+-:         
            :*%@@@@@#=                                         ..:-+#%@@@#-            
                -#@@@@@@#=                                     :+%@@@@@@@%+.             
                =%@@@@@@#*:                                -#%@@@@@@@#+-               
                +@@@@@@@%#:                           .++%@@@@@@@@@*-                 
                +%%@@@@@@%#:                         .*%@@@@@@@@@@+                   
                .%@@@@@@%%%#=                       .#%%@@@@@@%%@*                    
                =%+-==+*%%%##=    *.     .+        :*%%%%%@@@%%%%#                    
                =      *+==-=*=.. -++---++=  :    -*%%%%##%%@%%@%=                    
                :      -      -++-:=+++=**:-+.   =*%###****-:-:=#*                    
                        -.        =**+**#*+*+=.  :**-   .::+-      :=                   
                                    +###*++#+.  .=#:         +       =                   
                                    -*##*+#%#+=**=.          =                           
                                *%%%%%*%#%%%%#:                                       
                                .#@*%@@@@@@%=%@#+                                      
                                -%% +@@@@@@*  =%%+:                                    
                                .+@- -%@@@@%+   .+#*-                                   
                                -+*#  #@@%%%%*     *#+:                                  
                                +#*+ .++*+=-=*     :%*+                                  
                                .*%#. -***=-+*+=     -*=                                  
                             .**   *+*##*##+=-     ==:                                 
                             -=.   *+++#@#**-+.    -==                                 
                              *=    =###+@# ++==   -*++=                                
                            -+=-    .=-.@%  *%*  .# -++*=                              
                            :*#%#    .=- #@- +@#  .:  :*#*                              
                            =+##    :+=:-@* :@=     .*=:                               
                            #=.    :#+=.#% -#+                                        
                            :=      =#+- -@= =+                                        
                            =.      -*-. .@% :==                                       
                            =        +-  :%%:-==.                                      
                            -:             %* :*+*.                                     
                            =              *-  =+*-                                     
                            :-             .*:   .=+                                     
                            =              ##.     .                                     
                        .=             .%#=                                           
                        .*.             .++-                                           
                        .                                                             
'''

        #Skeletons Variables
        self.caminho_robo = f"{self.caminho_cemiterio}"
        self.caminho_log = f"{self.caminho_capelas}"
        self.skeleton_magic = '''
        APPEAR, MY CHILD! APPEAR!  

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

        #Demons Variables
        self.imp_magic = f'''
        *BLOOD-PACT*
        OBEY ME, DEMONS!
                                                                                        
                                        .::--+****#+.   ::--::.                        
                                        :+%@%%*####@@@@*.  .:-=*%+:                    
                        .   -=++-:--+*##+-.        -#@@@%-      +@%-                  
                                    .::.                .%@@@.      .#@#.                
                                            =+   .... *@@@%       :@@*                
                                            :@@#*#%%%#@@@@@:      *@@@                
                                        ..-+#%@@@@@@@@@@@@@@     =#@@@+                
                                    .-=%@@@@@@@@@@@@@@@@@@#+*#%@@@@@#                 
                                    -=*@@@@@@@@@@@@@%@@@@@@@@@@@@@#-                  
                                    -=#@@@@@@@@@@@@@@@@@@@@@@%%*+-.                    
                                ..:**%@@@@@@@@@@@%*-%@@@@#+-:                          
                                .=#@@@@@@@@@@@@@@#%@@%=*+*+:                           
                        .-=*##%@@@@@@@@@@@@@@@@@@@@@:--                               
                        .*@@@@@@@@@@@@@@@@@@@@@@@@@#=#%-                                
                        *@@@@@@@@@@@@@@@@@@@@@@@@@%+%+-+.                               
                        #@@@@@@@@@@@@%@@@@@@@@@@@@@@%#=..                               
                        :#@@@@@@@@@%%*%@@@@@@@@@@@@*@@@@#+:                              
                    .*@@@@@@@@@@@@@@@@@@@@@@@@@@=%@@@@@%@#:                            
                    .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@+                            
                    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@%@*                            
                    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@#@-                            
                    -@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@%*-**                             
                    :@@@@@@@@@@@@@@@@@%@@@@@@@@@@@%+%@= -%                              
                    -%@@@@@@@@%+*@@@@@@@@@@@@@@%%%@##@@--+@                              
                    *@@@@@#%@+   .@@@@@@@@@@@@%%#@@@@@%..%@.                             
                =@@@@@@@@+     .%@@@@@@@@@@@@@@@@++@: @@.                             
                -@@@@@@@@@+      -@@@@@@@@@@@@@@@#*@@*-@@:                             
                .+@@@@@@@@@@-      @@@@@@@@@@@@@@@@@%@..@==.                            
                *%@@@@@@@@@@%+     %@+%@@@@@@@@@@@@@%@* *@@%.                           
                +#%@@@@@@@@@@%@    *%@@#@@%%@@@@@@@%#%%-.-@@@=                           
            .*+@@@@@@@@@@%+%.  :@@#+#%+--=*@@@@@%@%+. :@@@#.                          
            .--@*%@@@@@@#.#+:  %@@+. :::   :-*#+@@%%: .@@@+                           
            . ++ :@@@@@@= ::. =@@#.           =++#%%-  %@@#                           
                *:   %@@@@@=     =.-*-           -..#%=   .+%%                           
                :   .=@@@@@+     :  ..           - :%+:     #@=                          
                    *@@@@@@.    :               .  =-      -++                          
                    :@@@@@@@=   .               .  -       .+                           
                    @@@@@@@@%- .                  .         :                          
                    .@@@@@@@@@@..                  .                                    
                    :@@@@@@@@+@#                   .                                    
                    %@@@@@@% %@=                                                       
                    =@@@@@@@=                                                          
                    =#@@@@@@*                                                         
                        .::.:                                                         
'''        
        
        #Ghouls Variables


    def cast_magic(self, magia):
        for linha in magia.splitlines():
            print(linha)
            time.sleep(0.05)


    def transmorphing(text):
        #trocar de windows para linux \\
        pass

    def transmuting(text):
        #trocar de windows para linux funcao ou caminho inteiro
        pass

    def crypt_polishing(self, venvs, caminho_venvs):
        # Identificar o sistema operacional usando sys.platform
        is_windows = sys.platform.startswith("win")

        # Configurar os comandos e caminhos baseados no sistema operacional
        python_cmd = "python" if is_windows else "python3"
        script_folder = "Scripts" if is_windows else "bin"
        
        #Criando venvs
        for venv, grimorio in venvs.items():
            cripta = os.path.join(caminho_venvs, venv)
            try:
                subprocess.run([python_cmd, "-m", "venv", cripta], check=True)
                print(f"Cripta criada {venv}")
            except subprocess.CalledProcessError as e:
                print(f"Erro ao criar cripta: {e}")

            #Criando o requirements.txt, ativando a venv, atualizando o pip e instalando as dependencias"
            try:
                requirements_path = os.path.join(cripta, "requirements.txt")
                with open(requirements_path, "w") as f:
                    f.write("\n".join(grimorio))
                
                # Caminho para o executável Python da venv
                python_executable = os.path.join(cripta, script_folder, "python")
                subprocess.run([python_executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
                subprocess.run([python_executable, "-m", "pip", "install", "-r", requirements_path], check=True)
            except subprocess.CalledProcessError as e:
                    print(f"Erro ao fazer upgrade do pip e instalar dependencias: {e}")
            print("Upgrade e Dependencias instaladas")




    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # CEMETERY #  
    def rise_cemetery(self, caminho_cemiterio, venvs, caminho_venvs, caminho_capelas):
        #Erguendo o cemitério
        self.cast_magic(self.cemetery_magic)    

        pastas = [caminho_cemiterio, caminho_capelas, caminho_venvs]
        for pasta in pastas:  
            if not os.path.exists(pasta):    
                os.makedirs(pasta, exist_ok=True)
    
        self.crypt_polishing(venvs, caminho_venvs)


    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

    
                                                            # IMPERIUM #                                                        
    def IMPerium(self, caminho_cemiterio):

        utils = os.path.join(caminho_cemiterio, "utilitarios")
        self.cast_magic(self.imp_magic)
        
        timer = f"""
import datetime
import time

class Timer:
    def __init__(self):
        self.__start_time = datetime.datetime.now()
        self.__stop_time = None

    @property
    def start_time(self):
        # Returns time that counter started counting
        return self.__start_time

    @property
    def stop_time(self):
        # Returns time that counter stopped counting
        return self.__stop_time

    @property
    def elapsed(self):
        # Get time passed since timer started counting
        deltatime = datetime.datetime.now() - self.__start_time
        miliseconds = deltatime.total_seconds() * 1000
        return round(miliseconds)

    def start(self):
        # Starts time counting
        self.__start_time = datetime.datetime.now()
        self.__stop_time - None

    def stop(self):
        # Stops time counting
        self.__stop_time = datetime.datetime.now()
"""
        
        log = f"""
# Logs

import os
import logging
import pyautogui
import psutil
import datetime

class Log:

    pathLogWithDateFormat = None
    lastScreenshot = ""
    debug = False

    def __init__(self, pathLog=None):
        try:
            if pathLog is not None:
                Log.debug = True
                now = datetime.datetime.now()
                dateFormat = datetime.datetime.strftime(now, "%Y-%m-%d")
                Log.pathLogWithDateFormat = os.path.join(pathLog, dateFormat)
                if not os.path.exists(Log.pathLogWithDateFormat):
                    os.makedirs(Log.pathLogWithDateFormat)

                computerName = ""
                try:
                    computerName = os.environ.get("COMPUTERNAME")
                except:
                    pass

                timeFormat = datetime.datetime.strftime(now, "%Hh%Mm%Ss")
                filenameLog = os.path.join(
                    Log.pathLogWithDateFormat, f"{{computerName}}-{{timeFormat}}.txt"
                )
                logging.basicConfig(
                    filename=filenameLog,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.INFO,
                )

                detailsMachine = Log.getDetailsMachine(True)
                logging.info(detailsMachine)

            else:
                Log.debug = False
        except:
            pass

    @staticmethod
    def error(exception=None, takeScreenshot=True):
        try:
            if Log.debug:
                detailsMachine = Log.getDetailsMachine()
                if (isinstance(exception, Exception)) or exception == None:
                    text = detailsMachine + "Erro"
                else:
                    text = detailsMachine + str(exception)

                logging.exception(text)

                if takeScreenshot:
                    Log.takeAndSaveScreenshot()

        except:
            pass

    @staticmethod
    def info(text, takeScreenshot=False):
        try:
            if Log.debug:
                detailsMachine = Log.getDetailsMachine()
                logging.info(detailsMachine + text)
                if takeScreenshot:
                    Log.takeAndSaveScreenshot()
        except:
            pass

    @staticmethod
    def takeAndSaveScreenshot(pathScreenshot=None):
        try:
            if Log.debug:
                if pathScreenshot == None:
                    now = datetime.datetime.now()
                    timeFormat = datetime.datetime.strftime(now, "%Hh%Mm%Ss")
                    pathScreenshot = os.path.join(
                        Log.pathLogWithDateFormat, f"{{timeFormat}}.png"
                    )

                pyautogui.screenshot(pathScreenshot)

                if os.path.exists(pathScreenshot):
                    Log.lastScreenshot = pathScreenshot
        except Exception as e:
            Log.error(exception=e, takeScreenshot=False)

    @staticmethod
    def getDetailsMachine(completed=False):
        try:
            cpu_percs = "{{:>6}}".format(str("%.2f" % psutil.cpu_percent(1, False)))
            ram_usage = "{{:>5}}".format(
                str("%.2f" % round(psutil.virtual_memory()[3] / 1000000000, 2))
            )
            ram_usage_perc = "{{:>6}}".format(
                str("%.2f" % round(psutil.virtual_memory()[2], 2))
            )
            detailsMachine = (
                f"CPU: {{cpu_percs}}% - RAM: {{ram_usage}}GB ({{ram_usage_perc}}%) - "
            )

            if completed:
                disk_usage = "{{:>6}}".format(
                    str("%.2f" % round(psutil.disk_usage("/")[1] / 1000000000, 2))
                )
                disk_usage_perc = "{{:>6}}".format(
                    str("%.2f" % round(psutil.disk_usage("/")[3], 2))
                )
                detailsMachine = (
                    f"{{detailsMachine}}DISK: {{disk_usage}}GB ({{disk_usage_perc}}%)"
                )

            return detailsMachine
        except Exception as e:
            logging.exception(e)
            return ""

"""
        
        webscrapping = f"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import requests
from bs4 import BeautifulSoup
import time

class SeleniumFunctions:

    def __init__(self, browser="chrome", implicit_wait=10):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser.lower() == "firefox":
            from webdriver_manager.firefox import GeckoDriverManager
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Navegador não suportado. Use 'chrome' ou 'firefox'.")

        self.driver.implicitly_wait(implicit_wait)
        self.wait = WebDriverWait(self.driver, implicit_wait)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text, clear_first=True):

        element = self.find_element(by, value)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def wait_for_element(self, by, value, timeout=10):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_and_click(self, by, value, timeout=10):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except Exception as e:
            print(f"Erro ao clicar no elemento: {{e}}")

    def scroll_to_element(self, by, value):
        element = self.find_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def quit(self):
        self.driver.quit()

        
class SoupFunctions:

    def __init__(self, url=None, html=None, parser="html.parser"):
        self.soup = None
        self.url = url
        self.parser = parser
        if url:
            self.load_url(url)
        elif html:
            self.soup = BeautifulSoup(html, parser)

    def load_url(self, url):
        self.url = url
        response = requests.get(url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, self.parser)
        else:
            raise Exception(f"Falha ao carregar a URL: {{url}} (Status {{response.status_code}})")

    def find(self, tag, attrs=None):
        return self.soup.find(tag, attrs=attrs)

    def find_all(self, tag, attrs=None, limit=None):
        return self.soup.find_all(tag, attrs=attrs, limit=limit)

    def select_one(self, selector):
        return self.soup.select_one(selector)

    def select(self, selector):
        return self.soup.select(selector)

    def wait_and_find(self, selector, timeout=10, interval=0.5):
        elapsed_time = 0
        element = None
        while elapsed_time < timeout:
            element = self.soup.select_one(selector)
            if element:
                break
            time.sleep(interval)
            elapsed_time += interval
        if not element:
            print(f"Elemento com seletor '{{selector}}' não encontrado em {{timeout}} segundos.")
        return element

    def extract_text(self, tag, attrs=None):
        element = self.find(tag, attrs)
        return element.get_text(strip=True) if element else None

    def get_links(self):
        links = []
        for a_tag in self.soup.find_all("a", href=True):
            links.append(a_tag["href"])
        return links

    def get_images(self):
        images = []
        for img_tag in self.soup.find_all("img", src=True):
            images.append(img_tag["src"])
        return images
"""
        
        criptography = f"""
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import json

class CryptoHelper:
    def __init__(self, password=None, key=None):
        # Inicializa o CryptoHelper com uma senha ou chave para criptografia
        # Se a senha for fornecida, ela será usada para gerar a chave de criptografia
        # Caso contrário, a chave deve ser fornecida diretamente
        # Args: password (str): Senha para gerar a chave (opcional); key (bytes): Chave de criptografia diretamente fornecida (opcional)

        if password:
            self.key = self.generate_key_from_password(password)
        elif key:
            self.key = key
        else:
            raise ValueError("É necessário fornecer uma senha ou chave.")

    def generate_key_from_password(self, password, salt=None):
        # Gera uma chave de criptografia a partir de uma senha, utilizando PBKDF2
        # Args: password (str): Senha para gerar a chave; salt (bytes): Sal (opcional). Se não fornecido, será gerado automaticamente
        # Returns: bytes: A chave gerada

        if salt is None:
            salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    def encrypt(self, data):
        # Criptografa os dados usando AES em modo CBC
        # Args: data (str): Dados a serem criptografados
        # Returns: str: Dados criptografados em base64

        iv = os.urandom(16)  # Vetor de inicialização aleatório
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self.pad(data.encode())
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, encrypted_data):
        # Descriptografa os dados usando AES em modo CBC
        # Args: encrypted_data (str): Dados criptografados em base64
        # Returns: str: Dados descriptografados

        encrypted_data = base64.b64decode(encrypted_data.encode())
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return self.unpad(decrypted_data).decode()

    def pad(self, data):
        # Aplica o padding PKCS7 para que os dados fiquem múltiplos de 16 bytes
        # Args: data (bytes): Dados a serem preenchidos
        # Returns: bytes: Dados com padding aplicado

        pad_length = 16 - len(data) % 16
        return data + bytes([pad_length] * pad_length)

    def unpad(self, data):
        # Remove o padding PKCS7 dos dados
        # Args: data (bytes): Dados com padding
        # Returns: bytes: Dados sem padding

        pad_length = data[-1]
        return data[:-pad_length]

    def save_passwords_to_file(self, password_data, filename="passwords.json"):
        # Salva as senhas criptografadas em um arquivo JSON
        # Args: password_data (dict): Dicionário de senhas a serem salvas; filename (str): Nome do arquivo de destino

        encrypted_passwords = {{key: self.encrypt(value) for key, value in password_data.items()}}
        with open(filename, "w") as file:
            json.dump(encrypted_passwords, file)

    def load_passwords_from_file(self, filename="passwords.json"):
        # Carrega e descriptografa senhas de um arquivo JSON
        # Args: filename (str): Nome do arquivo de onde as senhas serão carregadas
        # Returns: dict: Dicionário de senhas descriptografadas
        
        with open(filename, "r") as file:
            encrypted_passwords = json.load(file)
        return {{key: self.decrypt(value) for key, value in encrypted_passwords.items()}}
"""

        #Trazendo Imps
        if not os.path.exists(utils):    
            os.makedirs(utils)

        imps_dict = {
            os.path.join(utils, "timer.py"): timer,
            os.path.join(utils, "log.py"): log,
            os.path.join(utils, "webscrapping.py"): webscrapping,
            os.path.join(utils, "criptography.py"): criptography
        }
        for imp, script in imps_dict.items():
            try:
                with open(imp, "w") as f:
                    f.write(script)
            except Exception as e:
                print(f'Problema ao criar {imp}: {e}')
        print("Imps chamados")

    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # SKELETONS #
    
    def summon_skeletons(self, nome_robo, caminho_robo, caminho_log):
        caminho_log = os.path.join(caminho_log, nome_robo)
        caminho_robo = os.path.join(caminho_robo, nome_robo)
        
        self.cast_magic(self.skeleton_magic)
            
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

{self.caminho_venvs}\\skeleton\\Scripts\\Activate.bat & python {nome_robo}.py
        """

        #.sh
        skeleton_sh = f"""
#!/bin/bash

export ROBOT_NAME={nome_robo}/
export ROBOT_LOG={caminho_log}/
export INPUTS={caminho_robo}/INPUTS/
export OUTPUTS={caminho_robo}/OUTPUTS/
export LOCAL_PATH={caminho_robo}/LOCAL_ROBOT_FILES/

echo "Variaveis de ambiente OK"

pkill python3
cd {self.caminho_robo}/{nome_robo}/
source {self.caminho_venvs}/skeleton/bin/activate

# Execute o script Python
python3 {nome_robo}.py
        """

        #.py
        skeleton_py = f"""
# coding: ISO-8859-1

import sys
import os
import re
from datetime import datetime
from rich.console import Console
from rich.theme import Theme
from rich.traceback import install
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utilitarios.log import Log
from utilitarios.timer import Timer

###### Console customization ######
install()
custom_theme = Theme({{
    "info": "dim",
    "success": "green",
    "warning": "yellow",
    "error": "red"
}})
console = Console(theme=custom_theme)


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
        console.print(f"Comecando execucao do robo {{__NOME_ROBO}}", style="info")
        breakpoint()

    
        Log.info(f"Finalizando execucao do robo {{__NOME_ROBO}}")
        Log.info(f"{{timer.elapsed}}ms")
        console.print(f"Finalizando execucao do robo {{__NOME_ROBO}}", style="success")
    except Exception as e:
        Log.error(f"Erro no {{__NOME_ROBO}}: " + str(e))
        console.print(f"Erro no {{__NOME_ROBO}}: " + str(e), style="error")
        raise Exception(f"Erro no {{__NOME_ROBO}}")

        

if __name__ == "__main__":
    main()
        """
        
        pastas = [caminho_robo, caminho_log]
        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta, exist_ok=True)
        
        #Criando o .bat, .sh e .py
        skeletons_dict = {
            os.path.join(caminho_robo, f"{nome_robo}.bat"): skeleton_bat,
            os.path.join(caminho_robo, f"{nome_robo}.sh"): skeleton_sh,
            os.path.join(caminho_robo, f"{nome_robo}.py"): skeleton_py,
            # f"{caminho_robo}\\{nome_robo}.bat": skeleton_bat,
            # f"{caminho_robo}/{nome_robo}.sh": skeleton_sh,
            # f"{caminho_robo}\\{nome_robo}.py": skeleton_py
        }

        for skeleton, script in skeletons_dict.items():
            if (skeleton.endswith('.bat') and sys.platform == 'win32') or \
            (skeleton.endswith('.sh') and sys.platform != 'win32') or \
            skeleton.endswith('.py'):
                try:
                    with open(skeleton, "w") as f:
                        f.write(script)
                    if skeleton.endswith('.sh'):
                        # Set execute permissions on the file
                        os.chmod(skeleton, 0o755)
                except Exception as e:
                    print(f"Erro ao criar o arquivo {skeleton}: {e}")


        # Abre as pastas
        # os.startfile(self.caminho_robo)
        # os.startfile(self.caminho_log)

        print(f"Skeleton Sumonado: {nome_robo}")
        

    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # DEMONS #
    def invoke_demons():
        #docker, database, vdis, etc
        pass



    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # GHOULS #  
    def putrefied_ghouls():
        pass             


    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # GOBLINS #  
    def bribe_goblins():
        pass                                           



    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # CAST #  


if __name__ == "__main__":
    #NECROMANCY
    necro = Necromancy()
    
    # Base das pastas e venvs -> venvs = dict{venv: [grimorio]}
    necro.rise_cemetery(necro.caminho_cemiterio, necro.venvs, necro.caminho_venvs, necro.caminho_capelas) 
    # Criar somente venvs -> necro.crypt_polishing
    # venvs = {'skeleto_bard': ['librosa', 'pyaudio', 'audioread'], 'skeleto_druid': ['scikit-image', 'SciPy', 'OpenCV']}
    
    # Scirpts Utilitarios
    necro.IMPerium(necro.caminho_cemiterio) 
    
    # Robos (Skeletons) base
    necro.summon_skeletons('Skeletu', necro.caminho_robo, necro.caminho_log) # Robos
    #breakpoint()

    # necro.invoke_demons() #
    # necro.putrefied_ghouls() #
    # necro.bribe_goblins() #

    print("Reino da Necromancia Finalizado")
    #breakpoint()
        


