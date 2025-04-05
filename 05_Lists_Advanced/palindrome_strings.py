words = input().split()
palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
print(found_palindromes)

count = found_palindromes.count(palindrome)
print(f"Found palindrome {count} times")