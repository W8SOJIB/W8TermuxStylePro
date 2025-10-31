#!/usr/bin/env python3
"""
Elite Hacker Terminal Generator
Creates a custom stylish terminal with your name!
"""

import os
import sys
import subprocess
from datetime import datetime

# ANSI Colors for Python output
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    DARKGRAY = '\033[1;30m'
    GRAY = '\033[0;37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_ascii_art(text):
    """Generate ASCII art from text using pyfiglet or fallback"""
    try:
        import pyfiglet
        return pyfiglet.figlet_format(text, font='standard')
    except ImportError:
        # Fallback: Simple ASCII art generator
        return generate_simple_ascii(text)

def generate_simple_ascii(text):
    """Fallback ASCII art generator"""
    art = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║              {text.upper().center(43)}              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """
    return art

def print_banner():
    """Print the welcome banner"""
    clear_screen()
    print(f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              W8TERMUXSTYLEPRO - GENERATOR v3.0                ║
║                                                               ║
║            Create Your Custom Cyberpunk Terminal              ║
║                                                               ║
║          {Colors.GRAY}Credits: W8Team/W8SOJIB{Colors.CYAN}                             ║
║    {Colors.GRAY}GitHub: github.com/W8SOJIB/W8TermuxStylePro{Colors.CYAN}             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}
""")

def get_all_styles():
    """Return all 100 terminal styles"""
    return [
        # Original 20 styles
        ("1", "Standard", "Clean & Professional", "╰─➤", "GREEN"),
        ("2", "Advanced", "Maximum Effects", "┗━╼", "CYAN"),
        ("3", "Matrix", "Green Code Rain", "└──>", "GREEN"),
        ("4", "Neon Cyber", "Vibrant Neon Colors", "▶", "MAGENTA"),
        ("5", "Red Alert", "Red Hacker Theme", "⚠>", "RED"),
        ("6", "Ghost Protocol", "Stealth Mode", "»", "DARKGRAY"),
        ("7", "Dark Hacker", "Dark Minimalist", "→", "WHITE"),
        ("8", "Green Terminal", "Classic Green", "$", "GREEN"),
        ("9", "Blue Steel", "Cool Blue Theme", "►", "BLUE"),
        ("10", "Purple Haze", "Purple Aesthetic", "⟩", "MAGENTA"),
        
        # 10-20
        ("11", "Minimal", "Ultra Clean", ">", "WHITE"),
        ("12", "Retro DOS", "Old School DOS", "C:\\>", "YELLOW"),
        ("13", "Cyberpunk", "Cyberpunk 2077", "//»", "YELLOW"),
        ("14", "Anonymous", "Anonymous Style", "#>", "WHITE"),
        ("15", "Mr Robot", "fsociety Theme", "[!]>", "RED"),
        ("16", "Tron", "Tron Legacy", "◢◤>", "CYAN"),
        ("17", "Watchdogs", "ctOS Theme", "▰▰>", "BLUE"),
        ("18", "Black Hat", "Dark Ops", "●>", "RED"),
        ("19", "White Hat", "Security Pro", "○>", "GREEN"),
        ("20", "Elite", "Ultimate Hacker", "⟫", "CYAN"),
        
        # 21-40 - Movie/TV Inspired
        ("21", "Blade Runner", "Dystopian Future", "⟩⟩", "YELLOW"),
        ("22", "Ghost Shell", "Cybernetic", "◉>", "CYAN"),
        ("23", "Akira", "Neo Tokyo", "⚡>", "RED"),
        ("24", "Neuromancer", "Cyberspace", "▣>", "BLUE"),
        ("25", "Snow Crash", "Metaverse", "◈>", "WHITE"),
        ("26", "Black Mirror", "Dark Tech", "▼>", "DARKGRAY"),
        ("27", "Westworld", "AI Maze", "◇>", "YELLOW"),
        ("28", "Person Interest", "Machine", "⊡>", "BLUE"),
        ("29", "Halt Catch Fire", "Retro Tech", "⊚>", "GREEN"),
        ("30", "Silicon Valley", "Startup", "◐>", "CYAN"),
        
        # 31-50 - Game Inspired
        ("31", "Deus Ex", "Augmented", "⟐>", "YELLOW"),
        ("32", "System Shock", "SHODAN", "⟁>", "RED"),
        ("33", "Uplink", "Hacker Sim", "⊿>", "GREEN"),
        ("34", "Hacknet", "Terminal Game", "∴>", "CYAN"),
        ("35", "Shadowrun", "Cyberpunk RPG", "⬡>", "MAGENTA"),
        ("36", "Syndicate", "Corporate", "⬢>", "BLUE"),
        ("37", "Transistor", "Processing", "◬>", "RED"),
        ("38", "Observer", "Neural", "⊗>", "DARKGRAY"),
        ("39", "Ruiner", "Combat", "⊕>", "RED"),
        ("40", "Ghostrunner", "Cyber Ninja", "⟐", "CYAN"),
        
        # 41-60 - Tech Companies
        ("41", "Apple", "Think Different", "→", "WHITE"),
        ("42", "Google", "Colorful", "G>", "BLUE"),
        ("43", "Microsoft", "Azure", "⊞>", "BLUE"),
        ("44", "IBM", "Big Blue", "◈>", "BLUE"),
        ("45", "Oracle", "Database", "○>", "RED"),
        ("46", "Tesla", "Electric", "⚡>", "RED"),
        ("47", "SpaceX", "Rocket", "▲>", "WHITE"),
        ("48", "NASA", "Space", "★>", "BLUE"),
        ("49", "MIT", "Innovation", "∞>", "RED"),
        ("50", "CERN", "Particle", "◉>", "BLUE"),
        
        # 51-70 - Programming Languages
        ("51", "Python", "Simple Power", ">>>", "GREEN"),
        ("52", "JavaScript", "Web Power", "=>", "YELLOW"),
        ("53", "C++", "Performance", "::>", "BLUE"),
        ("54", "Rust", "Memory Safe", "|>", "RED"),
        ("55", "Go", "Concurrent", "go>", "CYAN"),
        ("56", "Ruby", "Elegant", "♦>", "RED"),
        ("57", "PHP", "Web Classic", "?>", "MAGENTA"),
        ("58", "Java", "Enterprise", "☕>", "RED"),
        ("59", "Swift", "iOS Native", "⚡>", "YELLOW"),
        ("60", "Kotlin", "Modern JVM", "K>", "MAGENTA"),
        
        # 61-80 - Hacker Terms
        ("62", "Root Access", "Full Control", "#>", "RED"),
        ("63", "Shell", "Command Line", "$>", "GREEN"),
        ("64", "Kernel", "Core System", "⊚>", "YELLOW"),
        ("65", "Daemon", "Background", "⊗>", "DARKGRAY"),
        ("66", "Firewall", "Protection", "⚠>", "RED"),
        ("67", "Exploit", "Vulnerability", "⚡>", "RED"),
        ("68", "Payload", "Code Inject", "◉>", "YELLOW"),
        ("69", "Backdoor", "Hidden Access", "◐>", "DARKGRAY"),
        ("70", "Crypter", "Encryption", "⊕>", "CYAN"),
        ("61", "Sudo", "Super User", "sudo>", "RED"),
        
        # 71-90 - OS/Distros
        ("71", "Kali Linux", "Pen Testing", "⟩>", "BLUE"),
        ("72", "Parrot OS", "Security", "🦜>", "CYAN"),
        ("73", "Ubuntu", "Humanity", "○>", "YELLOW"),
        ("74", "Arch", "I Use Arch", "▲>", "CYAN"),
        ("75", "Debian", "Stable", "◈>", "RED"),
        ("76", "Fedora", "Leading Edge", "∞>", "BLUE"),
        ("77", "CentOS", "Enterprise", "⊡>", "GREEN"),
        ("78", "Alpine", "Minimal", "⟩", "BLUE"),
        ("79", "Gentoo", "Compile", "∴>", "MAGENTA"),
        ("80", "BSD", "Berkeley", "◉>", "RED"),
        
        # 91-100 - Cyber Terms
        ("81", "Zero Day", "Unknown Vuln", "0>", "RED"),
        ("82", "DDoS", "Flood Attack", "▰▰▰>", "RED"),
        ("83", "Phishing", "Social Eng", "⚓>", "YELLOW"),
        ("84", "Ransomware", "Crypto Lock", "🔒>", "RED"),
        ("85", "Botnet", "Zombie Army", "⊚⊚>", "DARKGRAY"),
        ("86", "Malware", "Evil Code", "⚠⚠>", "RED"),
        ("87", "Trojan", "Hidden Threat", "🐴>", "YELLOW"),
        ("88", "Rootkit", "Deep Hide", "⊗>", "DARKGRAY"),
        ("89", "Keylogger", "Key Capture", "⌨>", "CYAN"),
        ("90", "RAT", "Remote Control", "🐀>", "RED"),
        ("91", "SQL Inject", "DB Attack", "';>", "BLUE"),
        ("92", "XSS", "Script Inject", "<>", "YELLOW"),
        ("93", "CSRF", "Cross-Site", "⟳>", "RED"),
        ("94", "Brute Force", "Try All", "###>", "RED"),
        ("95", "Dictionary", "Word List", "📖>", "GREEN"),
        ("96", "Rainbow Table", "Hash Crack", "🌈>", "MAGENTA"),
        ("97", "Man Middle", "Intercept", "↔>", "YELLOW"),
        ("98", "Sniffing", "Packet Capture", "👃>", "CYAN"),
        ("99", "Spoofing", "Fake Identity", "🎭>", "WHITE"),
        ("100", "Steganography", "Hidden Data", "🖼>", "BLUE"),
        ("101", "Remove", "Uninstall Terminal", "", "RED"),
    ]

