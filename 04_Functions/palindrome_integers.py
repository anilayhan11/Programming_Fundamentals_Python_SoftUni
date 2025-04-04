def is_palindrome(nums):
    for num in nums:
        regular_num = num
        reversed_num = num[::-1]
        if regular_num == reversed_num:
            print(True)
        else:
            print(False)


numbers = input().split(', ')
is_palindrome(numbers)
