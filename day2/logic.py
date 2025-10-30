#Grade Calculator

score = float(input("Enter your score(0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if score >= 60:
    result = "passed"
else:
    result = "Failed"

print(f"You got a grade {grade} and you have {result} the exam.")