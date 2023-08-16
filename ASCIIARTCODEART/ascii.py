import PIL.Image
import numpy as np

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Add uppercase letters

ASCII_CHARS.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


# Add lowercase letters

ASCII_CHARS.extend(list("abcdefghijklmnopqrstuvwxyz"))

# Add numbers

ASCII_CHARS.extend(list("0123456789"))

# Add additional symbols

additional_symbols = ["<", ">", "^", "~", "!", "$", "&", "-", "_", "`", "'", '"', "|", "\\"]

ASCII_CHARS.extend(additional_symbols)

# Optionally sort the full list

ASCII_CHARS.sort()

def ascii_art(encoding, image_file):


  # Open image and convert to grayscale

  image = PIL.Image.open(image_file).convert('L')


  # Resize image to fit the terminal

  width, height = image.size

  aspect_ratio = height/width

  new_width = 120

  new_height = aspect_ratio * new_width * 0.55

  image = image.resize((new_width, int(new_height)))


  # Convert each pixel to ascii character

  characters = "".join([ASCII_CHARS[pixel//25] for pixel in image.getdata()])


  return "\n".join([characters[index:index+new_width] for index in range(0, len(characters), new_width)])



def main():


  encoding, image_file = input("Enter encoding and image filename separated by comma: ").split(",")


  ascii_art = ascii_art(encoding, image_file)
  print(ascii_art)


if __name__ == "__main__":
  main()

