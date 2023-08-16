import argparse
from PIL import Image

def format_picture(ratio, image_path):

    # Open image
    image = Image.open(image_path)

    # Validate ratio
    if ratio not in ["1:1", "3:2", "5:4", "16:9", "1920:1090", "1280:720", "1080:1080"]:
        raise ValueError("Invalid ratio")

    # Get dimensions
    width, height = image.size

    # Calculate new dimensions
    if ratio:
        ratio_x, ratio_y = [int(x) for x in ratio.split(":")]
        new_width = width * ratio_x / ratio_y
        new_height = height * ratio_x / ratio_y
    else:
        new_width, new_height = width, height

    # Resize image
    image = image.resize((new_width, new_height))

    return image

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-ratio", choices=["1:1", "3:2", "5:4", "16:9", "1920:1090", "1280:720", "1080:1080"])
    parser.add_argument("-image", required=True)
    parser.add_argument("-saveto", required=True)
    args = parser.parse_args()

    # Format image
    formatted_image = format_picture(args.ratio, args.image)

    # Save image
    formatted_image.save(args.saveto)

if __name__ == "__main__":
   main()