def get_user_input():
    """Get user's name and preferences"""
    # First, ask for option
    print(f"{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║           SELECT YOUR HACKER TERMINAL STYLE (1-100)          ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    styles = get_all_styles()
    
    # Display in 2 columns
    mid = len(styles) // 2
    for i in range(mid):
        left = styles[i]
        right = styles[i + mid] if i + mid < len(styles) else None
        
        left_num, left_name, left_desc, left_symbol, left_color = left
        left_color_obj = getattr(Colors, left_color, Colors.WHITE)
        
        if left_num == "101":
            print(f"\n{Colors.RED}  [{left_num}] {left_name:<15} - {left_desc}{Colors.RESET}")
        else:
            left_str = f"{Colors.GREEN}[{left_num.rjust(3)}]{Colors.RESET} {Colors.WHITE}{left_name:<15}{Colors.RESET} {left_color_obj}{left_symbol:<8}{Colors.RESET}"
            
            if right:
                right_num, right_name, right_desc, right_symbol, right_color = right
                right_color_obj = getattr(Colors, right_color, Colors.WHITE)
                right_str = f"{Colors.GREEN}[{right_num.rjust(3)}]{Colors.RESET} {Colors.WHITE}{right_name:<15}{Colors.RESET} {right_color_obj}{right_symbol:<8}{Colors.RESET}"
                print(f"  {left_str}  {right_str}")
            else:
                print(f"  {left_str}")
    
    while True:
        style = input(f"\n{Colors.CYAN}▸ Select style [1-101]: {Colors.RESET}").strip()
        if style in [str(i) for i in range(1, 102)]:
            break
        print(f"{Colors.RED}✗ Please enter a number between 1-101{Colors.RESET}")
    
    # If removing, skip name and color
    if style == '101':
        return None, style, None
    
    # Ask for name
    print(f"\n{Colors.YELLOW}Enter your details:{Colors.RESET}\n")
    while True:
        name = input(f"{Colors.GREEN}▸ Enter your name/handle: {Colors.RESET}").strip()
        if name:
            break
        print(f"{Colors.RED}✗ Name cannot be empty!{Colors.RESET}")
    
    # Ask for color customization
    print(f"\n{Colors.CYAN}Choose your color scheme:{Colors.RESET}\n")
    print(f"  {Colors.GREEN}[1]{Colors.RESET} {Colors.GREEN}Green{Colors.RESET}    - Classic Hacker")
    print(f"  {Colors.RED}[2]{Colors.RESET} {Colors.RED}Red{Colors.RESET}      - Alert/Danger")
    print(f"  {Colors.BLUE}[3]{Colors.RESET} {Colors.BLUE}Blue{Colors.RESET}     - Cool/Tech")
    print(f"  {Colors.CYAN}[4]{Colors.RESET} {Colors.CYAN}Cyan{Colors.RESET}     - Matrix Style")
    print(f"  {Colors.MAGENTA}[5]{Colors.RESET} {Colors.MAGENTA}Magenta{Colors.RESET}  - Neon/Purple")
    print(f"  {Colors.YELLOW}[6]{Colors.RESET} {Colors.YELLOW}Yellow{Colors.RESET}   - Bright/Warning")
    print(f"  {Colors.WHITE}[7]{Colors.RESET} {Colors.WHITE}White{Colors.RESET}    - Clean/Minimal")
    print(f"  {Colors.GRAY}[8]{Colors.RESET} {Colors.DARKGRAY}Gray{Colors.RESET}     - Dark/Stealth")
    print(f"  {Colors.WHITE}[9]{Colors.RESET} Default  - Use style's color")
    
    while True:
        color_choice = input(f"\n{Colors.GREEN}▸ Select color [1-9]: {Colors.RESET}").strip()
        if color_choice in [str(i) for i in range(1, 10)]:
            break
        print(f"{Colors.RED}✗ Please enter a number between 1-9{Colors.RESET}")
    
    color_map = {
        '1': 'GREEN', '2': 'RED', '3': 'BLUE', '4': 'CYAN',
        '5': 'MAGENTA', '6': 'YELLOW', '7': 'WHITE', '8': 'DARKGRAY', '9': None
    }
    
    custom_color = color_map.get(color_choice)
    
    return name, style, custom_color

def create_welcome_script(name, ascii_art):
    """Create the standard welcome script"""
    script_content = f'''#!/bin/bash

# Elite Terminal - {name}
# Standard Version

# Colors
RED='\\033[1;31m'
GREEN='\\033[1;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[1;34m'
MAGENTA='\\033[1;35m'
CYAN='\\033[1;36m'
WHITE='\\033[1;37m'
GRAY='\\033[0;37m'
RESET='\\033[0m'

clear

# Top border
echo -e "${{CYAN}}╔═══════════════════════════════════════════════════════════════════════╗${{RESET}}"

# ASCII Art Banner
echo -e "${{GREEN}}${{BOLD}}"
cat << 'BANNER'
{ascii_art}
BANNER
echo -e "${{RESET}}"

# Subtitle
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"
echo -e "${{YELLOW}}               ▰▰▰ ${{WHITE}}ELITE CYBER TERMINAL${{YELLOW}} ▰▰▰${{RESET}}"
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

# System Info
echo -e "${{MAGENTA}}┌─[${{GREEN}}SYSTEM INFO${{MAGENTA}}]${{RESET}}"
echo -e "${{MAGENTA}}│${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Operator    ${{WHITE}}:${{GREEN}} {name}${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}User        ${{WHITE}}:${{GREEN}} $(whoami)${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Hostname    ${{WHITE}}:${{GREEN}} $(hostname)${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Shell       ${{WHITE}}:${{GREEN}} $SHELL${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Date        ${{WHITE}}:${{GREEN}} $(date '+%d %B %Y')${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Time        ${{WHITE}}:${{GREEN}} $(date '+%H:%M:%S %Z')${{RESET}}"

# Platform detection
if [ -d "/data/data/com.termux" ]; then
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Platform    ${{WHITE}}:${{GREEN}} Termux (Android)${{RESET}}"
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Storage     ${{WHITE}}:${{GREEN}} $(df -h /data | tail -1 | awk '{{print $4}}') Free${{RESET}}"
else
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Platform    ${{WHITE}}:${{GREEN}} $(uname -s)${{RESET}}"
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Kernel      ${{WHITE}}:${{GREEN}} $(uname -r)${{RESET}}"
fi

echo -e "${{MAGENTA}}└──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Status      ${{WHITE}}:${{GREEN}} ✓ READY${{RESET}}"

# Separator
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

# Quotes
quotes=(
    "The quieter you become, the more you can hear..."
    "In a world of locked rooms, the person with the key is king."
    "Code is poetry written in logic."
    "Access granted. Welcome back, operator."
    "Every system has vulnerabilities. Every lock has a key."
    "Think like a hacker, act like a guardian."
    "The best way to predict the future is to create it."
    "Knowledge is power. But wisdom is knowing how to use it."
)

random_quote=${{quotes[$RANDOM % ${{#quotes[@]}}]}}
echo -e "${{YELLOW}}   » ${{WHITE}}$random_quote${{RESET}}"

# Bottom border
echo -e "${{CYAN}}╚═══════════════════════════════════════════════════════════════════════╝${{RESET}}"

echo ""
echo -e "${{RED}}[${{GREEN}}✓${{RED}}]${{CYAN}} System initialized and ready...${{RESET}}"
echo ""

# Loading bar
echo -ne "${{GREEN}}[${{RESET}}"
for i in {{1..50}}; do
    echo -ne "${{GREEN}}═${{RESET}}"
    sleep 0.01
done
echo -e "${{GREEN}}]${{WHITE}} 100%${{RESET}}"
echo ""

# Set custom PS1 prompt permanently
export PS1="${{RED}}╭─${{GREEN}}[${{CYAN}}{name}${{GREEN}}@${{MAGENTA}}terminal${{GREEN}}]${{RED}}─${{YELLOW}}[${{WHITE}}\\w${{YELLOW}}]${{RESET}}\\n${{RED}}╰─${{BLUE}}➤${{RESET}} "
'''
    
    with open('welcome.sh', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    os.chmod('welcome.sh', 0o755)

def create_advanced_script(name, ascii_art):
    """Create the advanced welcome script"""
    script_content = f'''#!/bin/bash

# Elite Terminal - {name}
# Advanced Version with Maximum Effects

# Colors
RED='\\033[1;31m'
GREEN='\\033[1;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[1;34m'
MAGENTA='\\033[1;35m'
CYAN='\\033[1;36m'
WHITE='\\033[1;37m'
GRAY='\\033[0;37m'
DARKGRAY='\\033[1;30m'
RESET='\\033[0m'
BOLD='\\033[1m'

clear

# Initialize
echo -e "${{GREEN}}> Initializing secure connection...${{RESET}}"
sleep 0.3
echo -e "${{GREEN}}> Loading encryption modules...${{RESET}}"
sleep 0.2
echo -e "${{GREEN}}> Establishing neural link...${{RESET}}"
sleep 0.2
echo -e "${{CYAN}}> Connection established.${{RESET}}"
sleep 0.3
clear

# Top border
echo -e "${{CYAN}}╔═══════════════════════════════════════════════════════════════════════╗${{RESET}}"

# Main ASCII Banner
echo -e "${{GREEN}}${{BOLD}}"
cat << 'BANNER'
{ascii_art}
BANNER
echo -e "${{RESET}}"

# Subtitle
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"
echo -e "${{RED}}           ⟨⟨⟨ ${{WHITE}}${{BOLD}}QUANTUM CYBER OPERATIONS TERMINAL${{RED}} ⟩⟩⟩${{RESET}}"
echo -e "${{DARKGRAY}}                    [${{YELLOW}} CLEARANCE LEVEL: ${{GREEN}}OMEGA ${{DARKGRAY}}]${{RESET}}"
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

# Access granted message
echo -e "${{GREEN}}${{BOLD}}"
echo "    ██████╗  ██████╗ ██████╗███████╗███████╗███████╗"
echo "   ██╔════╝ ██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝"
echo "   ███████╗ ██║     ██║     █████╗  ███████╗███████╗"
echo "   ██╔═══██╗██║     ██║     ██╔══╝  ╚════██║╚════██║"
echo "   ╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║"
echo "    ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝"
echo -e "${{YELLOW}}"
echo "            ██████╗ ██████╗  ██████╗ ███╗   ██╗████████╗███████╗██████╗ "
echo "           ██╔════╝ ██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝██╔════╝██╔══██╗"
echo "           ██║  ███╗██████╔╝███████║██╔██╗ ██║   ██║   █████╗  ██║  ██║"
echo "           ██║   ██║██╔══██╗██╔══██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║"
echo "           ╚██████╔╝██║  ██║██║  ██║██║ ╚████║   ██║   ███████╗██████╔╝"
echo "            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝ "
echo -e "${{RESET}}"

sleep 0.2

# System Intelligence Panel
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"
echo -e "${{MAGENTA}}╔═══╡${{WHITE}}${{BOLD}} SYSTEM INTELLIGENCE ${{MAGENTA}}╞═══════════════════════════════════════════╗${{RESET}}"
echo -e "${{MAGENTA}}║${{RESET}}"

CURRENT_USER=$(whoami)
CURRENT_HOST=$(hostname)
CURRENT_SHELL=$(basename "$SHELL")
CURRENT_DATE=$(date '+%d %B %Y')
CURRENT_TIME=$(date '+%H:%M:%S')
UPTIME_INFO=$(uptime -p 2>/dev/null || echo "Unknown")

echo -e "${{MAGENTA}}║  ${{CYAN}}┌─${{RED}}[${{WHITE}}OPERATOR PROFILE${{RED}}]${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} HANDLE      ${{DARKGRAY}}::${{GREEN}} {name}${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} USERNAME    ${{DARKGRAY}}::${{GREEN}} $CURRENT_USER${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} HOSTNAME    ${{DARKGRAY}}::${{GREEN}} $CURRENT_HOST${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}└──➤${{YELLOW}} SHELL       ${{DARKGRAY}}::${{GREEN}} $CURRENT_SHELL${{RESET}}"
echo -e "${{MAGENTA}}║${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}┌─${{RED}}[${{WHITE}}TEMPORAL COORDINATES${{RED}}]${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} DATE        ${{DARKGRAY}}::${{GREEN}} $CURRENT_DATE${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} TIME        ${{DARKGRAY}}::${{GREEN}} $CURRENT_TIME${{RESET}}"
echo -e "${{MAGENTA}}║  ${{CYAN}}└──➤${{YELLOW}} UPTIME      ${{DARKGRAY}}::${{GREEN}} $UPTIME_INFO${{RESET}}"
echo -e "${{MAGENTA}}║${{RESET}}"

# Platform detection
if [ -d "/data/data/com.termux" ]; then
    PLATFORM="TERMUX [ANDROID]"
    STORAGE=$(df -h /data | tail -1 | awk '{{print $4}}')
    echo -e "${{MAGENTA}}║  ${{CYAN}}┌─${{RED}}[${{WHITE}}SYSTEM ARCHITECTURE${{RED}}]${{RESET}}"
    echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} PLATFORM    ${{DARKGRAY}}::${{GREEN}} $PLATFORM${{RESET}}"
    echo -e "${{MAGENTA}}║  ${{CYAN}}└──➤${{YELLOW}} STORAGE     ${{DARKGRAY}}::${{GREEN}} $STORAGE FREE${{RESET}}"
else
    PLATFORM=$(uname -s)
    KERNEL=$(uname -r)
    echo -e "${{MAGENTA}}║  ${{CYAN}}┌─${{RED}}[${{WHITE}}SYSTEM ARCHITECTURE${{RED}}]${{RESET}}"
    echo -e "${{MAGENTA}}║  ${{CYAN}}├──➤${{YELLOW}} PLATFORM    ${{DARKGRAY}}::${{GREEN}} $PLATFORM${{RESET}}"
    echo -e "${{MAGENTA}}║  ${{CYAN}}└──➤${{YELLOW}} KERNEL      ${{DARKGRAY}}::${{GREEN}} $KERNEL${{RESET}}"
fi

echo -e "${{MAGENTA}}║${{RESET}}"
echo -e "${{MAGENTA}}║  ${{GREEN}}█▓▒░${{WHITE}} STATUS: ${{GREEN}}${{BOLD}}OPERATIONAL${{RESET}} ${{GREEN}}░▒▓█${{RESET}}"
echo -e "${{MAGENTA}}╚═══════════════════════════════════════════════════════════════════════╝${{RESET}}"

# Security
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"
echo -e "${{RED}}[${{YELLOW}}!${{RED}}]${{GRAY}} Security Protocols: ${{GREEN}}ENABLED${{RESET}}"
echo -e "${{RED}}[${{YELLOW}}!${{RED}}]${{GRAY}} Encryption Level: ${{GREEN}}AES-256${{RESET}}"
echo -e "${{RED}}[${{YELLOW}}!${{RED}}]${{GRAY}} Neural Interface: ${{GREEN}}SYNCHRONIZED${{RESET}}"

# Quotes
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

quotes=(
    "The matrix is everywhere. It is all around us..."
    "Welcome to the real world."
    "There is no spoon."
    "The quieter you become, the more you can hear."
    "In a world of locked rooms, the person with the key is king."
    "Access is power. Knowledge is freedom."
    "Every system has vulnerabilities waiting to be discovered."
)

random_quote=${{quotes[$RANDOM % ${{#quotes[@]}}]}}
echo -e "${{DARKGRAY}}┌─${{RESET}}"
echo -e "${{DARKGRAY}}│${{YELLOW}}  ▸ ${{WHITE}}$random_quote${{RESET}}"
echo -e "${{DARKGRAY}}└─${{RESET}}"

# Bottom border
echo -e "${{CYAN}}╚═══════════════════════════════════════════════════════════════════════╝${{RESET}}"
echo ""

# Status
echo -e "${{GREEN}}[${{WHITE}}✓${{GREEN}}]${{CYAN}} Neural link established    ${{GREEN}}[${{WHITE}}✓${{GREEN}}]${{CYAN}} All systems operational${{RESET}}"
echo -e "${{GREEN}}[${{WHITE}}✓${{GREEN}}]${{CYAN}} Firewall active           ${{GREEN}}[${{WHITE}}✓${{GREEN}}]${{CYAN}} Encryption enabled${{RESET}}"
echo ""

# Loading
echo -e "${{YELLOW}}▸ Loading command interface...${{RESET}}"
echo -ne "${{DARKGRAY}}["
for i in {{1..50}}; do
    if [ $i -le 10 ]; then
        echo -ne "${{RED}}█"
    elif [ $i -le 25 ]; then
        echo -ne "${{YELLOW}}█"
    else
        echo -ne "${{GREEN}}█"
    fi
    sleep 0.01
done
echo -e "${{DARKGRAY}}]${{WHITE}} 100% ${{GREEN}}COMPLETE${{RESET}}"
echo ""

# Set custom PS1 prompt permanently
export PS1="${{RED}}┏━${{GREEN}}[${{CYAN}}${{BOLD}}{name}${{GREEN}}${{RESET}}${{GREEN}}@${{MAGENTA}}CYBER-OPS${{GREEN}}]${{RED}}━${{YELLOW}}[${{WHITE}}\\w${{YELLOW}}]${{RESET}}\\n${{RED}}┗━${{BLUE}}╼${{RESET}} "
'''
    
    with open('welcome_advanced.sh', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    os.chmod('welcome_advanced.sh', 0o755)

def create_launcher(name, has_standard, has_advanced):
    """Create launcher script"""
    script_content = f'''#!/bin/bash

# {name} Terminal Launcher

clear

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║               {name.upper()} TERMINAL LAUNCHER                "
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Select your terminal:"
echo ""
'''

    option_num = 1
    if has_standard:
        script_content += f'''
echo "  [{option_num}] Standard Style"
echo "      - Clean and fast"
echo ""
'''
        option_num += 1
    
    if has_advanced:
        script_content += f'''
echo "  [{option_num}] Advanced Cyber Ops Style"
echo "      - Maximum effects"
echo ""
'''
        option_num += 1
    
    script_content += f'''
echo "  [0] Exit"
echo ""
echo -n "Enter your choice: "
read choice

case $choice in
'''
    
    option_num = 1
    if has_standard:
        script_content += f'''
    {option_num})
        echo ""
        echo "Loading Standard Style..."
        sleep 0.3
        ./welcome.sh
        ;;
'''
        option_num += 1
    
    if has_advanced:
        script_content += f'''
    {option_num})
        echo ""
        echo "Loading Advanced Style..."
        sleep 0.3
        ./welcome_advanced.sh
        ;;
'''
    
    script_content += '''
    0)
        echo ""
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo ""
        echo "Invalid choice!"
        exit 1
        ;;
esac
'''
    
    with open('launcher.sh', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    os.chmod('launcher.sh', 0o755)

def setup_auto_startup(script_name):
    """Setup auto-startup by adding to .bashrc with auto-fix"""
    bashrc_path = os.path.expanduser("~/.bashrc")
    script_path = os.path.join(os.getcwd(), script_name)
    
    try:
        # Backup .bashrc first
        if os.path.exists(bashrc_path):
            import shutil
            shutil.copy(bashrc_path, bashrc_path + '.backup_auto')
        
        # Read current .bashrc
        existing_content = ""
        if os.path.exists(bashrc_path):
            with open(bashrc_path, 'r') as f:
                existing_content = f.read()
        
        # Auto-fix: Remove old entries (with or without 'source')
        if 'welcome.sh' in existing_content or 'welcome_advanced.sh' in existing_content or 'Terminal Auto-Start' in existing_content:
            print(f"{Colors.YELLOW}  ⚠ Detected old installation - Auto-fixing...{Colors.RESET}")
            
            lines = existing_content.split('\n')
            new_lines = []
            skip_next = False
            
            for line in lines:
                # Skip comment line
                if 'Terminal Auto-Start' in line or 'WELCOME Terminal Auto-Start' in line:
                    skip_next = True
                    continue
                # Skip the actual script line
                if skip_next and ('welcome.sh' in line or 'welcome_advanced.sh' in line):
                    skip_next = False
                    continue
                new_lines.append(line)
            
            # Write cleaned content
            with open(bashrc_path, 'w') as f:
                f.write('\n'.join(new_lines))
            
            print(f"{Colors.GREEN}  ✓ Cleaned old entries{Colors.RESET}")
        
        # Add new entry with source command (important for PS1 to persist!)
        with open(bashrc_path, 'a') as f:
            f.write(f"\n# {script_name.replace('.sh', '').upper()} Terminal Auto-Start\n")
            f.write(f"source {script_path}\n")
        
        print(f"{Colors.GREEN}  ✓ Added to startup (.bashrc) with 'source'{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}  ✗ Could not add to startup: {e}{Colors.RESET}")
        return False

def remove_terminal():
    """Remove terminal files and startup entries - restore normal Termux prompt"""
    print(f"\n{Colors.YELLOW}Removing Stylish Terminal...{Colors.RESET}\n")
    
    files_to_remove = ['welcome.sh', 'welcome_advanced.sh', 'launcher.sh', 'README.md']
    removed_count = 0
    
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"{Colors.GREEN}  ✓ Removed {file}{Colors.RESET}")
                removed_count += 1
            except Exception as e:
                print(f"{Colors.RED}  ✗ Could not remove {file}: {e}{Colors.RESET}")
    
    # Remove from .bashrc and restore normal prompt
    bashrc_path = os.path.expanduser("~/.bashrc")
    if os.path.exists(bashrc_path):
        try:
            # Backup before modifying
            import shutil
            shutil.copy(bashrc_path, bashrc_path + '.backup_remove')
            
            with open(bashrc_path, 'r') as f:
                lines = f.readlines()
            
            with open(bashrc_path, 'w') as f:
                skip_next = False
                removed_startup = False
                
                for line in lines:
                    # Skip Terminal Auto-Start comment
                    if 'Terminal Auto-Start' in line or 'WELCOME Terminal Auto-Start' in line:
                        skip_next = True
                        continue
                    
                    # Skip the source/script line
                    if skip_next and ('welcome.sh' in line or 'welcome_advanced.sh' in line or 'source' in line):
                        skip_next = False
                        removed_startup = True
                        continue
                    
                    f.write(line)
                
                if removed_startup:
                    print(f"{Colors.GREEN}  ✓ Removed from startup (.bashrc){Colors.RESET}")
                    print(f"{Colors.GREEN}  ✓ Restored normal Termux prompt{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}  ⚠ Could not clean .bashrc: {e}{Colors.RESET}")
    
    if removed_count > 0:
        print(f"\n{Colors.GREEN}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                                                               ║")
        print(f"║                  ✓ REMOVAL COMPLETE!                          ║")
        print(f"║                                                               ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
        print(f"{Colors.CYAN}Successfully removed {removed_count} file(s){Colors.RESET}")
        print(f"{Colors.YELLOW}Your terminal will return to normal Termux prompt{Colors.RESET}")
        print(f"\n{Colors.WHITE}To apply changes:{Colors.RESET}")
        print(f"  {Colors.CYAN}source ~/.bashrc{Colors.RESET}")
        print(f"  Or close and reopen terminal\n")
    else:
        print(f"\n{Colors.YELLOW}⚠ No terminal files found to remove{Colors.RESET}\n")

def create_custom_terminal(name, ascii_art, style, custom_color=None):
    """Create custom terminal based on style choice and optional custom color"""
    
    # Get style data from all styles
    styles = get_all_styles()
    style_data = None
    for s in styles:
        if s[0] == style:
            style_data = s
            break
    
    # Extract prompt symbol and default color
    if style_data:
        _, style_name, style_desc, prompt_symbol, default_color = style_data
    else:
        style_name, prompt_symbol, default_color = "Custom", "╰─➤", "GREEN"
    
    # Use custom color if provided, otherwise use default
    primary_color = custom_color if custom_color else default_color
    
    # Define color schemes for different styles (secondary and accent colors)
    # If custom color is provided, use it as primary, otherwise use style defaults
    color_schemes = {
        '1': {'secondary': 'CYAN', 'accent': 'YELLOW', 'prompt': 'terminal'},
        '2': {'secondary': 'CYAN', 'accent': 'YELLOW', 'prompt': 'CYBER-OPS'},
        '3': {'secondary': 'GREEN', 'accent': 'WHITE', 'prompt': 'MATRIX'},
        '4': {'secondary': 'CYAN', 'accent': 'YELLOW', 'prompt': 'NEON'},
        '5': {'secondary': 'RED', 'accent': 'WHITE', 'prompt': 'ALERT'},
        '6': {'secondary': 'GRAY', 'accent': 'WHITE', 'prompt': 'GHOST'},
        '7': {'secondary': 'WHITE', 'accent': 'GRAY', 'prompt': 'DARK'},
        '8': {'secondary': 'GREEN', 'accent': 'GREEN', 'prompt': 'TERM'},
        '9': {'secondary': 'CYAN', 'accent': 'WHITE', 'prompt': 'BLUE'},
        '10': {'secondary': 'MAGENTA', 'accent': 'WHITE', 'prompt': 'PURPLE'},
        '11': {'secondary': 'GRAY', 'accent': 'WHITE', 'prompt': 'MIN'},
        '12': {'secondary': 'YELLOW', 'accent': 'WHITE', 'prompt': 'DOS'},
        '13': {'secondary': 'CYAN', 'accent': 'MAGENTA', 'prompt': 'CP2077'},
        '14': {'secondary': 'RED', 'accent': 'WHITE', 'prompt': 'ANON'},
        '15': {'secondary': 'GREEN', 'accent': 'WHITE', 'prompt': 'fsociety'},
        '16': {'secondary': 'BLUE', 'accent': 'WHITE', 'prompt': 'TRON'},
        '17': {'secondary': 'CYAN', 'accent': 'YELLOW', 'prompt': 'ctOS'},
        '18': {'secondary': 'DARKGRAY', 'accent': 'WHITE', 'prompt': 'BLACKHAT'},
        '19': {'secondary': 'BLUE', 'accent': 'WHITE', 'prompt': 'WHITEHAT'},
        '20': {'secondary': 'MAGENTA', 'accent': 'YELLOW', 'prompt': 'ELITE'},
    }
    
    scheme = color_schemes.get(style, {'secondary': 'CYAN', 'accent': 'WHITE', 'prompt': style_name[:10].upper()})
    scheme['primary'] = primary_color  # Set the primary color
    
    script_content = f'''#!/bin/bash

# Elite Terminal - {name}
# Style: {style} - Custom Theme

# Colors
RED='\\033[1;31m'
GREEN='\\033[1;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[1;34m'
MAGENTA='\\033[1;35m'
CYAN='\\033[1;36m'
WHITE='\\033[1;37m'
GRAY='\\033[0;37m'
DARKGRAY='\\033[1;30m'
RESET='\\033[0m'
BOLD='\\033[1m'

clear

# Top border
echo -e "${{CYAN}}╔═══════════════════════════════════════════════════════════════════════╗${{RESET}}"

# ASCII Art Banner
echo -e "${{{scheme['primary']}}}${{BOLD}}"
cat << 'BANNER'
{ascii_art}
BANNER
echo -e "${{RESET}}"

# Subtitle
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"
echo -e "${{{scheme['accent']}}}               ▰▰▰ ${{WHITE}}ELITE CYBER TERMINAL${{{scheme['accent']}}} ▰▰▰${{RESET}}"
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

# System Info
echo -e "${{MAGENTA}}┌─[${{GREEN}}SYSTEM INFO${{MAGENTA}}]${{RESET}}"
echo -e "${{MAGENTA}}│${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Operator    ${{WHITE}}:${{{scheme['primary']}}} {name}${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}User        ${{WHITE}}:${{{scheme['primary']}}} $(whoami)${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Hostname    ${{WHITE}}:${{{scheme['primary']}}} $(hostname)${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Shell       ${{WHITE}}:${{{scheme['primary']}}} $SHELL${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Date        ${{WHITE}}:${{{scheme['primary']}}} $(date '+%d %B %Y')${{RESET}}"
echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Time        ${{WHITE}}:${{{scheme['primary']}}} $(date '+%H:%M:%S %Z')${{RESET}}"

# Platform detection
if [ -d "/data/data/com.termux" ]; then
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Platform    ${{WHITE}}:${{{scheme['primary']}}} Termux (Android)${{RESET}}"
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Storage     ${{WHITE}}:${{{scheme['primary']}}} $(df -h /data | tail -1 | awk '{{print $4}}') Free${{RESET}}"
else
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Platform    ${{WHITE}}:${{{scheme['primary']}}} $(uname -s)${{RESET}}"
    echo -e "${{MAGENTA}}├──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Kernel      ${{WHITE}}:${{{scheme['primary']}}} $(uname -r)${{RESET}}"
fi

echo -e "${{MAGENTA}}└──${{CYAN}}[${{WHITE}}○${{CYAN}}] ${{GRAY}}Status      ${{WHITE}}:${{{scheme['primary']}}} ✓ READY${{RESET}}"

# Separator
echo -e "${{CYAN}}╠═══════════════════════════════════════════════════════════════════════╣${{RESET}}"

# Quotes
quotes=(
    "Access granted. System online."
    "Initializing cyber protocols..."
    "The quieter you become, the more you can hear."
    "In a world of locked rooms, the key is power."
    "Code is poetry written in logic."
    "Every system has vulnerabilities."
    "Think like a hacker, act like a guardian."
    "Knowledge is the ultimate weapon."
)

random_quote=${{quotes[$RANDOM % ${{#quotes[@]}}]}}
echo -e "${{{scheme['accent']}}}   » ${{WHITE}}$random_quote${{RESET}}"

# Bottom border
echo -e "${{CYAN}}╚═══════════════════════════════════════════════════════════════════════╝${{RESET}}"

echo ""
echo -e "${{RED}}[${{GREEN}}✓${{RED}}]${{{scheme['secondary']}}} System initialized and ready...${{RESET}}"
echo ""

# Loading bar
echo -ne "${{{scheme['primary']}}}[${{RESET}}"
for i in {{1..50}}; do
    echo -ne "${{{scheme['primary']}}}═${{RESET}}"
    sleep 0.01
done
echo -e "${{{scheme['primary']}}}]${{WHITE}} 100%${{RESET}}"
echo ""

# Set custom PS1 prompt permanently
export PS1="${{RED}}╭─${{GREEN}}[${{CYAN}}{name}${{GREEN}}@${{{scheme['secondary']}}}{scheme['prompt']}${{GREEN}}]${{RED}}─${{YELLOW}}[${{WHITE}}\\w${{YELLOW}}]${{RESET}}\\n${{{scheme['primary']}}}{prompt_symbol}${{RESET}} "
'''
    
    with open('welcome.sh', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    os.chmod('welcome.sh', 0o755)

def create_readme(name):
    """Create README file"""
    readme_content = f"""# {name} - W8TermuxStylePro

Custom stylish terminal with advanced cyberpunk aesthetics.

🔗 **Project:** https://github.com/W8SOJIB/W8TermuxStylePro

## 🚀 Quick Start

```bash
./launcher.sh
```

Or run directly:
```bash
./welcome.sh          # Standard version
./welcome_advanced.sh # Advanced version
```

## ✨ Features

- 🎨 Custom ASCII art with your name: **{name}**
- 💻 Real-time system information
- 🔐 Hacker aesthetic design
- 🎲 Random motivational quotes
- ⚡ Animated loading effects
- 🎯 Custom styled command prompt
- 🚀 Auto-startup enabled

## 🗑️ Uninstall

To remove the terminal and auto-startup:

```bash
python Terminal_Generator.py
# Choose option [3] Remove Stylish Terminal
```

## 🎨 Customization

Edit the `welcome.sh` or `welcome_advanced.sh` files to:
- Change colors
- Modify quotes
- Add more system info
- Adjust animations

## 🔧 Requirements

- Bash shell
- Terminal with color support
- Unix-like environment (Linux, Termux, macOS, WSL)

## 📱 Compatible With

✓ Termux (Android)
✓ Linux/Unix
✓ macOS
✓ Windows (WSL/Git Bash)

---

**Created on:** {datetime.now().strftime('%Y-%m-%d')}  
**Generated by:** Elite Hacker Terminal Generator  
**Operator:** {name}  
**Credits:** W8Team/W8SOJIB

Enjoy your elite cyber terminal! 🔐💻
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

def main():
    """Main function"""
    print_banner()
    
    # Get user input
    name, style, custom_color = get_user_input()
    
    # Handle removal option
    if style == '101':
        remove_terminal()
        return
    
    print(f"\n{Colors.CYAN}Generating your terminal...{Colors.RESET}\n")
    
    # Generate ASCII art
    print(f"{Colors.YELLOW}▸ Generating ASCII art for '{name}'...{Colors.RESET}")
    ascii_art = generate_ascii_art(name)
    
    # Get style name from the styles list
    styles = get_all_styles()
    style_name = 'Custom'
    for s in styles:
        if s[0] == style:
            style_name = s[1]
            break
    
    color_msg = f" with {custom_color} color" if custom_color else ""
    print(f"{Colors.YELLOW}▸ Creating {style_name} terminal{color_msg}...{Colors.RESET}")
    
    # Create the terminal script based on style and custom color
    create_custom_terminal(name, ascii_art, style, custom_color)
    
    print(f"{Colors.GREEN}  ✓ welcome.sh created{Colors.RESET}")
    script_name = "welcome.sh"
    has_standard = True
    has_advanced = False
    
    # Create launcher
    print(f"{Colors.YELLOW}▸ Creating launcher...{Colors.RESET}")
    create_launcher(name, has_standard, has_advanced)
    print(f"{Colors.GREEN}  ✓ launcher.sh created{Colors.RESET}")
    
    # Create README
    print(f"{Colors.YELLOW}▸ Creating documentation...{Colors.RESET}")
    create_readme(name)
    print(f"{Colors.GREEN}  ✓ README.md created{Colors.RESET}")
    
    # Setup auto-startup
    print(f"{Colors.YELLOW}▸ Setting up auto-startup...{Colors.RESET}")
    setup_auto_startup(script_name)
    
    # Success message
    print(f"""
{Colors.GREEN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                    ✓ GENERATION COMPLETE!                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.CYAN}Your custom terminal is ready!{Colors.RESET}

{Colors.YELLOW}Quick Start:{Colors.RESET}
  {Colors.WHITE}./launcher.sh{Colors.RESET}     - Interactive menu

{Colors.YELLOW}Or run directly:{Colors.RESET}
""")
    
    if has_standard:
        print(f"  {Colors.WHITE}./welcome.sh{Colors.RESET}          - Standard style")
    if has_advanced:
        print(f"  {Colors.WHITE}./welcome_advanced.sh{Colors.RESET} - Advanced style")
    
    print(f"""
{Colors.CYAN}Files created:{Colors.RESET}
  {Colors.GREEN}✓{Colors.RESET} welcome.sh ({style_name} theme)
  {Colors.GREEN}✓{Colors.RESET} launcher.sh
  {Colors.GREEN}✓{Colors.RESET} README.md
""")
    
    print(f"""
{Colors.GREEN}✓ Auto-startup enabled with 'source' command!{Colors.RESET}
  Custom prompt will work correctly
  Terminal will appear when you open bash/termux

{Colors.YELLOW}To apply changes NOW:{Colors.RESET}
  {Colors.CYAN}source ~/.bashrc{Colors.RESET}
  Or close and reopen terminal

{Colors.YELLOW}To remove and restore normal prompt:{Colors.RESET}
  {Colors.WHITE}python Terminal_Generator.py{Colors.RESET}
  Then choose option [3] Remove Stylish Terminal
""")
    
    print(f"\n{Colors.MAGENTA}Created for: {Colors.BOLD}{name}{Colors.RESET}")
    print(f"{Colors.CYAN}Credits: {Colors.BOLD}W8Team/W8SOJIB{Colors.RESET}")
    print(f"{Colors.GRAY}Elite Cyber Terminal Generator v1.0{Colors.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}✗ Installation cancelled{Colors.RESET}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}✗ Error: {e}{Colors.RESET}\n")
        sys.exit(1)

