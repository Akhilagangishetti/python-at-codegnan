from data_store import load_data

def search_visitor():
    keyword = input("Enter Visitor ID or Name to search: ").lower()
    data = load_data()
    found = False

    for visitor in data:
        if keyword == visitor["id"].lower() or keyword in visitor["name"].lower():
            found = True
            print("\n--- Visitor Found ---")
            for key, value in visitor.items():
                print(f"{key}: {value}")
            print(" ")

    if not found:
        print(" No visitor found with that ID/Name.")