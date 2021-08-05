import math

def main():
    arr = [3, 13, 14, 22, 23, 51, 53, 54, 64, 67, 68, 122, 124, 152]  #array of random numbers in sorted order. TODO: Add random number array generator?
    target = int(input("\nEnter a number to search for: "))             #target to search for.
    answer = binarySearch(arr, target)                                        #calling function
    
    if answer == None:                                                #Target not found
        print("\n\nNumber not found.  Exiting....")
    else:                                                             #Number found
        print("\n\nYour chosen number is at index ", answer)
    
    return

def binarySearch(arr, target):          #calculate middle of array, if middle is less than target, set left number to middle plus 1, if middle is greater than target, set right to middle minus 1. repeat until middle is target or left > right.
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = math.floor((left + right) / 2)
        if left > right:
            return None
        elif arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        elif arr[middle] == target:
            return middle

if __name__ == "__main__":
    main()