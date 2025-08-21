# 🔐 Password Generator

[![CustomTkinter](https://img.shields.io/badge/Custom%20Tkinter%20-EEA8AA?style=for-the-badge&logo=python&logoColor=black)](https://customtkinter.tomschimansky.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


<div align="center">
  <img src="examples\dark_theme.jpg" width="1000" alt="Pogodkin Preview">

  *Minimalistic Strong Password Generator*
</div>

## ✨ Features

- 🔒 **Secure password generation** via the Fisher-Yates algorithm
- 🎚️ **Configuring parameters** of generation (length, character types)
- 🌙 **Support for themes** (Light/Dark)
- 📦 **Ready EXE** for Windows

## 🚀 Installation and launch

### Option 1: Ready EXE (for Windows)
1. Download the latest release from [Releases section](https://github.com/zkqw3r/Password-generator/releases)
2. Unzip the folder
3. Run `Parolkin.exe`

### Option 2: From source
```bash
# Clone the repository
git clone https://github.com/zkqw3r/Password-generator.git
cd password-keeper

# Install dependencies
pip install -r requirements.txt

# Run the application
python parolkin.py
```

## 🎨 Themes
### The application supports several color themes to choose from:
 
<div align="center">
  <h1>Standard Themes</h1>
  <img src="examples\greene_color.png" width="500" alt="Pogodkin Preview">

  *Green 🟢 - fresh green theme*
</div>

<div align="center">
  <img src="examples\blue_color.png" width="500" alt="Pogodkin Preview">

  *Blue 🔵 - classic blue theme*
</div>

<div align="center">
  <h1>Custom theme</h1>
  <img src="examples\dark_theme.jpg" width="500" alt="Pogodkin Preview">

  *Purple 🟣 - theme made by me, purple colors used*
</div>

### Changing the color theme:
#### To change the color theme, you need to change the line in Parolkin.py
```bash
CTK.set_default_color_theme("purple.json") # "blue" or "green" or "custom/theme/path.json"
```

## 🎮 Usage
- Select generation options:
- - Password length (12-100 characters)
- - Character types (numbers, letters, special characters)
- Click "Generate" to create a password
- Copy the password
- Use the password in the desired service

## 🛡️ Security
- Module *secrets* for cryptographically secure generation
- Fisher-Yates algorithm for uniform distribution of characters

#### No password saving - only generation and copying

### Dependencies
- customtkinter - modern GUI

- Pillow - image manipulation

- secrets - safe generation (built into Python)

## 🛠️ Compilation to EXE
### If you want to build the EXE yourself:

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Compile to EXE
```bash
pyinstaller -F -w Parolkin.py
```

#### Now you have a ready-made application! 🚀
