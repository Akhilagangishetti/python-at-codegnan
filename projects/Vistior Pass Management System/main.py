from register_visitor import register_visitor
from approve_pass import approve_pass
from search_visitor import search_visitor
from exit_visitor import exit_visitor
from data_store import load_data

def total_visitors_today():
    from datetime import datetime
    today = datetime.now().strftime("%Y-%m-%d")
    data = load_data()
    count = sum(1 for v in data if v["entry_time"].startswith(today))
    print(f" Total visitors today: {count}")

def menu():
    while True:
        print("\n Visitor Pass Management System ")
        print("1. Register Visitor")
        print("2. Approve Pass")
        print("3. Search Visitor")
        print("4. Exit Visitor")
        print("5. Total Visitors Today")
        print("6. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_visitor()
        elif choice == "2":
            approve_pass()
        elif choice == "3":
            search_visitor()
        elif choice == "4":
            exit_visitor()
        elif choice == "5":
            total_visitors_today()
        elif choice == "6":
            print("Thank you! Exiting...")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    menu()