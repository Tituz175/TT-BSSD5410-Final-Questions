from PIL import Image
import numpy as np


def encode(image_name, text):
    # Load image and flatten pixel values into a 1D array
    img = np.array(Image.open(image_name))
    image_shape = img.shape
    image_array = img.flatten()

    # Add termination string to the end of the message
    text += "[END]"

    # Convert message into a binary string representation
    text_array = [bin(ord(char))[2:].zfill(8) for char in text]

    # Iterate through each binary character and each bit in the character
    index = 0
    for char in text_array:
        for bit in str(char):
            # Combine bit with pixel value at current index using bitwise OR
            temp = image_array[index] | int(bit)
            # Store combined value in pixel array after masking with the bit using bitwise AND
            image_array[index] = temp & int(bit)
            # Move on to the next pixel index
            index += 1

    # Create new image from modified pixel array and save to file
    output_img = Image.fromarray(np.reshape(image_array, image_shape))
    output_img.save("output_img.png")

    return "Encoding complete\n"


def decode(image):
    # Load image and flatten pixel values into a 1D array
    img = np.array(Image.open(image))
    imgArr = np.array(img).flatten()

    # Initialize empty message string
    message = ""

    # Iterate through pixel array in groups of 8
    for i in range(8, len(imgArr), 8):
        # Extract group of 8 bits and convert to binary string
        char_int_list = imgArr[i - 8:i]
        char_bin_list = [str(bit % 2) for bit in char_int_list]
        char_bin = "".join(char_bin_list)

        # Convert binary string to corresponding ASCII character and add to message
        char = chr(int(char_bin, 2))
        message += char

        # Check if message ends with termination string, and break if so
        if message[-5:] == "[END]":
            break

    # Remove termination string from message and return
    return message[:len(message) - 5]
