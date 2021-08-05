def main():

    start = int(input("Please enter any positive integer: "))
    path = start % 2

    if start == 1  or start == 2 or start == 4:
        print("\nThis number ends in a paradox.")
        return
    elif path == 0:
        even(start)
        return
    elif path == 1:
        odd(start)
        return
    else:
        print("Something went wrong. Restart and try again.")
        return    

def even(start):
    start /= 2
    path = start % 2

    if start == 1 or start == 2 or start == 4:
        print("\nThis number ends in a paradox.")
        return
    elif path == 0:
        even(start)
        return
    elif path == 1:
        odd(start)
        return
    else:
        print("Something went wrong. Restart and try again.")
        return


def odd(start):
    start = start * 3 + 1
    path = start % 2

    if start == 1  or start == 2 or start == 4:
        print("\nThis number ends in a paradox.")
        return
    elif path == 0:
        even(start)
        return
    elif path == 1:
        odd(start)
        return
    else:
        print("Something went wrong. Restart and try again.")
        return



if __name__ == "__main__":
    main()
