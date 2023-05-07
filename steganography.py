from PIL import Image
import numpy as np


def encode(image_name, text):
    img = np.array(Image.open(image_name))
    image_shape = img.shape
    image_array = img.flatten()
    text += "[END]"
    text_array = [bin(ord(char))[2:].zfill(8) for char in text]
    index = 0
    for char in text_array:
        for bit in str(char):
            temp = image_array[index] | int(bit)
            image_array[index] = temp & int(bit)
            index += 1
    output_img = Image.fromarray(np.reshape(image_array, image_shape))
    output_img.save("output_img.png")
    return "Encoding complete\n"


def decode(image):
    img = np.array(Image.open(image))
    imgArr = np.array(img).flatten()

    message = ""
    for i in range(8, len(imgArr), 8):
        char_int_list = imgArr[i - 8:i]
        char_bin_list = [str(bit % 2) for bit in char_int_list]
        char_bin = "".join(char_bin_list)
        char = chr(int(char_bin, 2))
        message += char

        if message[-5:] == "[END]":
            break
    return message[:len(message) - 5]
