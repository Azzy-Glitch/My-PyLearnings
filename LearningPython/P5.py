def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))
