from steganography import *


def main():
    choice = input("Please enter mode (E)ncode or (D)ecode: ")
    if choice.lower() == "e":
        text = input("Please enter phrase: ")
        print(encode("img.png", text))
    elif choice.lower() == "d":
        text = decode("output_img.png")
        print(f"Found: {text}\n")


if __name__ == "__main__":
    main()
