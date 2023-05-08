from steganography import *
from square_grid import *


def question1():
    while True:
        choice = input("Please enter mode (E)ncode or (D)ecode: ")
        if choice.lower() == "e":
            text = input("Please enter phrase: ")
            print(encode("img.png", text))
        elif choice.lower() == "d":
            text = decode("output_img.png")
            print(f"Found: {text}\n")
        else:
            break


def question2():
    square_grid()


def main():
    print("==============Question 1==============")
    question1()
    print("======================================\n")
    print("==============Question 2==============\n")
    question2()


if __name__ == "__main__":
    main()
