# def fizz_buzz(number):
#     if number % 5 == 0 and number % 3 == 0:
#         return "fizz_buzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     return number
# print(fizz_buzz(1501))


from collections import Counter
question = "This is a common interview question"

char_frequency = {}
for char in question:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
highest_letter = max(char_frequency, key=char_frequency.get)
print(f"{highest_letter} = {char_frequency[highest_letter]}")