# Python to C++ Code Converter

## Overview
The **Python to C++ Code Converter** is a tool that converts Python code into equivalent C++ code. It simplifies the process of transitioning Python projects into C++ by providing a basic, automated translation of common Python constructs such as variables, loops, conditionals, classes, and functions into C++ syntax.

---

## Features
- **Variable Conversion**: Automatically detects Python variable declarations and converts them to appropriate C++ types.
- **Print Statements**: Translates Python's `print()` function to C++'s `std::cout` syntax.
- **Conditionals**: Converts `if`, `elif`, and `else` blocks to C++ syntax.
- **Loops**: Supports translation of Python's `for` and `while` loops.
- **Classes and Methods**: Handles basic class structures, methods, and inheritance.

### Dependencies
- Python 3.6 or higher
- Built-in `re` module for regular expressions

### Environment
- OS: Works on any system capable of running Python (Linux, Windows, macOS)
- Memory/Hardware: Standard computing device

---

### Example
#### Input (Python Code):
```python
x = 42
print("Hello, World!")
if x > 10:
    print("x is greater than 10")
```

#### Output (C++ Code):
```cpp
int x = 42;
std::cout << "Hello, World!" << std::endl;
if (x > 10) {
    std::cout << "x is greater than 10" << std::endl;
}
```
---

## Possible Additions
- **Support for Advanced Data Structures**: Add conversion for lists, dictionaries, and sets to their C++ equivalents.
- **External Library Handling**: Incorporate Python imports into C++ includes.
- **Improved Error Handling**: Ensure the program can gracefully handle invalid or edge-case Python code.
- **GUI Interface**: Develop a graphical interface for non-technical users.
- **Extended Type Inference**: Enhance support for detecting and converting complex types.
