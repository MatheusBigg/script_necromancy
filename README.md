# ☠️ Necromancy — Small scaffolding utility for bots 🌌

☠️ **Necromancy** is a simple Python script that raises a "graveyard" of directories, virtualenvs and utility scripts for starting projects/bots (skeletons).  
It works on both Windows and Linux and conjures examples of `.py`, `.sh`, and `.bat`, plus pre-baked utilities (timer, log, webscraping, cryptography).

**Main Features**
- 🪦 Creates folder structure (`graveyard/`, `graveyard/logs/`, `graveyard/venvs/`).
- 🧙‍♂️ Summons virtualenvs and installs listed dependencies.
- 📜 Generates **grimoires** under `graveyard/utilities/` (timer, log, webscraping, cryptography).
- 💀 Conjures skeletons (templates) with `.py`, `.sh` (Linux) and `.bat` (Windows).
- 😈 Compatible with Windows (`Scripts`) and Linux (`bin`).

**Requirements**
- 🐍 Python 3.8+ (Python 3.11+ recommended)
- 📦 `venv` module (comes with most distributions)
- 🕸️ `pip` available inside the virtualenv
- 🔑 Permissions to create folders in `C:\` (Windows) or `/home/<USER>/` (Linux)

> Note: the original file uses `ISO-8859-1` encoding. If your environment runs on UTF-8, convert/edit accordingly.

**Quickstart**
1. Save the script as `necromancy.py`.
2. Run:
🐧/🪟
```bash
# Linux
python3 necromancy.py

# Windows (PowerShell or CMD)
python necromancy.py
```

By default, it will create:
- 🪟 Windows: `C:\graveyard\`
- 🐧 Linux: `/home/<USER>/graveyard/`

And inside:
- 🧟 `venvs/` — virtualenvs (names from `self.venvs`)
- 📜 `logs/` — logs folder
- 🔮 `utilities/` — `timer.py`, `log.py`, `webscraping.py`, `cryptography.py`
- Bot skeleton folders with `.py`, `.sh`, `.bat`

**Customization**
- Edit `self.venvs` in the `__init__` of `Necromancy`:
  ```py
  self.venvs = {
      'skeleton': ['pyautogui', 'psutil', 'rich', 'tqdm'],
      'my_bot': ['requests', 'beautifulsoup4']
  }
  ```
- To change default paths, edit `base_caminho` (or patch to accept CLI params).

**What it generates (examples)**
- `graveyard/utilities/timer.py` ⏳
- `graveyard/utilities/log.py` 📜
- `graveyard/utilities/webscraping.py` 🕷️
- `graveyard/utilities/cryptography.py` 🪄
- `graveyard/venvs/<venv_name>/` 🧟
- `graveyard/<bot_name>/<bot_name>.py` 💀
- `graveyard/<bot_name>/<bot_name>.sh` 🐧
- `graveyard/<bot_name>/<bot_name>.bat` 🪟

**Warnings**
- 👹 Creates virtualenvs and runs `pip install` inside them — only invoke in safe realms.
- 🛡️ On Windows, ensure `python` is in PATH.
- 🏰 On servers/restricted envs, review `subprocess.run` before executing.
- 🔥 Never run during a full moon (or imps might actually show up).

**Quick Custom Example**
At the end of the script:
```py
necro.summon_skeletons('Skeletu', necro.caminho_robo, necro.caminho_log)
```
Swap `'Skeletu'` with your bot’s name to conjure scaffold files.

**Contributions**
- 🧪 Bring new spells ⛧°。 ⋆༺♱༻⋆。 °⛧
- Improve **Necromancy** → Open a PR (e.g., add CLI args, better logs, support for `pipx`/`poetry`/`uv`, script spliting).

**License**
MIT — free to use/modify.  
But beware… the dead always return 💀🩸
