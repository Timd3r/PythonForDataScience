import sys


def whatis():
    try:
        values = sys.argv
        value = values[1]
    except (IndexError):
        return
    try:
        if not value.isdigit():
            raise AssertionError("argument is not an integer")
        value = int(value)
        if (len(values) > 2):
            raise AssertionError("more than one argument is provided")
        if (value % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    whatis()


if __name__ == "__main__":
    main()
