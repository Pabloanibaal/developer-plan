#Calcular edad con verificacion

while True:
    birth_year = int(input("Enter your birth year: "))

    age = 2025 - birth_year
    print(f"You are {age} years old.")

    if age < 18:
        print("You are underage.")
    elif age <60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again == "no":
        print("Goodbye")
        break
