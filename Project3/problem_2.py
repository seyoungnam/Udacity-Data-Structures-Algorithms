def rotated_array_search(input_list, number):
    if input_list == "" or number == "":
        return -1

    l, r = 0, len(input_list) - 1

    while l <= r:
        mid = (l + r) // 2
        if number == input_list[mid]:
            return mid

        # the cliff located in the right
        if input_list[l] < input_list[mid]:
            # number located in the left
            if input_list[l] <= number < input_list[mid]:
                r = mid - 1
            # number located in the right
            else:
                l = mid + 1
        # the cliff located in the left
        else:
            if input_list[mid] < number <= input_list[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
        

def linear_search(input_list, number):
    if input_list == "" or number == "":
        return -1

    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    answer = rotated_array_search(input_list, number)
    if linear_search(input_list, number) == answer:
        print("Pass, the index is ", answer)
    else:
        print("Fail")

print("==== test case 1 ====")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])            # Pass, the index is  0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])            # Pass, the index is  5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])                   # Pass, the index is  2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])                   # Pass, the index is  3

print("==== test case 2 - edge case ====")
test_function([[6, 7, 8, 1, 2, 3, 4], ""])                  # Pass, the index is  -1
test_function(["", 3])                                      # Pass, the index is  -1

print("==== test case 3 - edge case ====")
test_function([[6, 7, 8, 1, 2, 3, 4], 10])                  # Pass, the index is  -1