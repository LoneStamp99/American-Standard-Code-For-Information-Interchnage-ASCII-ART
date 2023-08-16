import argparse
from command import execute_command
# Import PIL module
from PIL import Image

# Define image path
image_path = "Image"

# Open image
image = Image.open(image_path)

# Perform image processing/conversion
# ...

# Define save path
save_path = r"Output"

# Save image
image.save(save_path)


def parse_arguments():
    parser = argparse.ArgumentParser(description="ASCII Art Generator")

    # Add arguments here based on the command.txt file
    # Example:
    # parser.add_argument("-Colorized", choices=["Yes", "No"], help="Colorized/Non-colorized")

    parser.add_argument("-Colorized", choices=["Yes", "No"], help="Colorized/Non-colorized")
    parser.add_argument("-Encoding", choices=["Standard", "Alphabet/Characters", "Binary", "#", "$", "*", "@", "+", "=", ".", "-", "_", ",", "<", ">", "^", "%", "~", "!", "?"], help="ASCII encoding character")
    parser.add_argument("-Rename", help="Filename/image")
    parser.add_argument("-Location", help="C:/path/of/image")
    parser.add_argument("-Saveas", help="png/jpg/tiff/Etc")
    parser.add_argument("-Ratio", choices=["1:1", "3:2", "5:4", "16:9", "1920:1090", "1280:720", "1080:1080"], help="Image dimensions ratio")
    parser.add_argument("-Background", choices=["White: D8D9DA", "Pink: FCBAAD", "Yellow: F0DE36", "Black: 222831", "Grey: 393E46", "Cyan: 4FC0D0", "Red: B70404", "Green: CAD315", "Oranged: E25822"], help="Background")
    parser.add_argument("-Saveto", help="D:/where/the/image/saved")

    args = parser.parse_args()
    return args

def main():
    # Load the banner from banner.txt and display it here

    args = parse_arguments()

    execute_command(args)

if _name_ == "_main_":
    main()