import pyfiglet

Green = "\033[32m"
RESET = "\033[0m"

banner_text = pyfiglet.figlet_format("P A N C A K E")
banner = f"{Green}{banner_text}{RESET}"

print(banner)