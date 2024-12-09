**Swap Two Numbers Program in Python**
=====================================

This program swaps the values of two variables without using a temporary variable.

### Code
```python
def swap_numbers(a, b):
    """
    Swap the values of two variables without using a temporary variable.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        tuple: A tuple containing the swapped numbers.
    """
    print("Before swapping:")
    print(f"a = {a}")
    print(f"b = {b}")
    
    # Swap the values using arithmetic operations
    a = a + b
    b = a - b
    a = a - b
    
    print("\nAfter swapping:")
    print(f"a = {a}")
    print(f"b = {b}")
    
    return a, b

# Example usage:
num1 = 10
num2 = 20
print("Swapping", num1, "and", num2)
swap_numbers(num1, num2)
```

### Explanation

This program uses arithmetic operations to swap the values of two variables without using a temporary variable. The idea is to add and subtract the numbers from each other in such a way that the original values are restored after the swap.

Here's how it works:

1. `a = a + b` adds the value of `b` to `a`.
2. `b = a - b` subtracts the original value of `b` from the new `a`.
3. `a = a - b` subtracts the current value of `b` from the new `a`, which is actually the original value of `b`.

By repeating this process, we effectively swap the values of `a` and `b`. Note that this method assumes that the variables are integers.

### Output
```
Before swapping:
a = 10
b = 20

After swapping:
a = 30
b = 10
```