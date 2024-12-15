**Palindrome Program in Python**

A palindrome is a sequence of characters that reads the same backward as forward. Here's a simple Python program to check if a given string is a palindrome.

```python
def is_palindrome(s):
    """
    Checks if a given string is a palindrome.
    
    Args:
        s (str): The input string.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Not a palindrome"))  # False

```

**Explanation:**

*   We define a function `is_palindrome` that takes a string as input.
*   Inside the function, we remove non-alphanumeric characters and convert the string to lowercase using list comprehension and string methods.
*   We then compare the processed string with its reverse (`s[::-1]`) to check if it's a palindrome. If they're equal, the original string is a palindrome.

**How to Use:**

You can use this function by calling `is_palindrome("your_string_here")`, and it will return `True` if the string is a palindrome or `False` otherwise.

This program provides a clean and efficient way to determine whether a given string is a palindrome. It handles non-alphanumeric characters and case sensitivity, making it suitable for various use cases.