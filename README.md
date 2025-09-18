# Necromancy — Pequeno utilitário de scaffolding para robôs

**Descrição**
💀 **Necromancy** é um script Python simples que cria uma "cemitério" de diretórios, virtualenvs e scripts utilitários para você começar projetos/robôs (skeletons). Ele funciona tanto no Windows quanto no Linux e gera exemplos de `.py`, `.sh` e `.bat`, além de utilitários prontos (timer, log, webscrapping, criptography).

**Funcionalidades principais**
- 🪦 Cria estrutura de pastas (`cemiterio/`, `cemiterio/logs/`, `cemiterio/venvs/`).
- 🧙‍♂️ Invoca virtualenvs e instala dependências listadas.
- 📜 Gera **grimórios** utilitários em `cemiterio/utilitarios/` (timer, log, webscrapping, criptography).
- 💀 Conjura skeletons (templates) com arquivos `.py`, `.sh` (Linux) e `.bat` (Windows).
- 😈 Compatível com Windows (usa `Scripts`) e Linux (usa `bin`).

**Requisitos**
- 🐍 Python 3.8+ (recomendado Python 3.11+)
- 📦 módulo `venv` (já incluso na maioria das distribuições)
- `pip` disponível no executável da virtualenv
- 🔑 Permissão para criar pastas em `C:\` (Windows) ou em `/home/<USER>/` (Linux)

> Observação: o arquivo original utiliza codificação `ISO-8859-1`. Se seu ambiente usar UTF-8, converta/edite conforme necessário.

**Como usar (rápido)**
1. Salve o script como `necromancy.py`.
2. Execute:
🐧/🪟
```bash
# Linux
python3 necromancy.py

# Windows (PowerShell ou CMD)
python necromancy.py
```

Ao rodar, por padrão o script criará pastas:
- Windows: `C:\cemiterio\`
- Linux: `/home/<USER>/cemiterio/`

E dentro delas:
- 🧟 `venvs/` — virtualenvs criadas (nomes conforme `self.venvs`)
- 📜 `logs/` — pasta para logs
- 🔮 `utilitarios/` — `timer.py`, `log.py`, `webscrapping.py`, `criptography.py`
- pastas para cada skeleton/robo com `.py`, `.sh` e `.bat` gerados

**Configuração / Personalização**
- Para alterar quais virtualenvs e dependências serão criadas, edite a variável `self.venvs` dentro do `__init__` da classe `Necromancy`.
  ```py
  self.venvs = {
      'skeleton': ['pyautogui', 'psutil', 'rich', 'tqdm'],
      'meu_robo': ['requests', 'beautifulsoup4']
  }
  ```
- Para mudar caminhos padrão, edite `base_caminho` na inicialização (ou altere o código para aceitar parâmetros).

**O que o script gera (exemplos)**
- `cemiterio/utilitarios/timer.py` ⏳
- `cemiterio/utilitarios/log.py` 📜
- `cemiterio/utilitarios/webscrapping.py` 🕷️
- `cemiterio/utilitarios/criptography.py` 🗝️
- `cemiterio/venvs/<venv_name>/` (ambiente virtual) 🧟
- `cemiterio/<nome_robo>/<nome_robo>.py` (template) 💀
- `cemiterio/<nome_robo>/<nome_robo>.sh` (Linux) 🐧
- `cemiterio/<nome_robo>/<nome_robo>.bat` (Windows) 🪟

**Cuidados**
- 👹 O script cria virtualenvs e executa `pip install` dentro delas — execute em ambiente confiável.
- 🛡️ Em Windows, garanta que o executável `python` esteja disponível no PATH.
- Em servidores ou ambientes com restrições, revise os comandos `subprocess.run` antes de executar.
- 🔥 Só invoque em ambientes confiáveis (ou os imps podem escapar).

**Exemplo rápido de personalização**
No final do script você verá:
```py
necro.summon_skeletons('Skeletu', necro.caminho_robo, necro.caminho_log)
```
Troque `'Skeletu'` pelo nome do seu robô para gerar os arquivos de scaffold com esse nome.

**Contribuições**
- Traga novos feitiços ✨
- Melhore a Necromancia -> Abra um PR com melhorias (ex: aceitar argumentos CLI, melhorar logs, adicionar suporte a `pipx`/`poetry`/`uv`).

**Licença**
MIT — sinta-se à vontade para usar / modificar.
Mas cuidado… os mortos sempre voltam. 💀🩸

---
