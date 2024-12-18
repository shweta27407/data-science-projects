# Exception Handling

Common Exceptions in Python
Here are a few examples of exceptions we often run into and can handle using this tool:

1. ZeroDivisionError: This error arises when an attempt is made to divide a number by zero. Division by zero is undefined in mathematics, causing an arithmetic error. For instance:
For example:
result = 10 / 0 
print(result)


2. ValueError: This error occurs when an inappropriate value is used within the code. An example of this is when trying to convert a non-numeric string to an integer:
For example:
1 num = int("abc")


3. FileNotFoundError: This exception is encountered when an attempt is made to access a file that does not exist.
For example:
with open("nonexistent_file.txt", "r") as file:
     content = file.read()  


4. IndexError: An IndexError occurs when an index is used to access an element in a list that is outside the valid index range.
For example:

my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError


5. KeyError: The KeyError arises when an attempt is made to access a non-existent key in a dictionary.
For example:
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError


6. TypeError: The TypeError occurs when an object is used in an incompatible manner. An example includes trying to concatenate a string and an integer:
For example:
result = "hello" + 5   # Raises TypeError


7. AttributeError: An AttributeError occurs when an attribute or method is accessed on an object that doesn't possess that specific attribute or method. For instance:
For example:
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError


8. ImportError: This error is encountered when an attempt is made to import a module that is unavailable. For example: import non_existent_module

Note: Please remember, the exceptions you will encounter are not limited to just these. There are many more in Python. 
By using the technique provided below and following the correct syntax, you will be able to handle any exceptions that come your way.

Handling Exceptions:

Try and Except : You can use the try and except blocks to prevent your program from crashing due to exceptions.

The code that may result in an exception is contained in the try block.

try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
print("outside of try and except block")  # This line will be executed regardless of whether an exception occurred

