# Week 2: Simple Calculator

**Difficulty:** Beginner

## Learning Goals
- Use functions to organise code
- Handle user input and basic error cases
- Practise conditional logic (`if / elif / else`)
- Understand loops for repeated interactions

## Project Description
Build an interactive command-line calculator that can perform addition,
subtraction, multiplication, and division. The program keeps running until the
user chooses to quit.

## Concepts Covered
- Defining and calling functions
- `while` loops
- `if / elif / else` branching
- Exception handling with `try / except` (ZeroDivisionError, ValueError)
- Returning values from functions

## How to Run
```bash
python main.py
```

## Sample Output
```
=== Simple Calculator ===
Enter first number: 10
Choose operation (+, -, *, /): /
Enter second number: 4
Result: 10.0 / 4.0 = 2.5

Calculate again? (y/n): n
Goodbye!
```

## Challenges
1. Add support for the exponent (`**`) and modulo (`%`) operators.
2. Keep a running history of all calculations performed.
3. Add a "clear history" option.
