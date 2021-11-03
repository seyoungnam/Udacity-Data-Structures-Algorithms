def get_min_max(ints):
    if len(ints) == 0:
        return (-1, -1)
    minInt, maxInt = float('inf'), float('-inf')
    for num in ints:
        if num < minInt:
            minInt = num

        if num > maxInt:
            maxInt = num
    return (minInt, maxInt)

## Example Test Case of Ten Integers
import random

print("==== test case 1 ====")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass", get_min_max(l) if ((0, 9) == get_min_max(l)) else "Fail")            # Pass (0, 9)


print("==== test case 2 - edge case ====")
l = [0, 0, 0, 0]
print ("Pass", get_min_max(l) if ((0, 0) == get_min_max(l)) else "Fail")            # Pass (0, 0)


print("==== test case 3 - edge case ====")
l = []  # empty list
print ("Pass", get_min_max(l) if ((-1, -1) == get_min_max(l)) else "Fail")          # Pass (-1, -1)