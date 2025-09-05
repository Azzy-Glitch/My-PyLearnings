words = {
    "kutta": "Dog",
    "kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want meaning of: ")

print(words.get(word, "Word not found"))