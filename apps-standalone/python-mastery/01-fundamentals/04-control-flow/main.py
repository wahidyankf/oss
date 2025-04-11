"""
Python Control Flow Comprehensive Demo

This heavily commented example demonstrates:
1. All Python control flow structures
2. Practical examples with clear output
3. Special cases and edge behaviors
4. Best practices and common patterns

Key Concepts Covered:
- Conditional execution with if/elif/else
- Iteration with for and while loops
- Loop control statements (break, continue, pass)
- The else clause in loops
"""

# ========== CONDITIONAL STATEMENTS ==========
"""
Conditional execution:
- if: First condition to evaluate to True runs its block
- elif: Subsequent conditions checked if previous were False
- else: Runs if all conditions above were False

Note:
- Indentation determines block membership
- No switch statement in Python (use if/elif chains or dicts)
"""
print("=== CONDITIONAL STATEMENTS ===")

age = 25  # Test age value

if age < 13:
    print("Child")  # Runs if age under 13
elif age < 20:
    print("Teenager")  # Runs if age 13-19
elif age < 65:
    print("Adult")  # Runs if age 20-64
else:
    print("Senior")  # Runs if age 65+

# ========== FOR LOOPS ==========
"""
For loops iterate over sequences:
- Lists, tuples, strings, ranges, etc.
- enumerate() adds counter to iterations
- Can use with else clause (runs if no break)
"""
print("\n=== FOR LOOPS ===")

fruits = ["apple", "banana", "cherry"]  # List to iterate

print("Simple for loop:")
for fruit in fruits:
    print(f"- {fruit}")  # Prints each fruit

print("\nWith enumerate():")
for i, fruit in enumerate(fruits, 1):  # Start counting at 1
    print(f"{i}. {fruit}")  # Prints numbered list

# ========== WHILE LOOPS ==========
"""
While loops run while condition is True:
- Beware of infinite loops!
- Ensure condition will eventually become False
- Can use with else clause (runs if no break)
"""
print("\n=== WHILE LOOPS ===")
count = 3  # Initial counter value
print("Countdown:")
while count > 0:  # Runs while count > 0
    print(count)
    count -= 1  # Decrement counter
print("Blast off!")  # Runs after loop

# ========== LOOP CONTROL STATEMENTS ==========
"""
Loop control:
- break: Exit loop immediately
- continue: Skip to next iteration
- pass: Do nothing (placeholder)
"""
print("\n=== LOOP CONTROL ===")

print("break example:")
for num in range(10):  # 0 to 9
    if num == 5:
        break  # Exit loop when num is 5
    print(num)

print("\ncontinue example:")
for num in range(5):  # 0 to 4
    if num == 2:
        continue  # Skip printing 2
    print(num)

print("\npass example:")
for num in range(3):  # 0 to 2
    if num == 1:
        pass  # Placeholder for future code
    print(num)

# ========== ELSE CLAUSE IN LOOPS ==========
"""
Loop else clauses:
- Execute after normal loop completion
- Don't run if loop exited via break
- Often overlooked but useful feature
"""
print("\n=== ELSE IN LOOPS ===")

print("For loop with else:")
for num in range(3):  # 0 to 2
    print(num)
else:
    print("Loop completed normally")  # Runs after full iteration

print("\nWhile loop with else:")
n = 0
while n < 3:  # 0 to 2
    print(n)
    n += 1
else:
    print("Loop completed normally")  # Runs after full iteration
