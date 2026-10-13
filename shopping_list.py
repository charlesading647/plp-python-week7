shopping_list = []

while True:
    print("\nShopping List Manager")
    choice = input("Choose add / remove / show / done: ").lower().strip()

    if choice == "add":
        item = input("Enter item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "added to your list.")
        else:
            print("Item cannot be empty.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")