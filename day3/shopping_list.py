#Day 3 - Shopping list

shopping_list = []

print("Welcome to your shopping list!")
print("Type 'done' when you finish.\n")

while True:
    item = input("Add an item: ")
    if item.lower() == "done":
        break
    shopping_list.append(item)

print("\nYour shopping list:")
for product in shopping_list:
    print(f"- {product}")