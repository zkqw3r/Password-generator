# 🔐 Password Generator

[![CustomTkinter](https://img.shields.io/badge/Custom%20Tkinter%20-EEA8AA?style=for-the-badge&logo=python&logoColor=black)](https://customtkinter.tomschimansky.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


<div align="center">
  <img src="examples\dark_theme.jpg" width="1000" alt="Pogodkin Preview">

  *Minimalistic Strong Password Generator*
</div>

## ✨ Особенности

- 🔒 **Безопасная генерация** паролей через алгоритм Фишера-Йетса
- 🎚️ **Настройка параметров** генерации (длина, типы символов)
- 🌙 **Поддержка тем** (Light/Dark)
- 📦 **Готовый EXE** для Windows

## 🚀 Установка и запуск

### Вариант 1: Готовый EXE (для Windows)
1. Скачайте последний релиз из [Releases section](https://github.com/zkqw3r/Password-generator/releases)
2. Разархивируйте папку
3. Запустите `Parolkin.exe`

### Вариант 2: Из исходного кода
```bash
# Клонируйте репозиторий
git clone https://github.com/zkqw3r/Password-generator.git
cd password-keeper

# Установите зависимости
pip install -r requirements.txt

# Запустите приложение
python parolkin.py
```

## 🎨 Темы оформления
### Приложение поддерживает несколько цветовых тем на выбор:
 
<div align="center">
  <h1>Стандартные темы</h1>
  <img src="examples\greene_color.png" width="500" alt="Pogodkin Preview">

  *Green 🟢 - свежая зеленая тема*
</div>

<div align="center">
  <img src="examples\blue_color.png" width="500" alt="Pogodkin Preview">

  *Blue 🔵 - классическая синяя тема*
</div>

<div align="center">
  <h1>Кастомная тема</h1>
  <img src="examples\dark_theme.jpg" width="500" alt="Pogodkin Preview">

  *Purple 🟣 - тема сделанная мной, используются фиолетовые цвета*
</div>

### Смена цветовой темы:
#### Для смены цветовой темы нужно изменить строку в Parolkin.py
```bash
CTK.set_default_color_theme("purple.json") # "blue" or "green" or "custom/theme/path.json"
```

## 🎮 Использование
- Выберите параметры генерации:
- - Длина пароля (12-100 символов)
- - Типы символов (цифры, буквы, спецсимволы)
- Нажмите "Generate" для создания пароля
- Скопируйте пароль
- Используйте пароль в нужном сервисе

## 🛡️ Безопасность
- Module *secrets* для криптографически безопасной генерации
- Алгоритм Фишера-Йетса для равномерного распределения символов

#### Никакого сохранения паролей - только генерация и копирование

### Зависимости
- customtkinter - современный GUI

- Pillow - работа с изображениями

- secrets - безопасная генерация (встроен в Python)

## 🛠️ Компиляция в EXE
### Если хотите собрать EXE самостоятельно:

#### Установите зависимости
```bash
pip install -r requirements.txt
```

#### Скомпилируйте в EXE
```bash
pyinstaller -F -w Parolkin.py
```

#### Теперь у вас есть готовое приложение! 🚀