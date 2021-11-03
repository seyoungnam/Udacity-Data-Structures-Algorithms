def rearrange_digits(input_list):
    sorted_list = mergesort(input_list)
    if len(sorted_list) <= 1:
        return [-1, -1]
    ele1, ele2 = [], []
    for i, num in enumerate(sorted_list):
        if i % 2:
            ele2.append(str(num))
        else:
            ele1.append(str(num))
    return [int("".join(ele1)), int("".join(ele2))]

def mergesort(arr):
    if len(arr) in (0, 1):
        return arr
    
    mid = (len(arr) - 1) // 2
    left = arr[:mid+1]
    right = arr[mid+1:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):
    output = []

    while left and right:
        if left[0] > right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))

    while left:
        output.append(left.pop(0))

    while right:
        output.append(right.pop(0))

    return output

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print("==== test case 1 ====")
test_function([[1, 2, 3, 4, 5], [542, 31]])             # Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])         # Pass

print("==== test case 2 - edge case ====")
test_function([[], [-1, -1]])                           # Pass

print("==== test case 3 - edge case ====")
test_function([[3], [-1, -1]])                          # Pass