def main():

    start = int(input("Please enter any positive integer: "))   #initial value, assuming only a positive integer is added.
    path = start % 2    # prevents recursion overflow

    if start == 1  or start == 2 or start == 4: # checks if it hits paradox loop.
        print("\nThis number ends in a paradox.")
        return
    elif path == 0: #if number is even do the even math.
        even(start)
        return
    elif path == 1: #if number is odd do the odd math.
        odd(start)
        return
    else:           #catchall in-case something goes wrong. (theoretically shouldn't happen.)
        print("Something went wrong. Restart and try again.")
        return    

def even(start):
    start /= 2
    path = start % 2    # prevents recursion overflow

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
    path = start % 2    # prevents recursion overflow

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
