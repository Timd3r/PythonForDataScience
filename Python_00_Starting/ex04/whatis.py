import sys


def whatis():
    try:
        values = sys.argv
        value = values[1]
    except (IndexError):
        return
    try:
        value = int(value)
        if (len(values) > 2):
            print("AssertionError: more than one argument is provided")
            return
        if (value % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except (ValueError):
        print("AssertionError: argument is not an integer")


def main():
    whatis()


if __name__ == "__main__":
    main()
