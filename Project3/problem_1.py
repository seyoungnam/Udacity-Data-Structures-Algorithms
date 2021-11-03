def sqrt(number = None):
    if number is None:
        return None
    if number < 0:
        return -1
    l = 0
    r = number
    while l < r:
        mid = (l + r) // 2
        if mid**2 > number:     r = mid - 1
        elif mid**2 < number:   l = mid + 1
        else:                   return mid
    return l


print("==== test case 1 ====")
print ("Pass" if  (3 == sqrt(9)) else "Fail")       # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")       # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")      # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")       # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")      # Pass

print("==== test case 2 - edge case ====")
print ("Pass" if  (None == sqrt()) else "Fail")     # Pass

print("==== test case 3 - edge case ====")
print ("Pass" if  (-1 == sqrt(-33)) else "Fail")    # Pass
