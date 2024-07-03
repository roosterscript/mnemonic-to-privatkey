## mnemonic_to_privatkay


### Описание
Создает privatkey из mnemonic(seed фразы)

---

### Настройка
Указать свои mnemonic(seed фразы) в `mnemoniсs.txt`.
Каждая новая строка - новая seed фраза
Результат запишется в файл `privatkeys.txt`


---
### Запуск

1. Открыть консоль 
2. Перейти в папку скрипта `cd mnemonic_to_privatkey`
3. Создать виртуальное окружение  `python -m venv venv`
4. Активировать виртуальное окружение: 
на macOS и Linux: `source venv/bin/activate`
на Windows: venv\Scripts\activate.bat
5. Установить необходимые пакеты `pip install -r requirements.txt`
6. Запустить скрипт `python main.py`
7. Забрать результат в `privatkeys.txt`

