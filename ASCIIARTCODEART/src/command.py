import argparse
from PIL import image

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-Image', '--image', required=True, help='Path to input image')
    parser.add_argument("-Colorized", choices=["Yes", "No"])
    parser.add_argument("-Encoding", choices=["Standard", "Alphabet/Characters", "Binary", "#", "$", "*", "@", "+", "=", ".", "-", "_", ",", "<", ">", "^", "%", "~", "!", "?"])
    parser.add_argument("-Rename")
    parser.add_argument("Background", choices=["White: D8D9DA", "Pink: FCBAAD", "Yellow: F0DE36", "Black: 222831", "Grey: 393E46", "Cyan: 4FC0D0", "Red: B70404", "Green: CAD315", "Oranged: E25822"])
    parser.add_argument("-Saveas", choices=["jpg", "png", "tiff", "bmp", "tga", "netpbm", "pdf", "psd", "raw"])
    parser.add_argument("-Ratio", choices=["1:1", "3:2", "5:4", "16:9", "1920:1090", "1280:720", "1080:1080"])
    parser.add_argument("-Saveto", '--output', required=True, help='Output folder')

    return parser.parse_args()

def main():
    args = parse_args()

    print(f"-Image: {args.Images}")
    print(f"-Colorized: {args.Colorized}")
    print(f"-Encoding: {args.Encoding}")
    print(f"-Rename: {args.Rename}")
    print(f"-Location: {args.Location}")
    print(f"-Saveas: {args.Saveas}")
    print(f"-Ratio: {args.Ratio}")
    print(f"-Saveto: {args.Saveto}")

if __name__ == "__main__":
    main()