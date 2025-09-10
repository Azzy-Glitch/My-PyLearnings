def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

str = input("Enter a string: ")
print(char_frequency(str))

a = {}
a = char_frequency(str)
print(a.keys())
print(a.items())  
