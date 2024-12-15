Here's a simple "Hello World" Python program:

```python
# Define the main function
def main():
    # Print "Hello, World!" to the console
    print("Hello, World!")

# Call the main function when the script is run
if __name__ == "__main__":
    main()
```

Let me explain what each part of this code does:

*   The `def` keyword is used to define a new function called `main()`. This will contain our "Hello World" message.
*   Inside the `main()` function, we use the `print()` function to print out "Hello, World!" onto the console. Since it's inside a function, this output won't be visible when you run the script directly.
*   The `if __name__ == "__main__":` line checks whether the current script is being executed directly or not. If it's being imported as a module into another script (which is common in many Python projects), then this part of the code won't be executed.

You can save this to a file, like "helloworld.py", and then run it using Python:

```bash
python helloworld.py
```

This should output "Hello, World!" onto your console.