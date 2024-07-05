#file5.py

def sort_list(numbers):
    numbers.sort()
    return numbers

numbers = [5, 2, 8, 1, 3]
sorted_numbers = sort_list(numbers)
print(f"Sorted numbers: {sorted_numbers}")
