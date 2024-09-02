import os, subprocess, sys, time, webbrowser, shutil, random
from colorama import init, Fore, Back, Style
from tqdm import tqdm

# Initialize Colorama
init(autoreset=True)

# Function to display a banner
def display_banner():
    banner = f"""
{Fore.CYAN}██████╗ ██╗     ██╗   ██╗███╗   ███╗
██╔══██╗██║     ██║   ██║████╗ ████║
██████╔╝██║     ██║   ██║██╔████╔██║
██╔══██╗██║     ██║   ██║██║╚██╔╝██║
██║  ██║███████╗╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝{Style.RESET_ALL}
    """
    print(banner)
    print(f"{Style.BRIGHT}{Fore.YELLOW}Welcome to BLUM Tool!{Style.RESET_ALL}\n")
    print(f"{Style.BRIGHT}{Fore.MAGENTA}Author: Likhon Sheikh")
    print(f"{Style.BRIGHT}{Fore.MAGENTA}Telegram: @likhondotxyz{Style.RESET_ALL}\n")

# Function to install a package using pip
def install_package(package_name):
    print(f"{Fore.CYAN}Installing {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(f"{Fore.GREEN}{package_name} installed successfully!")

# Ensure required packages are installed
try:
    from tqdm import tqdm
except ImportError:
    install_package("tqdm")

try:
    from colorama import init, Fore, Back, Style
except ImportError:
    install_package("colorama")

# Display a progress bar with percentage
def progress_bar(task_name, duration=1):
    print(f"{Fore.CYAN}{task_name} in progress...")
    for i in tqdm(range(100), desc=f"{Fore.MAGENTA}{task_name}", ncols=100, colour='green'):
        time.sleep(duration / 100)
    print(f"{Fore.GREEN}{task_name} completed!")

# Check if Git is installed, install if not
def is_git_installed():
    if shutil.which("git") is None:
        print(f"{Fore.YELLOW}Git is not installed. Installing Git...")
        progress_bar("Installing Git", duration=2)
        subprocess.run(["pkg", "install", "git", "-y"], check=True)
        print(f"{Fore.GREEN}Git installed successfully!")

# Check if Node.js is installed, install if not
def is_nodejs_installed():
    if shutil.which("node") is None:
        print(f"{Fore.YELLOW}Node.js is not installed. Installing Node.js LTS...")
        progress_bar("Installing Node.js LTS", duration=2)
        subprocess.run(["pkg", "install", "nodejs-lts", "-y"], check=True)
        print(f"{Fore.GREEN}Node.js LTS installed successfully!")

# Check if Node.js version is 14 or higher, upgrade if needed
def is_nodejs_version_14_or_higher():
    try:
        node_version = subprocess.check_output(["node", "-v"]).decode("utf-8").strip().lstrip('v')
        major_version = int(node_version.split('.')[0])
        if major_version < 14:
            print(f"{Fore.RED}Node.js version is lower than 14. Upgrading to Node.js LTS...")
            progress_bar("Upgrading Node.js", duration=2)
            subprocess.run(["pkg", "uninstall", "nodejs", "-y"], check=True)
            subprocess.run(["pkg", "install", "nodejs-lts", "-y"], check=True)
            print(f"{Fore.GREEN}Node.js upgraded to LTS successfully!")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to check Node.js version. Ensure Node.js is installed properly.")

# Animated spinning wheel
def spinning_wheel():
    wheel = ['|', '/', '-', '\\']
    for _ in range(20):
        print(f"{Fore.CYAN}{random.choice(wheel)}", end='\r')
        time.sleep(0.1)
    print()

# Open a URL in the default browser
def open_url(url):
    webbrowser.open(url)

# Main application logic
def app():
    display_banner()
    
    is_nodejs_installed()
    is_nodejs_version_14_or_higher()
    is_git_installed()
    
    # Clone or update the repository
    if os.path.isdir("blum-tool"):
        os.chdir("blum-tool")
        print(f"{Fore.CYAN}Checking for updates...")
        progress_bar("Updating blum-tool", duration=1)
        subprocess.run(["git", "pull"], check=True)
    else:
        print(f"{Fore.GREEN}Cloning the repository...")
        progress_bar("Cloning blum-tool", duration=1)
        subprocess.run(["git", "clone", "https://github.com/decryptable/blum", "blum-tool"], check=True)
        os.chdir("blum-tool")
        print(f"{Fore.CYAN}Installing dependencies...")
        progress_bar("Installing dependencies", duration=1)
        subprocess.run(["npm", "install"], check=True)
    
    print(f"{Fore.MAGENTA}Starting the application...")
    spinning_wheel()
    subprocess.run(["node", os.path.join(os.getcwd(), "blum.js")])

    # Open the URLs in the default browser
    open_url("https://t.me/likhondotxyz")
    open_url("https://t.me/ProfitableRewards")

    # Author attribution
    print(f"{Style.BRIGHT}{Fore.YELLOW}\nAuthor: Likhon Sheikh\nTelegram: @rtx_likhon")

if __name__ == "__main__":
    app()
