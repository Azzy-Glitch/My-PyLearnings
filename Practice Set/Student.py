# class Student:
#     def __init__(self, name, roll, course):
#         self.std = (name, roll, course)

#     @property
#     def std(self):
#         """Readable property for student info"""
#         return (f"Student name is {self.name} "
#                 f"with roll number {self.roll} "
#                 f"enrolled in {self.course}")

#     @std.setter
#     def std(self, value):
#         """Setter: value should be a tuple (name, roll, course)"""
#         if not isinstance(value, tuple) or len(value) != 3:
#             raise TypeError("Value must be a tuple of (name, roll, course)")
        
#         name, roll, course = value
        
#         if not isinstance(name, str):
#             raise TypeError("Name must be a string")
#         if not isinstance(roll, int):
#             raise TypeError("Roll number must be an integer")
#         if not isinstance(course, str):
#             raise TypeError("Course must be a string")
        
#         self.name = name
#         self.roll = roll
#         self.course = course

#     def __str__(self):
#         return self.std


# def main():
#     students = []
    
#     try:
#         num_students = int(input("Enter number of students: "))
#     except ValueError:
#         print("Please enter a valid number!")
#         return

#     for i in range(num_students):
#         print(f"\nEnter details for student {i+1}:")
#         name = input("Name of student: ").strip()
        
#         try:
#             roll = int(input("Roll number: "))
#         except ValueError:
#             print("Roll Number must be an integer!")
#             continue
            
#         course = input("Course Enrolled in: ").strip()
        
#         # Create student object
#         student = Student(name, roll, course)
#         students.append(student)
        
#         # Optional: print immediately
#         print(student)

#     # === Save to file ===
#     with open("data.txt", "w") as f:
#         for student in students:
#             f.write(f"{student.name},{student.roll},{student.course}\n")
    
#     print(f"\n{len(students)} students saved to data.txt")


# def read_students():
#     """Read students from file"""
#     try:
#         with open("data.txt", "r") as f:
#             print("\n--- Students from file ---")
#             for line in f:
#                 if line.strip():
#                     name, roll, course = line.strip().split(",")
#                     print(f"Name: {name}, Roll: {roll}, Course: {course}")
#     except FileNotFoundError:
#         print("No data.txt file found yet.")

# # s = Student("Ali", 101, "Computer Science")
# # print(s)

# # if __name__ == "__main__":
# #     main()
# #     # Uncomment the line below if you want to read the file after saving
# #     # read_students()

class Student:
    def __init__(self, name: str, roll: int, course: str):
        self._validate(name, roll, course)

        self.name = name
        self.roll = roll
        self.course = course

    # ------------------------
    # Validation layer
    # ------------------------
    def _validate(self, name, roll, course):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if not isinstance(roll, int):
            raise TypeError("Roll number must be an integer")

        if not isinstance(course, str):
            raise TypeError("Course must be a string")

    # ------------------------
    # Update method
    # ------------------------
    def update(self, name: str, roll: int, course: str):
        self._validate(name, roll, course)

        self.name = name
        self.roll = roll
        self.course = course

    # ------------------------
    # Data representations
    # ------------------------
    def to_tuple(self):
        return self.name, self.roll, self.course

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "course": self.course
        }

    # ------------------------
    # Human-readable (end user)
    # ------------------------
    def __str__(self):
        return f"{self.name} | Roll: {self.roll} | Course: {self.course}"

    # ------------------------
    # Developer/debug representation
    # ------------------------
    def __repr__(self):
        return (
            f"Student(name='{self.name}', "
            f"roll={self.roll}, "
            f"course='{self.course}')"
        )


def main():
    students = []

    while True:
        print("\n--- Student Entry System ---")

        name = input("Enter name (or type 'exit' to stop): ").strip()
        if name.lower() == "exit":
            break

        try:
            roll = int(input("Enter roll number: ").strip())
        except ValueError:
            print("Invalid roll number! Must be integer.")
            continue

        course = input("Enter course: ").strip()

        try:
            student = Student(name, roll, course)
            students.append(student)
            print("Student added:", student)
        except TypeError as e:
            print("Error:", e)

    # Final output
    print("\n--- All Students ---")
    for s in students:
        print(s)


if __name__ == "__main__":
    main()