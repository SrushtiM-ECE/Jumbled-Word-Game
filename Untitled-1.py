word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
