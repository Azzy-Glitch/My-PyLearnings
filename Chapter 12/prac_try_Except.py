# try:
#     with open("1.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("2.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:
#     with open("3.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)


# print("Thank You!")

filenames = ["1.txt", "2.txt", "3.txt"]

for file in filenames:
    try:
        with open(file, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"Error while opening {file}: {e}")

print("Thank You!")
