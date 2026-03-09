import sys


def building():
    try:
        text = sys.argv[1]
    except (IndexError):
        print("What is the text to count?")
        text = input()
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0
    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c in "'.,;:?!":
            punc += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
    print(f"{upper} upper letters\n{lower} lower letters\n{punc}", end="")
    print(f" punctuation marks\n{space} spaces\n{digit} digits")


def main():
    building()


if __name__ == "__main__":
    main()
