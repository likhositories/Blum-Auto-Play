# Blum Auto Play

Blum Auto Play is a Python script that automates the setup and execution of essential tools like Git and Node.js. It is designed to be used in Termux but can also be run in other environments. The script includes a banner, progress bars, and animations to enhance user experience.

## Features
- **Automated Setup**: Installs Git and Node.js if not already installed.
- **Repository Management**: Clones or updates the `blum-tool` repository.
- **Dependency Installation**: Installs necessary dependencies using `npm`.
- **Visual Feedback**: Includes colorful banners, progress bars with percentages, and animations.

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/likhositories/Blum-Auto-Play.git
cd Blum-Auto-Play
```

### 2. Install Python Dependencies
Install the required Python packages:
```bash
pip install colorama tqdm
```

### 3. Run the Script
Run the script using Python:
```bash
python main.py
```

## Requirements
- Python 3.x
- Termux (recommended)
- Git (installed by the script if missing)
- Node.js LTS (installed by the script if missing)

## How It Works
- **Git & Node.js Setup**: Checks for Git and Node.js; installs them if missing.
- **Repository Management**: Clones the `blum-tool` repository or updates it if already cloned.
- **Dependency Installation**: Installs Node.js dependencies using `npm install`.
- **Application Launch**: Starts the application using `node blum.js`.

## Author
- **Likhon Sheikh**
- Telegram: [@likhondotxyz](https://t.me/likhondotxyz)

## License
This project is licensed under the MIT License.
```
