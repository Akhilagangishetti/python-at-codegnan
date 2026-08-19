# # opening a file in 'w' mode
# file = open("sample.txt", "w")
# file.write("Hello, Akhila")
# file.close()
# print("Content added")



# # opening a file in 'Append' mode
# file = open("sample.txt", "a")
# file.write("Hello, Akki")
# file.close()
# print("Content added")



# file = open("sample1.txt", "r+")
# # Takes cursur to 0th position
# string = """I am a student 
# i am learning python course"""
# file.seek(0)
# file.write(string)
# file.close()
# print("Content added")

# open a file in read mode
# file = None
# try:
#     file = open("sample.txt", "r")
#     # Takes cursur to 0th position
#     data = file.readlines()
#     print(data)
# except Exception as e:
#     print(f"Something Wrong, because: {e}")
# finally:
  
#     if file is not None:
#         file.close()

