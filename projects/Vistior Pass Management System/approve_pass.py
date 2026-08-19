from data_store import load_data, save_data

def approve_pass():
    visitor_id = input("Enter Visitor ID to approve: ")
    data = load_data()

    for visitor in data:
        if visitor["id"] == visitor_id:
            if visitor["status"] == "Pending":
                visitor["status"] = "Approved"
                save_data(data)
                print(f" Pass approved for {visitor['name']}")
            else:
                print(f" Visitor status is already '{visitor['status']}'")
            return

    print(" Visitor ID not found.")