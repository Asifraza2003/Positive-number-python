def get_positive_numbers(input_list):
    return [num for num in input_list if num > 0]

# Example inputs
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Output results
print("Input: list1 =", list1)
print("Output:", get_positive_numbers(list1))

print("Input: list2 =", list2)
print("Output:", get_positive_numbers(list2))
