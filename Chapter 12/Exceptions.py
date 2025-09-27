
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError:
    print("Invalid Input")
    
except Exception:
    print("Some error occured") 

print("Thank You")