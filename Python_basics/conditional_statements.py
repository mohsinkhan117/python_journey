# 1. if statement - checking age for voting eligibility
age = 18
if age >= 18:
    print("Eligible to vote")

# 2. if-else statement - checking pass/fail
marks = 35
if marks >= 40:
    print("Passed")
else:
    print("Failed")

# 3. if-elif-else statement - grading system
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Grade: {grade}")
#what is the difference between print(f"Grade: {grade}") and print("Grade: {grade}")

# 4. Nested if - checking login credentials
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

# 5. Multiple conditions with 'and' - loan approval
income = 50000
credit_score = 750
if income >= 40000 and credit_score >= 700:
    print("Loan approved")

# 6. Multiple conditions with 'or' - discount eligibility
is_member = True
purchase_amount = 50
if is_member or purchase_amount > 100:
    print("Discount applied")

# 7. Using 'not' - checking account status
is_blocked = False
if not is_blocked:
    print("Account is active")

# 8. Ternary operator (conditional expression) - assign based on condition
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# 9. Short-circuit evaluation - checking list emptiness
items = []
if items and len(items) > 0:  # Stops at first false condition
    print("Has items")

# 10. Checking multiple values with 'in' - role-based access
user_role = "editor"
if user_role in ["admin", "editor", "moderator"]:
    print("Access granted to edit content")

# 11. Pass statement - placeholder for future logic
user_input = "pending"
if user_input == "pending":
    pass  # TODO: implement later
else:
    print("Processed")

# 12. Match-case (Python 3.10+) - HTTP status codes
status_code = 404
match status_code:
    case 200:
        print("Success")
    case 404:
        print("Not found")
    case 500:
        print("Server error")
    case _:
        print("Unknown status")

# 13. Match-case with patterns - command handler
command = "get user 123"
match command.split():
    case ["get", "user", user_id]:
        print(f"Fetching user {user_id}")
    case ["delete", "user", user_id]:
        print(f"Deleting user {user_id}")
    case _:
        print("Invalid command")

# 14. Using any() - checking if any condition is True
grades = [45, 67, 30, 88]
if any(grade < 40 for grade in grades):
    print("Some students failed")

# 15. Using all() - checking if all conditions are True
tasks = [True, True, True]
if all(tasks):
    print("All tasks completed")