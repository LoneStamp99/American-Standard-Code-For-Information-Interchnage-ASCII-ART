import colorama
from colorama import Fore, Back, Style

# Dictionary mapping color names to colorama codes
COLORS = {
  "White: D8D9DA": Fore.WHITE,
  "Pink: FCBAAD": Fore.MAGENTA,
  "Yellow: F0DE36": Fore.YELLOW,
  "Black: 222831": Fore.BLACK,
  "Grey: 393E46": Fore.LIGHTBLACK_EX,
  "Cyan: 4FC0D0": Fore.CYAN,
  "Red: B70404": Fore.RED,
  "Green: CAD315": Fore.GREEN,
  "Oranged: E25822": Fore.LIGHTRED_EX
}

def colorize(ascii_art, image, background):

  # Get the specified background color code
  color_code = COLORS[background]

  # Colorize the ASCII art with the background color
  for line in ascii_art:
    print(f"{color_code}{line}{Style.RESET_ALL}")

def main():

  # Get background from command line arguments
  background = args.Background

  # Colorize ASCII art
  colorize(ascii_art, image, background)

if __name__ == "__main__":
  main()
