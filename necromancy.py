# coding: ISO-8859-1
import os
import sys
import time
import subprocess

                                                            # NECROMANCY # 
class Necromancy():
    def __init__(self):
        #Graveyard Variables
        is_windows = sys.platform.startswith("win")
        linux_username = os.environ.get("USER")
        base_path = "C:\\graveyard\\" if is_windows else f"/home/{linux_username}/graveyard/"
        self.path_graveyard = os.path.join(base_path)
        self.path_chapels = os.path.join(base_path, "logs")
        self.path_venvs = os.path.join(base_path, "venvs")
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
        
        self.graveyard_magic = f"""  
        RISE MY GRAVEYARD, I DEMAND IT!              
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
        self.path_skeleton = f"{self.path_graveyard}"
        self.path_log = f"{self.path_chapels}"
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
        #change from windows to linux \\
        pass

    def transmuting(text):
        #change from windows to linux
        pass

    def crypt_polishing(self, venvs, path_venvs):
        # Identify OS with sys.platform
        is_windows = sys.platform.startswith("win")

        # Config paths and commands based on OS
        python_cmd = "python" if is_windows else "python3"
        script_folder = "Scripts" if is_windows else "bin"
        
        #Creating venvs
        for venv, grimorio in venvs.items():
            crypt = os.path.join(path_venvs, venv)
            try:
                subprocess.run([python_cmd, "-m", "venv", crypt], check=True)
                print(f"crypt created {venv}")
            except subprocess.CalledProcessError as e:
                print(f"Error while creating crypt: {e}")

            #Requirements.txt, activating venv, pip upgrade and dependency installing"
            try:
                requirements_path = os.path.join(crypt, "requirements.txt")
                with open(requirements_path, "w") as f:
                    f.write("\n".join(grimorio))
                
                # Python executable path
                python_executable = os.path.join(crypt, script_folder, "python")
                subprocess.run([python_executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
                subprocess.run([python_executable, "-m", "pip", "install", "-r", requirements_path], check=True)
            except subprocess.CalledProcessError as e:
                    print(f"Error while trying to upgrade pip and dependency installation: {e}")
            print("Upgrade and Dependencies installed")




    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # GRAVEYARD #  
    def rise_graveyard(self, path_graveyard, venvs, path_venvs, path_chapels):
        #Graveyard Rising
        self.cast_magic(self.graveyard_magic)    

        folders = [path_graveyard, path_chapels, path_venvs]
        for folder in folders:  
            if not os.path.exists(folder):    
                os.makedirs(folder, exist_ok=True)
    
        self.crypt_polishing(venvs, path_venvs)


    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

    
                                                            # IMPERIUM #                                                        
    def IMPerium(self, path_graveyard):

        utils = os.path.join(path_graveyard, "utils")
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
                    text = detailsMachine + "Error"
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
            raise ValueError("Non existent browser. Use 'chrome' or 'firefox'.")

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
            print(f"Error while trying to click element: {{e}}")

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
            raise Exception(f"URL Failed to load: {{url}} (Status {{response.status_code}})")

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
            print(f"Element with selector: '{{selector}}' not found in {{timeout}} seconds.")
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
        # Initializes CryptoHelper with password or key for cryptography
        # If Password passed, will be used in cryptography
        # If not, key must be passed directly
        # Args: password (str): Password to generate key (optional); key (bytes): Cryptographed Key directly passed (optional)

        if password:
            self.key = self.generate_key_from_password(password)
        elif key:
            self.key = key
        else:
            raise ValueError("Key or Password necessary.")

    def generate_key_from_password(self, password, salt=None):
        # GGenerates cryptographed key based on a password, using PBKDF2
        # Args: password (str): Password to generate key; salt (bytes): Sal (optional). If not passed, automatically generated
        # Returns: bytes: Generated Key

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
        # Encrypts data using AES in CBC mode
        # Args: data (str): Data to be encrypted
        # Returns: str: Cryptographed data in base64

        iv = os.urandom(16)  # Random Initialization Vector
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self.pad(data.encode())
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, encrypted_data):
        # Decrypts data using AES in CBC mode
        # Args: encrypted_data (str): Encrypted data in base64
        # Returns: str: Decrypted data

        encrypted_data = base64.b64decode(encrypted_data.encode())
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        return self.unpad(decrypted_data).decode()

    def pad(self, data):
        # Applies PKCS7 padding to data
        # Args: data (bytes): Data to be padded
        # Returns: bytes: Data with padding

        pad_length = 16 - len(data) % 16
        return data + bytes([pad_length] * pad_length)

    def unpad(self, data):
        # Removes PKCS7 padding from data
        # Args: data (bytes): Data with padding
        # Returns: bytes: Data without padding

        pad_length = data[-1]
        return data[:-pad_length]

    def save_passwords_to_file(self, password_data, filename="passwords.json"):
        # Saves encrypted passwords to a JSON file
        # Args: password_data (dict): Passwords to be saved; filename (str): Filename of the JSON file

        encrypted_passwords = {{key: self.encrypt(value) for key, value in password_data.items()}}
        with open(filename, "w") as file:
            json.dump(encrypted_passwords, file)

    def load_passwords_from_file(self, filename="passwords.json"):
        # Loads encrypted passwords from a JSON file and decrypts them
        # Args: filename (str): Filename of the JSON file
        # Returns: dict: Decrypted passwords
        
        with open(filename, "r") as file:
            encrypted_passwords = json.load(file)
        return {{key: self.decrypt(value) for key, value in encrypted_passwords.items()}}
"""

        #Rising Imps
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
                print(f'Problem to rise {imp}: {e}')
        print("Imps summoned!")

    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################
    ################################################################################################################################################

                                                            # SKELETONS #
    
    def summon_skeletons(self, name_skeleton, path_skeleton, path_log):
        path_log = os.path.join(path_log, name_skeleton)
        path_skeleton = os.path.join(path_skeleton, name_skeleton)
        
        self.cast_magic(self.skeleton_magic)
            
        #.bat
        skeleton_bat = f"""
@CHCP 1252 > NUL
@echo off

cd {path_skeleton}\\
set PYTHONPATH={path_skeleton}\\

set "SKELETON_NAME={name_skeleton}"
set "SKELETON_LOG={path_log}\\"
set INPUTS={path_skeleton}\\INPUTS\\
set OUTPUTS={path_skeleton}\\OUTPUTS\\
set LOCAL_PATH=C:\\LOCAL_SKELETON_FILES\\{name_skeleton}\\

echo Environment Variables OK

%SystemRoot%\\System32\\taskkill.exe /IM python.exe
REM taskkill /IM python.exe /F

{self.path_venvs}\\skeleton\\Scripts\\Activate.bat & python {name_skeleton}.py
        """

        #.sh
        skeleton_sh = f"""
#!/bin/bash

export SKELETON_NAME={name_skeleton}/
export SKELETON_LOG={path_log}/
export INPUTS={path_skeleton}/INPUTS/
export OUTPUTS={path_skeleton}/OUTPUTS/
export LOCAL_PATH={path_skeleton}/LOCAL_SKELETON_FILES/

echo "Environment Variables OK"

pkill python3
cd {self.path_skeleton}/{name_skeleton}/
source {self.path_venvs}/skeleton/bin/activate

# Execute your Python script
python3 {name_skeleton}.py
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

from utils.log import Log
from utils.timer import Timer

###### Console customization ######
install()
custom_theme = Theme({{
    "info": "dim",
    "success": "green",
    "warning": "yellow",
    "error": "red"
}})
console = Console(theme=custom_theme)


__NAME_SKELETON = os.environ.get("SKELETON_NAME")
__DATA          = datetime.now().strftime("%Y-%m-%d")
__PATH_LOG      = os.environ.get("SKELETON_LOG")
__INPUTS        = os.environ.get("INPUTS")
__OUTPUTS       = os.environ.get("OUTPUTS")
__LOCAL_PATH    = os.environ.get("LOCAL_PATH")

Log(pathLog=__PATH_LOG)

Log.info(f"Criando pastas, configuracoes e verificacoes")
pastas = [__PATH_LOG, __INPUTS, __OUTPUTS, __LOCAL_PATH]
for pasta in pastas:
    if not os.path.exists(pasta):
        os.makedirs(pasta)


        
def main():
    Log.info(f"Skeleton rising {{__NAME_SKELETON}}")
    timer = Timer()
    try:
        console.print(f"Skeleton rising {{__NAME_SKELETON}}", style="info")
        breakpoint()

    
        Log.info(f"Skeleton descending {{__NAME_SKELETON}}")
        Log.info(f"{{timer.elapsed}}ms")
        console.print(f"Skeleton descending {{__NAME_SKELETON}}", style="success")
    except Exception as e:
        Log.error(f"Error with {{__NAME_SKELETON}}: " + str(e))
        console.print(f"Error with {{__NAME_SKELETON}}: " + str(e), style="error")
        raise Exception(f"Error with {{__NAME_SKELETON}}")

        

if __name__ == "__main__":
    main()
        """
        
        pastas = [path_skeleton, path_log]
        for pasta in pastas:
            if not os.path.exists(pasta):
                os.makedirs(pasta, exist_ok=True)
        
        #Criando o .bat, .sh e .py
        skeletons_dict = {
            os.path.join(path_skeleton, f"{name_skeleton}.bat"): skeleton_bat,
            os.path.join(path_skeleton, f"{name_skeleton}.sh"): skeleton_sh,
            os.path.join(path_skeleton, f"{name_skeleton}.py"): skeleton_py,
            # f"{path_skeleton}\\{name_skeleton}.bat": skeleton_bat,
            # f"{path_skeleton}/{name_skeleton}.sh": skeleton_sh,
            # f"{path_skeleton}\\{name_skeleton}.py": skeleton_py
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
                    print(f"Error while creating file {skeleton}: {e}")


        # Abre as pastas
        # os.startfile(self.path_skeleton)
        # os.startfile(self.path_log)

        print(f"Skeleton Sumonado: {name_skeleton}")
        

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
    necro.rise_graveyard(necro.path_graveyard, necro.venvs, necro.path_venvs, necro.path_chapels) 
    # venvs creation only -> necro.crypt_polishing
    # venvs = {'skeleto_bard': ['librosa', 'pyaudio', 'audioread'], 'skeleto_druid': ['scikit-image', 'SciPy', 'OpenCV']}
    
    # Scirpts Utils
    necro.IMPerium(necro.path_graveyard) 
    
    # Skeletons (Bots) base
    necro.summon_skeletons('Skeletu', necro.path_skeleton, necro.path_log)
    #breakpoint()

    # necro.invoke_demons() #
    # necro.putrefied_ghouls() #
    # necro.bribe_goblins() #

    print("Necromancy Kingdom summoned!")
    #breakpoint()
        


