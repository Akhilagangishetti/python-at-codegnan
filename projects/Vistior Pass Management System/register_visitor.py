import random
from datetime import datetime
from data_store import load_data, save_data
from email_notifier import send_notification


def generate_visitor_id():
    return "V" + str(random.randint(1000, 9999))

def register_visitor():
    name = input("Enter visitor name: ")
    phone = input("Enter phone number: ")
    purpose = input("Enter purpose of visit: ")
    whom_to_meet = input("Whom do you want to meet: ")
    host_email = input("Enter host's email (person to meet): ")

    data = load_data()
    visitor = {
        "id": generate_visitor_id(),
        "name": name,
        "phone": phone,
        "purpose": purpose,
        "whom_to_meet": whom_to_meet,
        "entry_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "exit_time": None,
        "status": "Pending"
    }
    data.append(visitor)
    save_data(data)
    print(f" Visitor registered successfully! Your ID: {visitor['id']}")

    send_notification(host_email, name, purpose, visitor["id"])