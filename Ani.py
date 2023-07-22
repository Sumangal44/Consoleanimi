import sys
import time
import colorama

# Initialize colorama to enable coloring of text on Windows
colorama.init()

def print_colored(text, color):
    colors = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'yellow': colorama.Fore.YELLOW,
        'blue': colorama.Fore.BLUE,
        'magenta': colorama.Fore.MAGENTA,
        'cyan': colorama.Fore.CYAN,
        'white': colorama.Fore.WHITE,
    }

    print(f"{colors[color]}{text}{colorama.Style.RESET_ALL}")

def starting_animation():
    print_colored("Welcome to My Awesome App!", 'green')
    print_colored("Initializing...", 'yellow')

    animation_frames = ['-', '\\', '|', '/']

    for _ in range(20):
        for frame in animation_frames:
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')

    print_colored("\nReady to go!", 'green')

if __name__ == "__main__":
    starting_animation()
  
