# def accept_list(numbers):
#     if not nums:
#         return []
    
#     first = nums[0]
#     rest = nums[1:]
    
#     if first % 2 == 0:
#         return first **2 + accept_list(rest)
    
#     else:
#         return accept_list
    
#     nums = [1,2,3.4,5,6]
#     result = accept_list(nums)
#     print("Original list: " ,nums)
    
#     print("New list: " ,result)

def process_list(numbers):
    # Base case: if the list is empty, return empty list
    if not numbers:
        return []
    
    # Take the first element
    first = numbers[0]
    rest = numbers[1:]
    
    # If first is even, square it and add recursively processed rest
    if first % 2 == 0:
        return [first ** 2] + process_list(rest)
    else:
        # Skip odd numbers
        return process_list(rest)


# Example usage
nums = [1, 2, 3, 4, 5, 6]
result = process_list(nums)
print("Original list:", nums)
print("Processed list:", result)
