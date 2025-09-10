with open("log.txt") as f:
    lines = f.readlines()

line_No = 1
for line in lines:
    if("python" in line.lower()):
        print(f"Yes python is present. Line no: {line_No}")
        break
    line_No += 1

else:
    print("No Python is not present")