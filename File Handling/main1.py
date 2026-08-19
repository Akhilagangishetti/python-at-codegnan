# import csv
# try:
#     with open('test.csv', 'w', newline="") as file:
#         writer = csv.writer(file)
#         header = ['Name', "contact"]
#         writer.writerow(header)
#         data [["ram", 123456789], ["sam", 1535273929]]
#         writer.writerows(data)
#         print("Content added")
# except Exception as e:
#     print("Something Wrong in test.csv: {e}")

# reading csv file content
# 


# updating contact number
import csv
try:
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = (list(reader))
        name = input()
        for ind, row in enumerate(contacts):
            if row[0] == name: 
                contacts[ind][1] = new_contact
                break
        else:
            print("Contact name not exists")
            
except Exception as e:
    print(f"Something Wrong in test.csv: {e}")

# writing content into file
try:
    with open('test.csv', 'w', newline ="") as file:
        writer = csv.writer(file)
        header = ['Name', "contact"]
        writer.writerows(contacts)
        data [["ram", 123456789], ["sam", 1535273929]]
        writer.writerows(data)
        print("Content added")
except Exception as e:
    print("Something Wrong in test.csv: {e}")

# add new contact
try:
    with open('test.csv','+rw')