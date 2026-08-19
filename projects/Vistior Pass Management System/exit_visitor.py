from datetime import datetime
from data_store import load_data, save_data

def exit_visitor():
    visitor_id = input("Enter Visitor ID for exit: ")
    data = load_data()

    for visitor in data:
        if visitor["id"] == visitor_id:
            if visitor["status"] == "Approved":
                visitor["exit_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                visitor["status"] = "Exited"
                save_data(data)
                print(f" Exit recorded for {visitor['name']}")
            elif visitor["status"] == "Pending":
                print(" Visitor pass not approved yet.")
            else:
                print(" Visitor has already exited.")
            return

    print(" Visitor ID not found.")