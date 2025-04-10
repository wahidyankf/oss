"""
Python Control Flow Demo

Key concepts demonstrated:
1. Conditional statements (if/elif/else)
2. For loops
3. While loops
4. Loop control (break, continue, pass)
5. Else clause in loops
"""

# 1. Conditional Statements
print("=== CONDITIONAL STATEMENTS ===")
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 2. For Loops
print("\n=== FOR LOOPS ===")
fruits = ["apple", "banana", "cherry"]
print("Simple for loop:")
for fruit in fruits:
    print(f"- {fruit}")

print("\nWith enumerate():")
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# 3. While Loops
print("\n=== WHILE LOOPS ===")
count = 3
print("Countdown:")
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# 4. Loop Control Statements
print("\n=== LOOP CONTROL ===")
print("break example:")
for num in range(10):
    if num == 5:
        break
    print(num)

print("\ncontinue example:")
for num in range(5):
    if num == 2:
        continue
    print(num)

print("\npass example:")
for num in range(3):
    if num == 1:
        pass  # Placeholder for future code
    print(num)

# 5. Else Clause in Loops
print("\n=== ELSE IN LOOPS ===")
print("For loop with else:")
for num in range(3):
    print(num)
else:
    print("Loop completed normally")

print("\nWhile loop with else:")
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("Loop completed normally")
