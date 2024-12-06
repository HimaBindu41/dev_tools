Here's a basic "Hello, World!" program in Python:

```python
# This is a comment - anything after the "#" symbol is ignored by the interpreter

# Define a function that prints out a message
def print_hello():
    # The print() function prints its argument to the console
    print("Hello, World!")

# Call the function
print_hello()
```

When you run this program, it will print "Hello, World!" to the console.

Alternatively, if you want an even simpler program that just prints out the message without a function:

```python
# Print Hello, World!
print("Hello, World!")
```

You can also use Python's built-in `main` function for a more modern way of writing command line applications. Here is an example:

```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```

In this program, the `if __name__ == "__main__":` block ensures that the `main` function only runs when the script is executed directly, not if it's imported as a module.