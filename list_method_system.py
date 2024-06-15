def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")


def handle_append(lst):
    try:
        el = input("Enter a value to add to the end of the list: ")
        if el != "":
            lst.append(el)
            print(lst)
        else:
            raise Exception("New element cannot be empty string. Try again...")
    except Exception as arg:
        print(arg)


def handle_extend(lst):
    new_values = input("Enter values to extend the list: ").split(", ")
    try:
        for el in new_values:
            if el != "":
                continue
            else:
                raise Exception("The are no new values or some of them are empty strings. Try again with new values...")
        lst.extend(new_values)
        print(lst)
    except Exception as arg:
        print(arg)


def handle_insert(lst):
    try:
        el_index = int(input("Enter the index at which new element should be located: "))
        el = input("Enter the new element: ")
        lst.insert(el_index, el)
        print(lst)
    except ValueError:
        print("element index must me a whole number. Try again...")


def handle_remove(lst):
    el = input("Enter a value to remove from the list: ")
    try:
        lst.remove(el)
        print(lst)
    except ValueError:
        print("The element you are trying to remove in not in the list.")


def handle_pop(lst):
    el_index = input("Optional - if you want to pop item at specific index, or tap enter and remove last element: ")
    if el_index == "":
        lst.pop()
    else:
        try:
            if not isinstance(int(el_index), int):
                raise ValueError
            if int(el_index) > len(lst):
                raise Exception
            lst.pop(int(el_index))
            print(lst)
        except (ValueError, Exception):
            if ValueError:
                print("Index must be a whole number which is in range of the list. Try again...")
            else:
                print(Exception)


def handle_clear(lst):
    lst.clear()
    print(lst)


def handle_index(lst):
    el = input("Enter value to find its index: ")
    try:
        print(f"The element - {el} you searched for is at index - {lst.index(el)}")
    except ValueError:
        print("The element you searched is not in the list. Try again...")


def handle_count(lst):
    el = input("Enter a value to count its occurrences in the list: ")
    print(f"The element - {el} exist {lst.count(el)} times in the list")


def handle_sort(lst):
    lst.sort(key=int)
    print(lst)


def handle_reverse(lst):
    lst.reverse()
    print(lst)


def handle_copy(lst):
    new_list = lst.copy()
    print(new_list)


def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(', ')

    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
