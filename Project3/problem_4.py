def sort_012(input_list):
    l = 0
    r = len(input_list) - 1
    i = 0
    while i <= r:
        if input_list[i] == 0:
            input_list[l], input_list[i] = input_list[i], input_list[l]
            l += 1
            i += 1
        elif input_list[i] == 2:
            input_list[r], input_list[i] = input_list[i], input_list[r]
            r -= 1
        else:
            i += 1
    return input_list
            

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass, ", sorted_array)
    else:
        print("Fail")

print("==== test case 1 ====")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])                                                        # Pass,  [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])           # Pass,  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])                                # Pass,  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

print("==== test case 2 - edge case ====")
test_function([0])                                                                                      # Pass,  [0]

print("==== test case 3 - edge case ====")
test_function([1])                                                                                      # Pass,  [1]
test_function([0, 0, 0, 0, 0, 0])                                                                       # Pass,  [0, 0, 0, 0, 0, 0]