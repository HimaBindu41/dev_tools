**Calculating the Sum of Two Numbers in Python**
=====================================================

You can calculate the sum of two numbers in Python using basic arithmetic operations. Here's an example:

```python
def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

# Example usage
num1 = 10
num2 = 20
result = calculate_sum(num1, num2)
print(f"The sum is: {result}")
```

Alternatively, you can use the built-in `+` operator to achieve the same result:

```python
def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers.

    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

# Example usage
num1 = 10
num2 = 20
result = calculate_sum(num1, num2)
print(f"The sum is: {result}")
```

In this code:

*   We define a function `calculate_sum` that takes two arguments, `num1` and `num2`.
*   Inside the function, we use the `+` operator to add `num1` and `num2` together.
*   The result is returned by the function.
*   We demonstrate how to call this function with example values for `num1` and `num2`.

Note that this code works with both integer and floating-point numbers, as Python supports these data types.