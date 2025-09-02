marks = {
    "Azzy": 100,
    "Nokia": 56,
    "Android": 23,
    0: "Azzy"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Azzy": 99, "Titanic": 100})
# print(marks)

print(marks.get("Azzy2")) # Prints None
print(marks["Azzy2"]) # Returns an error