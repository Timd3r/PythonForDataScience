import sys


def filterstring():
    """
    A program that accepts two arguments: a string (S) and an integer (N).
    The program outputs a list of words from S
    that have a length greater than N.
    """
    try:
        args = sys.argv
        if len(args) != 3:
            raise AssertionError("the arguments are bad")
        text = args[1]
        val = args[2]
        if not val.isdigit():
            raise AssertionError("the arguments are bad")
        val = int(val)
        list = []
        for word in text.split(' '):
            if len(word) > val:
                list.append(word)
        print(list)
    except AssertionError as e:
        print(f"AssertionError: {e}")


def main():
    filterstring()


if __name__ == "__main__":
    main()
